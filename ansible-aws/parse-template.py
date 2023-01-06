#!/usr/bin/env python3
#
# This script pulls the parameters from F5 cft/arm templates for use in Ansible playbook
#

import json

# Open the f5 CFT or ARM template file
with open('./raw-template.json') as json_file:  
    # Import the file as a JSON object
    data = json.load(json_file)
    # Loop through each parameter (p) in the parameters section
    for p in data['Parameters']:
        elements = data['Parameters'][p]
        # For each parameter, loop through each element (e)
        for e in elements:
            # If the element name is equal to Default, AllowedValues, Description or ConstraintDescription then print it's value.  
            # but if the value is a list, convert it to a string.  
            # or if the value is an integer (int), also convert to a string. 
            # then print the line.
            if e in ('Default', 'AllowedValues', 'Description', 'ConstraintDescription'):
                value = elements[e]
                if type(value) is list:
                    value = ''.join(value)
                if type(value) is int:
                    value = str(value)
                #print (p + ':  "' + e + ' ' + value + '"')
                print (p + ':  "'  + value + '"')


