HarperDBHashSearch
==================
Search for records in a target schema/table by hash value

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
- hash_attribute: the specific hash_attribute (ex- 'id') against which to search
- hash_values: List of hash_values (\[1, 3, 5\]) for which to search
- get_attributes: define which attributes you want returned as a List (\['id', 'name', 'email'\]), or use '*' to return all attributes
