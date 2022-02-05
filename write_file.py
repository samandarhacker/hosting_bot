
def write_file_py(chat_id):
	try:
		tekshiruv = open(f"{chat_id}/bots/wikipedia/main.py")
		t = tekshiruv.read()
		t_ = t.split(" ")
		te_ = len(t_)
		te_ = int(te_)
		print(te_)
		if te_ == 1:
			status = True
		else:
			status = True	
	except Exception as e:
		print(e)
		status = False
	if status:
		bot_file = open("bots/wikipedia/main.py","r")
		bot_read = bot_file.read()
		bot_split = bot_read.split(" ")
		open(f"{chat_id}/bots/wikipedia/main.py","w").close()
		e = 0
		for bot_ in bot_split:
			if e == 0:
				bot_ = f"chat_id=\"{chat_id}\"\n"
				e += 1

			print(bot_)
			with open(f"{chat_id}/bots/wikipedia/main.py","a") as a:
				a.write(f"{bot_} ")
