import csv


f = open("out.txt")
x = f.readlines()
s = []


for i in x:
	i = i.replace(",", "")
	j = i.replace(" ", ",")
	s.append(j)

print(s)

def save(name, journal_data):
	filename = get_full_pathname(name)
	print("...Saving to : {}".format(filename))

	with open(filename, 'w') as fout:
		for entry in journal_data:
			fout.write(entry + '\n')
# csvex = csv.writer(open("csvexport", "w"), delimiter=',' , quoting=csv.QUOTE_ALL)
# csvex.writerow(s)


# with open('jdv.txt', 'r') as in_file:
#     stripped = (line.strip() for line in in_file)
#     lines = (line.split(",") for line in stripped if line)
#     with open('jdv.csv', 'w') as out_file:
#         writer = csv.writer(out_file)
#         writer.writerows(lines)