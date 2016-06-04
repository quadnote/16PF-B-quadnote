#-*-coding:utf8
#상위 클래스 이름이 너무 길어져서 from import as 적용
from CashCardClass import SimpleCashCard as CashCard


#CashCardClass 모듈의 SimpleCashCard 클래스를
#상속받아 SafeCashCard 클래스를 정의한다
#SimpleCashCard는 SafeChahCard의 상위 클래스
#SafeCashCard 는 SimpleCashCard의 하위클래스
class SafeCashCard(CashCard):
    #SimpleCashCard의 다른 기능은 그대로 사용하고
    # {__init__(), deposit(). check_balance()}
    # withdraw () 메소드만 다시 정의한다
    def withdraw(self, amount_won):
        """
        SafeCashCard withdraw method
        Check balance before withdraw
        """
        print("SafeCashCard withdraw()") # 함수 호출 표식
        # 잔고가 충분하면
        if self. check_balance() >= amount_won:
            #
            #
            # 출금한다
            CashCard.withdraw(self, amount_won)
        # 그렇지 않으면
        else:
            #오류를 표시한다
            print("** 오류발생**")
            print("잔고가 부족합니다")
            print("인출되지 않았습니다")
# SafeCashCard 클래스 정의 끝
