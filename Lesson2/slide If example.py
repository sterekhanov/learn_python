#IF

#1. проверка с одним условием
balance = -10
print(bool(balance < 0))

if balance < 0:
print('Пожалуйста, пополните баланс!')


#2. Использование нескольких условий
balance = 100
price = 200
#print(bool(balance < 0 or price > balance)) 

#if balance <0 or price > balance:
#   print('Пожалуйста, пополните баланс!') 
   

#3. Проверка с развилкой
balance = 100
price = 200

if balance > price:
   print('Спасибо за покупку!')
else:
   print('Пожалуйста, пополните баланс!')      



#4. Проверка несколько условий  
temperature = 20
    
if temperature < 0:
    print('На улице холодно!')
elif 0 <= temperature <= 15:
    print('На улице прохладно')
elif 15 <= temperature <= 25:
    print('На улице тепло')
else:
    print('На улице жарко')  


#5. Помещаем условие внутрь функции
def weather(temperature):
    if temperature < 0:
        return 'На улице холодно!'
    elif 0 <= temperature <= 15:
        return 'На улице прохладно'
    elif 15 <= temperature <= 25:
        return 'На улице тепло'
    else:
        return 'На улице жарко'

print(weather(10))


#6. Условие внутри функции со скидками

phone1 = {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 'discount': 25}
phone2 = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 10}

def discounted(price, discount, max_discount=20, name=''):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('Слишком большая максимальная скидка')
    if discount >= max_discount or "iphone" in name.lower():
        return price
    else:
        return price - (price * discount / 100)

dis_iphone = discounted(phone1['price'], phone1['discount'], name=phone1['name'])
print(dis_iphone)
#65432.1

dis_android = discounted(phone2['price'], phone2['discount'], name=phone2['name'])
print(dis_android)
#45000.0