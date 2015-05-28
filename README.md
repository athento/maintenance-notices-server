## Synopsis

This is a django server to show maintenance notices in any system. It uses a REST API to get and create notices. It may be managed using Ansible.

## Example



## Motivation

We created this server to be a relay between Ansible and Nuxeo servers. This server stores notices for a Nuxeo plugin.

## Installation

This is a simple Django server. For deploying please refer to [Django documentation](https://docs.djangoproject.com/en/1.8/howto/deployment/)

## API Reference

### GET

Get your domain message using this url: "http://msg.server.com/index/get/your.domain.com/"

### CREATE

Create a domain message using this curl command (or similar):

```bash
curl http://msg.server.com/index/create/ \
--data "domain=your.server.com\$Default Domain 2" \
--data "message=<p>Server is going down for maintenance at 10:00 UTC. </p>" \
--data "user=manager" \
--data "start_date=2015-05-24 00:00" \
--data "end_date=2015-06-5 00:00"
```

### DELETE

Feature not implemented yet. Use web interface to delete messages.