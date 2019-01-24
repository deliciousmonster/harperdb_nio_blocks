HarperDBValueSearch
===================
Search for records in a target schema/table by attribute value

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
- hash_attribute: the hash_attribute (ex- 'id') of the target table
- search_attribute: specific attribute to search
- search_value: value for you wish to search - wild cards are allowed
- get_attributes: define which attributes you want returned as a List (\['id', 'name', 'email'\]), or use '*' to return all attributes
