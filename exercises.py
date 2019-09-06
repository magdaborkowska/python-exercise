

print((9*7) + (5*7))
print((17*6) - (9*7 + 5*7))


x = 2
y = x
print(y)


mv_population = 74728
mv_area = 11.995
mv_density = mv_population / mv_area
print(mv_density)




reservoir_volume = 4.445e8
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff
rainfall *= .9

# add the rainfall variable to the reservoir_volume variable
reservoir_volume = reservoir_volume + rainfall

# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm
reservoir_volume *= 1.05

# decrease reservoir_volume by 5% to account for evaporation
reservoir_volume *= .95

# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.
reservoir_volume -= 2.25e5

# print the new value of the reservoir_volume variable
print(reservoir_volume)

print(int(49.7))

print(float(3520 + 3239))




age = 14
is_teen = age > 12 and age < 20
print(is_teen)




sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area

# Write code that prints True if San Francisco is denser than Rio, and False otherwise

is_more_dense = sf_population/sf_area > rio_population/rio_area
print(is_more_dense)




username = "Yogesh"
timestamp = "16:20"
url = "http://petshop.com/pets/reptiles/pythons"

print(username + " " + "accessed the site" + " " + url + " " + "at" + " " + timestamp + ".")





mon_sales = "121"
tues_sales = "105"
wed_sales = "110"
thurs_sales = "98"
fri_sales = "95"

#TODO: Print a string with this format: This week's total sales: xxx
# You will probably need to write some lines of code before the print statement.

weekly_sales = int(mon_sales) + int(tues_sales) + int(wed_sales) + int(thurs_sales) + int(fri_sales)
weekly_sales = str(weekly_sales)

print("This week's total sales: " + weekly_sales)




# Write two lines of code below, each assigning a value to a variable

gender = "girl"
thing = "flowers"

# Now write a print statement using .format() to print out a sentence and the
#   values of both of the variables

print("Every {} likes red {}." .format(gender, thing))




verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"
print(verse)

# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!

print("The lenght of the string variable verse is {} characters.".format(len(verse)))

print("The first occurence of the word 'and' is at the {}th index.".format(verse.find('and')))

print("The last occurence of the word 'you' is at the {}th index.".format(verse.rfind('you')))

print("The word 'you' occurs {} times in the verse.".format(verse.count('you')))







verse = "If you can keep your head when all about you\nAre losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\nBut make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\nAnd yet don’t look too good, nor talk too wise:"
print(verse)

message = " The lenght of the string variable verse is {} characters.\n The first occurence of the word 'and' is at the {}th index.\n The last occurence of the word 'you' is at the {}th index.\n The word 'you' occurs {} times in the verse."

lenght = len(verse)
first_idx = verse.find('and')
last_idx = verse.rfind('you')
count = verse.count('you')

print(message.format(lenght, first_idx, last_idx, count))







