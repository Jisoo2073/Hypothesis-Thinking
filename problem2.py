from tkinter import SE

import numpy as np
import math as m
import scipy.stats as stats
from scipy.stats import norm
from scipy.stats import t

myFile = open('city_vehicle_survey.txt')
data1 = myFile.readlines()
data1 = [float(x) for x in data1]
myFile.close()


# code for question 2
print('Problem 2 Answers:')
# code below this line
n = len(data1) # sample size

x_bar = np.mean(data1) # sample mean

s = np.std(data1, ddof=1) # sample standard deviation
    
se = s / np.sqrt(n) # sample standard error

t_score = (x_bar - 5) / se # sample t-score

p_value = 2 * stats.t.cdf(-abs(t_score), n-1)

print("n =", n)
print("mean =", f"{x_bar:.4f}")
print("SE =", f"{se:.4f}")
print("t =", f"{t_score:.4f}")
print("p =", f"{p_value:.4f}")



# code for question 3
print('Problem 3 Answers:')
# code below this line
# find the largest standard error which the test will be significant at a level of 0.05


t_crit = t.ppf(1-0.05/2, n-1) # t_c = t.ppf(p, df)
# degrees of freedom = n - 1

se_max = abs((x_bar - 5) / t_crit)
print("Maximum standard error:", f"{se_max:.4f}")

# minimum sample size too.
s_new = 0.0614 * np.sqrt(1024)
n_min = (s_new / se_max)**2


print("Minimum sample size:", int(n_min))


# code for question 5
print('Problem 5 Answers:')
# code below this line


myFile1 = open('vehicle_data_1.txt')
data1 = myFile1.readlines()

myFile2 = open('vehicle_data_2.txt')
data2 = myFile2.readlines()

data1 = [float(x) for x in data1]
data2 = [float(y) for y in data2]
myFile1.close()
myFile2.close()

# Sample sizes
n1 = len(data1)
n2 = len(data2)

# Sample means
mean1 = np.mean(data1)
mean2 = np.mean(data2)

# Population standard deviations (z-test)
sd1 = np.std(data1, ddof=0)
sd2 = np.std(data2, ddof=0)

# Standard error
se = np.sqrt((sd1**2)/n1 + (sd2**2)/n2)

# z-score
z_score = (mean1 - mean2) / se

# Two-tailed p-value
p_value = 2 * (1 - norm.cdf(abs(z_score)))

# Results
print("Sample size of vehicle_data_1:", n1)
print("Sample size of vehicle_data_2:", n2)

print("Sample mean of vehicle_data_1:", f"{mean1:.4f}")
print("Sample mean of vehicle_data_2:", f"{mean2:.4f}")

print("Standard error:", f"{se:.4f}")
print("Standard score:", f"{z_score:.4f}")
print("p-value =", f"{p_value:.4e}")









