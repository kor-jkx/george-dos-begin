def do(module_name, *args):
    print(module_name, [i for i in args if len(args)])


_about = {
    'О себе': lambda mod='about': do(mod),
    'Помощь': lambda mod='pr_help': do(mod, 'All'),
    '-1': None,
    'Запуск хpанителя': do('keeper'),
    'Календарь': do('calendar'),
    'Калькулятор': do('calc'),
    '-2': None,
    'Системная дата': do('time_date', 'sys_date'),
    'Системное время': do('tima_date', 'sys_time'),
    '-3': None,
    'Настpойка пpогpаммы': do('features'),
    '-4': None,
    'Выход': do('exit_arm')
}

_sub_sprav = {
    "Внутренние счета": do('spr_sch', 1),
    "Счета затрат": do('spr_sch', 2),
    "Счета прихода": do('spr_sch', 3),
}

_sprav = {
    'Справочник МОЛ': do('spr_mol'),
    'Справочник счетов': _sub_sprav,
    'Справочник наименований': do('spr_tow'),
    'Справочник для pазноса pасхода': do('spr_razn')
}

_mes = {
    'Расчетный месяц': do('sel_mes'),
    '-1': None,
    'Перенос сальдо': do('saldo')
}

_disk = {
    'Сброс данных за месяц на диск': do('arh_c_a'),
    '\-': None,
    'Добавление данных с диска': do('arh_a_c'),
}

_print = {
    'Печать ведомости по расходу': do('print5'),
    'Печать расшифровки по расходу': do('print6'),
    'Расшифровка по расходу за год': do('print7'),
}

msys_menu = {
    '_MSYSMENU': {
        '_Menu0': {
            'Общее': _about,
            'Журнал': do('work'),
            'Справочники': _sprav,
            'Месяц': _mes,
            'Диск': _disk,
            'Печать': _print
        }
    }
}
