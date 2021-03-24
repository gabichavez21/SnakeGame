docs : snake_docs other_docs
	firefox snake.html

snake_docs : snake.py
	pydoc3 -w snake

other_docs :
	pydoc3 -w tkinter
	pydoc3 -w random
	pydoc3 -w pygame
	pydoc3 -w sys

pygame :
	python3 -m pip install pygame --user

clean :
	rm -rf *.html __pycache__
