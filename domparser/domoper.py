"""
domoper is a module that can operate the generated DOM.
It can do search, modify and remove. It is similar to
module such as BeautifulSoup (but with less features).
It also looks familiar with JavaScript code such as
document.getElementById() etc.
"""
def get_element_by_id(n, id_):
    """
    Get an element by its id, return the node as the result.
    If there is no element with the given id, return None
    """