#-*-coding:utf8
#모듈과 클래스를 구분하는 예제

balance_won = 0 #현금 카드 잔고


# 현금 카드로 할 수 있는 것: 입금, 출금, 잔고확인

def deposit(amount_won):
    """
    Deposit some amount of money into cash card
    """
    # deposit 함수 안의 balance_won이
    # #전역 변수임을 표시
    global balance_won

    #입금 하면 잔고가 증가한다
    balance_won += amount_won


def withdraw(amount_won):
    """
    Withdraw some amount of money from cash card
    """
    # Withdraw 함수 읜아 balance_won이
    # #전역 변수임을 표시
    global balance_won

    #출금하면 잔고가 감소한다
    balance_won += (-amount_won)


def check_balanace():
    """
    Check how much money is in th cash card
    """
    #통장 잔고를 반환한다
    # #reader function
    return balance_won


