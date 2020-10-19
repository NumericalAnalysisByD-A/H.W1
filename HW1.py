import sys

# Solution for phrase abs(a*(b/c-d)-e)
print("Please enter numbers that will allow you to get a solution for the phrase as follows: abs(a*(b/c-d)-e)")
a = float(input("a ="))
b = float(input("b ="))
c = float(input("c ="))
d = float(input("d ="))
e = float(input("e ="))

print(abs(a*(b/c-d)-e) - sys.float_info.epsilon)

# How we found the epsilon and what value was obtained
print(f"My machine precision is: {sys.float_info.epsilon}")