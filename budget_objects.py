import math


class Category:
    def __init__(self, category_name):
        self.category_name = category_name
        self.ledger_our = {}
        self.ledger = list()
        self.sum_all_values = sum(self.ledger_our.values())  # TO MODIFY
        # self.withdraw_total = list()
        self.withdraw_sum = 0

    def __str__(self):
        self.line1 = self.category_name.center(30, "*")

        max_line_length = 30
        # print(str(self.line1))
        self.line2_2 = str()

        for key in self.ledger_our:
            number = "{:.2f}".format(self.ledger_our[key])
            number_length = len(number)
            if number_length > 7:
                number = number[:7]
            elif number_length <= 7:
                number = number
            number_length = len(number)

            if len(key) > 23 and number_length < 7:
                key = key[:23]
            elif len(key) > 23 and number_length >= 7:
                key = key[:22]
            elif len(key) <= 23 and len(key) > 0:
                key = key
            elif len(key) == 0:  # not sure
                key = "        "

            description_length_initial = len(key)
            description_length_final = max_line_length - number_length
            description = key
            description_padding = 0
            printed_key = 0
            if description_length_final > description_length_initial:  # when it s short
                description_padding = int(
                    max_line_length - number_length - description_length_initial
                )
                description_length_final = description_padding + number_length  # + 1
                printed_key = str(key.ljust(description_length_final, " "))
            elif (
                description_length_final <= description_length_initial
            ):  # when it s too long
                description_length_final = max_line_length - number_length
                printed_key = key[:description_length_final]

            line2 = str(printed_key) + " " + number
            middle_padding = 31 - len(line2)

            if len(line2) < 30:
                line2 = str(printed_key) + " ".ljust(middle_padding, " ") + number
            elif len(line2) >= 30:
                line2 = line2
            self.line2_2 = self.line2_2 + line2 + "\n"

        self.line3 = str("Total: " + str("{:.2f}".format(self.sum_all_values)))
        # it expects a string not 3 print statements

        text = str(self.line1 + "\n" + self.line2_2 + self.line3)
        return text
        # print(self.line3)

        # instance variable called ledger that is a list !!! NOT A DICTIONARY
        # should append an object to the ledger list
        # in the form of {"amount": amount, "description": description}  including the {}

    def deposit(self, y, x=""):
        # ledger_new_entry = str('{"amount": ' + str(y) + ', "description": ' + '"' + x + '"' + '}')
        # ledger_new_entry = str('{"amount": ' + str(y) + ", \"description\": " + "\"" + x + "\"" + "}")
        self.ledger.append({"amount": y, "description": x})
        self.ledger_our[x] = y
        self.sum_all_values = self.sum_all_values + y

    # def check_funds(self, amount):
    #    print(amount)
    # if int(amount) < self.sum_all_values:
    # print('True')
    # return True

    # else:
    # print('False')
    # return False

    def withdraw(self, y, x=""):

        if isinstance(y, int):
            y = int(y)
        elif isinstance(y, float):
            y = float(y)

        if self.sum_all_values > y:
            # ledger_new_entry = str('{"amount": ' + str(-1 * y) + ', "description": ' + '"' + x + '"' + '}')
            # ledger_new_entry = str("{'amount': " + str(-1 * y) + ", 'description': " + "'" + x + "'" + "}")
            self.ledger.append({"amount": (-1 * y), "description": x})
            self.ledger_our[x] = -1 * y
            self.sum_all_values = self.sum_all_values - y

            self.withdraw_sum = self.withdraw_sum - y
            return True

        elif self.sum_all_values < (y):
            # print('False')
            return False

    def get_balance(self):
        # self.sum_all_values_2 = "{:.2f}".format(self.sum_all_values)
        return self.sum_all_values

        # self.sum_all_values_2 = "{:.2f}".format(self.sum_all_values)
        # return self.sum_all_values_2
        # print(self.sum_all_values_2)

    def transfer(self, amount, destination_category):  # food.transfer(200, clothing)
        if self.check_funds(amount):  # amount < self.sum_all_values:
            transfer_description_origin = str(
                "Transfer to " + destination_category.category_name
            )
            transfer_description_destination = str(
                "Transfer from " + self.category_name
            )
            self.withdraw(amount, transfer_description_origin)
            destination_category.deposit(amount, transfer_description_destination)
            return True

        elif self.check_funds(amount) is False:  # amount > self.sum_all_values:

            return False

    def check_funds(self, amount):
        if int(amount) > self.sum_all_values:
            # print(False)
            return False
        elif int(amount) <= self.sum_all_values:
            # print(True)
            return True


# FUNCTION - we have to get all the withdraw values from the classes to the function in a dictinary


