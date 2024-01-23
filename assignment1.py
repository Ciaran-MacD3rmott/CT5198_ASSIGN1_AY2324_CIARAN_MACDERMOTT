# Ciaran MacDermott

# import necessary libraries
import math
import statistics

# input function
sales_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


def customer_data_input():
    # initialising list

    customer_data = []

    # error handling for str etc.

    while True:
        try:
            for i in sales_week:
                daily_sales = int(input(f'Number of customers for {i}:'))
                customer_data.append(daily_sales)
            return customer_data

        except ValueError:
            print('You must only enter numeric data, please start again')
            customer_data = []


# Analysis Function to return dictionary of results


def quick_analysis(user_data):

    analysis_outputs = {

        "minimum_amount": min(user_data),
        "maximum_amount": max(user_data),
        "rounded_mean": math.floor(statistics.mean(user_data)),
        "weekly_total": sum(user_data)
    }
    return analysis_outputs


def main():
    customer_traffic = customer_data_input()
    print(f'\nCustomer traffic for the week: {customer_traffic}')

    analysis_results = quick_analysis(customer_traffic)

    # in-built function to return dictionary pairs as tuples
    for key, value in analysis_results.items():
        print(key, value)


if __name__ == '__main__':
    main()


