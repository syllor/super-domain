#!/usr/bin/python
f = open("en1.txt", 'r')
fw = open("en1.js", 'w')

content = ""
while True:
    line = f.readline()
    if len(line) == 0:
        break
    line = line.strip('\n')
    content = "'"+line+"',"+content
# print content
content = content[:len(content)-1]
js = "dict_en1 = [" + content + "]"
fw.write(js)
f.close()
fw.close()
