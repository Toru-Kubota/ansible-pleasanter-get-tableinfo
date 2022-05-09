## pst-get ansible module
Ansible module that exports pleasanter tables.


## Require
requests module must be installed in the running environment.
```sh
pip install requests
```
The ansible server and ansible client must be Linux servers.
We have confirmed the operation in the following environment.

* ansible server
Linux:Amazon Linux release 2
ansible:2.11.11
python:3.7.10

* ansible client
Linux:AlmaLinux release 8.5
python:Python 3.6.8

## Get started
Please set the following parameters.
Required except protocol

| variable | Description | Required | Default | Type |
| ------ | ------ | ------ | ------ | ------ |
| host_name | pleasanter server address |yes| - | string |
| api_key | api key to access pleasanter  | yes | - | string |
| item_id | table number you want to get | yes | - | int |
| protocol | True means https False means http access | No | False | bool |

If you set the parameters "host_name is 192.168.1.1:8080", "item_id is 1234",
request URL will be http://192.168.1.1:8080/api/items/1234/export


execute the ansible-playbook command.
```sh
ansible-playbook -i inventory sample.yml
```

## Example

### inventory.ini
```sh
[servers]
192.168.1.100

[servers:vars]
ansible_ssh_user=ansible
ansible_ssh_pass=ansible
ansible_python_interpreter=/usr/bin/python3
host_name=192.168.1.100:80
item_id=12345
api_key=*********************************************************************************
```
### sample.yml
```sh
---
- hosts: servers

  tasks:
    - name: Get pleasanter's table information
      pst_get:
        host_name: "{{ host_name }}"
        item_id: "{{ item_id }}"
        api_key: "{{ api_key }}"
      register: result

    - debug:
       var: result
```

### ansible-playbook command
```sh
ansible-playbook -i inventory sample.yml
```