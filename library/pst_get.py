import requests
import json

from ansible.module_utils.basic import *

def main():
    module = AnsibleModule(argument_spec=dict(
        host_name = dict(type = 'str', required = True),
        item_id = dict(type = 'int', required = True),
        api_key = dict(type = 'str', required = True),
        tls_enable = dict(type = 'bool', default = False)
    ))

    host_name = module.params['host_name']
    item_id = module.params['item_id']
    api_key = module.params['api_key']
    tls_enable = module.params.get('tls_enable')

    if tls_enable:
        protocol = "https"
    else:
        protocol = "http"

    url = '{}://{}/api/items/{}/export'.format(protocol,host_name,item_id)

    payload = {
                'ApiVersion': 1.1,
                'ApiKey': api_key,
                'ExportId': 1
            }

    response = requests.post(url, data=json.dumps(payload))
    result = dict(response = response.text)
    module.exit_json(**result)

if __name__ == '__main__':