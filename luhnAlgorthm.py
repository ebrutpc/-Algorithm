creditCard="1322423143322312"
def solution(creditCard):
    result = False
    cardSize = len(creditCard)
    checkSum = 0
    for i in range(cardSize-1,0,-2):
        ctrlDigit = int(creditCard[i])
        doubles = int(creditCard[i-1])*2
        while(doubles>9):
            doubles=doubles-9
        checkSum += ctrlDigit +doubles
    
    if(checkSum%10==0):
        result=True

    return result