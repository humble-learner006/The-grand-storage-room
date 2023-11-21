def isValid(number):
    if number % 10 == 0:
        return True
    else:
        return False


# this block is used to test whether the sum of odd and doubleeven number can be divided by 10
# to test whether it is vaild number
def getDigit(fetch):  # this is to choose the right digit to add in step 2
    if fetch * 2 // 10 != 0:  # if it divided by 10 and int part result not=0,means it is bigger than 0
        fetch = int(str(fetch * 2)[1]) + int(str(fetch * 2)[0])  # pick out the two place and add then together
        return fetch
    else:
        fetch *= 2
        return fetch


def sumOfDoubleEvenPlace(number):
    # in comment, I will elaborate by example ("123456789")
    leven = len(str(number))  # we first cal the len of string len("123456789")=9
    sub_number1 = str(number)[-2::-2]  # start from -2 index, pick out every 2 number sub_number1=("8642")
    sum1 = 0  # create a number type data to store the sum, remark!!: data creation should be out of loop
    for i in sub_number1:  # pick out the number in sub_number1 one by one
        i = int(i)
        sum1 += getDigit(i)  # all fetch is return in a int type, we add them up
    return sum1


def sumOfOddPlace(number):  # this is step 3
    sub_number2 = str(number)
    sub_number2 = sub_number2[::-2]  # similar from above block, this one is to pick out the odd place number
    sum2 = 0
    for i in sub_number2:
        sum2 += int(i)
    return sum2


def main():
    number = input("please input a credit card number: ")
    try:
        number = int(number)
    except:
        number = input("please input right things: ")  # this block make program robust enough
    if isValid(sumOfOddPlace(number) + sumOfDoubleEvenPlace(number)):
        print("this is a valid card number")
    else:
        print("this is not a valid card number")


# main function combine all function together

main()
