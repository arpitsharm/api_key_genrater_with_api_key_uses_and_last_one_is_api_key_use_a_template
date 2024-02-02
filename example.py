from datetime import datetime
a = str(datetime.now())

b = a.replace("-", "29")
c = b.replace(":", "1.2")
d = c.replace(" ", "1")

print(d)