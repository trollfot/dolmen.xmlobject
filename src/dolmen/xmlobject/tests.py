# -*- coding: utf-8 -*-

import unittest
import pkg_resources
import dolmen.xmlobject
from zope.component.testlayer import ZCMLFileLayer
from zope.testing import doctest


def test_suite():
    suite = unittest.TestSuite()
    readme = doctest.DocFileSuite(
        'README.txt', globs={'__name__': 'dolmen.xmlobject'},
        optionflags=(doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS))
    readme.layer = ZCMLFileLayer(dolmen.xmlobject)
    suite.addTest(readme)
    return suite
