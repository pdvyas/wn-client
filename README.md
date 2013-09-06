# wn-client

### Talk to wn framework over HTTP

## Install

```
pip install git+https://github.com/webnotes/wn-client
```

## Usage

```
In [1]: from wn_client import WNClient

In [2]: wn = WNClient('http://localhost:8000/server.py', 'Administrator', 'admin')

In [3]: wn.insert([{'doctype':'ToDo', 'description':'Try out wn-client'}])
Out[3]: 
[{u'creation': u'2013-09-06 15:33:22',
  u'description': u'Try out wn-client',
  u'docstatus': 0,
  u'doctype': u'ToDo',
  u'localname': u'',
  u'modified': u'2013-09-06 15:33:22',
  u'modified_by': u'Administrator',
  u'name': u'TDI00000004',
  u'owner': u'Administrator'}]

In [4]: wn.get_doc('ToDo', name='TDI00000004')
Out[4]: 
[{u'assigned_by': None,
  u'checked': None,
  u'creation': u'2013-09-06 15:33:22',
  u'date': None,
  u'description': u'Try out wn-client',
  u'docstatus': 0,
  u'doctype': u'ToDo',
  u'idx': None,
  u'modified': u'2013-09-06 15:33:22',
  u'modified_by': u'Administrator',
  u'name': u'TDI00000004',
  u'owner': u'Administrator',
  u'parent': None,
  u'parentfield': None,
  u'parenttype': None,
  u'priority': None,
  u'reference_name': None,
  u'reference_type': None,
  u'role': None}]
```
