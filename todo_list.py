def main():
    tasks = []

    while True:
        print('💫To - do List💫')
        print('1. Add Task')
        print('2. Show Tasks')
        print('3. Mark Task as Done')
        print('4. Exit')

        choice = input('Enter your choice:')

        if choice == '1':
            print()
            n_tasks = int(input('How many task you want to add: '))

            for i in range(n_tasks):
                task = input('Enter the task:')
                tasks.append({'task': task, 'done': False})
                print('Task added!')
        
        elif choice == '2':
            print('\nTasks:')
            for index, task in enumerate(tasks):
                status = 'Done' if task ['done'] else 'Not Done'
                print(f'{index + 1} {task['task']} - {status}')

main()