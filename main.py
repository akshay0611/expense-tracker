"""
Expense Tracker - Main Application
A simple command-line tool to track personal expenses
"""

from expense_tracker import ExpenseTracker
from utils import clear_screen, print_header


def display_menu():
    """Display the main menu options"""
    print("\n" + "="*50)
    print("           EXPENSE TRACKER MENU")
    print("="*50)
    print("1. Add New Expense")
    print("2. View All Expenses")
    print("3. View Expenses by Category")
    print("4. View Total Spending")
    print("5. Delete an Expense")
    print("6. Export to CSV")
    print("7. Exit")
    print("="*50)


def main():
    """Main application loop"""
    tracker = ExpenseTracker()
    
    print_header("Welcome to Expense Tracker!")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == "1":
            clear_screen()
            tracker.add_expense()
        
        elif choice == "2":
            clear_screen()
            tracker.view_all_expenses()
        
        elif choice == "3":
            clear_screen()
            tracker.view_by_category()
        
        elif choice == "4":
            clear_screen()
            tracker.view_total_spending()
        
        elif choice == "5":
            clear_screen()
            tracker.delete_expense()
        
        elif choice == "6":
            clear_screen()
            tracker.export_to_csv()
        
        elif choice == "7":
            print("\n👋 Thank you for using Expense Tracker!")
            print("Goodbye!\n")
            break
        
        else:
            print("\n❌ Invalid choice! Please enter a number between 1 and 7.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
