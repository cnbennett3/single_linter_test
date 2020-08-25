num = 39
if num > 1:
    for i in range(2, num):
    if (num % i) == 0:
<<<<<<< HEAD
        print(num, " is not a prime.")
        print(i, " times ", num//i, " is ", num, ".")
        break
    else:
        print(num, " is a prime.")
=======
      print(num, " is not a prime.")
      print(i," times ", num//i, " is ", num, ".")
       break
    else:
      print(num, " is a prime.")
>>>>>>> f0dea593c73d3d79ddfb566205f4a74905914cc6
else:
    print(num, " is not a prime.")
