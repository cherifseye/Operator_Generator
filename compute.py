import random
import operator

def random_operation():
    operators = {
        '+':operator.add,
        '-':operator.sub,
        '*':operator.mul,
        '/':operator.truediv
    }
    left_num = random.randrange(11)
    right_num = random.randrange(11)
    operations = random.choice(list(operators.keys()))
    answer = operators.get(operations)(left_num, right_num)
    print('what is', left_num, operations, right_num, '?')
    return answer

def ask_question():
    answer = random_operation()
    guess = float(input())
    return answer == guess

def game():
    score = 0
    for i in range(5):
        if ask_question() == True:
            print('Correct')
            score += 1
        else:
            print('incorrect')
    print('Your score is', score)

game()       