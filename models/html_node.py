from collections import Counter, defaultdict

class HTMLNode:
    """
    TODO: write me
    """
    def __init__(self, name="", parent_node=None, data=""):
        # TODO: add validation
        self.name = name
        self.children_nodes = []
        self.parent_node = parent_node
        self.attrs = defaultdict(list)
        self.data = data

    def add_children_node(self, node):
        if not isinstance(node, HTMLNode):
            raise TypeError("`node` must be the HTMLNode type")
        self.children_nodes.append(node)

    def add_attr(self, name, value):
        self.attrs[name].append(value)

    def get_absolute_path(self, separator=" > "):
        #TODO: Get a list of name nodes (with calculate index if need it).
        # Add new name to the head of list
        # after that make the string by separator
        pass


class HTMLTree:
    """
    TODO: write me
    """

    def __init__(self, base_node=HTMLNode()):
        self.base_node = base_node
        self.current_work_node = base_node
        self.attr_map = defaultdict(list)
        self.node_name_map = defaultdict(list)

    def add_children_node(self, name, data=""):
        children_node = HTMLNode(name, self.current_work_node, data)
        self.node_name_map[name].append(children_node)
        self.current_work_node.add_children_node(children_node)
        self.current_work_node = children_node

    def add_node_attr(self, name, value):
        attr_map_index = self.create_attr_map_index(name, value)
        self.attr_map[attr_map_index].append(self.current_work_node)
        self.current_work_node.add_attr(name, value)

    def set_node_data(self, data):
        self.current_work_node.data = data

    def go_to_parent_node(self):
        self.current_work_node = self.current_work_node.parent_node

    def find_nodes_by_attr(self, name, value):
        return self.attr_map.get(self.create_attr_map_index(name, value), None)

    def find_node_by_id(self, id_value):
        result = self.find_nodes_by_attr("id", id_value)
        if result:
            return result[0]
        return None

    def find_nodes_like_input_node(self, input_node):
        nodes_by_node_name = self.node_name_map.get(input_node.name)
        nodes_by_attrs = []
        count_of_attrs = len(input_node.attrs)
        for attr in input_node.attrs:
            for value in input_node.attrs.get(attr):
                nodes_by_attrs = nodes_by_attrs + self.attr_map.get(
                    self.create_attr_map_index(attr, value),
                    []
                )
        filtered_nodes_by_name = [item for item in nodes_by_node_name if item.data == input_node.data]

        c = Counter(nodes_by_attrs)
        countet_by_attrs = dict(c.values())
        for node in filtered_nodes_by_name:
            if node in countet_by_attrs:
                countet_by_attrs[node] = countet_by_attrs[node] + 1

        result_node = None
        max_number = 0
        for node in countet_by_attrs:
            number = countet_by_attrs[node]
            if number > max_number:
                result_node = node
        return result_node

    @staticmethod
    def create_attr_map_index(name, value):
        return f'{name}_{value}'
