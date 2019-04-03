#!/bin/usr/python3 

def sorting(departments):
    # convert department_id from string to int for sorting 
    for x in departments: 
        x['department_id'] = int(x['department_id'])

    # sort the products list based on department_id in ascending order 
    departments.sort(key=lambda x: x['department_id'], reverse=False)
