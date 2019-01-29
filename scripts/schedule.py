from threading import Timer
import sys


def teste():
	print "hello"


def run_scheduled_task(arg):
    timer = Timer(10, teste)
    timer.start()

def main():
	run_scheduled_task(1)
	print "do stuff"
if __name__=='__main__':
	main()