import sys
import Alfred

""" IMPORTANT: Check out the "Alfred.py" file for more information about the methods! """

# create a new alfred handler. It's important to add either a query or the system arguments
# example with an example query:
#handler = Alfred.Handler(query="QUERY")

# example with system arguments
handler = Alfred.Handler(args=sys.argv)

# Add items with add_item
handler.add_item(Alfred.Item(title="Example entry #1", subtitle="best entry!", icon="cake.png", uid=1, arg="#1"))
handler.add_item(Alfred.Item(title="Entry #2", subtitle="Cake!", uid=815, arg="#2"))

# Add item with add_new_item
handler.add_new_item(title="Sir, you're doing it wrong!", subtitle=handler.query, arg="Hello", uid="cake")

# push the items to Alfred
handler.push(max_results=3)