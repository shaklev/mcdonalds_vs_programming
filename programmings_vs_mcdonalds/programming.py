def programming():
    print "Thank God. You are obviuously a smart person and you don't want unhealthy food"
    print "Since you decided to program in which language are you most interested in:"
    languages= ['Java' , 'C#' ,'Python','C++','Web Development']
    for language in languages:
        print "* " , language
    lang=raw_input("> ")

# Here starts java_func()

    if "Java" in lang or "java" in lang:
        print "You have chosen to learn Java"
        print " Average salary: 6000 euros"
        print "Here are the caracteristics of Java:"
        print " -------------------------------"
        print"""
    - Simple
    - Object-Oriented
    - Platform independent
    - Secured
    - Robust
    - Architecture neutral
    - Portable
    - Dynamic
    - Interpreted
    - High Performance
    - Multithreaded
    - Distributed
    """
        print " -------------------------------"
        print "Which level do you prefer, beginner or advanced?"
        level_java=raw_input("> ")

        if "beginner" in level_java or "Beginner" in level_java:
            print "Okay language to start with. Since you are a begginer you'll be introduced with " \
                  "object-oriented programming here."
            print """Here are some resources that can help you

            http://www.oracle.com/events/global/en/java-outreach/resources/java-a-beginners-guide-1720064.pdf
            http://www.amazon.com/Java-Beginners-Guide-5th-Edition/dp/0071606327
            http://eclipsetutorial.sourceforge.net/totalbeginner.html
            """

        elif "advanced" in  level_java or "Advanced" in level_java:
            print "Nice, you want to be a super-hero at Java right? Here are some hints and books that might help you"
            print """
            Java Specification
            The elements of Java style
            Effective Java
            """
        else:
            print "Choose the right level."
# here ends java programming

#here starts c++ programming
    elif "c++" in lang or "C++" in lang:

        print "So you've decided to learn C++. You have to learn verry hard you know?"
        print "C++ is very 'huge' language and you have to take your time"
        print "Average salary : 5800 euros"
        print " Here are some characteristics"
        print " -------------------------------"
        print """
            C++ is an Object Oriented Programming Language (OOPL).
            C++ have huge Function Library
            C++ is highly Flexible language with Versatility.
            C++ can be used for developing System Software viz., operating systems, compilers, editors and data bases.
            C++ is suitable for Development of Reusable Software. , thus reduces cost of software development.
            C++ is a Machine Independent Language.
            """
        print " --------------------------------"
        print "Which level do you prefer, beginner,advanced?"
        level_cplus=raw_input("> ")
        if "beginner" in level_cplus or "Beginner" in level_cplus:
            print """
            Here are excelenet books for c++ for beginners:

            http://www.amazon.com/exec/obidos/ASIN/0321714113/solarianprogr-20/
            http://www.amazon.com/exec/obidos/ASIN/0321776402/solarianprogr-20/
            http://www.amazon.com/exec/obidos/ASIN/0321543726/solarianprogr-20/
            """
        elif "advanced" in level_cplus or "Advanced" in level_cplus:

            print """
            Here are advanced resources:
           - http://aszt.inf.elte.hu/~gsd/halado_cpp/
           - https://www.youtube.com/playlist?list=PLE28375D4AC946CC3
           """
        else:
            print "Choose the right level."
#here ends c++ programming

#here starts c# programming

    elif "c#" in lang or "C#" in lang:

        print "So Microsoft huh, good job. If you decided to stick with C# ,easy and fun language to learn."
        print "You can work on multiply platforms , and maybe one day in Microsoft , who knows.."
        print "Here are some characteristics of C#:"
        print "Average salary: 5500 euros"
        print " -------------------------------"
        print """
        C# is a simple ,modern,object oriented language derived from C++ and Java.
        It aims to combine the high productivity of Visual Basic and the raw power of C++.
        It is a part of Microsoft Visual Studio7.0.
        Visual studio supports Vb,VC++,C++,Vbscript,Jscript.All of these languages provide access to the Microsft .NET platform.
        .NET includes a Common Execution engine and a rich class library.
            """
        print " -------------------------------"
        print "Which level do you prefer, beginner or advanced?"
        level_csharp=raw_input("> ")
        if "beginner" in level_csharp or "Beginner" in level_csharp:
            print """
            http://www.blackwasp.co.uk/CSharpFundamentals.aspx
            http://www.codeproject.com/
            """

        elif "advanced" in level_csharp or "Advanced" in level_csharp:
            print """
            https://msdn.microsoft.com/en-us/library/ms228395%28v=vs.90%29.aspx
            http://www.ssw.uni-linz.ac.at/Teaching/Lectures/CSharp/Tutorial/Part2.pdf
            """

        else:
            print "Choose the right level."

# here ends c# programming

#here starts python programming

    elif "Python" in lang or "python" in lang:

        print "Wonderful choise. At the moment this game you are playing is written in Python"
        print "It's very intersting language and it's used for all types of jobs"
        print "Average salary 6200 euros"
        print " Here are some characteristics of Python language"
        print " ----------------------------------------"
        print """
        - Simple
        - Easy to learn
        - Free and Open source
        - Portable
        - High-level Language
        - Extensible
        """
        print "--------------------------------------------"
        print "Which level of Python do you prefer, beginner or advanced?"
        level_python=raw_input("> ")
        if "beginner" in level_python or "Beginner" in level_python:
            print """
            https://wiki.python.org/moin/BeginnersGuide
            https://www.youtube.com/watch?v=cpPG0bKHYKc (and part2,3...)
            Learn Python the Hard way
            """

        elif "advanced" in level_python or "Advanced" in level_python:
            print """
            http://www.codecademy.com/courses/python-beginner-en-KAgt5/0/1?curriculum_id=5057a8a1f7735c00020339b4
            http://www.python-course.eu/advanced_topics.php
            """

        else:
            print "Choose the right level."

# here ends python programming

#here starts Web-dev programming

    elif "web" in lang or "Web" in lang:

        print "You decided to go Web-programming.This includes front-end & back-end solutions"
        print "If you have eye for design you can work only front-end, but if you like logic more, shift to the backend"
        print "Average salary 5000 euros"
        print "Would you like front-end or back-end programming?"
        level_web=raw_input("> ")
        if "front" in level_web or "Front" in level_web:
            print """
            http://www.amazon.com/Web-Design-HTML-JavaScript-jQuery/dp/1118907442/ref=sr_1_2?s=books&ie=UTF8&qid=1435065517&sr=1-2&keywords=html
            (HTML, CSS , JavaScript , JQuery)
            """

        elif "back" in level_web or "Back" in level_web:
            print """
            - You should try learning PHP,Python(for web),Node.js,Ruby on Rails etc.
            There are many resources for these books & free courses on the Internet
            """

        else:
            print "Choose the right level."

# here ends Web-dev programming
    else:

        print "Choose one of the languages bellow"
        programming()
