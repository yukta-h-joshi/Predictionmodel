import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(42)
years = list(range(2000, 2024))
depth = [5.2, 5.8, 6.1, 6.7, 7.0, 7.4, 7.1, 7.8, 8.2, 8.9,
         9.1, 9.4, 9.0, 9.6, 10.1, 10.8, 11.2, 11.0, 11.6, 12.1,
         12.4, 12.9, 13.1, 13.6]

df = pd.DataFrame({'year': years, 'depth_mbgl': depth})

# Basic trend plot
plt.figure(figsize=(10, 5))
plt.plot(df['year'], df['depth_mbgl'], marker='o', color='steelblue')
plt.title('Groundwater Depth Over Time - Uttarakhand (2000-2023)')
plt.xlabel('Year')
plt.ylabel('Depth (meters below ground level)')
plt.grid(True)
plt.tight_layout()
plt.savefig('groundwater_trend.png')
plt.show()

print(df.describe())
print(f"\nAverage annual depletion: {(depth[-1] - depth[0]) / len(years):.2f} meters/year")
