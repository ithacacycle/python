if 5 % 3:
    print('真')
else:
    print('假')

sum100=0
counter=0
while counter <=100:
    counter += 1
    if counter % 2 :
        continue
    sum100+=counter
print("result is %d" % sum100)
