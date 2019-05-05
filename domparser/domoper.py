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
    li = get(n, "*", {"id":id_})
    return None if len(li) == 0 else li[0]


def get_elements_by_class(n, class_):
    """
    Get elements by class name, return a list of nodes as
    the result. If there is no element with the given class
    name, return an empty list
    """
    return get(n, "*", {"class":class_})


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


def get(n, type_, attr={}):
    """
    Get elements by their types and attributes. Return a
    list of nodes as the result, or an empty list if nothing
    found.

    `n` The root node of DOM

    `type_` The type of the element, such as div, span, p, it can
    also be set to *, which will find all elements instead of specific
    type of elements

    `attr` The attribute dict, such as {'id':'xyz'}, default
    is empty
    """
    stack = [n]
    result = []
    while len(stack) > 0:
        n = stack.pop()
        if type_ == "*":
            if _attr_match(n, attr):
                result.append(n)
        else:
            if n.type_ == type_ and _attr_match(n, attr):
                result.append(n)
        for c in n.children:
            stack.append(c)
    return result


def _attr_match(n, attr):
    "Return True if attributes match"
    for i in attr:
        if i not in n.prop:
            return False
        ki = attr[i]
        ni = n.prop[i]
        if ki != ni:
            return False
    return True