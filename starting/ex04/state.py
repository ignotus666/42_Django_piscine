import sys

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

def main():
	if len(sys.argv) != 2:
		return

	capital = sys.argv[1]
	states_by_code = {code: state for state, code in states.items()}
	for code, city in capital_cities.items():
		if city == capital:
			print(states_by_code[code])
			return

	print("Unknown capital city")

if __name__ == '__main__':
	main()
