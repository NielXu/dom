from domparser import parse_dom, _debug, parse_html, textnode
from freader import flat
from domoper import get_element_by_id, remove_element_by_id

if __name__ == "__main__":
    # # parse html to DOM, debug printing
    # n = parse_dom(flat("test/test.html"))
    # _debug(n)
    
    # # Parse the DOM tree back to html
    # # result save to test/outputtest.html
    # # Compare it to see if two files generate
    # # same view
    # print(parse_html(n, "test/outputtest.html"))

    # # test2
    # n = parse_dom(flat("test/test2.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest2.html")

    # # test3
    # n = parse_dom(flat("test/test3.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest3.html")

    # # test4
    # n = parse_dom(flat("test/test4.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest4.html")

    # # test5
    # n = parse_dom(flat("test/test5.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest5.html")

    # # test6
    # n = parse_dom(flat("test/test6.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest6.html")

    # test domoper
    n = parse_dom(flat("test/test7.html"))
    node = get_element_by_id(n, "red")
    node.children.append(textnode("Additional text"))
    print(node)
    node = remove_element_by_id(n, "blue")
    print(node)
    parse_html(n, "test/outputtest7.html")
