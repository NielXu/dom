"""
XPath parser
"""
import re


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
    q = []
    index = 0
    while index < len(x):
        ch = x[index]
        if ch == "/":
            next_index = _find_next(index, x)
            segment = x[index:next_index]
            index = next_index
            if "[" in segment:
                _parse_cond(segment)
            continue
        index += 1


def _find_next(index, x):
    "Find the closet next path and return the index"
    oindex = index
    if index < len(x) - 1 and x[index+1] == "/":
        oindex += 1
        index += 1
    while index < len(x):
        ch = x[index]
        if ch == "/" and index != oindex:
            return index
        index += 1
    return index


def _parse_cond(cond):
    "Parse the condition in xpath"
    print(cond)


if __name__ == "__main__":
    p1 = "/*//div/span[@class='className']//p/ng-button"
    parse_xpath(p1)
