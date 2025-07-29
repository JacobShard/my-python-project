# tracker.py

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

FILENAME = "expense_tracker/expenses.csv"

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.today().strftime('%Y-%m-%d')
    category = input("Enter category (e.g., Food, Transport): ")
    description = input("Enter description: ")
    amount = input("Enter amount: ")

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])
        print("✅ Expense added.")

def view_expenses():
    try:
        with open(FILENAME, mode='r') as file:
            reader = csv.reader(file)
            print("\nDate\t\tCategory\tDescription\tAmount")
            print("-" * 50)
            for row in reader:
                print("\t".join(row))
    except FileNotFoundError:
        print("⚠️ No expenses recorded yet.")

def filter_by_category():
    category_input = input("Enter category to filter by: ").lower()

    print(f"\n{'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>8}")
    print("-" * 60)

    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[1].lower() == category_input:
                date, category, desc, amount = row
                print(f"{date:<12} {category:<12} {desc:<20} £{amount:>6}")
                total += float(amount.replace('£', '').replace('$', ''))

    print("-" * 60)
    print(f"{'Filtered Total':<46} £{total:.2f}\n")

def filter_by_date():
    date_input = input("Enter date to filter by (YYYY-MM-DD): ")

    print(f"\n{'Date':<12} {'Category':<12} {'Description':<20} {'Amount':>8}")
    print("-" * 60)

    total = 0
    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row and row[0] == date_input:
                date, category, desc, amount = row
                print(f"{date:<12} {category:<12} {desc:<20} £{amount:>6}")
                total += float(amount.replace('£', '').replace('$', ''))

    print("-" * 60)
    print(f"{'Filtered Total':<46} £{total:.2f}\n")

def show_totals_by_category():
    totals = {}

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                _, category, _, amount = row
                amount = float(amount.replace('£', '').replace('$', ''))
                totals[category] = totals.get(category, 0) + amount

    print("\nCategory Totals:")
    for category, total in totals.items():
        print(f"• {category.capitalize():<12} : £{total:.2f}")

    print(f"{'=' * 30}\nTotal Spend     : £{sum(totals.values()):.2f}\n")

def show_pie_chart():
    totals = {}

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                _, category, _, amount = row
                amount = float(amount.replace('£', '').replace('$', ''))
                totals[category] = totals.get(category, 0) + amount

    if not totals:
        print("No data to show.")
        return

    plt.figure(figsize=(6, 6))
    plt.pie(totals.values(), labels=totals.keys(), autopct='%1.1f%%')
    plt.title("Spending by Category")
    plt.show()

def show_bar_chart_by_date():
    try:
        df = pd.read_csv(FILENAME, names=["Date", "Category", "Description", "Amount"])
        df["Amount"] = pd.to_numeric(df["Amount"], errors="coerce")
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df.dropna(subset=["Date", "Amount"], inplace=True)

        summary = df.groupby("Date")["Amount"].sum().reset_index()
        plt.figure(figsize=(8, 5))
        plt.bar(summary["Date"].dt.strftime('%Y-%m-%d'), summary["Amount"], color='skyblue')
        plt.title("Daily Spending Totals")
        plt.xlabel("Date")
        plt.ylabel("Amount (£)")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error generating chart: {e}")

def main():
    while True:
        print("\n==== Expense Tracker ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. View Totals by Category")
        print("4. Show Spending Pie Chart")
        print("5. Filter by Category")
        print("6. Filter by Date")
        print("7. Show Bar Chart by Date")
        print("8. Exit")

        choice = input("Choose an option (1-8): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_totals_by_category()
        elif choice == "4":
            show_pie_chart()
        elif choice == "5":
            filter_by_category()
        elif choice == "6":
            filter_by_date()
        elif choice == "7":
            show_bar_chart_by_date()
        elif choice == "8":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
