#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import datetime


class Logger:
    """Konfigurationsklasse für den remanenten Datenzugriff von Parametern."""
    def __init__(self, file_path='logger.txt', usage='some app'):
        absolute_path = (os.path.dirname(os.path.abspath(__file__))).replace('\\', '/')
        self.file_path = absolute_path + '/' + file_path
        try:
            f = open(self.file_path, 'r')
        except FileNotFoundError:
            f = open(self.file_path, 'w')
            f.write('===== Logger Events for {} - File created {} =====\n'.format(usage, datetime.datetime.today()))
            f.close()

    def debug(self, text):
        time = str(datetime.datetime.today())
        with open(self.file_path, 'a') as f:
            print('|' + time + '| ' + str(text), file=f)
        print(text)


if __name__ == '__main__':
    logger = Logger()
    logger.debug('Hello World')
    logger.debug('End')
