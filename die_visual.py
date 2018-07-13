import pygal
from die import Die
#Create two D6 dice
die1  = Die()
die2 = Die()

# Make soem rolls and save the results in a list
results = []
for roll in range(1000):
    result1 = die1.roll()
    result2 = die2.roll()
    result = result1 + result2
    results.append(result)

# Analyse the results

frequencies = []
for value in range(1,die1.num_sides+die1.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results
hist = pygal.Bar()

hist.title = "results of rolling two D6 1000 times"
hist.x_labels = ["1", "2", "3", "4", "5", "6","7", "8", "9", "10", "11", "12"]
hist.x_title = "Results"
hist.y_title = "Frequency of results"

hist.add("D6 + D6", frequencies)
hist.render_to_file('die_visual.svg')
