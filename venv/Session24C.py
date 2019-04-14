import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))

jobs = [100, 80, 60]
domains = ["IT", "Marketing", "Accounts"]

plt.pie(jobs, labels=domains)
plt.legend()
plt.show()