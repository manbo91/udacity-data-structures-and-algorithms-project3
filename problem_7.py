# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler=None):
        self.root = RouteTrieNode(handler)

    def insert(self, order_path, handler):
        if len(order_path) == 1: # root
            self.root.handler = handler
            return
        self.insert_recursive(self.root, 1, order_path, handler)

    def insert_recursive(self, node, index, order_path, handler):
        path = order_path[index]

        if index == len(order_path) - 1:
            node.insert(path, handler)
            return

        if not path in node.children:
            node.insert(path)

        self.insert_recursive(node.children[path], index+1, order_path, handler)

    def find(self, order_path):
        if len(order_path) == 1: # root
            return self.root.handler

        node = self.root
        for path in order_path[1:]:  # except root path
            if path in node.children:
                node = node.children[path]
            else:
                return None

        return node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, path, handler=None):
        if not path in self.children:
            self.children[path] = RouteTrieNode(handler)


class Router:
    def __init__(self, handler, not_found_handler):
        self.route = RouteTrie(handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        order_path = self.split_path(path)
        self.route.insert(order_path, handler)

    def lookup(self, path):
        order_path = self.split_path(path)
        handler = self.route.find(order_path)

        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self, path):
        order_path = path.split("/")
        if len(order_path) >= 2 and order_path[-1] == '':
            order_path = order_path[:-1]
        return order_path


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route

# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one""
