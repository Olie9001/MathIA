import csv
import itertools
import random
import math
import time
from itertools import permutations

##
datafile = "birthdays.csv"
birthday_set_size = 23

num_birthdays = 0           # number of birthdays in the csv file
num_birthdays_sets = 0      # number of birthday sets tested so far
num_birthday_match = 0      # number of tests where two birthdays are the same
info_step = 100000          # print current info every n tests
max_steps = 10000000         # total number of tests 
total_combinations = 0.0    # calculated number of combinations we can make from the birthdays csv    
elapsed_time = 0.0          # current elapsed running time for test

## Print out the current findings
def info():
    print(
        f"Found {num_birthday_match/num_birthdays_sets}% {num_birthday_match} in {num_birthdays_sets} sets of {birthday_set_size} birthdays in {elapsed_time} seconds. Time remaining {((elapsed_time/num_birthdays_sets)*max_steps)-elapsed_time}")

# Check if the list has any duplicates
def anydup(thelist):
    seen = set()
    for x in thelist:
        if x in seen:
            return True
        seen.add(x)
    return False

# load the birthdays from a csv
print(f"Read {datafile}")
birthdays = []
with open(datafile, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        birthdays.append(row[0])
num_birthdays = len(birthdays)
print(f"Read {num_birthdays} birthdays")

fac_n = math.factorial(num_birthdays)
fac_r = math.factorial(birthday_set_size)
fac_nr = math.factorial(num_birthdays-birthday_set_size)
total_combinations = fac_n / (fac_nr*fac_r)
print(f"Total combinations of sets of {birthday_set_size} from a set of {num_birthdays} is {total_combinations}.")

# randomly sample N combinations
start_time = time.process_time()
while(num_birthdays_sets<max_steps):
    p = random.sample(birthdays,birthday_set_size)
    num_birthdays_sets = num_birthdays_sets+1
    if (anydup(p)):
        num_birthday_match = num_birthday_match+1
    if (num_birthdays_sets % info_step == 0):
        elapsed_time = time.process_time() - start_time
        info()    

# generate all permutation of 23 birthdays
# for p in permutations(birthdays, birthday_set_size):
#     num_birthdays_sets = num_birthdays_sets+1
#     if (anydup(p)):
#         num_birthday_match = num_birthday_match+1
#     if (num_birthdays_sets % info_step == 0):
#         info()

info()

# Calculate time to test all combinations
one_step_time = elapsed_time/max_steps;
total_combinations_time = total_combinations*one_step_time
total_combinations_time_h = (total_combinations*one_step_time)/(60*60)
total_combinations_time_d = (total_combinations*one_step_time)/(60*60*24)
total_combinations_time_y = (total_combinations*one_step_time)/(60*60*24*365)

age_of_the_universe = 13770000000
age_of_the_earth = 4543000000
age_of_humans = 300000
total_combinations_time_aou = total_combinations_time_y/age_of_the_universe
total_combinations_time_aoe = total_combinations_time_y/age_of_the_earth
total_combinations_time_aoh = total_combinations_time_y/age_of_humans

print(f"elapsed time {elapsed_time}, num steps {max_steps}")
print(f"Time to test all {total_combinations} combinations from the set of {num_birthdays} birthdays would be {total_combinations_time} seconds.")
print(f"Time to test all {total_combinations} combinations from the set of {num_birthdays} birthdays would be {total_combinations_time_y} years.")
print(f"Which is {total_combinations_time_aou} time the age of the universe.")
print(f"Which is {total_combinations_time_aoe} time the age of the earth.")
print(f"Which is {total_combinations_time_aoh} time the age of the humans.")
