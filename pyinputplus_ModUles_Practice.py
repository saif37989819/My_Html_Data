import pyinputplus as pyip

age = pyip.inputInt(prompt='Apni age likhein: ',lessThan=100, greaterThan=5,limit=3, timeout=10, blank=False)
print('Aapki age:', age)

fruit = pyip.inputChoice(['apple', 'banana', 'mango'], prompt='Konsa fruit pasand hai? ')
print('Aapne chuna:', fruit)

num = pyip.inputNum(prompt='1 se 10 ke darmiyan koi number likhein: ', min=1, max=10)
print('Aapne likha:', num)

answer = pyip.inputYesNo(prompt='Kya aap Python seekhna chahtay hain? (yes/no): ')
print('Jawab:', answer)

email = pyip.inputEmail(prompt='Apna email likhein: ')
print('Aapka email:', email)
import pyinputplus as pyip

num1 = pyip.inputInt(prompt='Ek number likhein: ', limit=3, default='No input')
print('Aapne likha:', num1)
name = pyip.inputStr(prompt='Apna naam likhein: ', timeout=10, default='Guest')
print('Naam:', name)

comment = pyip.inputStr(prompt='Kuch kehna chahenge? (chhod bhi saktay hain): ', blank=True)
print('Aapka jawab:', comment)

email = pyip.inputEmail(
    prompt='Apna email den: ',
    limit=3,
    timeout=20,
    default='noemail@example.com',
    blank=False
)
print('Email:', email)





 
