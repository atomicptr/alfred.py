import sys
import Alfred

# create a new alfred handler. It's important to add either a query or the system arguments
# example with an example query:
#handler = Alfred.Handler(query="QUERY")

# example with system arguments
handler = Alfred.Handler(args=sys.argv)

handler.add_item(Alfred.Item(title="Example entry #1", subtitle="best entry!", icon="cake.png", uid=1, arg="#1"))
handler.add_item(Alfred.Item(title="Entry #2", subtitle="Cake!", uid=815, arg="#2"))
handler.add_new_item(title="Sir, you're doing it wrong!", subtitle=handler.query, arg="Hello", uid="cake")

handler.push(max_results=3)