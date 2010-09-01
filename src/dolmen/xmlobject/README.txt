================
dolmen.xmlobject
================

  >>> from dolmen.content import Content
  >>> from dolmen.xmlobject.schema import dump
  
  >>> item = Content(title=u"My item")
  >>> print dump(item)
  <content factory="Some factory">
    <title>My item</title>
  </content>

If the content is named, the name is dumped as well as a node property::

  >>> item.__name__ = u"my.item"
  >>> print dump(item)
  <content factory="Some factory" id="my.item">
    <title>My item</title>
  </content>
