# To plot multipal plots in same frame.
import matplotlib.pyplot as plt

sub =["Python", "SDD", "Info-Sec", "Marketing"]
marks = [74, 74, 72, 69]

plt.figure(figsize=(10,5))

plt.subplot(1, 2, 1)
plt.bar(sub, marks)
plt.title("Bar Chart") 
plt.xlabel("Subject") 
plt.ylabel("Marks")

plt.subplot(1,2,2)
plt.pie(marks, labels=sub, autopct='%1.1f%%')
plt.title("Pie Chart")


plt.show()