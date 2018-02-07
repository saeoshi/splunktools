#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import urllib2

def cvelist_get():
    try:
        response = urllib2.urlopen('http://jvndb.jvn.jp/myjvn\?method\=getVulnOverviewList').read()
        print response

    except urllib2.URLError as e:
        if hasattr(e, 'reason'):
            print 'We failed to reach a server.'
            print 'Reason: ', e.reason
        elif hasattr(e, 'code'):
            print 'The server couldn\'t fulfill the request.'
            print 'Error code: ', e.code

if __name__ == '__main__':
    cvelist_get()
