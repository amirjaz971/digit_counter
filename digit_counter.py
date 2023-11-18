def count_digits(num):
    count=0
    while num>0:
        num//=10
        count+=1
    return count
number_to_word={"1":"one","0":"zero","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine","10":"ten"}
num=int(input("enter the number: "))
if num>0:
    count_digits(num)
    digits=number_to_word.get(str(count_digits(num)))
    print(f"{num} has {digits} digits") 
else:
    print("invalid value!")   