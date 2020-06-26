counter = 0
divisor = 11
min = 100
max = 50000
for i in range(min,max+1):
        t = i/divisor
        tt = round(t)
        ttt = tt - t
        #print(i)
        if ttt == 0:
                counter += 1
                #print(i)
        #print(t)
        #if isinstance(t,long):
         #       counter += 1
          #      print(counter)


print(counter)
