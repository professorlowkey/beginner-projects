# Python credit card validator

sum_odd = 0
sum_even = 0
total = 0

# step 1

card_number = input("enter credit card #: ")
card_number = card_number.replace("-", "")
card_number = card_number.replace(" ", "")
card_number = card_number[::-1]

# step 2
for x in card_number[::2]:
    sum_odd += int(x)

# step 3
for x in card_number[1::2]:
    x = int(x) * 2
    if x >= 10:
        sum_even += int(1 + (x % 10))
    else:
        sum_even += int(x)

# step 4
total = sum_even + sum_odd

# step 5
if total % 10 == 0:
    print("valid")
else:
    print("not valid")
