import math as m
import numpy as np
import scipy.stats as stats

# import or paste dataset here
data = np.array([135, 140, 130, 145, 150, 138, 142, 137, 136, 148, 141, 139, 143, 147, 149, 134, 133, 146, 144, 132])


# code for Question 1
print('Problem 1 Answers:')
# code below this line
n = len(data)

# Sample mean
x_bar = np.mean(data)

# Sample standard deviation
s = np.std(data, ddof=1)

# Standard error
SE = s / np.sqrt(n)

# Confidence level
c = 0.90
df = n - 1

# Critical t-value
t_c = stats.t.ppf(1 - (1-c)/2, df)

# Margin of errora
ME = t_c * SE

# Confidence interval
lower = x_bar - ME
upper = x_bar + ME

print("Sample Mean =", f"{x_bar:.4f}")
print("Standard Error =", f"{SE:.4f}")
print("t-score =", f"{t_c:.4f}")
print("90% CI = (", f"{lower:.4f}, {upper:.4f})")


# code for Question 2
print('Problem 2 Answers:')
# code below this line
c = 0.95
df = n - 1

t_c = stats.t.ppf(1 - (1-c)/2, df)

ME = t_c * SE

lower = x_bar - ME
upper = x_bar + ME

print(f"standard error = {SE:.4f}")
print(f"t-score = {t_c:.4f}")

print("95% CI = (", f"{lower:.4f}, {upper:.4f})")

# code for Question 3
print('Problem 3 Answers:')
# code below this line
sigma = 5 # population standard deviation

SE = sigma / np.sqrt(n)
z_c = stats.norm.ppf(1 - (1-c)/2)

ME = z_c * SE

lower = x_bar - ME
upper = x_bar + ME

print("Standard error =", f"{SE:.4f}")
print("z-score =", f"{z_c:.4f}")
print(f"95% CI = ({lower:.4f}, {upper:.4f})")