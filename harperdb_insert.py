from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty, Property)
from nio.block.mixins import EnrichSignals
from .harperdb_base import HarperDBBase
import uuid

class HarperDBInsert(HarperDBBase, Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    schema = StringProperty(title='Schema', default='dev', order=2)
    table = StringProperty(title='Table', default='dog', order=3)
    records = Property(title='Records', default='{{ [$.to_dict()] }}', order=4)

    def process_signals(self, signals):
        out_sigs = []
        for signal in signals:
            signal.id = str(uuid.uuid4())
            payload = {
              "schema": self.schema(),
              "table": self.table(),
              "operation": "insert",
              "records": self.records(signal)
            }
            result = self.sendQuery(payload)
            out_sigs.append(self.get_output_signal(result, signal))

        self.notify_signals(out_sigs)

