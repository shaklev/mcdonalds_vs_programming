import  mcdonalds_positions

global statement
statement ="answer 'yes' or 'no' "

def mcdonalds_work():
        print "Wow you really want to spend your life on nothinhg , huh .."
        print "So here comes the boss and asks you,where do you want to work:"
        garbage=['cleaner' , 'McCafe worker' , 'Kitchen worker ', 'Cash-worker','Grill']
        for job_type in garbage:
            print " \n > " , job_type

        work=raw_input("> ")

        if "cleaner" in work or "Cleaner" in work:
               mcdonalds_positions.cleaner()
        elif "McCafe" in work:
               mcdonalds_positions.mcCafe()
        elif "Kitchen" in work or "kitchen" in work:
               mcdonalds_positions.kitchen_worker()
        elif "Cash" in work or "cash" in work:
               mcdonalds_positions.cashier()
        elif "Grill" in work or "grill" in work:
               mcdonalds_positions.grill_worker()
        else:
            print "Just answer the damn question, since you want to play :/"
            mcdonalds_work()

def mcdonalds():
    print "Hi you choosed the left side"
    print "Welcome to Mcdonalds"
    mcdonalds_work()


