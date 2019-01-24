HarperDBUpdate
==============
Update records into a target schema/table

Properties
----------
- ssl: https or http
- server: server hostname or address
- port: server port number
- credentials: UID and PWD used for database authentication
- allow_redirects: allow query to be redirected to another server (rare)
- timeout: amount of time to wait before returning an error (default: 15s)
- schema: schema within which the target table is located
- table: table from which the targeted records will be deleted
- records: comma-delimited list of record objects (\[{}, {}, {}\]) containing AT LEAST a hash value and one additional attribute to update
