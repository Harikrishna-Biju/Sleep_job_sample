import logging
import os
import requests
import json
import time

# TODO: make this an environment variable, not hard-coded 
apikey = ""
    

def upload_test_results(report_file):

    github_actions_url = os.environ.get('GITHUB_ACTIONS_URL','None')
    logging.debug('Github Actions URL: ' + github_actions_url)
    
    url = "https://qtmcloud.qmetry.com/rest/api/automation/importresult"
    qmetry_headers = {
        "Content-Type": "application/json",
        "apiKey": apikey
    }
    environ = os.getenv('TEST_ENV', 'dev')
    data = {
        "format": "JUNIT",
        "isZip": False,
        "attachFile": False,
        "fields": {
            "testCycle":{
				"summary": "Acceptance Tests",
				"description": "Acceptance Tests",
				"status": "Done"
			}
		},
        "matchTestSteps": False
    }

    response = requests.post(url, headers=qmetry_headers, data=json.dumps(data))
    
    ## if response code is does not have status code of 200 family then return
    if response.status_code not in range(200, 210):
        logging.info('Failed to upload test results to QMetry')
        return
    
    tracking_Id = response.json()['trackingId']

    # Upload file
    url = response.json()['url']
    headers = {'Content-Type': 'multipart/form-data'}
    files = {
        'file': ('report.xml', open(report_file, 'rb'), 'text/xml')
    }

    upload_response = requests.put(url, headers=headers, files=files)

    # Get the result
    url = f"https://qtmcloud.qmetry.com/rest/api/automation/importresult/track?trackingId={tracking_Id}"
    headers = {"Content-Type": "application/json", "apiKey": apikey}
    upload_response = requests.get(url, headers=headers)

    # If processStatus value is not 'SUCCESS' then wait for 10 seconds and try again for 10 times
    count = 0
    while count < 2:
        if upload_response.status_code == 200 and upload_response.json().get('processStatus') == 'SUCCESS':
            break
        time.sleep(10)
        upload_response = requests.get(url, headers=headers)
        count += 1

    #logging.info('QMetry report import status:' + response.json()['importStatus'])