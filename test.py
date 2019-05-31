from dom import domparser, domoper
import unittest
import requests
from bs4 import BeautifulSoup


class TestContent(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        with open('test\\test.html') as f:
            self.soup = BeautifulSoup(f, features="html.parser")
        self.dom = domparser.parse_dom(domparser.flatfile('test\\test.html'))
    
    def comp_text(self, a, b):
        a = "".join(a.split())
        b = "".join(b.split())
        self.assertEqual(a, b)
    
    def comp_element(self, e):
        expect = self.soup.findAll(e)
        actual = domoper.getAll(self.dom, e)
        self.assertEqual(len(expect), len(actual))
        for i in range(len(expect)):
            self.comp_text(expect[i].text, actual[i].getText())

    def test_all_tags(self):
        expect = self.soup.findAll()
        actual = domoper.getAll(self.dom, "*")
        self.assertEqual(len(expect), len(actual))
    
    def test_html(self):
        self.comp_element("html")
    
    def test_header(self):
        self.comp_element("head")
    
    def test_body(self):
        self.comp_element("body")
    
    def test_h2(self):
        self.comp_element("h2")
    
    def test_h1(self):
        self.comp_element("h1")


class TestHtml2(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        with open('test\\test2.html') as f:
            self.soup = BeautifulSoup(f, features="html.parser")
        self.dom = domparser.parse_dom(domparser.flatfile('test\\test2.html'))
    
    def comp_text(self, a, b):
        a = "".join(a.split())
        b = "".join(b.split())
        self.assertEqual(a, b)
    
    def comp_element(self, e):
        expect = self.soup.findAll(e)
        actual = domoper.getAll(self.dom, e)
        self.assertEqual(len(expect), len(actual))
        for i in range(len(expect)):
            self.comp_text(expect[i].text, actual[i].getText())
    
    def test_all_tags(self):
        expect = self.soup.findAll()
        actual = domoper.getAll(self.dom, "*")
        self.assertEqual(len(expect), len(actual))
    
    def test_html(self):
        self.comp_element("html")
    
    def test_header(self):
        self.comp_element("head")
    
    def test_body(self):
        self.comp_element("body")
    
    def test_h2(self):
        self.comp_element("h2")
    
    def test_h1(self):
        self.comp_element("h1")
    
    def test_a(self):
        self.comp_element("a")


class TestHtml3(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        with open('test\\test3.html') as f:
            self.soup = BeautifulSoup(f, features="html.parser")
        self.dom = domparser.parse_dom(domparser.flatfile('test\\test3.html'))
    
    def comp_text(self, a, b):
        a = "".join(a.split())
        b = "".join(b.split())
        self.assertEqual(a, b)
    
    def comp_element(self, e):
        expect = self.soup.findAll(e)
        actual = domoper.getAll(self.dom, e)
        self.assertEqual(len(expect), len(actual))
        for i in range(len(expect)):
            self.comp_text(expect[i].text, actual[i].getText())
    
    def comp_attr(self, e):
        expect = self.soup.find(e).attrs
        actual = domoper.get(self.dom, e).prop
        self.assertEqual(len(list(expect)), len(list(actual)))
        for i in expect:
            self.assertEqual(expect[i], actual[i])

    def test_all_tags(self):
        expect = self.soup.findAll()
        actual = domoper.getAll(self.dom, "*")
        self.assertEqual(len(expect), len(actual))
    
    def test_html(self):
        self.comp_element("html")
    
    def test_header(self):
        self.comp_element("head")
    
    def test_body(self):
        self.comp_element("body")
    
    def test_h2(self):
        self.comp_element("h2")
    
    def test_h1(self):
        self.comp_element("h1")
    
    def test_a(self):
        self.comp_element("a")
    
    def test_input(self):
        self.comp_element("input")
    
    def test_a_attr(self):
        self.comp_attr("a")
    
    def test_input_match(self):
        expect = self.soup.find("input", attrs={"type":"text"}).attrs['type']
        actual = domoper.get(self.dom, "input", attr={"type":"text"}).prop['type']
        self.assertEqual(expect, actual)
        expect = self.soup.find("input", attrs={"type":"password"}).attrs['type']
        actual = domoper.get(self.dom, "input", attr={"type":"password"}).prop['type']
        self.assertEqual(expect, actual)
        expect = self.soup.find("input", attrs={"type":"submit"}).attrs['value']
        actual = domoper.get(self.dom, "input", attr={"type":"submit"}).prop['value']
        self.assertEqual(expect, actual)


class TestHtml5(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        with open('test\\test5.html') as f:
            self.soup = BeautifulSoup(f, features="html.parser")
        self.dom = domparser.parse_dom(domparser.flatfile('test\\test5.html'))
    
    def comp_text(self, a, b):
        a = "".join(a.split())
        b = "".join(b.split())
        self.assertEqual(a, b)
    
    def comp_element(self, e):
        expect = self.soup.findAll(e)
        actual = domoper.getAll(self.dom, e)
        self.assertEqual(len(expect), len(actual))
        for i in range(len(expect)):
            self.comp_text(expect[i].text, actual[i].getText())

    def test_all_tags(self):
        expect = self.soup.findAll()
        actual = domoper.getAll(self.dom, "*")
        self.assertEqual(len(expect), len(actual))
    
    def test_html(self):
        self.comp_element("html")
    
    def test_header(self):
        self.comp_element("head")
    
    def test_body(self):
        self.comp_element("body")
    
    def test_h2(self):
        self.comp_element("h2")
    
    def test_h1(self):
        self.comp_element("h1")

    def test_input(self):
        self.comp_element("input")
    
    def test_spec_a(self):
        expect = self.soup.findAll("a")
        actual = domoper.getAll(self.dom, "a")
        self.assertEqual(len(expect), len(actual))

        expect = self.soup.find("a", attrs={"title": "Go to home"}).text
        actual = domoper.get(self.dom, "a", attr={"title": "Go to home"}).getText()
        self.assertEqual(expect, actual)
    
    def test_match_id(self):
        expect = self.soup.find(attrs={"id":"content"}).text
        actual = domoper.get_element_by_id(self.dom, "content").getText()
        self.comp_text(expect, actual)
    
    def test_match_class(self):
        expect = self.soup.findAll(attrs={"class":"linkcs"})
        actual = domoper.get_elements_by_class(self.dom, "linkcs")
        self.assertEqual(len(expect), len(actual))


class TestExternalHtml(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        targ = "https://duckduckgo.com/"
        self.soup = BeautifulSoup(requests.get(targ).text, features="html.parser")
        self.dom = domparser.parse_url(targ)
    
    def comp_text(self, a, b):
        a = "".join(a.split())
        b = "".join(b.split())
        self.assertEqual(a, b)
    
    def comp_element(self, e):
        expect = self.soup.findAll(e)
        actual = domoper.getAll(self.dom, e)
        self.assertEqual(len(expect), len(actual))
        for i in range(len(expect)):
            self.comp_text(expect[i].text, actual[i].getText())

    def test_all_tags(self):
        expect = self.soup.findAll()
        actual = domoper.getAll(self.dom, "*")
        self.assertEqual(len(expect), len(actual))
    
    def test_html(self):
        self.comp_element("html")
    
    def test_header(self):
        self.comp_element("head")
    
    def test_body(self):
        self.comp_element("body")
    
    def test_h2(self):
        self.comp_element("h2")
    
    def test_h1(self):
        self.comp_element("h1")


if __name__ == "__main__":
    unittest.main()