from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty)
from nio.block.mixins import EnrichSignals
from .harperdb_base import HarperDBBase

class HarperDBValueSearch(HarperDBBase, Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    schema = StringProperty(title='Schema', default='dev', order=2)
    table = StringProperty(title='Table', default='dog', order=3)
    hash_attribute = StringProperty(title='Hash Attribute', default='id', order=4)
    search_attribute = StringProperty(title='Search Attribute', default='name', order=5)
    search_value = StringProperty(title='Search Value', default='Harper', order=6)
    get_attributes = StringProperty(title='Get Attributes', default='*', order=7)

    def process_signals(self, signals):
        out_sigs = []
        for signal in signals:
            payload = {
              'schema': self.schema(),
              'table': self.table(),
              'operation': 'search_by_value',
              'hash_attribute': self.hash_attribute(),
              'search_attribute': self.search_attribute(),
              'search_value': self.search_value(),
              'get_attributes': self.get_attributes()
            }
            result = self.sendQuery(payload)
            for r in result:
                out_sigs.append(self.get_output_signal(r, signal))

        self.notify_signals(out_sigs)

