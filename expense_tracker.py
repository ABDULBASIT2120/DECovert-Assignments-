# GOOD EVERYONE, EVERYONE!
# THIS IS MY WEEK 3 CAPSTONE PROJECT.
# HOPE I DID WELL.
#######################################################EXPENSE_TRACKER#######################################################
import csv
import sys
from datetime import datetime

transactions = []

file_name = "transactions.csv"

fields = ["S/N", "date", "type", "category", "description", "amount"]

expense_categories = [
    "Food",
    "Transport",
    "Data",
    "School",
    "Rent",
    "Health",
    "Entertainment",
    "Other",
]

income_categories = ["Allowance", "Salary", "Gift", "Other"]

# test_dummy = {
#     "S/N" : ,
#     "date" : ,
#     "type" : ,
#     "category" : ,
#     "description" : ,
#     "amount" :
# }


#####################################################################################################################################################################
#######################################################SAVE_TRANSACTIONS#######################################################
def save_transactions(saving):
    try:
        with open(file_name, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(fields)
            for stack in saving:
                writer.writerow(
                    [
                        stack["S/N"],
                        stack["date"],
                        stack["type"],
                        stack["category"],
                        stack["description"],
                        f"{stack['amount']:.2f}",
                    ]
                )
    except OSError:
        print(
            "\nCould not save to the file! Close it if it is open in another program!\n"
        )


#####################################################################################################################################################################
#######################################################LOAD_TRANSACTIONS#######################################################
def load_transactions(loading):
    skipped = 0
    try:
        with open(file_name, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            if reader.fieldnames is None:
                print(f"{file_name} is empty. Starting fresh!\n")
                return
            if set(fields) - set(reader.fieldnames):
                print(f"{file_name} has the wrong header! It must contain: {fields}")
                print(
                    "Fix or rename the file and run again. Nothing was overwritten!\n"
                )
                sys.exit()
            for row in reader:
                try:
                    kind = row["type"].strip().lower()
                    category = row["category"].strip()
                    amount = float(row["amount"])
                    if kind not in ("expense", "income") or category == "":
                        raise ValueError
                    if not 0 < amount < float("inf"):
                        raise ValueError
                    date = datetime.strptime(row["date"].strip(), "%Y-%m-%d")
                    stack = {
                        "S/N": int(row["S/N"]),
                        "date": date.strftime("%Y-%m-%d"),
                        "type": kind,
                        "category": category,
                        "description": row["description"].strip(),
                        "amount": round(amount, 2),
                    }
                    loading.append(stack)
                except (ValueError, TypeError, AttributeError, KeyError):
                    skipped += 1
    except FileNotFoundError:
        print(f"No {file_name} found. Starting fresh!\n")
        return
    except OSError:
        print(f"Could not read {file_name}! Close it if it is open elsewhere.\n")
        sys.exit()
    if skipped > 0:
        print(f"Skipped {skipped} unreadable row(s). They go away on the next save!")
    print(f"Loaded {len(loading)} transaction(s) from {file_name}.\n")


#####################################################################################################################################################################
#######################################################ASKING_INPUTS#######################################################
def ask_type():
    choosing = input("Select the Type!\n1 - 'Expense'\n2 - 'Income'\n")
    if choosing == "1":
        return "expense"
    elif choosing == "2":
        return "income"
    else:
        print("Please, enter a valid input 'Between 1 & 2'!\n")
        return ask_type()


def ask_category(kind):
    if kind == "expense":
        options = expense_categories
    else:
        options = income_categories
    print("Select the Category!")
    for number, option in enumerate(options, start=1):
        print(f"{number} - '{option}'")
    try:
        choosing = int(input())
        if 1 <= choosing <= len(options):
            return options[choosing - 1]
        print(f"Please, enter a valid input 'Between 1 & {len(options)}'!\n")
        return ask_category(kind)
    except ValueError:
        print("Please, enter only numbers!\n")
        return ask_category(kind)


def ask_amount():
    try:
        amount = float(input("Enter the Amount: ").replace(",", ""))
        if 0 < amount < float("inf"):
            return round(amount, 2)
        print("Please, enter an amount greater than '0'!\n")
        return ask_amount()
    except ValueError:
        print("Please, enter only numbers!\n")
        return ask_amount()


def ask_date():
    asking = input("Enter the Date 'YYYY-MM-DD' or press Enter for today: ")
    if asking.strip() == "":
        return datetime.today().strftime("%Y-%m-%d")
    try:
        return datetime.strptime(asking.strip(), "%Y-%m-%d").strftime("%Y-%m-%d")
    except ValueError:
        print("Please, enter a real date like '2026-10-30'!\n")
        return ask_date()


def ask_month():
    asking = input("Enter the Month 'YYYY-MM': ")
    try:
        return datetime.strptime(asking.strip(), "%Y-%m").strftime("%Y-%m")
    except ValueError:
        print("Please, enter a real month like '2026-10'!\n")
        return ask_month()


#####################################################################################################################################################################
#######################################################CALCULATIONS#######################################################
def next_serial_number(counting):
    if not counting:
        return 1
    return max(stack["S/N"] for stack in counting) + 1


def filter_transactions(filtering, category="", month=""):
    result = filtering
    if category:
        result = [
            stack for stack in result if stack["category"].lower() == category.lower()
        ]
    if month:
        result = [stack for stack in result if stack["date"].startswith(month)]
    return list(result)


def calculate_totals(totaling):
    income = sum(stack["amount"] for stack in totaling if stack["type"] == "income")
    expense = sum(stack["amount"] for stack in totaling if stack["type"] == "expense")
    return round(income, 2), round(expense, 2), round(income - expense, 2)


def summarize_categories(summing, kind):
    totals = {}
    for stack in summing:
        if stack["type"] == kind:
            name = stack["category"].title()
            totals[name] = totals.get(name, 0) + stack["amount"]
    totals = {name: round(total, 2) for name, total in totals.items()}
    return dict(sorted(totals.items(), key=lambda item: item[1], reverse=True))


#####################################################################################################################################################################
#######################################################DISPLAY#######################################################
def display_transactions(showing):
    if not showing:
        print("\nNo transactions to show!\n")
        return
    print(f"\n{'S/N':<5}{'Date':<12}{'Category':<15}{'Description':<24}{'Amount':>14}")
    print("-" * 70)
    for stack in sorted(showing, key=lambda item: (item["date"], item["S/N"])):
        if stack["type"] == "income":
            sign = "+"
        else:
            sign = "-"
        amount_text = f"{sign}N{stack['amount']:,.2f}"
        print(
            f"{stack['S/N']:<5}{stack['date']:<12}{stack['category']:<15}"
            f"{stack['description'][:22]:<24}{amount_text:>14}"
        )
    print(f"({len(showing)} transaction(s))\n")


def display_summary(summing, label):
    if not summing:
        print("\nNo transactions for this period!\n")
        return
    income, expense, balance = calculate_totals(summing)
    print(f"\n===== SUMMARY: {label} =====")
    print(f"Total income : N{income:,.2f}")
    print(f"Total spent  : N{expense:,.2f}")
    print(f"Balance      : N{balance:,.2f}")
    by_category = summarize_categories(summing, "expense")
    if not by_category:
        print("\nNo expenses recorded for this period!\n")
        return
    print("\nSpending by category:")
    for name, total in by_category.items():
        percent = total / expense * 100
        bar = "#" * int(percent // 5)
        print(f"  {name:<15}{'N' + format(total, ',.2f'):>14}  {percent:5.1f}%  {bar}")
    top = next(iter(by_category))
    print(f"\nHighest spending: {top} (N{by_category[top]:,.2f})\n")


#####################################################################################################################################################################
#######################################################ADD_TRANSACTION#######################################################
def add_transaction_l_1():
    def add_transaction_l_2(
        serial_number, date, kind, category, description, amount, creating
    ):
        stack = {
            "S/N": serial_number,
            "date": date,
            "type": kind,
            "category": category,
            "description": description,
            "amount": amount,
        }

        creating.append(stack)
        return stack

    kind = ask_type()
    category = ask_category(kind)
    amount = ask_amount()
    date = ask_date()
    description = input("Enter the Description 'Optional': ").strip()
    stack = add_transaction_l_2(
        next_serial_number(transactions),
        date,
        kind,
        category,
        description,
        amount,
        transactions,
    )
    save_transactions(transactions)
    print(f"\nAdded S/N {stack['S/N']}: {kind} of N{amount:,.2f} ({category})!\n")


def confirm_add_1():
    confirm_1_1 = input("Do you want to add another transaction? ")
    if confirm_1_1.lower() == "yes":
        add_transaction_l_1()
        confirm_add_1()
    elif confirm_1_1.lower() == "no":
        print("Moving on!\n")
        confirm_add_2()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        confirm_add_1()


def confirm_add_2():
    confirm_1_2 = input(
        "What do you want to do next?\n1 - 'Read Transactions'\n2 - 'Delete Transaction'\n3 - 'View Summary'\n4 - 'Exit System'!\n"
    )
    if confirm_1_2 == "1":
        read_transactions()
        confirm_read_1()
    elif confirm_1_2 == "2":
        delete_transaction_l_1()
        confirm_delete_1()
    elif confirm_1_2 == "3":
        view_summary()
        confirm_summary_1()
    elif confirm_1_2 == "4":
        exit_system()
    else:
        print("Please Enter a valid input!")
        confirm_add_2()


#####################################################################################################################################################################
#######################################################READ_TRANSACTIONS#######################################################
def read_transactions():
    asking = input(
        "What do you want to read?\n1 - 'All Transactions'\n2 - 'By Category'\n3 - 'By Month'\n"
    )
    if asking == "1":
        display_transactions(transactions)
    elif asking == "2":
        name = input("Enter the Category name: ")
        display_transactions(filter_transactions(transactions, category=name))
    elif asking == "3":
        display_transactions(filter_transactions(transactions, month=ask_month()))
    else:
        print("Please, enter a valid input 'Between 1 & 3'!\n")
        read_transactions()


def confirm_read_1():
    confirm_2_1 = input("Do you want to read again? ")
    if confirm_2_1.lower() == "yes":
        read_transactions()
        confirm_read_1()
    elif confirm_2_1.lower() == "no":
        print("Moving on!\n")
        confirm_read_2()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        confirm_read_1()


def confirm_read_2():
    confirm_2_2 = input(
        "What do you want to do next?\n1 - 'Add Transaction'\n2 - 'Delete Transaction'\n3 - 'View Summary'\n4 - 'Exit System'!\n"
    )
    if confirm_2_2 == "1":
        add_transaction_l_1()
        confirm_add_1()
    elif confirm_2_2 == "2":
        delete_transaction_l_1()
        confirm_delete_1()
    elif confirm_2_2 == "3":
        view_summary()
        confirm_summary_1()
    elif confirm_2_2 == "4":
        exit_system()
    else:
        print("Please Enter a valid input!")
        confirm_read_2()


#####################################################################################################################################################################
#######################################################DELETE_TRANSACTION#######################################################
def delete_transaction_l_1():
    if not transactions:
        print("\nThere are no transactions to delete!\n")
        return
    display_transactions(transactions)
    try:
        deleting = int(input("Enter the S/N of the transaction you want to delete: "))
    except ValueError:
        print("Please, enter only numbers!\n")
        delete_transaction_l_1()
        return
    target = None
    for stack in transactions:
        if stack["S/N"] == deleting:
            target = stack
    if target is None:
        print("\nNo transaction has that S/N!\n")
        return

    def delete_transaction_l_2():
        sure = input(f"Are you sure you want to delete S/N {deleting}? ")
        if sure.lower() == "yes":
            transactions.remove(target)
            save_transactions(transactions)
            print("\nDeleted!\n")
        elif sure.lower() == "no":
            print("\nCancelled!\n")
        else:
            print("Please, enter a 'yes' or 'no'!\n")
            delete_transaction_l_2()

    delete_transaction_l_2()


def confirm_delete_1():
    confirm_3_1 = input("Do you want to delete another transaction? ")
    if confirm_3_1.lower() == "yes":
        delete_transaction_l_1()
        confirm_delete_1()
    elif confirm_3_1.lower() == "no":
        print("Moving on!\n")
        confirm_delete_2()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        confirm_delete_1()


def confirm_delete_2():
    confirm_3_2 = input(
        "What do you want to do next?\n1 - 'Add Transaction'\n2 - 'Read Transactions'\n3 - 'View Summary'\n4 - 'Exit System'!\n"
    )
    if confirm_3_2 == "1":
        add_transaction_l_1()
        confirm_add_1()
    elif confirm_3_2 == "2":
        read_transactions()
        confirm_read_1()
    elif confirm_3_2 == "3":
        view_summary()
        confirm_summary_1()
    elif confirm_3_2 == "4":
        exit_system()
    else:
        print("Please Enter a valid input!")
        confirm_delete_2()


#####################################################################################################################################################################
#######################################################VIEW_SUMMARY#######################################################
def view_summary():
    asking = input("Summary for?\n1 - 'All Time'\n2 - 'One Month'\n")
    if asking == "1":
        display_summary(transactions, "All Time")
    elif asking == "2":
        month = ask_month()
        display_summary(filter_transactions(transactions, month=month), month)
    else:
        print("Please, enter a valid input 'Between 1 & 2'!\n")
        view_summary()


def confirm_summary_1():
    confirm_4_1 = input("Do you want to view another summary? ")
    if confirm_4_1.lower() == "yes":
        view_summary()
        confirm_summary_1()
    elif confirm_4_1.lower() == "no":
        print("Moving on!\n")
        confirm_summary_2()
    else:
        print("Please, enter a 'yes' or 'no'!\n")
        confirm_summary_1()


def confirm_summary_2():
    confirm_4_2 = input(
        "What do you want to do next?\n1 - 'Add Transaction'\n2 - 'Read Transactions'\n3 - 'Delete Transaction'\n4 - 'Exit System'!\n"
    )
    if confirm_4_2 == "1":
        add_transaction_l_1()
        confirm_add_1()
    elif confirm_4_2 == "2":
        read_transactions()
        confirm_read_1()
    elif confirm_4_2 == "3":
        delete_transaction_l_1()
        confirm_delete_1()
    elif confirm_4_2 == "4":
        exit_system()
    else:
        print("Please Enter a valid input!")
        confirm_summary_2()


#####################################################################################################################################################################
#######################################################EXIT_SYSTEM#######################################################
def exit_system():
    print("\nThank you for using ExpenseTracker!\nSee you later!\n")
    sys.exit()


#####################################################################################################################################################################
#######################################################ACTUAL_IMPLEMENTATION_OF_EXPENSE_TRACKER#######################################################
def expense_tracker():
    select = input(
        "Select an Operation!\n1 for 'Adding Transaction'\n2 for 'Reading Transactions'\n3 for 'Deleting Transaction'\n4 for 'Viewing Summary' &\n5 for 'Exiting System'!\n"
    )
    if select == "1":
        add_transaction_l_1()
        confirm_add_1()
    elif select == "2":
        read_transactions()
        confirm_read_1()
    elif select == "3":
        delete_transaction_l_1()
        confirm_delete_1()
    elif select == "4":
        view_summary()
        confirm_summary_1()
    elif select == "5":
        exit_system()
    else:
        print("Enter a valid input!\n")
        expense_tracker()


#####################################################################################################################################################################
#######################################################EXPENSE_TRACKER_LAUNCH#######################################################
def ExpenseTracker():
    print("Welcome to the ExpenseTracker!\n")
    load_transactions(transactions)
    expense_tracker()


try:
    ExpenseTracker()
except (KeyboardInterrupt, EOFError):
    print("\n\nInterrupted! Your changes are already saved!")
    print("Thank you for using ExpenseTracker!\nSee you later!\n")
