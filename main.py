#!/usr/bin/env python
# coding: utf-8

# In[61]:


import requests
# from xml.etree import ElementTree
import xml.etree.ElementTree as ET
import json
import pandas as pd   


# In[2]:


ApiToken = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
FormID='F1.672008'


# In[72]:


url="https://apac.fieldview.viewpoint.com/FieldViewWebServices/WebServices/JSON/API_FormsServices.asmx"
#headers = {'content-type': 'application/soap+xml'}
headers = {'content-type': 'text/xml'}
body = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <GetForm xmlns="https://localhost.priority1.uk.net/Priority1WebServices/JSON">
      <apiToken>"""+ApiToken+"""</apiToken>
      <formId>"""+FormID+"""</formId>
    </GetForm>
  </soap:Body>
</soap:Envelope>"""

response = requests.post(url,data=body,headers=headers)
namespaces = {
    'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
    'a': 'https://localhost.priority1.uk.net/Priority1WebServices/JSON',
}
response_data=ET.fromstring(response.text)
extract_data = response_data.findall('./soap:Body'
                    '/a:GetFormResponse'
                    '/a:GetFormResult',
                   namespaces,)
for extract in extract_data:
    output = json.loads(extract.text)
    #print(output['FormInformation'])
    df= pd.json_normalize(output['FormInformation'])

print(df.head(10))
