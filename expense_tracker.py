"""
ExpenseTracker class - Core functionality for managing expenses
"""

import json
import os
from datetime import datetime
from expense import Expense
from utils import print_header


class ExpenseTracker:
    """Main class to manage expense tracking operations"""
    
    def __init__(self, data_file="expenses.json"):
        self.data_file = data_file
        self.expenses = []
        self.load_expenses()
    
    def load_expenses(self):
        """Load expenses from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.expenses = [Expense.from_dict(exp) for exp in data]
            except (json.JSONDecodeError, KeyError):
                print("⚠️  Warning: Could not load expenses. Starting fresh.")
                self.expenses = []
        else:
            self.expenses = []
    
    def save_expenses(self):
        """Save expenses to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump([exp.to_dict() for exp in self.expenses], f, indent=2)
    
    def add_expense(self):
        """Add a new expense"""
        print_header("Add New Expense")
        
        # Get expense details
        description = input("Description: ").strip()
        if not description:
            print("❌ Description cannot be empty!")
            return
        
        try:
            amount = float(input("Amount: $"))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
        except ValueError:
            print("❌ Invalid amount!")
            return
        
        category = input("Category (e.g., Food, Transport, Entertainment): ").strip()
        if not category:
            category = "Other"
        
        # Create and add expense
        expense = Expense(description, amount, category)
        self.expenses.append(expense)
        self.save_expenses()
        
        print(f"\n✅ Expense added successfully! (ID: {expense.id})")
    
    def view_all_expenses(self):
        """Display all expenses"""
        print_header("All Expenses")
        
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return
        
        print(f"\n{'ID':<8} {'Date':<12} {'Description':<20} {'Category':<15} {'Amount':>10}")
        print("-" * 70)
        
        for exp in self.expenses:
            print(exp)
    
    def view_by_category(self):
        """View expenses filtered by category"""
        print_header("View by Category")
        
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return
        
        # Get unique categories
        categories = set(exp.category for exp in self.expenses)
        print("\nAvailable categories:")
        for i, cat in enumerate(sorted(categories), 1):
            print(f"{i}. {cat}")
        
        category = input("\nEnter category name: ").strip()
        
        filtered = [exp for exp in self.expenses if exp.category.lower() == category.lower()]
        
        if not filtered:
            print(f"\n❌ No expenses found in category '{category}'")
            return
        
        print(f"\n{'ID':<8} {'Date':<12} {'Description':<20} {'Category':<15} {'Amount':>10}")
        print("-" * 70)
        
        total = 0
        for exp in filtered:
            print(exp)
            total += exp.amount
        
        print("-" * 70)
        print(f"{'Total:':<55} ${total:>10.2f}")
    
    def view_total_spending(self):
        """Display total spending and breakdown by category"""
        print_header("Total Spending")
        
        if not self.expenses:
            print("📭 No expenses recorded yet.")
            return
        
        total = sum(exp.amount for exp in self.expenses)
        
        # Calculate by category
        category_totals = {}
        for exp in self.expenses:
            category_totals[exp.category] = category_totals.get(exp.category, 0) + exp.amount
        
        print(f"\n{'Category':<20} {'Amount':>15} {'Percentage':>12}")
        print("-" * 50)
        
        for category, amount in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            percentage = (amount / total) * 100
            print(f"{category:<20} ${amount:>14.2f} {percentage:>11.1f}%")
        
        print("-" * 50)
        print(f"{'TOTAL':<20} ${total:>14.2f}")
    
    def delete_expense(self):
        """Delete an expense by ID"""
        print_header("Delete Expense")
        
        if not self.expenses:
            print("📭 No expenses to delete.")
            return
        
        self.view_all_expenses()
        
        expense_id = input("\nEnter expense ID to delete: ").strip()
        
        for i, exp in enumerate(self.expenses):
            if exp.id == expense_id:
                confirm = input(f"Are you sure you want to delete '{exp.description}'? (y/n): ")
                if confirm.lower() == 'y':
                    self.expenses.pop(i)
                    self.save_expenses()
                    print("\n✅ Expense deleted successfully!")
                else:
                    print("\n❌ Deletion cancelled.")
                return
        
        print(f"\n❌ Expense with ID '{expense_id}' not found!")
    
    def export_to_csv(self):
        """Export expenses to CSV file"""
        print_header("Export to CSV")
        
        if not self.expenses:
            print("📭 No expenses to export.")
            return
        
        filename = input("Enter filename (default: expenses.csv): ").strip()
        if not filename:
            filename = "expenses.csv"
        
        if not filename.endswith('.csv'):
            filename += '.csv'
        
        try:
            with open(filename, 'w') as f:
                f.write("ID,Date,Description,Category,Amount\n")
                for exp in self.expenses:
                    f.write(f"{exp.id},{exp.date},{exp.description},{exp.category},{exp.amount}\n")
            
            print(f"\n✅ Expenses exported successfully to '{filename}'!")
        except Exception as e:
            print(f"\n❌ Error exporting to CSV: {e}")
