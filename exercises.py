

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










