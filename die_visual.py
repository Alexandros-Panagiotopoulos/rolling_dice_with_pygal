import pygal
from die import Die
#Create two D6 dice
die1  = Die()
die2 = Die(10)

# Make some rolls and save the results in a list
results = []
for roll_num in range(50000):
    result1 = die1.roll()
    result2 = die2.roll()
    result = result1 + result2
    results.append(result)

# Analyse the results

frequencies = []
for value in range(2,die1.num_sides+die2.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results
hist = pygal.Bar()

hist.title = "results of rolling a D6 and a D10 50000 times"
hist.x_labels = ["2", "3", "4", "5", "6","7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]
hist.x_title = "Results"
hist.y_title = "Frequency of results"

hist.add("D6 + D10", frequencies)
hist.render_to_file('die_visual.svg')
