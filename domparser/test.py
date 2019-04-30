from domparser import parse_dom, _debug, parse_html
from freader import flat

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

    # test3
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

    # test6
    n = parse_dom(flat("test/test6.html"))
    _debug(n)
    parse_html(n, "test/outputtest6.html")
