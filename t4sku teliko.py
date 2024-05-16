def categories(option=None):
    from colorama import init, Back, Fore
    init(autoreset=True)

    for index, option in enumerate(option, start=1):
        print(Back.LIGHTBLUE_EX + Fore.BLACK + f"{index}. {option}")


def sort_options(options, sort_by):
    from colorama import init
    init(autoreset=True)

    if sort_by == "A-Z":
        return sorted(options)

        print(Back.LIGHTBLUE_EX + Fore.BLACK + str(variables_sorted))

        # Εμφάνιση των επιλογών


def display_options():
    from colorama import init
    init(autoreset=True)
    pass


def choose_option(sorted_options2, value_1=None):
    from colorama import Back, Fore
    options = ["home", "work", "shopping", "phone", "dates", "activities", "others"]

    print(Back.LIGHTBLUE_EX + Fore.BLACK + f"Welcome! Value: {value_1}")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Please select how to sort the options:")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "1. Alphabetically (A-Z)")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "2. None")
    sort_choice = input("Enter your choice (1 or 2 ): ")

    while sort_choice not in ["1", "2"]:
        print(Back.RED + Fore.BLACK + "Invalid choice. Please select 1 or 2")
        sort_choice = input("Enter your choice (1 or 2): ")

    sorted_options2(options, "A-Z")
    if sort_choice == "1":
        words = ["home", "work", "shopping", "phone", "dates", "activities", "others"]
        sorted_words = sorted(words)

        for word in sorted_words:
            print(word)

    else:
        print("home", "work", "shopping", "phone", "dates", "activities", "others")
    return ()

    # Επιλογή κατηγορίας


from colorama import init, Back, Fore
selected_category = None  # Αρχική τιμή

# Ελέγχουμε την επιλογή του χρήστη
category_choice = int(input("Choose a category (1 to 7): "))

while category_choice not in range(1, 8):
    print(Back.RED + Fore.BLACK + "Invalid category choice. Please choose a number between 1 and 7.")
    category_choice = int(input("Choose a category (1 to 7): "))

# Ορίζουμε τη μεταβλητή selected_category με βάση την επιλογή του χρήστη
selected_category = sort_options(category_choice - 1)

print(Back.LIGHTBLUE_EX + Fore.BLACK + f"You selected category: {selected_category}")

# καταχώρηση  της εργασίας σε κάθε κατηγορία
category_choice = input("Select a category to place your value in (1 to 7): ")
while category_choice not in ["1", "2", "3", "4", "5", "6", "7"]:
    print(Back.RED + Fore.BLACK + "Invalid choice. Please select a number between 1 and 7.")
    category_choice = input("Select a category to place your value in (1 to 7): ")

category_index = int(category_choice) - 1
selected_category = sort_options(category_index)

from datetime import datetime


# Ορισμός της κλάσης Task για την αναπαράσταση των εργασιών
class Task:
    def __init__(self, dates, time, description):
        self.date = dates
        self.time = time
        self.description = description


# Ορισμός της κλάσης Calendar για τη διαχείριση των εργασιών στο ημερολόγιο
def display_calendar():
    from colorama import init, Back, Fore
    init(autoreset=True)

    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Calendar:")
    Calendar()

    # Εμφάνιση ημερολογίου


class Calendar:
    def __init__(self):
        # Κώδικας αρχικοποίησης

        self.tasks = []
        # Αρχικοποίηση μιας κενής λίστας εργασιών

    # Μέθοδος για την προσθήκη εργασιών στο ημερολόγιο
    def add_task(self, task):
        self.tasks.append(task)

    # Μέθοδος για την εμφάνιση όλων των εργασιών στο ημερολόγιο
    def display_calendar(self):
        pass


def printcalendar(self=None):
    from colorama import init, Back, Fore
    init(autoreset=True)

    for month in range(1, 13):
        print(Back.LIGHTBLUE_EX + Fore.BLACK + f"month {month}:")
        for day in range(1, 32):
            try:
                dates = datetime(2024, month, day).strftime("%Y-%m-%d")
                tasks_for_date = []
                for task in self.tasks:
                    if task.date == dates:
                        tasks_for_date.append(task)
                if tasks_for_date:
                    print(Back.LIGHTBLUE_EX + Fore.BLACK + f"day {day}:")
                    for task in tasks_for_date:
                        print(Back.LIGHTBLUE_EX + Fore.BLACK + f"\t{task.time}: {task.description}")
            except ValueError:
                pass


