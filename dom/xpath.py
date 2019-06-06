"""
XPath parser
"""
def parse_xpath(x):
    """
    Pasing the xpath, return a list that represents
    the order of traversal, following the order
    of the list will find the corresponding
    element, or None if such element does
    not exist.
    
    @Support
    ---
    `/` a single element
    
    `//` all elements
    
    `[0]` index
    
    `contains()` contains

    `*` wild card

    `text()` Text

    @param
    ---
    `x` The xpath in string
    """
