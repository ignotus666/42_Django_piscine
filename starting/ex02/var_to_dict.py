def get_musicians():
	d = [
		('Hendrix', '1942'),
		('Allman', '1946'),
		('King', '1925'),
		('Clapton', '1945'),
		('Johnson', '1911'),
		('Berry', '1926'),
		('Vaughan', '1954'),
		('Cooder', '1947'),
		('Page', '1944'),
		('Richards', '1943'),
		('Hammett', '1962'),
		('Cobain', '1967'),
		('Garcia', '1942'),
		('Beck', '1944'),
		('Santana', '1947'),
		('Ramone', '1948'),
		('White', '1975'),
		('Frusciante', '1970'),
		('Thompson', '1949'),
		('Burton', '1939')
	]
	return d

def to_year_dict(pairs):
	years = {}
	for name, year in pairs:
		years.setdefault(year, []).append(name)
	return years

def main():
	musicians_by_year = to_year_dict(get_musicians())
	for year, names in musicians_by_year.items():
		print(f"{year} : {' '.join(names)}")

if __name__ == '__main__':
	main()
