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

def build_lookup(states, capital_cities):
    code_to_state = {}
    for state_name, state_code in states.items():
        code_to_state[state_code] = state_name
    lookup = {}
    for code, city in capital_cities.items():
        state = code_to_state.get(code)
        if state:
            pair = (state, city)
            lookup[state.lower()] = pair
            lookup[city.lower()] = pair
    return lookup

def clean_strings(arg_str):
    cleaned_values = []
    for cap_or_state in arg_str.split(","):
        clean = " ".join(cap_or_state.split())
        if clean:
            cleaned_values.append(clean)
    return cleaned_values

def all_in():
    if len(sys.argv) != 2:
        return

    lookup = build_lookup(states, capital_cities)
    for cap_or_state in clean_strings(sys.argv[1]):
        found = lookup.get(cap_or_state.lower())
        if not found:
            print(f"{cap_or_state} is neither a capital city nor a state")
            continue
        print(f"{found[1]} is the capital of {found[0]}")

if __name__ == '__main__':
    all_in()
