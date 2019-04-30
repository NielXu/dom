"""
This is a DOM generator, what it does is reading HTML source
code and generate a DOM tree based on it. It also have functions
that can convert DOM tree to html, and save to the given file.
"""
from freader import flat


class node():
    """
    A node on DOM tree, representing a tag in HTML
    A node contains the following fields:

    `type_` The type of this tag
    
    `prop` Properties of this tag, such as color, size and so on, using dict
    
    `val` The value of this tag contains, None if no values

    `children` A list of children, empty list if no children
    """
    def __init__(self, type_):
        self.type_ = type_
        self.prop = {}
        self.children = []
    
    def __str__(self):
        return "node(type={0}, properties={1})".format(
            self.type_,
            self.prop
        )
    
    def __repr__(self):
        return self.__str__()
    
    def json(self):
        """
        Get json(dict) representation of the data, contains:
        type, value, children, property
        """
        j = {}
        j['type'] = self.type_
        j['children'] = self.children
        j['property'] = self.prop
        return j


class textnode(node):
    "Text node is the leaf that contains only plain text, extended node"
    def __init__(self, text):
        "text: the plain text that this node contains"
        super().__init__(text)
    
    def __str__(self):
        return "node(PlainText=" + self.type_+")"
    
    def __repr__(self):
        return self.__str__()


class singlenode(node):
    "Single node are those nodes that does not require close tag"
    def __init__(self, type_):
        super().__init__(type_)


def parse_dom(html):
    """
    Parse a DOM tree based on the given HTML.
    The provided HTML must be a list that contains
    lines of codes. The return result will be the
    root node of the DOM tree, and it is fully parsed.
    Please notice that it does not do any error handling,
    therefore missing end tags might caused the tree
    parsed incorrectly and get an unexpected result.
    The passed in HTML should be merged to one line
    first before parsing to DOM, consider using 
    freader.flat(f).
    """
    n = node("html")
    _parse(html, n)
    return n.children[0]


def _parse(html, root):
    "Parsing html"
    index = 0
    s = ""
    while index < len(html):
        ch = html[index]
        if ch == "<":
            end = html.find(">", index)
            tag = html[index+1:end]
            tag, prop = _prop(tag)
            tup = _search_closed_tag(html, index, tag)
            if tup:
                # If there is end tag for this open tag
                result = tup[0]
                iend = tup[1]
                if len(s.strip()) != 0:
                    root.children.append(textnode(s))
                s = ""
                n = node(tag)
                n.prop = prop
                root.children.append(n)
                _parse(html[end+1:result], n)
                index = iend
            else:
                # No end tag
                index = end
                n = singlenode(tag)
                n.prop = prop
                if len(s.strip()) != 0:
                    root.children.append(textnode(s))
                s = ""
                root.children.append(n)
        else:
            s += ch
        index += 1
    if len(s.strip()) != 0:
        root.children.append(textnode(s))


def _prop(tg):
    "Analyze properties inside tag"
    splitted = tg.split()
    # index 0 always indicates the tag
    if len(splitted) == 1:
        return splitted[0], {}
    mp = {}
    for i in range(1, len(splitted)):
        prop = splitted[i]
        name, val = prop.split("=")
        mp[name] = val
    return splitted[0], mp


def _search_closed_tag(html, index, tg):
    """
    Search for a specific closed tag as near as possible from the
    starting index. Return the index if found, None otherwise.
    The returned index will be the following:
    <h2>Hi</h2>, search closed tag(h2) -> index 10
    """
    while index < len(html):
        ch = html[index]
        if ch == "<":
            end = html.find(">", index)
            if html[index+1] == "/" and html[index+2:end] == tg:
                return index, end
        index += 1


def _debug(n):
    "Debug printing for DOM tree"
    def _dp(n, d):
        prev = "   " * d
        if type(n) == textnode:
            print(prev + "**" + n.type_)
        else:
            print(prev+">>", n.type_, "has properties:", n.prop, "has children:")
            for i in n.children:
                _dp(i, d+1)
    _dp(n, 0)


def parse_html(dom, targ=None):
    """
    Generate a single line html code that converted from
    the given DOM tree. If targ is specified, the code
    will be saved to the given location. The passed in
    dom should be a node.
    If writing to a given file, it will use w+, which
    creates a new file if not exist, and then overwrite
    the content
    """
    r = _gen_html(dom)
    if targ:
        with open(targ, "w+") as f:
            f.write(r)
    return r


def _gen_html(n):
    type_ = n.type_
    if type(n) == textnode:
        return type_
    if type(n) == singlenode:
        prop = n.prop
        full = "<" + type_
        for i in prop:
            val = prop[i]
            full += " "+i+"="+val
        return full + ">"
    prop = n.prop
    full = "<" + type_
    for i in prop:
        val = prop[i]
        full += " "+i+"="+val
    s = full + ">"
    for i in n.children:
        s += _gen_html(i)
    return s + "</"+type_+">"
    