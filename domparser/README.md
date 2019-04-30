# Intro
domparser is a useful tool to convert between DOM and HTML. It can parse a HTML file and create a corresponding DOM. And converting the DOM back should have the similar code with the original HTML file and they two should share a same rendering view. Please notice that generated HTML file from DOM is a one-line file, which means there will be no fomratting be done.


# Example
First of all, import the necessary modules
```python
from freader import flat
from domparser import parse_html, parse_dom
```
read the html file and generate the DOM
```python
html = flat("{path}")       # replace path to html file
dom = parse_dom(html)       # dom now represents the root of DOM
```
convert DOM back to html file, and save to a given location
```python
parse_html(dom, "{path}")          # replace path to html file
```
Compare to see if two HTML files create a same view on browser


# TODO
- [x] Save properties of tags, such as name, value, href etc.
- [ ] Easier way to let user build a DOM, instead of reading from file
- [ ] Basic error checking
- [ ] Ignore comments in html file