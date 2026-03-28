from elem import Elem, Text
from elements import (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, 
                      Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br)

class Page:
    def __init__(self, root: Elem):
        self.root = root

    def is_valid(self):
        return self.__recursive_check(self.root)

    def __recursive_check(self, node):
        # Rule: Only specific types or Text (str) allowed
        allowed_types = (Html, Head, Body, Title, Meta, Img, Table, Th, Tr, Td, 
                         Ul, Ol, Li, H1, H2, P, Div, Span, Hr, Br, Text, str)
        if not isinstance(node, allowed_types):
            return False

        # Text/str nodes are leaves, they don't have children to validate
        if isinstance(node, (Text, str)):
            return True

        content = node.content

        # Rule: Html must strictly contain a Head, then a Body.
        if isinstance(node, Html):
            if len(content) != 2 or not isinstance(content[0], Head) or not isinstance(content[1], Body):
                return False

        # Rule: Head must only contain one Title and only one Title.
        elif isinstance(node, Head):
            # The rule says "only one Title", implying exactly one child which is a Title
            if len(content) != 1 or not isinstance(content[0], Title):
                return False

        # Rule: Body and Div must only contain H1, H2, Div, Table, Ul, Ol, Span, or Text.
        elif isinstance(node, (Body, Div)):
            allowed = (H1, H2, Div, Table, Ul, Ol, Span, Text, str)
            if any(not isinstance(c, allowed) for c in content):
                return False

        # Rule: Title, H1, H2, Li, Th, Td must only contain one Text and only this Text.
        elif isinstance(node, (Title, H1, H2, Li, Th, Td)):
            if len(content) != 1 or not isinstance(content[0], (Text, str)):
                return False

        # Rule: P must only contain Text.
        elif isinstance(node, P):
            if any(not isinstance(c, (Text, str)) for c in content):
                return False

        # Rule: Span must only contain Text or some P.
        elif isinstance(node, Span):
            if any(not isinstance(c, (Text, str, P)) for c in content):
                return False

        # Rule: Ul and Ol must contain at least one Li and only some Li.
        elif isinstance(node, (Ul, Ol)):
            if len(content) == 0 or any(not isinstance(c, Li) for c in content):
                return False

        # Rule: Tr must contain at least one Th or Td and only some Th or Td. Mutually exclusive.
        elif isinstance(node, Tr):
            if len(content) == 0:
                return False
            has_th = any(isinstance(c, Th) for c in content)
            has_td = any(isinstance(c, Td) for c in content)
            if has_th and has_td:
                return False
            if any(not isinstance(c, (Th, Td)) for c in content):
                return False

        # Rule: Table: must only contain Tr and only some Tr.
        elif isinstance(node, Table):
            if len(content) == 0 or any(not isinstance(c, Tr) for c in content):
                return False

        # Recursive check for all children
        for child in content:
            if not self.__recursive_check(child):
                return False

        return True

    def __str__(self):
        res = ""
        if isinstance(self.root, Html):
            res += "<!DOCTYPE html>\n"
        res += str(self.root)
        return res

    def write_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(self))

if __name__ == "__main__":
    # Test 1: Valid structure from Exercise 04
    print("--- Test 1: Valid Exercise 04 Structure ---")
    valid_html = Html([
        Head(Title(Text('"Hello ground!"'))),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    p1 = Page(valid_html)
    print(f"Is Valid? {p1.is_valid()}") # True
    print(p1)

    # Test 2: Invalid HTML - Wrong order in Html
    print("\n--- Test 2: Invalid HTML (Body before Head) ---")
    bad_order = Html([Body([H1(Text("Hi"))]), Head(Title(Text("Title")))])
    print(f"Is Valid? {Page(bad_order).is_valid()}") # False

    # Test 3: Invalid Head - More than one Title
    print("\n--- Test 3: Invalid Head (Two Titles) ---")
    # Note: Our current Elem.add_content allows lists.
    bad_head = Html([
        Head([Title(Text("T1")), Title(Text("T2"))]),
        Body([H1(Text("Hi"))])
    ])
    print(f"Is Valid? {Page(bad_head).is_valid()}") # False

    # Test 4: Invalid Tr - Mixed Th and Td
    print("\n--- Test 4: Invalid Tr (Mixed Th/Td) ---")
    bad_tr = Html([
        Head(Title(Text("Title"))),
        Body([
            Table([
                Tr([Th(Text("H")), Td(Text("D"))])
            ])
        ])
    ])
    print(f"Is Valid? {Page(bad_tr).is_valid()}") # False

    # Test 5: Valid Table
    print("\n--- Test 5: Valid Table ---")
    good_table = Html([
        Head(Title(Text("Table"))),
        Body([
            Table([
                Tr([Th(Text("H1")), Th(Text("H2"))]),
                Tr([Td(Text("V1")), Td(Text("V2"))])
            ])
        ])
    ])
    p5 = Page(good_table)
    print(f"Is Valid? {p5.is_valid()}") # True

    # Test 6: Invalid P - Contains Div
    print("\n--- Test 6: Invalid P (Contains Div) ---")
    bad_p = Html([
        Head(Title(Text("Title"))),
        Body([
            P([Text("Hello"), Div(Text("I am lost"))])
        ])
    ])
    print(f"Is Valid? {Page(bad_p).is_valid()}") # False

    # Test 7: Writing to file
    print("\n--- Test 7: Writing Valid HTML to file ---")
    p1.write_to_file("output.html")
    print("File 'output.html' generated.")

    # Test 8: Root is not Html (No Doctype)
    print("\n--- Test 8: Root is not Html (No Doctype) ---")
    # El Div ahora contiene una lista con un H1 y un Span
    not_html_root = Div([
        H1(Text("Title inside Div")),
        Span(Text("This is a span inside a div"))
    ])
    p8 = Page(not_html_root)
    print(f"Is Valid? {p8.is_valid()}") # True
    print("Resulting HTML (should not have DOCTYPE):")
    print(p8)
