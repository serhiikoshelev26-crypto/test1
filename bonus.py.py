import  time
times = 10000000
a = 1000000
total1 = 0
total2 = 0
print('Початок обчислення за допомогою "time": ')
for i in range(10):

    sum1 = a
    sumtime = time.perf_counter()
    for i in range(times):
        sum1 += 3
    sumfinish = time.perf_counter() - sumtime


    minu = a
    minutime = time.perf_counter()
    for j in range(times):
        minu /= 3
    minufinish = time.perf_counter() - minutime



    total1 += sumfinish
    total2 += minufinish
total1 = total1 / 10
total2 = total2 / 10

print(f"Середній час додавання: {total1}")
print(f"Середній час ділення: {total2}")
print(f"Середня різниця: {abs(total1 - total2)}")

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------")
print('Обчислення за допомогою "timeit": ')
import timeit

a = 1000000
timess = 10000000
def dod():
    return a + 3
def dil():
    return a / 3

dodtime = timeit.repeat(dod, number=timess, repeat=10)
diltime = timeit.repeat(dil, number=timess, repeat=10)


print(f"Середній час додавання: {sum(dodtime) / len(dodtime)}")
print(f"Середній час ділення: {sum(diltime) / len(diltime)}")
print(f"Середня різниця: {abs(sum(dodtime) / len(dodtime) - sum(diltime) / len(diltime))}")

print("Обчислення завершено.")


