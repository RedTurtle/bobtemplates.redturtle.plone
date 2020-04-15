# -*- coding: utf-8 -*-


class RegEntry(object):
    def __init__(self):
        self.template = ''
        self.plonecli_alias = ''
        self.depend_on = None
        self.deprecated = False
        self.info = ''


def buildout_redturtle():
    reg = RegEntry()
    reg.template = 'bobtemplates.redturtle.plone:buildout_redturtle'
    reg.plonecli_alias = 'buildout_redturtle'
    return reg
