import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        node2 = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        node3 = HTMLNode(props= None).props_to_html()
        node4 = HTMLNode(props= {}).props_to_html()
        self.assertEqual(node, node2)
        self.assertEqual(node3, node4)

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

if __name__ == "__main__":
    unittest.main()