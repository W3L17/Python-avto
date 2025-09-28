#как-то получить от пользователя оценку 

rate_as_str = input("оценка работы специалиста:")
rate = int(rate_as_str)

#проверить что оценка от 1 до 5 
if(rate < 1):
    rate = 1

if(rate > 1):
    rate = 5


#в зависимости от оценки предложить дать обратную связь 


feedback = " "

if (rate == 1):
    feedback = input('Криповоз')

elif(rate == 2):
    feedback = input('AAAAA')

elif(rate == 3):
    feedback = input("fwefwefw")

elif(rate == 4):
    feedback = input("dqdqwdq")

else:
    feedback = input("dwqdqwdqwdqvvve!")

print(feedback)