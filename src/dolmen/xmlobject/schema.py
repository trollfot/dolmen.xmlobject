#!/usr/bin/python
# -*- coding: utf-8 -*-

from lxml import etree
from dolmen import content
from z3c.schema2xml import serialize_to_tree, deserialize


def dump(obj):
    """Dumps a IBaseContent object into an XML mash
    """
    if not content.IBaseContent.providedBy(obj):
        raise NotImplementedError("The given object is not an IBaseContent")

    name = getattr(obj, '__name__', None)
    schema = content.schema.bind().get(obj)[0]
    factory = u"Some factory"  # here, we need a way to get the factory

    if name is not None:
        item = etree.Element(u"content", id=unicode(name), factory=factory)
    else:
        item = etree.Element(u"content", factory=factory)
        
    result = serialize_to_tree(item, schema, obj)
    return etree.tostring(item, encoding=u"UTF-8", pretty_print=True)


def load(obj):
    raise NotImplementedError
