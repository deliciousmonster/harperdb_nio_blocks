from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty, Property)
from nio.block.mixins import EnrichSignals
from .harperdb_base import HarperDBBase

class HarperDBUpdate(HarperDBBase, Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    schema = StringProperty(title='Schema', default='dev', order=2)
    table = StringProperty(title='Table', default='dog', order=3)
    records = Property(title='Records (Use {{}} to cast to an array)', default='{{ [{"id": 1, "age": $new_age_1}, {"id": 3, "age": $new_age_2}] }}', order=4)

    def process_signals(self, signals):
        out_sigs = []
        for signal in signals:
            payload = {
              'schema': self.schema(),
              'table': self.table(),
              'operation': 'update',
              'records': self.records(signal)
            }
            result = self.sendQuery(payload)
            out_sigs.append(self.get_output_signal(result, signal))

        self.notify_signals(out_sigs)

