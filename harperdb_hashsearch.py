from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty, Property)
from nio.block.mixins import EnrichSignals
from .harperdb_base import HarperDBBase

class HarperDBHashSearch(HarperDBBase, Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    schema = StringProperty(title='Schema', default='dev', order=2)
    table = StringProperty(title='Table', default='dog', order=3)
    hash_attribute = StringProperty(title='Hash Attribute', default='id', order=4)
    hash_values = Property(title='Hash Values', default='1, 3', order=5)
    get_attributes = StringProperty(title='Get Attributes', default='name, breed', order=6)

    def process_signals(self, signals):
        out_sigs = []
        for signal in signals:
            payload = {
              'schema': self.schema(),
              'table': self.table(),
              'operation': 'search_by_hash',
              'hash_attribute': self.hash_attribute(),
              'hash_values': self.hash_values(signal).replace(" ","").split(","),
              'get_attributes': self.get_attributes()
            }
            result = self.sendQuery(payload)
            for r in result:
                out_sigs.append(self.get_output_signal(r, signal))

        self.notify_signals(out_sigs)

