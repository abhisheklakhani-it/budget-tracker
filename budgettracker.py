import matplotlib.pyplot as plt

class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}
        self.total_expenses = 0

    def add_income(self, amount):
        self.income += amount
        print(f"Income added: ${amount:.2f}")

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        self.total_expenses += amount
        print(f"Expense added: ${amount:.2f} in category '{category}'")

    def get_balance(self):
        return self.income - self.total_expenses

    def summary(self):
        print(f"\nTotal Income: ${self.income:.2f}")
        print(f"Total Expenses: ${self.total_expenses:.2f}")
        print(f"Balance: ${self.get_balance():.2f}")
        print("Expenses by Category:")
        for category, amount in self.expenses.items():
            print(f"  {category}: ${amount:.2f}")

    def visualize_expenses(self):
        if not self.expenses:
            print("No expenses to visualize.")
            return

        categories = list(self.expenses.keys())
        amounts = list(self.expenses.values())

        plt.figure(figsize=(10, 6))
        plt.pie(amounts, labels=categories, autopct='%1.1f%%', startangle=140)
        plt.title("Expenses by Category")
        plt.axis('equal')
        plt.show()

    def visualize_income_vs_expenses(self):
        data = {'Income': self.income, 'Expenses': self.total_expenses}
        names = list(data.keys())
        values = list(data.values())

        plt.figure(figsize=(10, 6))
        plt.bar(names, values, color=['green', 'red'])
        plt.title("Income vs. Expenses")
        plt.ylabel('Amount ($)')
        plt.show()

def main():
    tracker = BudgetTracker()

    def add_income():
        try:
            amount = float(input("Enter income amount: $"))
            tracker.add_income(amount)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def add_expense():
        category = input("Enter expense category: ")
        try:
            amount = float(input("Enter expense amount: $"))
            tracker.add_expense(category, amount)
        except ValueError:
            print("Invalid input. Please enter a number.")

    def show_summary():
        tracker.summary()

    def visualize_expenses():
        tracker.visualize_expenses()

    def visualize_income_vs_expenses():
        tracker.visualize_income_vs_expenses()

    def exit_program():
        print("Exiting the program.")
        exit(0)

    choices = {
        '1': add_income,
        '2': add_expense,
        '3': show_summary,
        '4': visualize_expenses,
        '5': visualize_income_vs_expenses,
        '6': exit_program
    }

    while True:
        print("\n1. Add Income")
        print("2. Add Expense")
        print("3. Show Summary")
        print("4. Visualize Expenses by Category")
        print("5. Visualize Income vs Expenses")
        print("6. Exit")
        choice = input("Choose an option: ")

        action = choices.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
