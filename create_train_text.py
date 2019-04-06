import csv

with open("500_Person_Gender_Height_Weight_Index.csv", 'r') as input, open('modified_data.csv', 'w') as output:
    reader = csv.reader(input, delimiter = ',')
    writer = csv.writer(output, delimiter = ',')

    all = []
    row = next(reader)
    row.insert(0, 'ID')
    all.append(row)
    for k, row in enumerate(reader):
        all.append(['Person00' + str(k+1)] + row)
    writer.writerows(all)

csv_file = input('Enter the name of your input file: ')
txt_file = input('Enter the name of your output file: ')
with open(txt_file, "w") as my_output_file:
    with open(csv_file, "r") as my_input_file:
        [my_output_file.write("\t".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()