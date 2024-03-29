# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 17:41:37 2019

@author: dhanasettyabhishek
"""

class Purchase_Analytics(object):
    def main(self):    
        prod_dict = dict()
        try:
            """
            Creating a dictionary to store product_id and department_id information.
            key: product_id
            value: department_id
            """
            with open("./input/products.csv", mode = "r", encoding="utf8") as products:        
                next(products)
                for j in products:
                    j = j.strip().split(",")
                    if int(j[0]) not in prod_dict:
                        prod_dict[int(j[0])] = int(j[-1])
            products.close()
        # If products.csv file doesnot exists.
        except FileNotFoundError:
            print("products.csv file doesnot exists")
            return

        op_pid_reord = dict()
        try:
            """
            Creating a dictionary to store department_id and reordered details.
            key: department_id
            value: list(reordered products)
            """
            with open("./input/order_products.csv", mode = "r", encoding="utf8") as order_products:
                next(order_products)
                for i in order_products:
                    i = i.strip().split(",")
                    if prod_dict[int(i[1])] not in op_pid_reord:
                        op_pid_reord[prod_dict[int(i[1])]] = list()
                        op_pid_reord[prod_dict[int(i[1])]].append(int(i[-1]))
                    else:
                        op_pid_reord[prod_dict[int(i[1])]].append(int(i[-1]))
            order_products.close()
        # If order_products.csv file doesnot exists
        except FileNotFoundError:
            print("order_products.csv file doesnot exists")
            return
        """
        Storing the required information and calculating the number of requests per product.
        """
        output = open("./output/report.csv", mode = "w", encoding="utf8")
        output.write("department_id,number_of_orders,number_of_first_orders,percentage\n")
        for key, value in sorted(op_pid_reord.items(), key = lambda x: x[0]):
            output.write("{},{},{},{}\n".format(str(key), str(len(value)), str(len(value)-sum(value)), "{:.2f}".format(float(len(value)-sum(value))/float(len(value)))))
        output.close()
        
if __name__ == "__main__":
    pa = Purchase_Analytics()
    pa.main()