#!/bin/src/python3

from read import read_files
from count import count_products
from sort import sorting
from write import write_files

orders_path = './input/order_products.csv'
products_path = './input/products.csv'
products = read_files(orders_path, products_path)

departments = count_products(products)

sorting(departments)

output_path = './output/report.csv'
write_files(output_path, departments)

