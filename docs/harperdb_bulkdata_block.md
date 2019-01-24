HarperDBBulkData
================
Import large data sets from csv into the specified table in HarperDB. You may select the source of the csv data, be it a signal, a local file, or a URL.

> *Note*: The data attribute for 'csv_file_load' refers to the location of the file relative to the database daemon- not where the service using this block is running.

>If the file isn't accessible to the database daemon, it won't be able to load it via 'csv_file_load'.

>To import a file from a nio node using this block:
> - read the file in using the nio [CSV block](https://github.com/nio-blocks/csv_files)
> - feed that output into this block and use the 'csv_data_load' operation, instead.

Properties
----------
- ssl: https or http
- server: server hostname or address
- port: server port number
- credentials: UID and PWD used for database authentication
- allow_redirects: allow query to be redirected to another server (rare)
- timeout: amount of time to wait before returning an error (default: 15s)
- schema: schema within which the target table is located
- table: the table into which the data will be loaded
- newdata: the raw csv data, local file, or remote url to be loaded into the target table