def create_spend_chart(categories_list):
    category1 = categories_list[0]
    category2 = False
    category3 = False
    category4 = False

    try:
        category2 = categories_list[1]
    except:
        category2 = False
    try:
        category3 = categories_list[2]
    except:
        category3 = False

    value_list = list()
    names_list = list()
    value1 = category1.withdraw_sum
    name1 = category1.category_name
    value_list.append(value1)
    names_list.append(name1)
    if category2:
        value2 = category2.withdraw_sum
        value_list.append(value2)
        name2 = category2.category_name
        names_list.append(name2)
    if category3:
        value3 = category3.withdraw_sum
        value_list.append(value3)
        name3 = category3.category_name
        names_list.append(name3)
    if category4:
        value4 = category4.withdraw_sum
        value_list.append(value4)
        name4 = category4.category_name
        names_list.append(name4)
    # print(len(value_list))
    # print(value_list)
    total = sum(value_list)
    # print(total)
    percentages_list = list()
    o_list = list()
    # scale_list = ['100| ', ' 90| ', ' 80| ', ' 70| ', ' 60| ', ' 50| ', ' 40| ', ' 30| ', ' 20| ',
    # ' 10| ', '  0| ']
    line1 = "100| "
    line2 = " 90| "
    line3 = " 80| "
    line4 = " 70| "
    line5 = " 60| "
    line6 = " 50| "
    line7 = " 40| "
    line8 = " 30| "
    line9 = " 20| "
    line10 = " 10| "
    line11 = "  0| "
    lines_list = list()

    lines_list.append(line1)
    lines_list.append(line2)
    lines_list.append(line3)
    lines_list.append(line4)
    lines_list.append(line5)
    lines_list.append(line6)
    lines_list.append(line7)
    lines_list.append(line8)
    lines_list.append(line9)
    lines_list.append(line10)
    lines_list.append(line11)
    # print(lines_list)

    o_line = 0
    dashed_lines_number = 0

    for x in value_list:
        dashed_lines_number = dashed_lines_number + 3
        percent = int(math.trunc(x / total * 100) / 10)

        # print(percent)  # this is to check if the percentages are rounded down corectly
        column_length = 0
        #  o_line = str('o' * int(percent))  initial version 12.19 3:20pm
        o_line = str("o" * (int(percent) + 1))
        padding = int(11 - len(o_line))
        oline_appended = o_line.rjust((padding + len(o_line)), " ")
        column_length = len(oline_appended)
        o_line_split = list(
            oline_appended
        )  # this is [' ', ' ', ' ', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        for a in range(column_length):
            lines_list[a] = lines_list[a] + o_line_split[a] + "  "

    dashed_lines_line = str("    -" + "-" * dashed_lines_number)

    # from here downward until for a in lines_list loop we have the column name graph part
    # entertainment
    name_line1 = "     "
    name_line2 = "     "
    name_line3 = "     "
    name_line4 = "     "
    name_line5 = "     "
    name_line6 = "     "
    name_line7 = "     "
    name_line8 = "     "
    name_line9 = "     "
    name_line10 = "     "
    name_line11 = "     "
    name_line12 = "     "
    name_line13 = "     "
    # name_line14 = ('     ')
    name_lines_list = list()

    name_lines_list.append(name_line1)
    name_lines_list.append(name_line2)
    name_lines_list.append(name_line3)
    name_lines_list.append(name_line4)
    name_lines_list.append(name_line5)
    name_lines_list.append(name_line6)
    name_lines_list.append(name_line7)
    name_lines_list.append(name_line8)
    name_lines_list.append(name_line9)
    name_lines_list.append(name_line10)
    name_lines_list.append(name_line11)
    name_lines_list.append(name_line12)
    name_lines_list.append(name_line13)
    # name_lines_list.append(name_line14)

    # !!!!  print   Percentage spent by category

    # print(names_list)
    name_column = 0

    for x in names_list:
        column_length = 13
        padding = int(13 - len(x))
        letters_line_appended = x.ljust((padding + len(x)), " ")
        #    column_length = len(oline_appended)
        letters_line_split = list(
            letters_line_appended
        )  # this is [' ', ' ', ' ', 'o', 'o', 'o', 'o', 'o', 'o', 'o']
        for a in range(column_length):
            name_lines_list[a] = name_lines_list[a] + letters_line_split[a] + "  "

    # end of column name graph part

    # this code block is the initial version where we didnt have one big string, but rather printed each line separately
    # for a in lines_list:
    #    print(a)
    # print(dashed_lines_line)
    # for a in name_lines_list:
    #    print(a)

    # this is the code block where we concatenate everything into one big string
    big_string = str("Percentage spent by category\n")
    for a in lines_list:
        a = str(a + "\n")
        big_string = str(big_string + a)
    dashed_lines_line = str(dashed_lines_line + "\n")
    big_string = str(big_string + dashed_lines_line)
    for a in name_lines_list:
        a = str(a + "\n")
        big_string = str(big_string + a)

    big_string = big_string[:-1]
    # print(big_string)
    return big_string


# 1
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
# food.deposit(900, "deposit")
# food.deposit(45.56)
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")

# food.deposit(900, "deposit")
# food.withdraw(45.67)
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)
# food.deposit(10, "deposit")
# food.deposit(100, "deposit")
# food.withdraw(100.10)
# food.deposit(100, "deposit")
# food.transfer(200, entertainment)
# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.transfer(20, entertainment)

food.deposit(900, "deposit")
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
create_spend_chart([business, food, entertainment])


# food.deposit(900, "deposit")
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.deposit(45.56)
print(food.ledger[1])
print(food.get_balance())
# food.check_funds(945.56)

print(food.ledger)

# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)

print(food)
# print(clothing)

# food.deposit(45.56)
# food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")
# food.withdraw(45.67)

# print(food)
# print(food.withdraw_total)
# print(food.withdraw_sum)

# food.get_balance()
# food.check_funds(5000)


# entertainment.deposit(988324, 'initial deposit to clothes')
# entertainment.withdraw(432, 'buy pizza')
# entertainment.withdraw(100)
# entertainment.withdraw(988, 'tomatoes')
# entertainment.withdraw(2345, 'icecream')


# print(entertainment)
# print(clothing.ledger)


# print('transfering...')
# food.get_balance()
# clothing.get_balance()
# print(food.ledger.values())
# print(food.sum_all_values)
# print(food.category_name)


# create_spend_chart([food, entertainment])
