from echo_demo import echo

'''referencing echo from another file because will eventually want to 
separate code into separate files. The if __name__ = "__main__" allows you to not execute the other
lines in the echo.py file and just execute whatever that is under when you call the echo.py. But, 
in this file, it only runs the echo not the other code about yelling something from a mountain. 
When printing this file in the console, it will just output hi from outside the file'''

print(echo("hi"), "from outside file")