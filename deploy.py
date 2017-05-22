import json
import base64
import os
from subprocess import call
import requests
from requests.auth import HTTPBasicAuth

# Edit these as needed.
DX_USERNAME = 'root'
DX_PASSWORD = 'root'
DX_RELATIONSHIP = 'jahia'

platform_relationships = os.getenv('PLATFORM_RELATIONSHIPS')
if platform_relationships:
    relationships = json.loads(base64.b64decode(platform_relationships).decode('utf-8'))

    # Extract the relationships that we want to expose to the application.
    jahia = relationships[DX_RELATIONSHIP][0]

    contextPath = ''

    DX_REST_URL="http://{}:{}/modules/api/bundles/".format(
        jahia['host'],
        jahia['port'],
    )

    #env = dict(os.environ)
    #install = env['JARS_INSTALL'].split()
    #setup = env['JARS_SETUP'].split()
    #start = env['JARS_START'].split()

    # Make this dynamic, or more easily editable, or something.
    filename = 'jahia-module/target/audit-trail-1.0-SNAPSHOT.jar'

    with open(filename, 'rb') as jar_handle:
        #print "File open"
        files = {"bundle": jar_handle}
        data = {'start': 'true'}
        #print "Sending request"
        response = requests.post(DX_REST_URL, files=files, data=data, auth=HTTPBasicAuth(DX_USERNAME, DX_PASSWORD))
        response.raise_for_status()
        #print "Sent request"
        #print "Status: " + str(response.status_code)
