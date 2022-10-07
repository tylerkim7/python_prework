#Question 1
def hello_name(user_name):
    print(f'hello_{user_name.upper()}!')


#Question 2
def first_odds():
    numbers = list(range(101))
    for number in numbers:
        if number % 2 == 1:
            print(number)
        else:
            continue
    return


#Question 3
def max_num_in_list(a_list):
    x = sorted(a_list)
    print(x[-1])


#Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        return True
    elif a_year % 400 == 0 and a_year % 100 == 0:
        return True
    else:
        return False


#Question 5
def is_consecutive(a_list):
    sorted_list = sorted(a_list)
    consecutive_list = list(range(min(a_list), max(a_list)+1))
    if sorted_list == consecutive_list:
        return True
    else:
        return False