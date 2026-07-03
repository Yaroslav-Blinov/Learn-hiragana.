# введение

print("eng or rus?:")
l = input()

y = 0
n = 0


if l == "eng":
    print(
        """Hi, this simple program will help you reinforce your knowledge of hiragana. A character will be displayed, and you have to type its sound. You'll see your results at the end. To start, type 'yes'."""
    )
    print("version: 1.0")

elif l == "rus":
    print(
        """Привет! Эта простая программа поможет тебе закрепить знания хираганы. На экране будет появляться символ, а тебе нужно будет ввести его звучание. В конце ты увидишь свои результаты. Чтобы начать, введи «yes»."""
    )
    print("версия: 1.0")
else:
    print("error, try again:)")

a = input()

# первый символ

if a == "yes":
    print("\n\n\n")
    print("あ")

if l == "eng":
    a = input("Your answer:")
else:
    a = input("Ваш ответ:")

if a == "a":
    y = y + 1
    print("\n")
    print("✅")
elif y == 0:
    y == 0
else:
    y = y - 0
    print("\n")
    print("❌")

# второй символ

print("\n\n\n")
print("か")

if l == "eng":
    a = input("Your answer:")
else:
    a = input("Ваш ответ:")

if a == "ka":
    y = y + 1
    print("\n")
    print("✅")
elif y == 0:
    y == 0
else:
    y = y - 0
    print("\n")
    print("❌")

# третий символ

print("\n\n\n")
print("き")

if l == "eng":
    a = input("Your answer:")
else:
    a = input("Ваш ответ:")

if a == "ki":
    y = y + 1
    print("\n")
    print("✅")
elif y == 0:
    y == 0
else:
    y = y - 0
    print("\n")
    print("❌")

# итог

print("\n\n\n\n\n")

y = str(y)

if l == "eng":
    print("Correct answers:", y + "/" + "3")
else:
    print("Верных ответов:", y + "/" + "3")

# временный блок

print(
    "\n",
    "Rus: Да пока всего три символа, не было времени на большее, ждите обновление",
    "\n",
    "Eng:For now, there are only three characters—I didn't have time for more—so stay tuned for an update.",
)

asd = input()
