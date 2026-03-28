class Intern:
	def __init__(self, name = "My name? I'm nobody, an intern, I have no name"):
		self.name = name
	def __str__(self):
		return self.name
	class Coffee:
		def __str__(self):
			return "This is the worst coffee you ever tasted."
	def work(self):
		raise Exception("I'm just an intern, I can't do that...")
	def make_coffee(self):
		return self.Coffee()
	
if __name__ == '__main__':
	nameless_intern = Intern()
	named_intern = Intern("Mark")
	print(f"Nameless intern: {nameless_intern}")
	print(f"Named intern: {named_intern}")
	print("Hey Mark, make me a coffee will you?")
	print(named_intern.make_coffee())
	print("Hey whatsyername, do some work will you?")
	try:
		nameless_intern.work()
	except Exception as e:
		print(e)