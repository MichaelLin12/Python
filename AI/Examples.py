import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Example 1
"""
x = [i for i in range(100)]
x = np.array(x)
x = 2 * np.pi* x * 0.01
y = np.sin(x) 
plt.plot(x,y)
plt.title('Sin Plot')
plt.xlabel('x')
plt.ylabel('Sin')
plt.show()
"""
# Example 2
"""
x = np.linspace(-np.pi, np.pi, 50) 
y1 = np.sin(x)
y2 = np.cos(x) 
plt.plot(x, y1, color = 'blue', marker = "s", label='Sin') 
plt.plot(x, y2, color = 'red', marker = "o", label='Cos')
plt.legend()
plt.show()
"""

# Example 3
"""
x = [i for i in range(100)]
x = np.array(x)
y1 = 3 * x + 5
y2 = 2 * x + 1
y3 = x + 9
plt.plot(x, y1, color = 'blue', marker = "s", label='3x+5')
plt.plot(x, y2, color = 'red', marker = "o", label='2x+1')
plt.plot(x, y3, color = 'green', marker = "v", label='x+9')
plt.legend()
plt.show()
"""
 
# Example 4
"""
data = {'Name':    ['Tony','Robert','John','Alice'],
        'Age':     [18,24,19,21],
        }
 
df = pd.DataFrame (data, columns = ['Name','Age'])
 
print (df)
df.to_csv('test.csv', index=False)
"""