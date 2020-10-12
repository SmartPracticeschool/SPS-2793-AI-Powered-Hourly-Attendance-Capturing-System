# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 22:37:33 2020

@author: Aniket
"""

import boto3
import requests

client=boto3.client('rekognition',
                    aws_access_key_id="ASIAWISGGXYLKIUWBVGE",
                        aws_secret_access_key="5VElgHK2GI9VPKnRFkFVG2v9aBWS8pE67jzN7jXc",
                        aws_session_token="FwoGZXIvYXdzEGIaDCxLE4cWE1tWG7TmIyLUAcaiIRAi90+I5WYqFawXHaAVIcd4iyxBSoU+TFlKMn4JJvrw/goGEw3+NUCSysuhh81RWLOyEVATJn5a28M5MbfPKhSV+MCwBlIPZ1h5NUPjQigVFUBbQs1PkMBaILt1DmUCQoF4mOtMtDi8lMbVIJ2fk5CLgFRAMQE82ogKon9xQlqwIeuqKxKH6FVWoUbgK9ERhoZfI4xJM3TZG1LN3vWmVC4oko+Jr/4iW6z7PC8JNcPiuxC1oJIEj8kc2h45kUKjRfKewcgQAyftqZpwUYvI/QxAKJmP2PsFMi0gcbt6lxPJIw5FrFNzOE8fHEUniJ6honWSZDP6oa8HQ5MLCMOmDHQKainTZjc=",
                        region_name='us-east-1')

with open(r'C:\Users\khala\OneDrive\Desktop\aws\source_1.jpg','rb') as source_image:
    source_bytes=source_image.read()
print(type(source_bytes))

print("Recognition Service")
response = client.detect_custom_labels(
    ProjectVersionArn='arn:aws:rekognition:us-east-1:430717713942:project/attendance/version/attendance.2020-10-01T15.44.51/1601547290907',
   
    Image={
        'Bytes':source_bytes

    },
