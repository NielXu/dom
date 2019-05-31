# Intro
domparser is a useful tool to convert between DOM and HTML. It can parse a HTML file and create a corresponding DOM. And converting the DOM back should have the similar code with the original HTML file and they two should share a same rendering view. Please notice that generated HTML file from DOM is a one-line file, which means there will be no fomratting be done.


# Example
First of all, import the necessary modules
```python
from domparser import parse_html, parse_dom, flatfile
```
read the html file and generate the DOM
```python
html = flatfile("{path}")       # replace path to html file
dom = parse_dom(html)       # dom now represents the root of DOM
```
convert DOM back to html file, and save to a given location
```python
parse_html(dom, "{path}")          # replace path to html file
```
Compare to see if two HTML files create a same view on browser

# Bugs
- ~~Parsing large html files might cause error(corresponding to `test.TestExternalHtml`)~~


# TODO
- [x] Save properties of tags, such as name, value, href etc.
- [x] More functions to manipulate DOM tree
- [ ] Basic error checking
- [ ] Support XPath in domoper
- [ ] Deal with encoding problems
- [ ] Docs
- [x] Ignore comments in html file