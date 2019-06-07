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
    `/` absolute
    
    `//` relative
    
    `[0]` index
    
    `contains()` contains

    `*` wild card

    `text()` Text

    `div, class, span, ...` tags

    @example
    ---
    `//div`, `//*`, `//div[@class="xyz"]`,
    `//div//div//*`, `//*[contains(@class, "xyz")]`,
    `//span[contains(text(), "xyz")]`, ...

    @param
    ---
    `x` The xpath in string
    """