# Κύρια συνάρτηση για την εκτέλεση του προγράμματος

# Αρχικοποίηση του colorama
init(autoreset=True)


# Κύρια συνάρτηση για την εκτέλεση του προγράμματος
def success_rate_percentage():
    pass


def failure_rate_percentage():
    pass


def main():
    global category_choice
    from colorama import Back, Fore
    calendar = Calendar()
    # αρχή του προγράμματος
    print(Back.LIGHTBLUE_EX + Fore.Black + "Welcome to T4sku.Please press Any number to continue")
    
    # Έλεγχος για έγκυρη επιλογή κατηγορίας
    while category_choice not in range(0, 10):
        print(Back.RED + Fore.BLACK + "Invalid category choice. Please choose a number between 0 and 9.")
        category_choice = int(input("Choose a category (0 to 9): "))

    # Εμφάνιση ημερολογίου
    def print_calendar():
        print_calendar()

    # Δημιουργία ενός αντικειμένου Calendar για το ημερολόγιο

    while True:
        print(Back.LIGHTBLUE_EX + Fore.BLACK + "1. add new task")
        print(Back.LIGHTBLUE_EX + Fore.BLACK + "2. calendar")
        print(Back.LIGHTBLUE_EX + Fore.BLACK + "3. exit")

        choice = input("choose ")

        if choice == "1":  # Προσθήκη νέας εργασίας
            dates = input("choose a date  ")
            time = input("choose time ")

            task = Task(dates, time)  # Δημιουργία εργασίας
            calendar.add_task(task)  # Προσθήκη εργασίας στο ημερολόγιο
            task_creation()
            print(Back.GREEN + "new task just added !")

        def category(value_1):
            if choice == "2":  # Εμφάνιση ημερολογίου
                from colorama import init, Back, Fore
                def printcalendar():
                    calendar = Calendar()
                    calendar.display_calendar()

                    def display_options():
                        print(Back.LIGHTBLUE_EX + Fore.BLACK + "Options:")
                        print(Back.LIGHTBLUE_EX + Fore.BLACK + "1. Completed tasks")
                        print(Back.LIGHTBLUE_EX + Fore.BLACK + "2. Duration of task")
                        print(Back.LIGHTBLUE_EX + Fore.BLACK + "3. Successful tasks")
                        print(Back.LIGHTBLUE_EX + Fore.BLACK + "4. Failed tasks")
                        print(Back.LIGHTBLUE_EX + Fore.BLACK + "5. Productivity")

                    def user_choice():
                        choice = input("Choose an option (1-5): ")
                        return choice

                    # Κύριο πρόγραμμα
                    while True:
                        display_options()
                        choices = user_choice()

                        if choices == "1":
                            mark_completed_task()
                        elif choice == "2":
                            duration_of_task()
                        elif choice == "3":
                            success_rate_percentage()
                        elif choice == "4":
                            failure_rate_percentage()
                        elif choice == "5":
                            productivity()

                        else:
                            print(Back.RED + Fore.BLACK + "Invalid option. Please choose a number between 1 and 5.")

            # εμφάνιση των επιλογών για την εμφανιση στατιστικών
            elif choice == "3":  # Έξοδος από το πρόγραμμα
                from colorama import init, Back, Fore
                print(Back.YELLOW + "bye!")
            else:
                from colorama import init, Back, Fore
                print(Back.RED + "please choose a valid option.")


# Έλεγχος αν είμαστε στο κύριο πρόγραμμα
if __name__ == "__main__":
    main()

import datetime
from datetime import date

today = date.today()

all_tasks = ()  # λίστα όλων των task (στην task_creation)
easy_tasks = ()  # λιστες βάσει βαθμό δυσκολίας EASY (στην task_creation)
normal_tasks = ()  # λιστες βάσει βαθμό δυσκολίας NORMAL (στην task_creation)
hard_tasks = ()  # λιστες βάσει βαθμό δυσκολίας HARD (στην task_creation)
completed_tasks_in_week1 = ()
completed_tasks_in_week2 = ()
completed_tasks_in_week3 = ()
completed_tasks_in_week4 = ()
completed_tasks_in_week5 = ()


