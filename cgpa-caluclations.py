print("sem 1")
def mar(n):
    if n <= 100 and n >= 90:

        return 10
    elif n <= 89 and n >= 80:

        return 9
    elif n <= 79 and n >= 70:

        return 8
    elif n <= 69 and n >= 60:

        return 7
    elif n <= 59 and n >= 50:

        return 6
    elif n <= 49 and n >= 0:

        return 0


a = int(input("marks in technical english:\t"))
aaa = mar(a)
b = int(input("marks in maths 1:\t\t"))
bbb = mar(b)
c = int(input("marks in chemistry :\t\t"))
ccc = mar(c)
d = int(input("marks in EEE:\t\t\t"))
ddd = mar(d)
e = int(input("marks in python:\t\t"))
eee = mar(e)
f = int(input("marks in chemistry lab:\t\t"))
f = f * 2
fff = mar(f)
g = int(input("marks in python lab:\t\t"))
ggg = mar(g)

print("sem 2")
z = int(input("marks in maths 2:\t\t"))
zz = mar(z)
y = int(input("marks in physics for engineering:"))
yy = mar(y)
x = int(input("marks in drawing :\t\t"))
xx = mar(x)
p = int(input("marks in digital system :\t"))
pp = mar(p)
q = int(input("marks in c and c++:\t\t"))
qq = mar(q)
r = int(input("marks in data structure :\t"))
rr = mar(r)
s = int(input("marks in physics lab :\t\t"))
s = s * 2
ss = mar(s)
t = int(input("marks in digital system lab :\t"))
tt = mar(t)
u = int(input("marks in data structure lab :\t"))
uu = mar(u)

cgp = aaa * 3 + bbb * 3 + ccc * 4 + ddd * 3 + eee * 3 + fff * 1 + ggg * 2
print("cgp sem 1=\t", cgp)
cgpa = (cgp / 19)
print("cgpa in sem 1=\t", cgpa)

sem2cgp = zz * 3 + yy * 4 + xx * 3 + pp * 3 + qq * 3 + rr * 3 + ss * 1 + tt * 2 + uu * 2
print("cgp sem 2= \t", sem2cgp)
sem2cgpa = (sem2cgp / 24)
print("cgpa sem 2=\t", sem2cgpa)
totalcgpa = (cgp + sem2cgp) / 43
print("total cgpa=\t", totalcgpa)
