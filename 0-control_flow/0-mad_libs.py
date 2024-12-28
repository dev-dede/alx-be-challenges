day_adjective = input("Enter an adjective to describe the day (eg.. windy, bright): ")
while day_adjective == "beautiful":
    day_adjective = input("Please enter any adjective apart from beautiful: ")

monkey_adjective = input("Enter an adjective to describe a funny monkey (eg., cute, silly): ")
while monkey_adjective == "funny": #Validate input to prevent repetition since adjective funny would be used in story
    monkey_adjective = input("Please enter any adjective other than funny: ")

lion_adjective = input("Enter an adjective to describe a lion (eg., large, ferocious): ")
while lion_adjective == "majestic": #Validate input to prevent repetition since adjective majestic would be used in story
    lion_adjective = input("Please enter any adjective other than majestic: ")

experience_adjective = input("Enter an adjective to describe your experience for the day(eg. wonderful, frightening): ")
while experience_adjective == "wild": #Validate input to prevent repetition since adjective wild would be used in story
     experience_adjective = input("Please enter any adjective other than wild: ")
 
feelings_for_monkeys = "I love monkeys" if monkey_adjective not in ["ugly", "annoying"] else  "I am not a fun of monkeys"

ending = "I really loved the zoo" if experience_adjective not in ["frightening", "boring"] else "I am never going to the zoo again"

story = f"""
On a beautiful {day_adjective} day, I went to the zoo. 
I saw a funny {monkey_adjective} monkey swinging from the trees. {feelings_for_monkeys}
Then, I spotted a majestic {lion_adjective} lion lounging in the sun.  
What a wild and {experience_adjective} experience!
{ending}
"""

print(story)