import os
import csv


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_file)
    revenue = []
    date = []
    change_rev = []
    for row in csvreader:
        revenue.append(float(row[1]))
        date.append(row[0])

print('Financial Analysis')
print('----------------------------')
print("Total Months:", len(date))
print("Total: ", sum(revenue))

for i in range(1,len(revenue)):
        change_rev.append(revenue[i] - revenue[i-1])   
        avg_rev_change = (sum(change_rev)/len(change_rev))

        max_rev_change = max(change_rev)

        min_rev_change = min(change_rev)

        max_rev_change_date = str(date[change_rev.index(max(change_rev))])
        min_rev_change_date = str(date[change_rev.index(min(change_rev))])


print("Avereage Revenue Change: $", round(avg_rev_change, 2))
print("Greatest Increase in Revenue:", max_rev_change_date,"($", max_rev_change,")")
print("Greatest Decrease in Revenue:", min_rev_change_date,"($", min_rev_change,")")

output_file = os.path.join('analysis', 'analysis.txt')

output_file = os.path.join('analysis', "finance_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('Financial Analysis\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total Months: {len(date)}\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Total:, {sum(revenue)}\n')
    datafile.write('-------------------------\n')
    datafile.write(f'Avereage Revenue Change: $, {round(avg_rev_change, 2)}\n')
    datafile.write(f'Greatest Increase in Revenue:, {max_rev_change_date}, ${max_rev_change,}\n')
    datafile.write(f'Greatest Decrease in Revenue:, {min_rev_change_date}, ${min_rev_change,}\n')
    datafile.write('-------------------------\n')