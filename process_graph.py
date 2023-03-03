import matplotlib.pyplot as plt
# Define max_stride and tickets
max_stride = 12
tickets = {'A': 3, 'B': 2}

# Calculate strides and initial pass values
strides = {proc: max_stride / tickets[proc] for proc in tickets}
pass_values = {proc: strides[proc] for proc in tickets}

# Initialize lists for x and y coordinates of points
x_values = [0]
y_values_A = [pass_values['A']]
y_values_B = [pass_values['B']]

# Iterate over 10 time slots
for i in range(1, 11):
    # Determine which process has the lowest pass value
    min_pass_proc = min(pass_values, key=pass_values.get)
    
    # Update pass value for the process that was chosen
    pass_values[min_pass_proc] += strides[min_pass_proc]
    
    # Append x and y values to the lists
    x_values.append(i)
    y_values_A.append(pass_values['A'])
    y_values_B.append(pass_values['B'])

# Plot the pass values over time
plt.plot(x_values, y_values_A, 'r*-', label='Process A')
plt.plot(x_values, y_values_B, 'mP-', label='Process B')

# Set plot labels and legend
plt.xlabel('Time (quanta)')
plt.ylabel('Pass Value')
plt.title(f'Max stride={max_stride}, Tickets: A={tickets["A"]}, B={tickets["B"]}')
plt.legend()

# Display the plot
plt.show()
