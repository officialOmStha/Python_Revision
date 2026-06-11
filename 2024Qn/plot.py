import matplotlib.pyplot as plt

plt.subplot(1,2,1)
plt.title("Bar chart")
plt.bar(["Apple", "Ball", "Cartoon"], [82,97,108])
plt.xlabel("Things")
plt.ylabel("Cost")

plt.subplot(1,2,2)
plt.title("Pie Chart")
plt.pie([50,30,20], labels=["Apple", "Ball", "Cartoon"], autopct="%1.1f%%")



plt.show()