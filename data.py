from collections import namedtuple

Transaction = namedtuple(
    'Transaction', [
        'amount',
        'description',
        'datetime',
        'after_balance',
        'before_balance'
    ])
