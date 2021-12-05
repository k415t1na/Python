import re




def main():

	used = []
	with open('input.csv', 'r') as csv_file:

		for row in csv_file:
			proces_row = row.split(',')
			row = proces_row[0].strip()
			col = proces_row[1].strip()

			seat = [row,col]

			col_pattern = re.compile(r'^([0-1]?[0-9]|20)$')
			row_pattern = re.compile(r'^(100|[1-9][0-9]?)$')


		
			if col_pattern.match(col) and row_pattern.match(row):
				if seat not in used:
					used.append(seat)
				else:
					print("Indeed there is a duplicate: ", seat)


			# else just ignore that row
			







		

if __name__ == "__main__":
	main()
