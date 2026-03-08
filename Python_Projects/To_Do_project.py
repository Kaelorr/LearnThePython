''' Hey there!, this is to-do program where you will add your tasks, see your task anytime and delete your task anytime'''
class Min:
    def __init__(self):
        self.task_data = []


class Min():
    def __init__(self):
        self.task_data = []

        enter = None
        try:
            enter = int(input("Press 1 to continue & 0 to exit: "))
        except ValueError:
            print('Invalid input!')

        if enter == 1:
            while True:
                user_want = None
                try:
                    user_want = int(input('''
1. Add task
2. See task
3. Delete task
0. Exit
Enter your option: '''))
                except ValueError:
                    print('Invalid number!')
                    continue

                if user_want == 1:
                    self.add_task()
                elif user_want == 2:
                    self.see_task()
                elif user_want == 3:
                    self.delete_task()
                elif user_want == 0:
                    print('You have exited!')
                    break
                else:
                    print('Invalid option!')
        else:
            print('You have exited!')

    def add_task(self):
        task = input('Write your task: ')
        self.task_data.append(task)
        print(f'Task added: {task}')

    def see_task(self):
        if not self.task_data:
            print('No tasks found!')
        else:
            print("Your tasks:")
            for i, task in enumerate(self.task_data, 1):
                print(f"{i}. {task}")

    def delete_task(self):
        self.see_task()
        try:
            num = int(input('Which task number to delete? '))
            removed = self.task_data.pop(num - 1)
            print(f'Deleted: {removed}')
        except (ValueError, IndexError):
            print('Invalid task number!')

run = Min()
