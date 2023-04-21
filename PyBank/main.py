import os
import csv

months_list = []
profit_list = []
total = 0
change_list = []


csvpath = os.path.join('Resources', 'budget_data.csv')
txtpath = os.path.join('Analysis', 'Analysis.txt')
analysis_output = open("Analysis/Analysis.txt","w")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        months_list.append(row[0])

        profit_list.append(row[1])

        total += int(row[1])

    for nr in range(len(months_list)-1):
        change_list.append((int(profit_list[nr+1])) - int(profit_list[nr]))

    max_profit = change_list.index(max(change_list))
    min_loss = change_list.index(min(change_list))

    date_profit = months_list[max_profit]
    date_loss = months_list[min_loss]
    average_change = round(int(sum(change_list))/(int(len(months_list))-1),2)


    print("Financial Analysis")
    analysis_output.write("Financial Analysis\n")

    print("--------------------------------------------------")
    analysis_output.write("--------------------------------------------------\n")

    print(f'Total months: {len(months_list)}')
    analysis_output.write(f'Total months: {len(months_list)} \n')

    print(f'Total: ${total}')
    analysis_output.write(f'Total: ${total} \n')

    print(f'Average change: ${average_change}')
    analysis_output.write(f'Average change: ${average_change} \n')

    print(f'Greatest Increase in Profits: {date_profit} $({max(change_list)})')
    analysis_output.write(f'Greatest Increase in Profits: {date_profit} $({max(change_list)}) \n')

    print(f'Greatest Decrease in Profits: {date_profit} $({min(change_list)})')
    analysis_output.write(f'Greatest Decrease in Profits: {date_profit} $({min(change_list)}) \n')
