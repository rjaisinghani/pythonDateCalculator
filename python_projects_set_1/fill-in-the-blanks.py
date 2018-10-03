# Quiz project
# Rohit Jaisinghani
# v1.0
# This is a project I worked on outside of class. It is designed to allow the user to chose between three levels of
# quizzes. The user then fills in the blanks of this quiz, and the full paragraph is slowly redisplayed with the answers
# I use a list to store the answers. I could have used a dictionary as well. A future goal with this program are to
# limit the number of incorrect guesses a user is allowed. I also want to loop the main so that the user can keep
# playing until they say stop. I also want to shorten the size of paragraph replace by creating helper functions for it
# Lastly, instead of partially filling in the paragraph, I want the user to answer their first fill in,then go
# through the paragraph to replace all instances of that answer, then answer the next fill in. Helper functions might
# make this easier to accomplish

# These are my answer keys for the paragraphs
p1AnswerKey = [['__1__','function'], ['__2__','variables'], ['__3__','None'], ['__4__','lists'],['','']]
p2AnswerKey = [['__1__','cpu'], ['__2__','psu'], ['__3__','hard drive'], ['__4__','operating system'], ['__5__','driver']]
p3AnswerKey = [['__1__','cross up'], ['__2__','counter'], ['__3__','combo'], ['__4__','neutral'], ['__5__','overhead']]

# These three functions return the paragraph string based on which one is selected. 1 being easiest, 3 being hardest
def displayParagraph1():
    sample = '''A __1__ is created with the def keyword. You specify the inputs a __1__ takes by
    adding __2__ separated by commas between the parentheses. __1__s by default return __3__ if you
    don't specify the value to return. __2__ can be standard data types such as string, number, dictionary,
    tuple, and __4__ or can be more complicated such as objects and lambda functions.'''
    return sample


def displayParagraph2():
    s = '''A __1__ is the brain of a computer and handles the computation. The
    __2__ provides power to all components in a desktop. The __3__ is where a users
    information is stored. A(n) __4__ is the software that makes interacting with
    a computer intuitive and easy. A(n) __5__ is a type of software that controls
    different peripherals and devices such as mice,keyboards, printers, etc.'''
    return s


def displayParagraph3():
    s = '''A(n) __1__ is a term in fighting games that refers to a move hitting behind you.
    A(n) __2__ is a move that lands a hit while your opponent is performing a move.
    A series of attacks that land without interruption is referred to as a(n) __3__.
    When neither you nor your opponent are performing combos or attack strings against
    each other, you are in __4__ game play. A(n) __5__ move hits you when you are
    crouching.'''
    return s


# This functions determines which paragraph to return based on the user's input choice.
def paragraphChooser(level):
    if level == 'easy':
        return displayParagraph1()
    elif level == 'medium':
        return displayParagraph2()
    else:
        return displayParagraph3()


# This function determines which answer key to return based on the level selected by the user.
def answerKeyChooser(level):
    if level == 'easy':
        return p1AnswerKey
    elif level == 'medium':
        return p2AnswerKey
    else:
        return p3AnswerKey


# this will be a helper function for paragraphReplace
#def unnamedFunc(s, key):

#   return


# This function does the brunt of the work by going through the paragraph, looking for numbered blanks, comparing them
# with answers, replacing the blanks if the answer is correct, and adding everything to a new string that will be
# returned. This function is the one that I need to work on. I need to shorten it by creating helper functions.
def paragraphReplace(s, key):
    print(s)
    index = 0
    str = ''
    while index < len(s):
        if s[index:index + 5] == key[0][0]:
            ans1 = input("Enter your answer for 1: \n")
            if ans1 == key[0][1]:
                str += ans1

                index += 5
            else:
                print("Sorry, that was not the right answer: Try again")
        elif s[index:index + 5] == key[1][0]:
            ans2 = input("Enter your answer for 2: \n")
            if ans2 == key[1][1]:
                str += ans2

                index += 5
            else:
                print("Sorry, that was not the right answer: Try again")
        elif s[index:index + 5] == key[2][0]:
            ans3 = input("Enter your answer for 3: \n")
            if ans3 == key[2][1]:
                str += ans3

                index += 5
            else:
                print("Sorry, that was not the right answer: Try again")
        elif s[index:index + 5] == key[3][0]:
            ans4 = input("Enter your answer for 4: \n")
            if ans4 == key[3][1]:
                str += ans4

                index += 5
            else:
                print("Sorry, that was not the right answer: Try again")
        elif s[index:index + 5] == key[4][0]:
            ans5 = input("Enter your answer for 5: \n")
            if ans5 == key[4][1]:
                str += ans5
                index += 5
            else:
                print("Sorry, that was not the right answer: Try again")
        else:
            str += s[index]
            index += 1
    return str


# The main function calls the functions above to run the program
def main():
    user_wants_to_play = True
    userPlays =''
    while user_wants_to_play is True:
        userPlays = input("Want to test your knowledge? \n")
        if userPlays == 'yes':
            level_choice = input("Enter your level choice: easy, medium, or hard! ")
            answer_choice = answerKeyChooser(level_choice)
            paragraph_choice = paragraphChooser(level_choice)
            print(paragraphReplace(paragraph_choice,answer_choice))
            print('looks like you passed the quiz!')
        else:
            print("See you next time!")
            break


# Call to main
main()
