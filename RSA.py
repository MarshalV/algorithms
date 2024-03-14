# Алгоритм шифрования PSA


# Алгоритм RSA (Rivest-Shamir-Adleman) является одним из самых широко используемых алгоритмов асимметричного шифрования и создания электронной подписи.
# Он был предложен в 1977 году Рональдом Ривестом, Ади Шамиром и Леонардом Адлеманом.

# Генерация ключей:
# Выбираются два простых числа p и q, обычно большие.
# Вычисляется их произведение n=p×q, которое является модулем шифрования и дешифрования.
# Вычисляется значение функции Эйлера φ(n)=(p−1)×(q−1), где φ - функция Эйлера.
# Выбирается целое число e, взаимно простое с φ(n) и меньшее, чем φ(n). e становится открытым ключом.
# Вычисляется число d, обратное e по модулю φ(n), т.е. d×e≡1(modφ(n)). d становится закрытым ключом.

# Шифрование сообщения:
# Сообщение M представляется в виде числа, меньшего, чем n.
# Шифрование выполняется с помощью открытого ключа e: C≡M^e (mod n). Здесь C - зашифрованное сообщение.

# Дешифрование сообщения:
# Полученное зашифрованное сообщение C дешифруется с помощью закрытого ключа d: M≡C^d (mod n). Здесь M - исходное сообщение.

# Подпись сообщения:
# Чтобы подписать сообщение M, вычисляется его хэш-значение H(M).
# Полученное хэш-значение H(M) шифруется с использованием закрытого ключа: S≡H(M)^d (mod n). S - подпись сообщения.

# Проверка подписи сообщения:
# Полученное подписанное сообщение M проверяется с использованием открытого ключа и подписи S: H(M)≡S^e (mod n).
# Если полученное значение совпадает с хэш-значением исходного сообщения H(M), то подпись считается верной.

# Алгоритм RSA обладает высокой стойкостью к взлому, если используются достаточно длинные ключи.
# Он широко применяется в сферах криптографии, безопасности данных, аутентификации и защите информации.


"""Передача открытого и закрытого ключей другому пользователю требует безопасного канала связи. Вот несколько способов передачи ключей и пример того,
как получатель может использовать их для расшифровки сообщения:

                                       Личная передача ключей:

Если возможно, можно лично передать открытый и закрытый ключи другому пользователю, используя, например, USB-накопители или другие съемные носители.
Этот способ обеспечивает высокую степень безопасности, поскольку не требует передачи через сеть.

                                        Шифрование ключей с помощью публичного ключа получателя:

Отправитель может зашифровать открытый и закрытый ключи с использованием открытого ключа получателя,
а затем отправить зашифрованные ключи через открытые каналы связи, такие как электронная почта или мессенджеры.
Получатель может расшифровать ключи с помощью своего закрытого ключа.

                                        Использование аутентифицированных каналов связи:

Используйте специализированные инструменты или протоколы, такие как SSL/TLS, которые обеспечивают безопасную передачу данных через интернет.
В таких случаях открытые и закрытые ключи могут быть встроены в цифровой сертификат, который может быть проверен и использован автоматически.


                                        Пример расшифровки сообщения получателем с использованием переданных ключей:

Получатель получает открытый и закрытый ключи от отправителя.
Получатель использует открытый ключ для расшифровки сообщения, зашифрованного отправителем.
Если сообщение также подписано отправителем, получатель использует открытый ключ отправителя для проверки подписи и убедиться в его подлинности.
"""


import random
import sympy

def send_encrypted_message(encrypted_message):
    # В реальной системе это будет функция, отправляющая зашифрованное сообщение по выбранному каналу связи,
    # такому как сетевое соединение или сохранение в файле.
    print("Зашифрованное сообщение отправлено")

def receive_encrypted_message():
    # В реальной системе это будет функция, принимающая зашифрованное сообщение из выбранного источника,
    # такого как сетевое соединение или чтение из файла.
    # Здесь мы просто возвращаем фиктивное зашифрованное сообщение для демонстрационных целей.
    return [123, 456, 789]

def generate_keypair():
    # Генерация двух простых чисел p и q
    p = sympy.randprime(2**10, 2**12)
    q = sympy.randprime(2**10, 2**12)

    # Вычисление модуля n и функции Эйлера phi(n)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбор открытой экспоненты e
    e = random.randint(1, phi)
    while sympy.gcd(e, phi) != 1:
        e = random.randint(1, phi)

    # Вычисление закрытой экспоненты d
    d = sympy.mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    e, n = public_key
    # Шифрование каждого символа в строке plaintext с использованием открытого ключа
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    # Дешифрование каждого символа в списке ciphertext с использованием закрытого ключа
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext

# Пример использования:
if __name__ == "__main__":
    # Генерация ключей
    public_key, private_key = generate_keypair()
    print("Открытый ключ:", public_key)
    print("Закрытый ключ:", private_key)

    # Шифрование сообщения
    message = "Hello, RSA!"
    encrypted_message = encrypt(public_key, message)
    print("Зашифрованное сообщение:", encrypted_message)

    # Дешифрование сообщения
    decrypted_message = decrypt(private_key, encrypted_message)
    print("Расшифрованное сообщение:", decrypted_message)





    # Отправитель
    public_key, private_key = generate_keypair()  # Генерация ключей
    message = "Secret message"
    encrypted_message = encrypt(public_key, message)  # Шифрование сообщения
    send_encrypted_message(encrypted_message)  # Отправка зашифрованного сообщения

    # Получатель
    received_encrypted_message = receive_encrypted_message()  # Получение зашифрованного сообщения
    decrypted_message = decrypt(private_key, received_encrypted_message)  # Дешифрование сообщения
    print("Расшифрованное сообщение:", decrypted_message)  # Вывод расшифрованного сообщения