try:
    first_word = str(input("Write 1 word/numb: "))
    second_word = str(input("Write 2 word/numb: "))
    first_word, second_word = second_word, first_word

    print("The first word now: " + first_word +
         "\nThe second word now: " + second_word)
    if first_word == " " or second_word == " ":
         raise Exception("There is an empty lines")
except Exception as exi:
     print(exi)