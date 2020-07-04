
file = open("Greek.txt", mode='r', encoding='UTF-8')

edits = []
for i in range(0,24):
    line = file.readline()
    if not line: break
    temp = line.split()
    edit = ["    //"+temp[0],"\n    const std::string", temp[1]+"(\""+temp[2]+"\");"]
    edits.append(edit)

for i in range(0,24):
    line = file.readline()
    if not line: break
    temp = line.split()
    edit = ["    //"+temp[0],"\n    const std::string", temp[1].lower()+"(\""+temp[2]+"\");"]
    print(edit)
    edits.append(edit)
print('\u03BC')
file.close()

file  =open("Greekedit.txt", mode='w', encoding='UTF-8')


for edit in edits:
    for word in edit:
        file.write(word+" ")
    file.write("\n")

file.close()