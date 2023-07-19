# Dependencies
import csv
import os

# Get the current directory
current_directory = os.path.dirname(__file__)

# Path to the budget data file
budget_data_path = os.path.join(current_directory, 'resources', 'budget_data.csv')

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
profit_changes = []
greatest_increase = ['', 0]
greatest_decrease = ['', 0]

# Read the budget data file
with open(budget_data_path, 'r') as file:
    csvreader = csv.reader(file, delimiter=',')
    header = next(csvreader)  # Skip the header row

    for row in csvreader:
        # Count the total number of months
        total_months += 1

        # Calculate the net total amount of profit/losses
        current_profit_loss = int(row[1])
        net_total += current_profit_loss

        # Calculate the change in profit/losses
        if total_months > 1:
            profit_change = current_profit_loss - previous_profit_loss
            profit_changes.append(profit_change)

            # Find the greatest increase and decrease in profits
            if profit_change > greatest_increase[1]:
                greatest_increase = [row[0], profit_change]
            elif profit_change < greatest_decrease[1]:
                greatest_decrease = [row[0], profit_change]

        previous_profit_loss = current_profit_loss

# Calculate the average change
average_change = sum(profit_changes) / len(profit_changes)

# Print the financial analysis results
print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")

# Define the path to the output text file
output_file_path = os.path.join(current_directory, 'analysis', 'results.txt')

# Export the financial analysis results to a text file
with open(output_file_path, 'w') as output_file:
    output_file.write("Financial Analysis\n")
    output_file.write("--------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${net_total}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# Print a message indicating the successful export of the results
print(f"Results exported to: {output_file_path}")
