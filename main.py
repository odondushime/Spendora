## Necessary Python Libraries
## CLI: Command Line Interface
import os
import sys
import argparse

## Making sure the project root directory is in the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

## Importing the necessary modules
from db.connection import get_db_connection
from models.transaction import TransactionManager
from models.category import CategoryManager
from reports.summary import generate_summary 

def setup_parser():
    """Setup the command line parser"""
    parser = argparse.ArgumentParser(description='Spendora - Personal Expense Tracker')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    ## Add expense command
    add_parser = subparsers.add_parser('add', help='Add a new expense')
    add_parser.add_argument('-a', '--amount', type=float, required=True, help='Expense amount')
    add_parser.add_argument('-d', '--description', required=True, help='Expense description')
    add_parser.add_argument('-c', '--category', default='Miscellaneous', help='Expense category')
    add_parser.add_argument('-t', '--date', help='Transaction date (YYYY-MM-DD)')

    ## List expenses command
    list_parser = subparsers.add_parser('list', help='List expenses')
    list_parser.add_argument('-c', '--category', help='Filter by category')
    list_parser.add_argument('-m', '--month', help='Filter by month (MM-YYYY)')
    list_parser.add_argument('-l', '--limit', type=int, default=10, help='Limit results')

    ## Categories commands
    cat_parser = subparsers.add_parser('categories', help='Manage categories')
    cat_subparsers = cat_parser.add_subparsers(dest='cat_command')

    ## Add category subcommand
    cat_subparsers.add_parser('list', help='List all categories')

    ## Report command 
    report_parser = subparsers.add_parser('report', help='Generate expense reports')
    report_parser.add_argument('-t', '--type', choices=['monthly', 'category', 'yearly'], default='monthly', help='Report type')
    report_parser.add_argument('-m', '--month', help='Month for report (MM-YYYY)')
    report_parser.add_argument('-y', '--year', help='Year for report (YYYY)')

    return parser

def main():
    """Main function to run the Spendora application"""
    parser = setup_parser()
    args = parser.parse_args()  

    ## Initialize database connection
    conn = get_db_connection()

    ## Initialize managers
    transaction_mgr = TransactionManager(conn)
    category_mgr = CategoryManager(conn)

    if args.command == 'add':
        # Handle adding expenses
        category_mgr.ensure_category_exists(args.category)
        transaction_mgr.add_transaction(
            amount=args.amount,
            description=args.description,
            category=args.category,
            date=args.date
        )
        print(f"Added expense: ${args.amount:.2f} for {args.description} in category '{args.category}'")
        
    elif args.command == 'list':
        # Handle listing expenses
        transactions = transaction_mgr.get_transactions(
            category=args.category,
            month=args.month,
            limit=args.limit
        )

        if not transactions:
            print("No transactions found matching your criteria.")
            return
        
        print("\nTransaction List:")
        print("-" * 70)
        print(f"{'Date':<12}{'Category':<15}{'Amount':<10}{'Description':<30}")
        print("-" * 70)

        for t in transactions:
            print(f"{t['date']:<12}{t['category']:<15}${t['amount']:<9.2f}{t['description']:<30}")
    
    elif args.command == 'categories':
        if args.cat_command == 'add':
            category_mgr.add_category(args.name)
            print(f"Added category: {args.name}")
        elif args.cat_command == 'list':
            categories = category_mgr.get_all_categories()
            print("\nAvailable Categories:")
            print("-" * 30)
            for cat in categories:
                print(f"- {cat}")
    
    elif args.command == 'report':
        generate_summary(
            conn=conn,
            report_type=args.type,
            month=args.month,
            year=args.year
        )
    
    else:
        parser.print_help()
    
    # Close the database connection
    conn.close()

if __name__ == "__main__":
    main()
            