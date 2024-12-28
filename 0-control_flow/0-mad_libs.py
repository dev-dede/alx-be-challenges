day_adjective = input("Enter an adjective to describe the day (eg.. windy, bright): ")
while day_adjective == "beautiful":
    print("Please enter any adjective apart from beautiful")
    day_adjective = input("Enter an adjective to describe the day (eg.. windy, bright): ")

monkey_adjective = input("Enter an adjective to describe a funny monkey (eg., cute, silly): ")
while monkey_adjective == "funny":
    print("Please enter any adjective other than funny")
    monkey_adjective = input("Enter an adjective to describe a funny monkey (eg., cute, silly): ")

lion_adjective = input("Enter an adjective to describe a lion (eg., large, ferocious): ")
while lion_adjective == "majestic":
    print("Please enter any adjective other than majestic")
    lion_adjective = input("Enter an adjective to describe a lion (eg., large, ferocious): ")

experience_adjective = input("Enter an adjective to describe your experience for the day(eg. wonderful, frightening): ")
while experience_adjective == "wild":
     print("Please enter any adjective other than wild")
     experience_adjective = input("Enter an adjective to describe your experience for the day(eg. wonderful, frightening): ")

ending = ""
feelings_for_monkeys = ""

if monkey_adjective == "ugly" or monkey_adjective == "annoying":
    feelings_for_monkeys = "I am not a fun of monekys"
else:
    feelings_for_monkeys =  "I love monkeys!!"

if experience_adjective == "frightening" or experience_adjective == "boring":
    ending = "I am never going to the zoo again"
else:
    ending = "I really loved the zoo"

story = f"""
On a beautiful {day_adjective} day, I went to the zoo. 
I saw a funny {monkey_adjective} monkey swinging from the trees. {feelings_for_monkeys}
Then, I spotted a majestic {lion_adjective} lion lounging in the sun.  
What a wild and {experience_adjective} experience!
{ending}
"""

print(story)