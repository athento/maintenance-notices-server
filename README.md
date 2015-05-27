## Synopsis

This is a django server to show maintenance notices in any system. It uses a REST API to get and create notices. It may be managed using Ansible.

## Code Example

```python
@json_response
def get(request, domain):
....
def create(request):
....
@login_required(login_url='/login/')
def index(request):
```
## Motivation

We created this server to be a relay between Ansible and Nuxeo servers. This server stores notices for a Nuxeo plugin.

## Installation



## API Reference



## Tests


