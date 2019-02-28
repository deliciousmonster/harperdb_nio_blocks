from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty)
from nio.block.mixins import EnrichSignals
from .harperdb_base import HarperDBBase

class HarperDBSQL(HarperDBBase, Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    sql = StringProperty(title='SQL Query', default='SELECT id, name, breed FROM dog WHERE age < 10', order=2)

    def process_signal(self, signal, input_id=None):
        _sql = self.sql(signal)
        
        payload = {
          'operation': 'sql',
          'sql': self.sql(signal)
        }

        result = self.sendQuery(payload)

        self.notify_signals(self.get_output_signal({'result': result }, signal))


