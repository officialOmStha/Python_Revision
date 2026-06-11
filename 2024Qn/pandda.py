import pandas as pd

data = {
    "Name" : ["Ram", "Shyam", "Hari", "Sita"],
    "age" : [18,20,22,18]
}

df = pd.DataFrame(data)
print(df)