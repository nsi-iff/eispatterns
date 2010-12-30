#from domain.multiton import multiton
from domain.configurable import Configurable

class ResourceConfiguration(Configurable):

    template_configuration_text = '[A/An] <resource mask> version <resource mask version> is [a/an] <type>, <description>, measured by <unit>'

    def __init__(self):
        Configurable.__init__(self)
        self.unit = None

    def parse(self, configuration_text):
        #elesbom code goes here
        return 0

