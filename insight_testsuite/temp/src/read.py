#!/bin/usr/python3

import csv

def read_files(orders_path, products_path):
 
    products = []
    # read in and save orders information
    with open(orders_path) as csv_file:
         csv_reader = csv.DictReader(csv_file)
         for row in csv_reader:
             info = {}
             info['product_id'] = row['product_id']
             info['reordered'] = row['reordered']
             products.append(info)
    

    # read in and save products information 
    with open(products_path) as csv_file2:
         csv_reader2 = csv.DictReader(csv_file2)
         for row in csv_reader2: 
             # find the position where the product is saved in the products list
             i = [i for i,x in enumerate(products) if x['product_id']==row['product_id']]
          
             if i:
                 dex = i[0]
                 products[dex].update({'department_id' : row['department_id']})
             else:
                 print('product not found')
             
    return products
