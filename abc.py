"""Double letters
The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row.
For example, the string "hello" has l twice in a row,
while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter.
The parameter is a string.
Your function must return True if there are two identical letters in a row in the string,
and False otherwise.
"""

# def double_letters(a):
#     for i in range(len(a) - 1):
#         if a[i] == a[i + 1]:
#             print("true")
#             exit()
#     print("false")
#     exit()
#
#
# double_letters("ab")


"""Write a function named add_dots that takes a string and adds "." in between each letter.
For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function,
write another function named remove_dots that removes all dots from a string.
For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct,
calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
"""
# def add_dot(a):
#     return '.'.join(a)
#
# def remove_dot(a):
#     return a.replace(".", "")
#
# a = "dell"
# print(add_dot(a))
# print(remove_dot(add_dot(a)))
#
# a = 1234
# print(a)
# x = 0
# while a != 0:
#     div = a % 10
#     x = x * 10 + div
#     a//=10
#
# print(x)
#
"""
Define a function named count that takes a single parameter. 
The parameter is a string. 
The string will contain a single word divided into syllables by hyphens, such as these:

"ho-tel"
"cat"
"met-a-phor"
"ter-min-a-tor"
Your function should count the number of syllables and return it.

For example, the call count("ho-tel") should return 2."""
# d = "abc"
#
#
# def counta(d):
#     if str('-') in a:
#         b = a.count('-')
#         c = b + 1
#     print(c)
# counta(d)

n = "mr Amey"
print(n)
x = n.lstrip("mr ")
print(x)
