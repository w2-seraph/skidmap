import time
from yaspin import yaspin


with yaspin(text=f"Counting... ") as sp:
	# Support all basic termcolor text colors
	sp.color = 'blue'

	num_lines = sum(1 for line in open('/home/xs/searx/dorks_out.txt'))

	time.sleep(299)

	num_lines2 = sum(1 for line in open('/home/xs/searx/dorks_out.txt'))

	num3 = num_lines2-num_lines

	DPH = num3*12

	print(f"{DPH}/h")
	f0 = open("/media/xs/dorks-h.txt", "w")
	f0.write(f"{DPH}/h")
	f0.close()
