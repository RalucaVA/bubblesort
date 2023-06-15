import time
st = time.time()

def bubblesort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
  
  
import random;
if __name__ == "__main__":
  data = []
for i in range(4902939):
    #x=random.randrange(0, 500000339783)
    data.append(x)
  
  bubblesort(data)

  for i in range(len(data)):
      print("%d" % data[i], end=" ")

et = time.time()
elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
