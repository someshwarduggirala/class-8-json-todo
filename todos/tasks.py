from datetime import datetime
#from copy import deepcopy

from .exceptions import (
   InvalidTaskStatus, TaskAlreadyDoneException, TaskDoesntExistException)
from .utils import parse_date, parse_int


def new():
    return []


def create_task(tasks, name, description=None, due_on=None):
    if due_on and type(due_on) != datetime:
        due_on = parse_date(due_on)
    
    task = {
        'task': name,
        'description': description,
        'due_on': due_on,
        'status': 'pending'
    }
    tasks.append(task)


def list_tasks(tasks, status='all'):
    
    if status not in ['pending','done','all']:
        raise InvalidTaskStatus
    
    task_list = []
    for idx, task in enumerate(tasks, 1):
        if task['due_on'] is not None:
            due_on = task['due_on'].strftime('%Y-%m-%d %H:%M:%S')
        else:
            due_on = None

        t = (idx, task['task'], due_on, task['status'])
        if status == 'all' or task['status'] == status:
            task_list.append(t)

    return task_list


def complete_task(tasks, name):
    new_tasks = []
    id=parse_int(name)
    found_flag=False
    
    for task_id,task in enumerate(tasks,1):
        if task['task']==name or task_id==id:
            if task['status'] == 'done':
                raise TaskAlreadyDoneException
            task=task.copy()
            task['status']='done'
            found_flag=True
        new_tasks.append(task)
        
    if not found_flag:
        raise TaskDoesntExistException
        
    return new_tasks
    

