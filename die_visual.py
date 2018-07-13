import pygal
from die import Die
#Create a D6
die  = Die()

# Make soem rolls and save the results in a list
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)

# Analyse the results

frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualise the results
hist = pygal.Bar()

hist.title = "results of rolling one D6 1000 times"
hist.x_labels = ["1", "2", "3", "4", "5", "6"]
hist.x_title = "Results"
hist.y_title = "Frequency of results"

hist.add("D6", frequencies)
hist.render_to_file('die_visual.svg')
