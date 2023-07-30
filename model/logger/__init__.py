#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .logger import Logger

logger = Logger(usage='EWS Application')


def logger_debug(text):
    logger.debug(text)
