# created by ZHANG Jiachen
# simplest AI algorithm - linear regression
# goal equation is y = bx + a

# import
import matplotlib.pyplot as plt

# specify known cases
x = [3,6,5,0,4,5,3,6,5,3]
y = [87,98,100,29,76,89,67,92,79,78]

# specify unknown cases
x_unknown = 2

# intermediate variables
n = len(x)                  # num. of known cases

sum_x_y = 0
sum_x_square = 0
sum_x = 0
sum_y = 0

for i in range(n):
    sum_x += x[i]
    sum_y += y[i]
    sum_x_y += x[i]*y[i]
    sum_x_square += x[i]**2

b = n * sum_x_y - sum_x * sum_y
b = b / (n * sum_x_square - sum_x ** 2)

a = sum_y / n - b * sum_x / n

# make predictions
y_prediction = x_unknown * b + a

print('prediction for unknown case is %f' % y_prediction)

# plot results
plt.plot(x,y,'r^',ms=20)
plt.plot([0,7], [a,7*b+a],'b-')
plt.plot(x_unknown, y_prediction,'ks', ms=20)

plt.xlabel('average num. of hrs. for studying')
plt.ylabel('final exam score')
plt.title('Fig. 3: Prediction of Final Score')
plt.axis([0,7,20,100])
plt.show()
