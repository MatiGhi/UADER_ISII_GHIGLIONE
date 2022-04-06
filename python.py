import sys

if len(sys.argv) == 1:
        # prime number calculator: find all primes up to n
		input("\nBienvenido/a! \nEste Script le permitirá encontrar los Números Primos. Continuamos?")
		max = int(input("Fino a quale numero vuoi trovare Primes? : "))
		primeList = []
		#for loop for checking each number
		for x in range(2, max + 1):
			isPrime = True
			index = 0
			root = int(x ** 0.5) + 1
			while index < len(primeList) and primeList[index] <= root:
				if x % primeList[index] == 0:
					isPrime = False
					break
				index += 1
			if isPrime:
				primeList.append(x)
		print(primeList)
		#-------------------------------------------------------------
		# prime number calculator: find the first n primes
		count = int(input("Quanti numeri primi vuoi trovare?: "))
		primeList = []
		x = 2
		while len(primeList) < count:
			isPrime = True
			index = 0
			root = int(x ** 0.5) + 1
			while index < len(primeList) and primeList[index] <= root:
				if x % primeList[index] == 0:
					isPrime = False
					break
				index += 1
			if isPrime:
				primeList.append(x)
			x += 1
		print(primeList)
elif len(sys.argv) == 2:
    argumentos = sys.argv
    max = int(argumentos[1])
    primeList = []
    for x in range(2, max + 1):
        isPrime = True
        index = 0
        root = int(x ** 0.5) + 1
        while index < len(primeList) and primeList[index] <= root:
            if x % primeList[index] == 0:
                isPrime = False
                break
            index += 1
        if isPrime:
            primeList.append(x)
    print(primeList)
elif len(sys.argv) == 3:
    argumentos = sys.argv
    max = int(argumentos[1])
    primeList = []
    for x in range(2, max + 1):
        isPrime = True
        index = 0
        root = int(x ** 0.5) + 1
        while index < len(primeList) and primeList[index] <= root:
            if x % primeList[index] == 0:
                isPrime = False
                break
            index += 1
        if isPrime:
            primeList.append(x)
    print(primeList)
    #------------------------------------------#
    # prime number calculator: find the first n primes
    count = int(argumentos[2])
    primeList = []
    x = 2
    while len(primeList) < count:
        isPrime = True
        index = 0
        root = int(x ** 0.5) + 1
        while index < len(primeList) and primeList[index] <= root:
            if x % primeList[index] == 0:
                isPrime = False
                break
            index += 1
        if isPrime:
            primeList.append(x)
        x += 1
    print(primeList)