#!/usr/bin/env python3

"""
A class-based system for rendering html.
"""


# This is the framework for the base class

def render_tags(tag: str, kwarg: dict, self_closing = False) -> tuple:
    space = ""
    if kwarg:
        space = " "
    if self_closing:
        return "<" + tag + space + ",".join([k + '=' + v for k,v in kwarg.items()]) + "/>"
    opening_tag = "<" + tag + space + ",".join([k + '=' + v for k,v in kwarg.items()]) + ">"
    closing_tag = "</" + tag + ">"
    return opening_tag, closing_tag


class Element(object):
    #tag = 'html'
    indent = ""
    self_closing = False
    def __init__(self, content=None, **kwarg):
        self.content = content
        self.content_list = list()
        self.kwarg_dict = kwarg
        if self.self_closing:
            if self.content:
                raise TypeError
            self.content_list = [render_tags(self.tag, self.kwarg_dict, self.self_closing)]
        else:
            if content:
                self.content = content
                self.content_list = [self.tag, self.content, self.tag ]
            else:
                self.content_list = [self.tag, self.tag]
            self.content_list[0], self.content_list[-1] = render_tags(self.tag, self.kwarg_dict)
    def append(self, new_content):
        if type(new_content) == str:
            self.content_list.insert(len(self.content_list) - 1, new_content)
        else:
            self.closing_tag = self.content_list[-1]
            self.content_list = self.content_list[:-1] + new_content.content_list
            self.content_list.append(self.closing_tag)
    def render(self, out_file, cur_ind=""):
        self.cut_ind = cur_ind + self.indent
        for content in self.content_list:
            out_file.write("\n" + self.cut_ind + content + "\n")

class Html(Element):
    tag = "html"
    indent = ""
    def render(self,out_file,cur_ind=""):
        self.cur_ind = cur_ind + self.indent
        out_file.write(self.cur_ind + "<!DOCTYPE html>")
        Element.render(self, out_file, cur_ind="")

class Body(Element):
    tag = 'body'
    indent = "    "
    pass

class P(Element):
    indent = "        "
    tag = 'p'
    pass

class Head(Element):
    indent = "    "
    tag = 'head'
    pass

class OneLineTag(Element):
    indent = ""
    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + self.indent
        for content in self.content_list:
            out_file.write(" " + self.cur_ind + content + " ")

class Title(OneLineTag):
    indent = "        "
    tag = 'title'
    pass

class Hr(Element):
    tag = 'hr'
    self_closing = True
    indent = "        "
    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + self.indent
        self.tag = render_tags(tag, self.kwarg_dict, self.self_closing)
        out_file.write(self.cur_ind + self.tag)

class Br(Element):
    tag = 'br'
    indent = "        "
    self_closing = True
    def render(self, out_file, cur_ind=''):
        self.cur_ind = cur_ind + self.indent
        self.tag = render_tags(tag, self.kwarg_dict, self.self_closing)
        out_file.write(self.cur_ind + self.tag)


class A(Element):
    tag = 'a'
    def __init__(self,link,content):
  #      Element.__init__(self)
        self.link = link
        self.content = content
        self.content_list = ["<{0} href={1}>{2}</{0}>".format(self.tag, self.link,self.content)]


class Ul(Element):
    indent = "            "
    tag = 'ul'
    pass


class Li(Element):
    indent = "            "
    tag = 'li'
    pass

class H(OneLineTag):
    indent = "    "
    tag = 'h'
    def __init__(self, level, header):
        self.level = level
        self.header = header
        self.content_list = ["<{0}{1}>{2}</{0}{1}>" .format(self.tag, self.level, self.header)]


class Meta(OneLineTag):
    indent = "        "
    tag = 'meta'
    self_closing = True
