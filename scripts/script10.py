def check(*args):
    pass


class State:
    def __init__(self):
        self.state = 'unauthorized'

    def __str__(self):
        return self.state


transition_table = {
    'unauthorized': [
        ('login', check(), 'authorized')
    ],
    'authorized': [
        ('logout', check(), 'unauthorized'),
        ('deposit', check(), 'authorized'),
        ('withdraw', check(), 'authorized'),
        ('balance', check(), 'authorized')
    ]
}

init_state = State()


class ATM:
    def __init__(self, init_state, init_balance, transition_table, )

    def next()


def main():
    state1 = State()
    print(state1)


if __name__ == "__main__":
    main()


"""
sample input should start with first line password
2nd line balance
3rd line is number of commands

subsequent lines are commands
login password
withdraw 20
deposit 40
withdraw 20
balance
logout 

expected output:
Success = (true or False) (state) (balance)
"""
