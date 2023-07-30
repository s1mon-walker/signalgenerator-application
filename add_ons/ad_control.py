from ctypes import *
from WaveFormsSDK.dwfconstants import *
import sys
import time
import numpy as np
from add_ons.base_signals import *
from add_ons.plot_oop import PlotSimple2

# ===== shadow builtin print function to write logger file =====
from model.logger import logger
print = logger.debug
# ==============================================================

dwf = cdll.dwf
dpi = 140


class AnalogDiscoveryController:
    def __init__(self):
        # === Digilent Analog Discovery Basic Setup ===
        self.hdwf = c_int()

        self.version = create_string_buffer(16)
        dwf.FDwfGetVersion(self.version)
        self.version_str = 'DWF Version: ' + str(self.version.value)
        print('[AD] ' + self.version_str)

        self.cdevices = c_int()
        dwf.FDwfEnum(c_int(0), byref(self.cdevices))
        print("[AD] Number of Devices: " + str(self.cdevices.value))

        dwf.FDwfDeviceOpen(c_int(0), byref(self.hdwf))

        if self.cdevices.value == 0:
            print("[AD] no device available")

        if self.hdwf.value == hdwfNone.value:
            print("[AD] failed to open device")

        # === Initialise Variables ===
        self.channel = c_int(0)
        self.rgdSamples = None
        self.n_sp = 100
        self.signal = [0] * 100
        self.ch1 = None
        self.ch2 = None
        self.t_sp = None
        self.f_sp = None
        self.offset = None
        self.sampling_rate = None
        self.time = None
        self.amplitude = None
        self.factor = 1
        self.n_signals = 0
        self.signal_list = []
        self.ad_state = None

        self.setup()

    def start(self, parent=None, callback=None):
        """configures the device based on the controller state and starts the measurement"""
        dwf.FDwfAnalogOutNodeEnableSet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_bool(True))
        dwf.FDwfAnalogOutNodeFunctionSet(self.hdwf, self.channel, AnalogOutNodeCarrier, funcCustom)
        dwf.FDwfAnalogOutNodeDataSet(self.hdwf, self.channel, AnalogOutNodeCarrier, self.rgdSamples, c_int(self.n_sp))
        dwf.FDwfAnalogOutNodeFrequencySet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_double(self.f_sp))
        dwf.FDwfAnalogOutNodeAmplitudeSet(self.hdwf, self.channel, AnalogOutNodeCarrier, c_double(self.amplitude))
        dwf.FDwfAnalogOutRunSet(self.hdwf, self.channel, c_double(self.t_sp))  # run for 1 periods
        dwf.FDwfAnalogOutWaitSet(self.hdwf, self.channel, c_double(0.0))  # wait 0.0 s
        dwf.FDwfAnalogOutRepeatSet(self.hdwf, self.channel, c_int(500))  # repeat x times
        # ===========================================================================================
        dwf.FDwfAnalogInFrequencySet(self.hdwf, c_double(self.sampling_rate))
        dwf.FDwfAnalogInChannelRangeSet(self.hdwf, c_int(-1), c_double(10.0))
        dwf.FDwfAnalogInBufferSizeSet(self.hdwf, c_int(self.n_sp))

        time.sleep(1.0)  # wait for analog in offset to stabilize
        print("[AD] Starting acquisition")
        dwf.FDwfAnalogOutConfigure(self.hdwf, self.channel, c_bool(True))
        dwf.FDwfAnalogInConfigure(self.hdwf, c_int(1), c_int(1))

        sts = c_int()
        start_time = time.time()
        t_mess = parent.t_mess
        while True:
            dwf.FDwfAnalogInStatus(self.hdwf, c_int(1), byref(sts))  # write AD state to sts variable
            if sts.value == DwfStateDone.value:                      # if sts is done status
                break  # 0=Ready,1=Armed,2=Done,3=Triggerd/Running,4=Config,5=Prefill,6=?,7=Wait
            time.sleep(0.02)
            self.ad_state = sts.value

            if parent:
                if self.ad_state == 5:
                    time_val = int((time.time()-start_time)/t_mess * 60)
                    parent.update_progress_bar(20 + time_val)
                elif self.ad_state == 3:
                    time_val = int((time.time()-start_time)/t_mess * 60)
                    parent.update_progress_bar(20 + time_val)

        #===========================================================================================
        # Read data from Oszilloscope
        rg1 = (c_double * self.n_sp)()
        dwf.FDwfAnalogInStatusData(self.hdwf, c_int(0), rg1, len(rg1))
        rg2 = (c_double * self.n_sp)()
        dwf.FDwfAnalogInStatusData(self.hdwf, c_int(1), rg2, len(rg2))

        if parent:
            parent.update_progress_bar(80)

        self.ch1 = [0.0] * len(rg1)
        self.ch2 = [0.0] * len(rg2)
        for i in range(0, len(self.ch1)):
            self.ch1[i] = rg1[i]
            self.ch2[i] = rg2[i]

        # ===========================================================================================
        # Deactivate signalgenerator
        dwf.FDwfAnalogOutReset(self.hdwf, self.channel)
        dwf.FDwfAnalogInReset(self.hdwf, self.channel)
        # dwf.FDwfDeviceCloseAll()

        if parent:
            parent.update_progress_bar(90)

        if callback is not None:
            callback()

        # ===========================================================================================
        print('[AD] finished')

    def setup(self):
        """sets up the sample array"""
        self.rgdSamples = (c_double*self.n_sp)()
        # samples to c_double
        for i in range(0, self.n_sp, 1):
            self.rgdSamples[i] = c_double(self.signal[i])

    def set_function(self, function=None):
        """configures the controller based on the given function or the existing signal list"""
        if function:
            pass
        else:
            function = sum(self.signal_list)
        function.normalise()
        self.n_sp = function.n_sp
        self.t_sp = function.t_sp
        self.time = function.t
        self.f_sp = 1 / self.t_sp
        self.offset = function.offset
        self.sampling_rate = function.sampling_rate
        self.signal = function.signal
        self.amplitude = function.amplitude * self.factor

        self.setup()

    def set_channel(self, ch):
        """set output channel of AD"""
        self.channel = ch-1

    def plot(self):
        """shows plot of the data"""
        plot_messung = PlotSimple2(width=10, height=2, dpi=dpi)
        plot_messung.plot(self.time, [self.ch1, self.ch2])

    def close(self):
        """close the connection with AD device"""
        dwf.FDwfDeviceCloseAll()


if __name__ == '__main__':

    ad = AnalogDiscoveryController()

    sin1 = Sinus(f=100, n_sp=2**12, amplitude=2.0, n=2, phase=0, offset=1.0)
    sin2 = Sinus(f=1000, n_sp=2**12, amplitude=1.0, n=20, phase=0, offset=0.0)
    func = sin1 * sin2

    ad.set_function(func)
    ad.start()
    ad.plot()


