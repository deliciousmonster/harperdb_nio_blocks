from nio.block.base import Block
from nio.properties import (VersionProperty, StringProperty, SelectProperty, Property)
from nio.block.mixins import EnrichSignals
from .harperdb_base import HarperDBBase
from enum import Enum

class Operation(Enum):
    DATA = 'csv_data_load'
    FILE = 'csv_file_load'
    URL = 'csv_url_load'

class HarperDBBulkData(HarperDBBase, Block, EnrichSignals):

    version = VersionProperty('0.1.0')
    operation = SelectProperty(Operation, title='Data Source', default=Operation.DATA, order=2)
    schema = StringProperty(title='Schema', default='dev', order=3)
    table = StringProperty(title='Table', default='dog', order=4)
    data = Property(title='Data (escaped string, file, or url)', default='{{ $data }}', order=5)

    def process_signals(self, signals):
        out_sigs = []
        for signal in signals:
            payload = {
              'schema': self.schema(),
              'table': self.table(),
              'action': 'insert',
              'operation': self.operation().value,
            }
            if self.operation() is Operation.DATA:
                payload['data'] = self.data(signal).replace('\\n', '\n')
            if self.operation() is Operation.FILE:
                payload['file_path'] = self.data(signal)
            if self.operation() is Operation.URL:
                payload['csv_url'] = self.data(signal)
            result = self.sendQuery(payload)
            job_result = self.get_job_result(result["message"].replace("Starting job with id ",""))
            out_sigs.append(self.get_output_signal(job_result, signal))

        self.notify_signals(out_sigs)

