"""
This is a DOM generator, what it does is reading HTML source
code and generate a DOM tree based on it. It also have functions
that can convert DOM tree to html, and save to the given file.
"""
from requests import get
import re


class node():
    """
    A node on DOM tree, representing a tag in HTML
    A node contains the following fields:

    `type_` The type of this tag
    
    `prop` Properties of this tag, such as color, size and so on, using dict
    
    `val` The value of this tag contains, None if no values

    `children` A list of children, empty list if no children

    `mark` Tell if this node had been visited or not, internal use only
    """
    def __init__(self, type_):
        self.type_ = type_
        self.prop = {}
        self.children = []
        self.mark = False
    
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
    return _parse(html)


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


def readurl(url):
    """
    Read a url and try to retrieve html from the website.
    And then generate the DOM tree based on the html.
    """
    return parse_dom(flat(get(url).text))


def flat(s):
    """
    Given a string, remove all next lines and extra whitespaces,
    and return the new string.
    """
    s = s.replace('\n', '')
    s = " ".join(s.split())
    return s


def flatfile(d):
    """
    Read lines of file and strip whitespaces on both sides.
    The multi-lines file will be merged to one line and
    separated by a whitespace.
    """
    f = open(d, "r")
    lines = f.readlines()
    s = ""
    for i in lines:
        s += i.strip() + " "
    return s[:-1]


def _parse(html):
    "Parsing html"
    index = 0
    s = ""
    stack = []
    while index < len(html):
        ch = html[index]
        if ch == "<":
            end = html.find(">", index)
            tag = html[index+1:end]
            if tag.startswith("!"):
                # Ignore comment
                index = end+1
                continue
            # tag is: a, li, ul ...
            # mp is attributes in dict
            tag, mp = _prop(tag)
            if tag.startswith("/"):
                # It is a close tag, search for corresponding open tag
                li = []
                tag = tag[1:]
                while len(stack) > 0:
                    if stack[-1].type_ == tag and stack[-1].mark == False:
                        break
                    li.append(stack.pop())
                stack[-1].children = li[::-1]
                stack[-1].mark = True
                if len(s.strip()) != 0:
                    stack[-1].children.append(textnode(s))
                s = ""
            else:
                if _search_closed_tag(html, index, tag):
                    n = node(tag)
                else:
                    n = singlenode(tag)
                if len(s.strip()) != 0:
                    stack.append(textnode(s))
                s = ""
                n.prop = mp
                stack.append(n)
            index = end
        else:
            s += ch
        index += 1
    return stack.pop()


def _prop(tg):
    "Analyze properties inside tag"
    attr = re.findall(r"[a-zA-Z0-9-_]*\s*=\s*[\"'].*?[\"']", tg)
    tag = tg.split()[0]
    # index 0 always indicates the tag
    if len(attr) == 0:
        return tag, {}
    mp = {}
    for i in range(0, len(attr)):
        prop = attr[i]
        name, val = prop.split("=", maxsplit=1)
        name = name.replace("\"", "").replace("'", "")
        val = val.replace("\"", "").replace("'", "")
        mp[name] = val
    return tag, mp


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


def _gen_html(n):
    type_ = n.type_
    if type(n) == textnode:
        return type_
    if type(n) == singlenode:
        prop = n.prop
        full = "<" + type_
        for i in prop:
            val = prop[i]
            full += " "+i+"=\""+val + "\""
        return full + ">"
    prop = n.prop
    full = "<" + type_
    for i in prop:
        val = prop[i]
        full += " "+i+"=\""+val+"\""
    s = full + ">"
    for i in n.children:
        s += _gen_html(i)
    return s + "</"+type_+">"
