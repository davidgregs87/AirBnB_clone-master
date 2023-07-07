#!/usr/bin/python3
import cmd
import sys

class MyConsole(cmd.Cmd):
	prompt = ">>> "

	def do_pld(self, line):
		print("We are having a pld")

	def do_create(self, line):
		print('I have created', line)

	def precmd(self, line):
		# make the app work non-interactively
		if not sys.stdin.isatty():
			print()
#command, other = line.split(' ')
#line = '{} shoes'.format(command)
		if '.' in line:
			line = line.replace('.', ' ').replace('(', '').replace(')', '')
			line = line.split(' ')
			line = "{zero} {one}".format(zero=line[1], one=line[0])
		print(line)
		return cmd.Cmd.precmd(self, line)

	def do_EOF(self, line):
		print()
		return True


if __name__ == "__main__":
	MyConsole().cmdloop()
