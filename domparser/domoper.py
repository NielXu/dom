"""
domoper is a module that can operate the generated DOM.
It can do search, modify and remove. It is similar to
module such as BeautifulSoup (but with less features).
It also looks familiar with JavaScript code such as
document.getElementById() etc.
"""
from domparser import textnode


def get_element_by_id(n, id_):
    """
    Get an element by its id, return the node as the result.
    If there is no element with the given id, return None.
    """
    if "id" in n.prop:
        if n.prop["id"] == id_:
            return n
    for c in n.children:
        f = get_element_by_id(c, id_)
        if f is not None:
            return f


def remove_element_by_id(n, id_):
    """
    Remove an element from the DOM by its id. If there is
    no element with the given id, do nothing and return
    None, otherwise, return the removed node.
    Please notice that removing a single element will
    cause all its sub elements being removed as well.
    """
    if n is None:
        return
    for c in n.children:
        if "id" in c.prop:
            if c.prop["id"] == id_:
                n.children.remove(c)
                return c
        f = remove_element_by_id(c, id_)
        if f is not None:
            return f
