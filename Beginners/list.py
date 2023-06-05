user = ['Frey', 'Prince','Hacker']
game  = ['soccer', 'Tic Tac Toe', 'Snack', 'Puzzle', 'Really']


game[1] = "GTA" # list ---> mutable 

names = int(input("Index of the user:-"))
choice = int(input("Index of the game:-"))

print(user[names])
print(game[choice])


bitch = "Aagya"     # immutable 
print(bitch[0])

x = "Nishant"

print(x[3]+x[4]+x[6])