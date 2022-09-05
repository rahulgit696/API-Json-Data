import requests


_API_URL = 'https://jsonplaceholder.typicode.com/todos'


# open json data
todo_list = requests.get(_API_URL).json()
# we create a dict to sum the number of tasks per user
todo_by_user = dict()

# now we iterate over the result json data
for todo in todo_list:
    # if we don't have yet that user in our
    # todo_by_user, then we create a record for it
    # and we use the userID as the identifier
    if todo['userId'] not in todo_by_user:
        user_id = todo['userId']
        todo_by_user[user_id] = {
            'total_todo': 0,
            'total_completed': 0
        }

        # then we increase by one the total
        todo_by_user[user_id]['total_todo'] = todo_by_user[user_id]['total_todo'] + 1
        # if the task is completed, we increase the total_completed by 1 too
        if todo['completed'] is True:
            todo_by_user[user_id]['total_completed'] = todo_by_user[user_id]['total_completed'] + 1


# now we need to iterate over the result and check if the
# total_completed is grater than 50% of the total_todo
for user_id, todo in todo_by_user.items():
    # getting the percentage
    percentage = todo['total_completed'] / todo['total_todo'] * 100
    if percentage >= 50:
        print(f'UserID: `{user_id}` has more than 50 percentage of its task completed')
    else:
        print(f'UserID: `{user_id}` has only {percentage} completed')
