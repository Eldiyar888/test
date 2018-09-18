text = ("Python;the;best")
maxlenght = 0
spl_line = text.split(";")
for i in spl_line:
      if len(i) > maxlenght:
            maxlenght = len(i)

for i in spl_line:
      if len(i) == maxlenght:
          print(i)

