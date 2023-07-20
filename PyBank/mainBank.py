import csv

#variables
chgs = [] #changes
total_months = 0
net_total_prof_loss = 0
prev_prof_loss = None
great_incr = {"date": " ", "amount": None} #greatest increase
great_decr = {"date": " ", "amount": None} #greatest decrease

#open/read CSV file
with open ('budget_data.csv', 'r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        total_months +=1
        current_prof_loss = int(row['Profit/Losses'])
        net_total_prof_loss += current_prof_loss
        if prev_prof_loss is not None:
            chg = current_prof_loss - prev_prof_loss
            chgs.append(chg)
            if great_incr["amount"] is None or chg > great_incr["amount"]:
                great_incr = {"date": row["Date"], "amount": chg}
            if great_decr["amount"] is None or chg < great_decr["amount"]:
                great_decr = {"date": row["Date"], "amount": chg}
        prev_prof_loss = current_prof_loss
    
#calculate average change
avg_chg = sum(chgs) / len(chgs)

#print analysis
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total_prof_loss}")
print(f"Average Change: ${avg_chg: .2f}")
print(f"Greatest Increase in Profits: {great_incr['date']} (${great_incr['amount']})")
print(f"Greatest Decrease in Profits: {great_decr['date']} (${great_decr['amount']})")

#export results to txt file
with open('financial_analysis.txt', 'w') as file:
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total_prof_loss}\n")
    file.write(f"Average Change: ${avg_chg: .2f}n")
    file.write(f"Greatest Increase in Profits: {great_incr['date']} (${great_incr['amount']})\n")
    file.write(f"Greatest Decrease in Profits: {great_decr['date']} (${great_decr['amount']})\n")

