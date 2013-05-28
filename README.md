alfred.py
==========

Lightweight Python binding for [Alfred workflows](http://alfredapp.com).

How to use it
-------------

Check out my [example.py](example.py) or look at this fancy example:

```python
import sys
import Alfred
	
handler = Alfred.Handler(args=sys.argv)
	
handler.add_item(Alfred.Item(title="The cake is a lie!", subtitle="IMPORTANT: This item may contain a Portal spoiler! :P" icon="cake.png", uid="cake_is_a_lie", arg="CAKE_LIE"))
	
item = Alfred.Item(title="Title only!")
	
handler.add_item(item)
	
handler.push(max_results=4)
```

Workflows using alfred.py
--------------------------

* [alfred-haxelib](https://github.com/Kasoki/alfred-haxelib)
* [Cyberduck-Favorites](https://github.com/Kasoki/Cyberduck-Favorites)
* [Maestro](https://github.com/Kasoki/Maestro)

You want to add your workflow here? Just [write me a mail ;)](mailto:ikasoki@gmail.com).

Licence
--------

This binding is licenced under the terms of the [MIT Licence](http://opensource.org/licenses/MIT)
