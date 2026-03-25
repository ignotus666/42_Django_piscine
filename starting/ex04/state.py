import sys


def get_data():
	states = {
		"Oregon" : "OR",
		"Alabama" : "AL",
		"New Jersey": "NJ",
		"Colorado" : "CO"
	}
	capital_cities = {
		"OR": "Salem",
		"AL": "Montgomery",
		"NJ": "Trenton",
		"CO": "Denver"
	}
	return states, capital_cities


def main():
	if len(sys.argv) != 2:
		return

	capital = sys.argv[1]
	states, capital_cities = get_data()

	state_code = None
	for code, city in capital_cities.items():
		if city == capital:
			state_code = code
			break

	if state_code is None:
		print("Unknown capital city")
		return

	for state_name, code in states.items():
		if code == state_code:
			print(state_name)
			return


if __name__ == '__main__':
	main()
