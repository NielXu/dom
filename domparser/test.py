from domparser import parse_dom, _debug, parse_html, textnode, flatfile, readurl
from domoper import get_element_by_id, remove_element_by_id, get_elements_by_class, get

if __name__ == "__main__":
    # # parse html to DOM, debug printing
    # n = parse_dom(flatfile("test/test.html"))
    # _debug(n)
    
    # # Parse the DOM tree back to html
    # # result save to test/outputtest.html
    # # Compare it to see if two files generate
    # # same view
    # print(parse_html(n, "test/outputtest.html"))

    # # test2
    # n = parse_dom(flatfile("test/test2.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest2.html")

    # # test3
    # n = parse_dom(flatfile("test/test3.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest3.html")

    # # test4
    # n = parse_dom(flatfile("test/test4.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest4.html")

    # # test5
    # n = parse_dom(flatfile("test/test5.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest5.html")

    # # test6
    # n = parse_dom(flatfile("test/test6.html"))
    # _debug(n)
    # parse_html(n, "test/outputtest6.html")

    # test domoper
    # n = parse_dom(flatfile("test/test7.html"))
    # node = get_element_by_id(n, "red")
    # node.children.append(textnode("Additional text"))
    # print(node)
    # node = remove_element_by_id(n, "blue")
    # print(node)
    # parse_html(n, "test/outputtest7.html")

    # n = parse_dom(flatfile("test/test5.html"))
    # for i in get(n, "div", {"id":"topbar"}):
    #     print(i)
    
    # for i in get_elements_by_class(n, "linkcs"):
    #     print(i)
    
    # print(get_element_by_id(n, "topbar"))

    # An example using domoper with duckduckgo
    d = readurl('https://duckduckgo.com/')
    li = get(d, 'div')
    for i in li:
        print(i)
    print("TOTAL:", len(li))
    