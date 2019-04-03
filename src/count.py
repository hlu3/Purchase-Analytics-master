#!/bin/usr/python3

import math

def count_products(products): 
    departments = []
    for row in products:
        # check if the product has been ordered before 
        if int(row['reordered']):
            add = 0
        else:
            add = 1
 
        # find the position where stores this department information 
        i = [i for i,v in enumerate(departments) if v['department_id']==row['department_id']]
 
        if i: 
            dex = i[0]
            departments[dex]['number_of_orders'] += 1
            departments[dex]['number_of_first_orders'] += add
        else: 
            info = {}
            info['department_id'] = row['department_id']
            info['number_of_orders'] = 1
            info['number_of_first_orders'] = add
            departments.append(info)

    # calculate percentage =  number_of_first_orders/number_of_orders
    for row in departments:
        perc = row['number_of_first_orders'] / row['number_of_orders']
        row.update({'percentage' : '%.2f' % perc})

    return departments
