guess = int(input("guess a number"))
secret = 10
while guess != secret:
	if guess % 2 == 1:
		print("try again the secret number is even")
	elif guess > 20:
		print("try again the secret number is less than 20")
	guess = int(input("guess again"))
