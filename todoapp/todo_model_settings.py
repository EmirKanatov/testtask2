

class TodoStatuses:
    NOT_DONE = 'Не выполнено'
    IN_PROCESS = 'В процессе'
    DONE = 'Выполнено'

    @classmethod
    def choices(cls):
        return (
            (cls.NOT_DONE, cls.NOT_DONE),
            (cls.IN_PROCESS, cls.IN_PROCESS),
            (cls.DONE, cls.DONE),
        )


class TodoImportance:

    FIRST = 'Срочно и Важно'
    SECOND = 'Срочно'
    THIRD = 'Важно'
    FOURTH = 'Cредне'
    FIFTH = 'Не особо важно'

    @classmethod
    def choices(cls):
        return (
            (cls.FIRST, cls.FIRST),
            (cls.SECOND, cls.SECOND),
            (cls.THIRD, cls.THIRD),
            (cls.FOURTH, cls.FOURTH),
            (cls.FIFTH, cls.FIFTH),
        )
