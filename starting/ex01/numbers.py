def main():
	with open("numbers.txt", "r", encoding="utf-8") as file:
		numbers_string = file.read().strip()
	for number in numbers_string.split(","):
		print(number.strip())

if __name__ == '__main__':
	main()
