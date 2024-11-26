user_input1 = (input("List 1: "))
user_input2 = (input("List 2: "))

rm_characters = ",[] "

translation_table = str.maketrans("", "", rm_characters) 

user1_result = user_input1.translate(translation_table)
user2_result = user_input2.translate(translation_table)

if user1_result == user2_result:
    print("Lists are equal")
else:
    print("Lists are not equal")
