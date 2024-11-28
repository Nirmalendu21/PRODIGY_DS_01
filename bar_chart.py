import matplotlib.pyplot as plt
import numpy as np

# Generate a sample dataset for age distribution (e.g., 1000 people)
np.random.seed(0)
ages = np.random.randint(18, 80, size=1000)  # Ages between 18 and 80

# Create a histogram for age distribution
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=15, color='skyblue', edgecolor='black')
plt.title('Age Distribution in a Population')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
