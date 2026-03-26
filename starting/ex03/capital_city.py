import sys

def get_data():
	states = {
		"Oregon": "OR",
		"Alabama": "AL",
		"New Jersey": "NJ",
		"Colorado": "CO"
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

	state_name = sys.argv[1]
	states, capital_cities = get_data()

	state_code = states.get(state_name)
	if state_code is None:
		print("Unknown state")
		return

	print(capital_cities[state_code])

if __name__ == '__main__':
	main()
