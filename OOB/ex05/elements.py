from elem import Elem, Text

class Html(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('html', attr, content, 'double')

class Head(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('head', attr, content, 'double')

class Body(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('body', attr, content, 'double')

class Title(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('title', attr, content, 'double')

class Meta(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('meta', attr, content, 'simple')

class Img(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('img', attr, content, 'simple')

class Table(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('table', attr, content, 'double')

class Th(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('th', attr, content, 'double')

class Tr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('tr', attr, content, 'double')

class Td(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('td', attr, content, 'double')

class Ul(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ul', attr, content, 'double')

class Ol(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('ol', attr, content, 'double')

class Li(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('li', attr, content, 'double')

class H1(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h1', attr, content, 'double')

class H2(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('h2', attr, content, 'double')

class P(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('p', attr, content, 'double')

class Div(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('div', attr, content, 'double')

class Span(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('span', attr, content, 'double')

class Hr(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('hr', attr, content, 'simple')

class Br(Elem):
    def __init__(self, content=None, attr={}):
        super().__init__('br', attr, content, 'simple')


if __name__ == '__main__':

    # Subject test 1
    print("\nHtml with Head and Body:\n")
    print(Html([Head(), Body()]))
    print('=' * 50)

    # Subject test 2
    print("\nMore complete HTML document")
    page = Html([
        Head(Title(Text('"Hello ground!"'))),
        Body([
            H1(Text('"Oh no, not again!"')),
            Img(attr={'src': 'http://i.imgur.com/pfp3T.jpg'})
        ])
    ])
    result = str(page)
    print(f"\n{result}")
    print('=' * 50)

    # Elements with attributes
    print("\nElements with attributes:")
    div = Div(Text('Some random content'), attr={'class': 'container', 'id': 'main'})
    result = str(div)
    print(f"\n{result}")
    print('=' * 50)

    # Simple tags
    print("\nSelf-closing tags:")
    img = Img(attr={'src': 'test.jpg', 'alt': 'Test'})
    result = str(img)
    print(f"\n{result}")
    print('=' * 50)

    # Lists of elements
    print("\nLists of elements:")
    list_elem = Ul([
        Li(Text('Item 1')),
        Li(Text('Item 2')),
        Li(Text('Item 3'))
    ])
    result = str(list_elem)
    print(f"\n{result}")
    print('=' * 50)

    # Nested elements
    print("\nNested elements:")
    nested = Div([
        Div([
            Div(Text('Deep content'))
        ])
    ])
    result = str(nested)
    print(f"\n{result}")
    print('=' * 50)
