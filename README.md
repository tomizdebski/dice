#Dice
##Workshop: The Dice

Board games and paper RPGs use many types of dice, not just the well-known cubic ones. One of the more popular dice, for example, is the ten-sided dice, or even the hundred-sided dice! Since dice are thrown frequently in games, it would be tedious, difficult and waste a lot of paper to write every time "throw two dice, add 20 to the result". In such situations the code "roll 2D10+20" is used.

The code for such a cube looks as follows:

xDy+z
where:

y - the type of dice to be used (e.g. D6, D10),
x - number of dice throws; if we throw once, this parameter is negligible,
z - number to add (or subtract) to the result of the throws (optional).
Examples:

2D10+10: 2 throws of D10, add 10 to the result,
D6: an ordinary throw of a cube,
2D3: a toss of two tridiagonal dice,
D12-1: a throw of D12 dice, subtract 1 from the result.
Write a function that:

accepts this code as a string in a parameter,
recognizes all input data:
type of dice,
number of throws,
modifier,
if the given string is invalid, it will return an appropriate message,
simulates the throws and returns the result.
Dice types found in games: D3, D4, D6, D8, D10, D12, D20, D100.

