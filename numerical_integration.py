"""
Create polynomial ax^2 + bx^3
integrate using rectangle method
solve analytically
plot error vs number of rectangles
repeat with the W1

"""
import matplotlib.pyplot as plt



def f_x(a, b, c, d, mid):
    y = (a * (mid ** 3)) + (b * (mid ** 2)) + (c * mid) + d
    print y
    return y

def midpoint(a, b, c, d, n, dx, upper_bound, lower_bound):
    x_a = lower_bound
    x_b = dx + lower_bound
    step = 0
    step_array = []
    Mn_array = []

    print ("1")

    while x_b <= upper_bound:

        x_b = x_a + dx

        mid = (x_a + x_b) / 2
        y = f_x(a, b, c, d, mid)

        Mn = dx * (y)
        Mn_array.append(Mn)

        step = step + dx
        step_array.append(step)
        print(step)
        x_a = x_b
    midpoint_sum = sum(Mn_array)
    print (Mn_array)
    #print (midpoint_sum)

    plt.plot(step_array, Mn_array)
    plt.ylabel("y-axis")    #midpoint(a, b, c, d, n, i, mid, upper_bound, lower_bound)

    plt.xlabel("x-axis")


"""  INITIALIZE  """

a = 1
b = 2
c = 3
d = 4

""" f(x) = ax^3 + bx^2 + cx + d """

lower_bound = 1
upper_bound = 5
n = 10 #number of rectangles
i = upper_bound - lower_bound
dx = (upper_bound - lower_bound) * 1.00 / n #step size
print upper_bound, lower_bound, dx
#midpoint(a, b, c, d, n, dx, upper_bound, lower_bound)
x_a = lower_bound
x_b = dx + x_a
step = 0
step_array = []
Mn_array = []

print x_a, x_b, dx

while x_b <= upper_bound:

    x_b = x_a + dx

    mid = (x_a + x_b) / 2
    y = f_x(a, b, c, d, mid)

    Mn = dx * (y)
    Mn_array.append(Mn)

    step = step + dx
    step_array.append(step)
    #print(step)
    x_a = x_b
midpoint_sum = sum(Mn_array)
print (Mn_array)
#print (midpoint_sum)

plt.plot(step_array, Mn_array)
plt.ylabel("y-axis")    #midpoint(a, b, c, d, n, i, mid, upper_bound, lower_bound)
plt.xlabel("x-axis")
plt.show()
