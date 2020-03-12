# -*- coding: utf-8 -*-
#
# Copyright (c) 2020~2999 - Cologler <skyoflw@gmail.com>
# ----------
#
# ----------

try:
    iter([])
except NameError:
    # framework core - Version: 2.6.3
    # NameError: global name 'iter' is not defined
    def iter(iterable):
        return (i for i in iterable)

try:
    next(iter([]), None)
except NameError:
    # framework core - Version: 2.6.3
    def next(iterable, *defaults):
        if len(defaults) > 1:
            raise TypeError('next expected at most 2 arguments, got {}'.format(len(defaults) + 1))
        try:
            return iterable.next()
        except StopIteration:
            if defaults:
                return defaults[0]
            raise
