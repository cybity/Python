cubles = [i**3 for i in range(5)]

sq_2 = [i*2 for i in range(20)]

evens = [i**2 for i in range(10) if i**2 % 2 == 0]

print(cubles)

print(sq_2)

print(evens)

"""
Given a word as input, output a list, containing only the letters
of the word that are not vowels.
The vovels are a,e,i,o,u.

Sample Input :- awesome
Smple Output :- ['w','s','m']

"""
word = input("Enter your word:-")

vowels = ['a','e','i','o','u','A','E','I','O','U']

ls = []

for i in word:
    if i not in vowels:
        ls.append(i)
print(ls)