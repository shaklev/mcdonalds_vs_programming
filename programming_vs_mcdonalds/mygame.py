import  sys
import mc_donalds
import programming
global statement
statement ="answer 'yes' or 'no' "

def start():
    print "Hello human , do you wanna play a game ? ", statement
    answer=raw_input("> ")
    if "yes" in answer or "Yes" in answer:
        print "Glad you want , to play"
        print "Just to warn you , i will be very honest with you"

        print "Choose left or right door:"
        side=raw_input("> ")
        if "left" in side:
            print "So you have time to go back to the start, but would you ?" , statement
            annswer=raw_input("> ")
            if "yes" in annswer or "Yes" in annswer:
                start()
            elif  "no" in annswer or "No" in annswer:
               mc_donalds.mcdonalds()
            else:
                print "Here we go from the start ....."
                start()
        elif "right" in side:
            programming.programming()
        else:
            print "You didn't choose either side , probably you are just another 'follower' "
            print "Too bad..."

    elif  "no" in answer or "No" in answer:
        print "Too bad , i just wanted to play .... :("
        sys.exit(0)

    else:
        print "Wow just answer yes or no !!!"
        start()

start()



