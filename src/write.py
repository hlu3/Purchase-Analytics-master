#!/bin/usr/python3

import csv 

def write_files(output_path, departments):
    # save the products information into a file
    with open(output_path, mode='w') as csv_file: 
         fieldnames = ['department_id', 'number_of_orders', 'number_of_first_orders', 'percentage']
         writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
         writer.writeheader()
         writer.writerows(departments)
