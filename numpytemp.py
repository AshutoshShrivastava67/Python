import statistics

temp_week = [22.5, 24.3, 19.8, 23.7, 21.2, 22.1, 20.5]

mean_temp = statistics.mean(temperatures)
median_temp = statistics.median(temperatures)
variance_temp = statistics.variance(temperatures)
std_dev_temp = statistics.stdev(temperatures)

print(f"Temperatures: {temperatures}")
print(f"Mean Temperature: {mean_temp:.2f}°C")
print(f"Median Temperature: {median_temp:.2f}°C")
print(f"Variance of Temperature: {variance_temp:.2f}")
print(f"Standard Deviation of Temperature: {std_dev_temp:.2f}")

with open("temperature_statistics.py", "w") as file:
    file.write(script_content)
print("Python script saved as 'temperature_statistics.py'")
