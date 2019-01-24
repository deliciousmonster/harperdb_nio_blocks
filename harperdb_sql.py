from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty)
from nio.block.mixins import EnrichSignals
from .harperdb_base import HarperDBBase

class HarperDBSQL(HarperDBBase, Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    sql = StringProperty(title='SQL Query', default='select * from dev.dog where id = 1', order=2)

    def process_signals(self, signals):
        out_sigs = []
        for signal in signals:
            payload = {
              'operation': 'sql',
              'sql': self.sql(signal)
            }
            result = self.sendQuery(payload)
            for r in result:
                out_sigs.append(self.get_output_signal(r, signal))

        self.notify_signals(out_sigs)


