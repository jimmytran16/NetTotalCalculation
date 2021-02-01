#open the data.txt file containing the data sets , and read the lines
file = open('sampledata.txt','r')
Lines = file.readlines()

#close the file
file.close()

# var to count to weeks
counter = 0

# iterate through each line, splitting it by a ' ' char to turn it into an array
# get the total costs, and total income and get difference to get the total net income
for line in Lines:
	payment_arr = line.split(' ')
	payment_arr_to_int = [float(numeric_string) for numeric_string in payment_arr]
	total_costs = payment_arr_to_int[0] + payment_arr_to_int[1] + payment_arr_to_int[2] + payment_arr_to_int[3] + payment_arr_to_int[4] + payment_arr_to_int[5] + payment_arr_to_int[6]
	total_income = payment_arr_to_int[7] + payment_arr_to_int[8]
	total_net = total_income - total_costs
	print('Week {} TOTAL NET: {}'.format(counter,total_net)) # print total net income with corresponding week
	counter = counter + 1

print('\n\nWeeks TOTAL: {}'.format(counter))
