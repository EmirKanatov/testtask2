

class TodoStatuses:
    NOT_DONE = 'not_done'
    IN_PROCESS = 'in_progress'
    DONE = 'done'

    @classmethod
    def choices(cls):
        return (
            (cls.NOT_DONE, 'Не выполнено'),
            (cls.IN_PROCESS, 'В процессе'),
            (cls.DONE, 'Выполнено'),
        )


class TodoImportance:

    FIRST = '1'
    SECOND = '2'
    THIRD = '3'
    FOURTH = '4'
    FIFTH = '5'

    @classmethod
    def choices(cls):
        return (
            (cls.FIRST, 'Срочно и Важно'),
            (cls.SECOND, 'Срочно'),
            (cls.THIRD, 'Важно'),
            (cls.FOURTH, 'Cредне'),
            (cls.FIFTH, 'Не особо важно'),
        )