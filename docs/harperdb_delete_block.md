HarperDBDelete
==============
Delete records from a target schema/table by hash_value(s)

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
- hash_values: comma-delimited list of hash_values (\[1, 3, 5\]) of the records to be deleted
