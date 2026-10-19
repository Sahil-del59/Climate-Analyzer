import numpy as np
#load file to file handle
f=np.loadtxt("climate_data.csv",delimiter=",",skiprows=1)
years=f[:,0]#exract year from file
months=f[:,1]#extract month from file
temperatures=f[:,2]#extract temperature from file
print("loaded temperatures",temperatures)

#calculate basic stats using numpy
avg_temp=np.mean(temperatures)
max_temp=np.max(temperatures)
min_temp=np.min(temperatures)

print("climate report summary")
print(f"average temperature of year {avg_temp:.2f}°C")
print(f"maximum temperature of year {max_temp}°C")
print(f"minimum temperature of year {min_temp}°C")

#exporting data to a new file
with open("climate_report.txt","w") as fh:
    fh.write("climate report summary---\n")
    fh.write(f"average temperature of year {avg_temp:.2f}°C")
    fh.write(f"average temperature of year {avg_temp:.2f}°")
    fh.write(f"maximum temperature of year {max_temp}°C")
    fh.write(f"minimum temperature of year {min_temp}°C")

print("report succesfull")


