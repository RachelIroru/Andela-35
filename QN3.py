def check_if_binary_number(RACHEL):
    if False in ([digit == '0' or digit == '1' for digit in RACHEL] or len(RACHEL)==4):
        return False
    else:
        return RACHEL

def binary_numbers(RACHEL):
	numbers_list = RACHEL.split(',')
	numbers_divisable_by_5 = ""
	for number in numbers_list:
		if check_if_binary_number(number):
			if int(number)%5 == 0:
				if numbers_divisable_by_5 == "":
					numbers_divisable_by_5 = str(number)
				else:
					numbers_divisable_by_5 += "," + str(number)

	return numbers_divisable_by_5

binary_string = "1000,0001,1010,1100"
print(binary_numbers(binary_string))