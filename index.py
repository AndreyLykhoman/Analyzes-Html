import sys

from models.html_parser import HTMLToTreeParser


def parse_htm_to_tree(file_path):
    html_file = open(file_path, "r")
    htm_file_readlines = html_file.readlines()
    html_to_tree_parser = HTMLToTreeParser()
    clean_lines = [l.strip() for l in htm_file_readlines if l.strip()]
    # for line in htm_file_readlines:
    html_to_tree_parser.feed(data=' '.join(clean_lines))


    return html_to_tree_parser.get_html_tree()


def analize_html(input_origin_file_path, input_other_sample_file_path, node_id="make-everything-ok-button"):
    origin_html_tree = parse_htm_to_tree(input_origin_file_path)
    origin_node = origin_html_tree.find_node_by_id(node_id)
    other_sample_html_tree = parse_htm_to_tree(input_other_sample_file_path)
    other_same_node = other_sample_html_tree.find_nodes_like_input_node(origin_node)
    return other_same_node.get_absolute_path()


if __name__ == "__main__":
    arg = sys.argv
    print(analize_html(arg[1], arg[2]))
