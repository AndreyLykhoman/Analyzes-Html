from html.parser import HTMLParser

from .html_node import HTMLTree


class HTMLToTreeParser(HTMLParser):
    """
    TODO: write me
    """

    def __init__(self):
        super().__init__()
        self.html_tree = HTMLTree()

    def handle_starttag(self, tag, attrs):
        self.html_tree.add_children_node(tag)
        for attr in attrs:
            name, value = attr
            if name == "class":
                for val in value.split(" "):
                    self.html_tree.add_node_attr(name, val)
            else:
                self.html_tree.add_node_attr(name, value)

    def handle_endtag(self, tag):
        self.html_tree.go_to_parent_node()

    def handle_data(self, data):
        self.html_tree.set_node_data(data)

    def get_html_tree(self):
        return self.html_tree

