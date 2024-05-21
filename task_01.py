'''Маємо набір монет [50, 25, 10, 5, 2, 1].
Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити оптимальний спосіб видачі решти покупцеві.

Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:

Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, 
і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. 
Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.'''

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    result = {}
    
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            amount -= coin * count
            result[coin] = count

    return result

# Приклад використання
print(find_coins_greedy(113))  # {50: 2, 10: 1, 2: 1, 1: 1}


'''Функція динамічного програмування find_min_coins. 
Ця функція також повинна приймати суму для видачі решти, 
але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет,
необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом.
Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}'''

def find_min_coins(amount, coins, memo):
    if amount in memo:
        return memo[amount]
    if amount == 0:
        return {}
    if amount < 0:
        return None

    min_coins = None
    for coin in coins:
        remaining_amount = amount - coin
        result = find_min_coins(remaining_amount, coins, memo)
        
        if result is not None:
            current_result = result.copy()
            if coin in current_result:
                current_result[coin] += 1
            else:
                current_result[coin] = 1
            
            if min_coins is None or sum(current_result.values()) < sum(min_coins.values()):
                min_coins = current_result

    memo[amount] = min_coins
    return min_coins

def main():
    coins = [50, 25, 10, 5, 2, 1]
    amount = 113
    memo = {}
    
    result = find_min_coins(amount, coins, memo)
    
    if result:
        print(result)
    else:
        print("Не можна видати задану суму з наявними номіналами монет.")

if __name__ == "__main__":
    main()
