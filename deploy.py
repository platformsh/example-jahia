import json
import base64
import os
import requests
from requests.auth import HTTPBasicAuth

# Edit these as needed.
DX_RELATIONSHIP = 'jahia'

def dx_username():
    return os.getenv('DX_DEPLOY_USERNAME')

def dx_password():
    return os.getenv('DX_DEPLOY_PASSWORD')

def send_install_request(filename):
    url = dx_rest_url()
    auth_info = HTTPBasicAuth(dx_username(), dx_password())
    data = {'start': 'true'}
    with open(filename, 'rb') as jar_handle:
        files = {"bundle": jar_handle}
        response = requests.post(url, files=files, data=data, auth=auth_info)
        response.raise_for_status()
        print "Plugin {} installed and started successfully.".format(filename)

def install_plugins(commands):
    if 'install' in commands.keys():
        for filename in commands['install']:
            send_install_request(filename)

def uninstall_plugins(commands):
    pass

def dx_rest_url():
    platform_relationships = os.getenv('PLATFORM_RELATIONSHIPS')
    if platform_relationships:
        relationships = json.loads(base64.b64decode(platform_relationships).decode('utf-8'))

        # Extract the relationships that we want to expose to the application.
        jahia = relationships[DX_RELATIONSHIP][0]

        url = "http://{}:{}/modules/api/bundles/".format(
            jahia['host'],
            jahia['port'],
        )
        return url

def run():
    with open('deploy.json', 'r') as json_file:
        commands = json.load(json_file)

    install_plugins(commands)
    uninstall_plugins(commands)

run()
