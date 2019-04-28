from domparser import parse_DOM, _debug, gen
from freader import flat

if __name__ == "__main__":
    # parse html to DOM, debug printing
    n = parse_DOM(flat("test/test.html"))
    _debug(n)
    
    # Parse the DOM tree back to html
    # result save to test/outputtest.html
    # Compare it to see if two files generate
    # same view
    print(gen(n, "test/outputtest.html"))
