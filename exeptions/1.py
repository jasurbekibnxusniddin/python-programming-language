# number = 10
# if number > 5:
#     raise Exception(f"The number should not exceed 5. ({number=})")
# print(number)

# num = 1

# assert (num < 5), f"The number should not exceed 5. ({num=})"

# print(num)

# try:
#     pass
# except Exception as e:
#     print(e)

try:
    print(10/0)
except ZeroDivisionError as e:
    print("Error", e)
else:
    print("else")
finally:
    print("finally")