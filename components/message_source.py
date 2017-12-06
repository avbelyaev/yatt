from config.state_config import Language



message_source = {
    Language.ENG: {
        'write_me': 'Just write me something to create a new one :)',
        'no_tasks_yet': 'You don\'t have any tasks yet',
        'selected_lang': 'Selected engish language',
        'your_tasks':"{}, here are yout tasks",
        'task_created': 'task with id {} has been created',
        'cant_find_task': 'Sorry, can`t find task with id {}',
        'set_date':'Setting date to {} for task:',
        'error': 'Error. Latest task id: {}. Command trace: {}',
    },

    Language.RUS: {
        'write_me': 'Просто напишите мне что-нибудь, чтобы создать :)',
        'no_tasks_yet': 'у вас еще нет задач',
        'selected_lang': 'Выбран русский язык',
        'your_tasks': "{}, Ваши задачи:\n",
        'task_created': 'задача с id {} была создана',
        'cant_find_task': 'Извините, не могу найти задачу с id {}',
        'set_date': 'Поставлена дата {} для задачи:',
        'error': 'Ошибка. id последней задачи: {}. Command trace: {}'
    }
}