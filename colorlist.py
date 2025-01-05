col1=["red","orange","blue"]
col2=["gren","red"]

for i in range(len(col1)):
    if col1[i] not in col2:
        print(col1[i])