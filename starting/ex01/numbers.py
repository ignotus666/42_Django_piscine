from pathlib import Path


def main():
	file_path = Path(__file__).with_name("numbers.txt")
	content = file_path.read_text(encoding="utf-8").strip()
	for number in content.split(","):
		print(number.strip())


if __name__ == '__main__':
	main()
