# horoscope project for Python-boothcamp
print("Welcome,let's get to know your horoscope for today!!!")
condition = True
while condition==True:
    print('''
    1.Capricorn: January 20 to February 16
    2.Aquarius: February 16 to March 11
    3.Pisces: March 11 to April 18
    4.Aries: April 18 to May 13
    5.Taurus: May 13 to June 21
    6.Gemini: June 21 to July 20
    7.Cancer: July 20 to August 10
    8.Leo: August 10 to September 16
    9.Virgo: September 16 to October 30
    10.Libra: October 30 to November 23
    11.Scorpio: November 23 to December 17
    12.Sagittarius: December 17 to January 20
     ''')
    sign=int(input("Please pick your sign number and press enter\n " ))
    print(sign)

    if sign==1:
        print('''A passionate encounter with a love partner might cement the bond between you so thoroughly that you start talking about 
                 commitment or even a wedding.
                 A romantic haze may permeate your interactions. Still, exercise some restraint in expressing your feelings. 
                 Hitting your friend with too much at once could have the opposite effect from the one you're hoping for. Be patient!
        ''')
    elif sign==2:
        print(''' Have you been feeling less than your normal self, Aquarius? If so, today you may suddenly regain your strength and be raring to go.
        You might even be tempted to start a rigorous exercise program. 
        Go ahead and start, but pace yourself and try not to make up for lost time all at once.
        You need to ease into these things.Maybe start with walking and yoga.
        ''')
    elif sign==3:
        print('''Love and romance aren't just part of your life today, Pisces, they're your whole life.
        If you're single, an exciting potential partner could have you reeling.
        If you're currently involved, recent events may have created such a powerful bond between you and your beloved that you think it will never end.
        Consider what led to this feeling and find a way to repeat it.This can only benefit you.
        ''')
    elif sign==4:
        print('''Does your house look like a cyclone hit it? Your tidy nature should drive you to clean it up.
        In the course of wading through the mess, don't be surprised if you discover some objects you thought you'd lost forever.
        Once you finish, you'll probably find that the place looks beautiful,better than it did before it was messed up.
        Something good can indeed come out of chaos.
        ''')
    elif sign==5:
        print('''An exciting phone call or email could come from a friend who has some great news for you, Taurus.
        Love, romance, and success in the arts are all highlighted now, and this communication could bring it to your attention.
        Conversations could bring inspiration your way, and your mind is apt to be going a thousand miles an hour for most of the day.
        Make the most of it!
        ''')
    elif sign==6:
        print('''An online group could form today, Gemini, perhaps friends who are involved in the arts or meditation or spiritual studies.
        This group is likely to be close, probably through mutual interests, so communicating with them this evening should be both intellectually stimulating and emotionally gratifying.
        What takes place today could also bring healing of some kind, either for you or for someone else.
        ''')
    elif sign==7:
        print('''Communication involving romance could come unexpectedly today, Cancer.
        You may get a loving message from a romantic partner, or you could hear of a wedding to take place in the future amongst your circle of friends.
        You could also read a love poem or romance novel or write something along the same lines yourself! Someone might also express affection to you.
        Don't be surprised. You deserve it!
        ''')
    elif sign==8:
        print('''A chance to increase your income by participating in an artistic project of some kind could come your way today, Leo.
        You might take part in the creative work or you could promote it in a business capacity. Whichever it is, you're likely to form some firm friendships in the process.
        If you're single, one of your colleagues might turn out to be a potential love partner.Enjoy!
        ''')
    elif sign==9:
        print('''Inspiration could hit today, Libra. It's a beautiful feeling, but you might not be sure how to channel it.
        It could represent a spiritual breakthrough, artistic inspiration, increased understanding of others, or all of the above.
        What's almost certain is that you'll want to spend time alone to take it all in and figure out how to use it.
        Don't dismiss any possibility,however outrageous it may seem.
        ''')
    elif sign==10:
        print('''You might have the chance to speak with new people in interesting fields, perhaps from foreign lands, Scorpio.
        Your conversational abilities are at an all-time high, so you'll not only enjoy talking with everyone, but they'll enjoy talking with you, too.
        Intriguing ideas and useful information could have your mind buzzing all night.
        Try to take a walk in the evening to clear your head.
        ''')
    elif sign==11:
        print('''Information gleaned from surprising sources could lead to sudden, fortunate career breaks, Sagittarius.
        You might explore totally new fields, although this could be temporary.
        Your efforts should attract the attention of those who matter and eventually lead to advancement or a raise.
        Don't be afraid to continue to explore these sources. Keep up the good work!
        ''')
    elif sign==12:
        print('''A passionate encounter with a love partner might cement the bond between you so thoroughly that you start talking about commitment or even a wedding. A romantic haze may permeate your interactions.
        Still, exercise some restraint in expressing your feelings.
        Hitting your friend with too much at once could have the opposite effect from the one you're hoping for.Be patient!
        ''')
    else:
        print("You might have choosen wrong option try again!")

    condition = True if input("\nHey,do want to read for other signs as well?(Y/N)")=="Y" else False

print("Thank you!!")