def productivity():
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "Productivity Options:")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "1. Progress Comparison")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "2. Statistics")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "3.failed")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "4.success")
    print(Back.LIGHTBLUE_EX + Fore.BLACK + "5.comparison by weeks of progress abd statistics")
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        progress_comparison()
    elif choice == "2":
        statistics_total()
        statistics_weekly()
    elif choice == "3":
        failure_rate_percentage()
    elif choice == "4":
        success_rate_percentage()
    elif choice == "5":
        progress_and_statistics_comparison_by_weeks()

    else:
        print("Invalid option. Please choose either 1 or 2.")


# ιδιοτητες ενος task (class Task)
class Task:
    def __init__(self, title, description, deadline_date, difficulty, status, creation_date,
                 completion_date):  # βελτίωση: αναλυση deadline ετσι ωστε weekly tasks, daily task κτλ)
        self.title = title
        self.description = description
        self.deadline = deadline_date
        self.difficulty = difficulty
        self.status = status
        self.creation_date = creation_date
        self.completion_date = completion_date

    # Δημιουργία ενός task


all_tasks = []
easy_tasks = []
normal_tasks = []
hard_tasks = []


def task_creation():
    title = input('Enter a task.')
    description = input('Add a description for this task.')
    deadline_str = input('Set a deadline for this task: DD-MM-YYYY')  # date string
    status = 'in progress'
    creation_date = today
    deadline_date = datetime.datetime.strptime(deadline_str, '%d-%m-%Y').date()  # μετατροπη date string σε date object
    difficulty = input(
        'Set the difficulty level of this task: (easy/normal/hard)').lower()  # οι επιλογές case sensitive
    task = Task(title, description, deadline_date, difficulty, status,
                creation_date)  # βελτιωση: αριθμηση των tasks κατα την δημιουργία, πχ task_1, task_2 κτλ

    # Από εδώ και κάτω προστίθεται το task στις αντίστοιχες λίστες (all tasks, difficulty based sorting)
    all_tasks.append(task)  # συνολική λίστα
    if task.difficulty == 'easy':  # ταξινόμηση κατά βαθμό δυσκολίας (easy/normal/hard)
        easy_tasks.append(task)
    elif task.difficulty == 'normal':
        normal_tasks.append(task)
    elif task.difficulty == 'hard':
        hard_tasks.append(task)

    return task


# υπολογισμος διαρκειας που χρειαsτηκε για να μαρκαριστει ενα task
def duration_of_task(task):
    duration = task.completion_date - task.creation_date
    return duration


# συναρτηση για μαρκαρισμα εργασιων
def mark_completed_task(task):
    if task.status == 'in progress':
        if date.today() <= task.deadline_date:  # checks daedline
            task.status = 'completed'
            task.completion_date = today
            duration_of_task()
            print('Task', task.title, 'is marked as', task.status)
        else:
            task.status = 'failed'
            print('Cannot mark task as completed. Deadline has passed. Task', task.status)
    # αν είναι ήδη ορισμένο ως 'completed'
    else:
        print('Task', task.title, 'is already marked as', task.status)
    # αρχιοθετηση του task by week of completion
    sorting_completed_tasks_by_week_of_completion(task)


# δημιουργία ενος μετρητη για τα completed tasks
def completed_tasks_counter(alltasks):
    global completed_tasks_counter
    for task in alltasks:
        completed_tasks_counter = 0
        if task.status == 'completed':
            completed_tasks_counter += 1
    return completed_tasks_counter


# δημιουργία ενος μετρητη για τα failed tasks
def failed_tasks_counter(alltasks):
    global failed_tasks_counter
    for task in alltasks:
        failed_tasks_counter = 0
        if task.status == 'failed':
            failed_tasks_counter += 1
    return failed_tasks_counter


# για να ενημερώνονται αυτόματα οι counters
while True:
    completed_tasks_counter(all_tasks)
    failed_tasks_counter(all_tasks)


# ΣΤΑΤΙΣΤΙΚΗ ΑΝΑΛΥΣΗ

