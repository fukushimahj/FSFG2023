
with open('FSFG2023.csv',encoding='utf-8') as f:
    lines = f.readlines()

data = {}
i = 0
for line in lines:
  d = line.split(",")
  if(d[5] == "招待講演"):
    print("[[\"",d[0], "\",\"", d[2], "\",\"", "I", "\",\"", d[6], "\"]]")
  else:
    print("[[\"",d[0], "\",\"", d[2], "\",\"", "N", "\",\"", d[6], "\"]]")

