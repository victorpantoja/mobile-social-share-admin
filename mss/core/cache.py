# coding: utf-8

import logging
import hashlib

from django.core.cache import cache


def expire_key(cachekey):
    '''
        expire keys from cache
    '''

    md5key = hashlib.md5(cachekey).hexdigest()

    print("[CACHE][expire] - %s {%s}" % (md5key, cachekey))

    cache.delete(md5key)