# ΓΕΝΙΚΗ ΣΥΝΑΡΤΗΣΗ - υπολογισμος συνολικού ποσοστού επιτυχίας
def success_rate_precentage():  # παιρνει λιστες
    success_rate = completed_tasks_counter() / len(),
    successrateprecentage = (success_rate * 100, '%')
    return successrateprecentage


# ΓΕΝΙΚΗ ΣΥΝΑΡΤΗΣΗ - υπολογισμος συνολικού ποσοστού αποτυχίας
def failure_rate_precentage():  # παιρνει λιστες
    failure_rate = failed_tasks_counter() / len(),
    failurerateprecentage = (failure_rate * 100, '%')
    return failurerateprecentage


# εξέταση απόδοσης με χρήση στατιστικών
class X_category_tasks:
    pass


def statistics_total():  # total, ανά βαθμό δυσκολίας
    total_success_rate_precentage = success_rate_precentage(all_tasks)
    total_failure_rate_precentage = failure_rate_precentage(all_tasks)
    # difficulty based SUCCESS rate precentage
    easy_tasks_success_rate_precentage = success_rate_precentage(easy_tasks)
    normal_tasks_success_rate_precentage = success_rate_precentage(normal_tasks)
    hard_tasks_success_rate_precentage = success_rate_precentage(hard_tasks)
    # difficulty based FAILURE rate precentage
    easy_tasks_failure_rate_precentage = failure_rate_precentage(easy_tasks)
    normal_tasks_failure_rate_precentage = failure_rate_precentage(normal_tasks)
    hard_tasks_failure_rate_precentage = failure_rate_precentage(hard_tasks)

    return {'Total Success Rate : ': total_success_rate_precentage,  # divided by success and fail
            'Success Rate for easy Tasks :': easy_tasks_success_rate_precentage,
            'Success Rate for normal Tasks :': normal_tasks_success_rate_precentage,
            'Success Rate for hard Tasks :': hard_tasks_success_rate_precentage,

            'Total Failure Rate : ': total_failure_rate_precentage,
            'Failure Rate for easy Tasks :': easy_tasks_failure_rate_precentage,
            'Failure Rate for normal Tasks :': normal_tasks_failure_rate_precentage,
            'Failure Rate for hard Tasks :': hard_tasks_failure_rate_precentage
            }


# γενικη συγκριση αποδοσης
def progress_comparison(week_a_tasks, week_b_tasks):
    if completed_tasks_counter(week_a_tasks) < completed_tasks_counter(week_b_tasks):
        print('Productivity has increased!')
    else:
        print(
            'Productivity has decreased...')

    # κατηγοριοποίηση ενός task βάσει την εβδομάδα που μαρκαρίστηκε completed


completed_tasks_in_week1 = []
completed_tasks_in_week2 = []
completed_tasks_in_week3 = []
completed_tasks_in_week4 = []
completed_tasks_in_week5 = []


def sorting_completed_tasks_by_week_of_completion(task):
    completion_date_integer = int(task.completion_date.strftime("%d%m%Y"))  # μετρατροπη ενος date object σε int
    completion_date_day_integer = int(str(completion_date_integer)[:2])  # κρατάει μονο το DD απο DDMMYYYY
    a_num = (completion_date_day_integer / 7)
    a_string = str(a_num)
    a_first_digit = int(a_string[0])

    completion_week_of_task = a_first_digit + 1  # start: week 1
    if completion_week_of_task == 1:
        completed_tasks_in_week1.append(task)
    elif completion_week_of_task == 2:
        completed_tasks_in_week2.append(task)
    elif completion_week_of_task == 3:
        completed_tasks_in_week3.append(task)
    elif completion_week_of_task == 4:
        completed_tasks_in_week4.append(task)
    elif completion_week_of_task == 5:
        completed_tasks_in_week5.append(task)


# στατιστικα εβδομαδας
def statistics_weekly():
    pass


# συγκριση αποδοσης και στατιστικων ανα εβδομάδα
def progress_and_statistics_comparison_by_weeks(completed_tasks_in_weeka, completed_tasks_in_weekb):
    progress_comparison(completed_tasks_in_weeka, completed_tasks_in_weekb)
    print("{} -> {}".format(statistics_weekly(), statistics_weekly()))
