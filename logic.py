from collections import defaultdict

def check_win(curstate):
	win = 0
	for i in range(3):
		if curstate[i][0] == curstate[i][1] == curstate[i][2] == 'O':
			win = "Player wins!!!!!"
		if curstate[0][i] == curstate[1][i] == curstate[2][i] == 'O':
			win = "Player wins!!!!!"

	for i in range(3):
		if curstate[i][0] == curstate[i][1] == curstate[i][2] == 'X':
			win = "Computer wins!"
		if curstate[0][i] == curstate[1][i] == curstate[2][i] == 'X':
			win = "Computer wins!"

	if curstate[0][0] == curstate[1][1] == curstate[2][2] == 'O':
		win = "Player wins!!!!!"
	if curstate[0][2] == curstate[1][1] == curstate[2][0] == 'O':
		win = "Player wins!!!!!"

	if curstate[0][0] == curstate[1][1] == curstate[2][2] == 'X':
		win = "Computer wins!"
	if curstate[0][2] == curstate[1][1] == curstate[2][0] == 'X':
		win = "Computer wins!"

	negcount = 0
	for i in range(3):
		negcount += curstate[i].count('')
	if win == 0 and negcount == 0:
		win = 'Draw!'
	return win

def convert(curstate):
	arr = curstate[:][:]
	for i in range(3):
		arr[i] = tuple(arr[i])
	arr = tuple(arr)
	return arr

def player(curstate, d, nex):
	arr = convert(curstate)

	win = check_win(curstate)
	if win != 0:
		d[arr] = win[0]
		return

	flag = 0
	for i in range(3):
		for j in range(3):
			if curstate[i][j] == '':
				curstate[i][j] = 'O'
				player_pc(curstate, d, nex)
				if flag == 0 and d[convert(curstate)] == 'P':
					d[arr] = 'P'
					flag = 1
				curstate[i][j] = ''

	for i in range(3):
		for j in range(3):
			if curstate[i][j] == '':
				curstate[i][j] = 'O'
				if flag == 0 and d[convert(curstate)] == 'D':
					d[arr] = 'D'
					flag = 1
				curstate[i][j] = ''

	if flag == 0:
		d[arr] = 'C'


def player_pc(curstate, d, nex):
	arr = convert(curstate)

	win = check_win(curstate)
	if win != 0:
		d[arr] = win[0]
		return

	flag = 0
	for i in range(3):
		for j in range(3):
			if curstate[i][j] == '':
				curstate[i][j] = 'X'
				player(curstate, d, nex)
				if flag == 0 and d[convert(curstate)] == 'C':
					d[arr] = 'C'
					nex[arr] = convert(curstate) 
					flag = 1
				curstate[i][j] = ''


	for i in range(3):
		for j in range(3):
			if curstate[i][j] == '':
				curstate[i][j] = 'X'
				if flag == 0 and d[convert(curstate)] == 'D':
					d[arr] = 'D'
					nex[arr] = convert(curstate) 
					flag = 1
				curstate[i][j] = ''

	for i in range(3):
		for j in range(3):
			if curstate[i][j] == '':
				curstate[i][j] = 'X'
				if flag == 0 and d[convert(curstate)] == 'P':
					d[arr] = 'P'
					nex[arr] = convert(curstate) 
					flag = 1
				curstate[i][j] = ''


def solve(curstate):
	w = check_win(curstate)
	if w != 0 and w[0] == 'D':
		return (-1, -1)

	d = defaultdict(str)
	nex = defaultdict(tuple)
	ori = convert(curstate)
	player_pc(curstate, d, nex)

	newstate = nex[convert(curstate)]
	for i in range(3):
		for j in range(3):
			if curstate[i][j] != newstate[i][j]:
				return (i, j)



