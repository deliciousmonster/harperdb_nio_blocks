HarperDBSQL
===========
Update records into a target schema/table

Properties
----------
- ssl: https or http
- server: server hostname or address
- port: server port number
- credentials: UID and PWD used for database authentication
- allow_redirects: allow query to be redirected to another server (rare)
- timeout: amount of time to wait before returning an error (default: 15s)
- sql: a raw sql query to be executed against the specified database instance
