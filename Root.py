"""

This Module finds roots of number using vedic maths

All the digits since the first one are accurate to 100%
The first digit of root is found by direct method and thereafter in a loop to find the remaining decimels
the loop is self terminating

To understad the working, it is recommended that you first find out
how to find roots of numbers using LONG DIVISION METHOD on google

P.S. root_detailed is deprecated

"""


def sqrt(number: int,  digits: int = 5) -> str:

    power = 2
    # power exists so that i can modify the code to find nth root
    ## in the next versions
    """ returns nth root of the given number as string \n
        upto the no of digits specified ( default 5 )
        """

    # type checking

    if number < 0:
        TypeError("Squares are positive ")
    if number == 0 or 1:
        # return num
        pass

    #  we need to start by reversing the string

    number = str(number)
    float_num = ""

    if "." in number:
        number, float_num = number.split(".")
        ## splitting if the input is a float

    diff = len(number) % power
    if diff != 0:
        # here we are making sure that the string i
        number = "0" * (power - diff) + number
    # s exactly divisible by the number

    #  now grouping accoding to our needs
    ## basically , i take range with intervals as power ( 2 )
    ## then use that place number generated  to find peices of string for the list
    num_list = [(number[place: place + power])
                for place in range(0, len(number), power)]
    float_num_list = [float_num[place:place + power]
                      for place in range(0, len(float_num), power)]

    #  in begining discriminant is 0
    discriminant = 0

# this is generator for providing next digits required
#  I'm using this to add save memory
    def num_generator(list_of_num, float_list):

        for num in list_of_num:
            yield num
        yield "."
        for x in range(digits):
            try:
                yield float_list[x]
            except IndexError:
                yield "00"

    # initializing the generator
    N_generator = num_generator(num_list, float_num_list)

    # original number is put back when working on finding the root
    # here generator gives a benefit as the code does not need to worry about indexes
    original_number = int(next(N_generator))

    # finding the first discriminant or the digit of the root
    for num in range(1, 11):
        if num ** power > original_number:
            discriminant = num - 1
            original_number -= discriminant ** power
            break

    #  root is a string so that it's easy to add next digits by concatation
    root = str(discriminant)  # first digit is found !!
    ##
    discriminant *= 2  # first discriminant

    ## this is the main loop with all the serious jobs
    ## it finds the rest of the digits and heavy crunching of numbers happens here

    for number in N_generator:

        if number == '.':  # if decimal point is supplied by the generator that means
            ## we need to add the same to the root and that the root is a float
            ## the henceforth digits supplied will always be "0" * power given
            root += "."
            continue  # go to the next number

        if original_number == 0:
            break  # stopping once the root is found

        original_number = int(str(original_number) + number)
        ## original number is changed on the fly until it becomes zero
        discriminant *= 10
        ## getting discriminant ready for the next loop

        next_digit = 0

        # finding the digit by trial and error
        for num in range(1, 11):
            if (discriminant + num) * num > original_number:
                next_digit = num - 1
                break

                ## changing stuff once the next digit is found
        original_number -= (discriminant + next_digit) * next_digit
        discriminant += 2 * next_digit
        root += str(next_digit)

    return root


def root_detailed( square , digits = 5 ):
    
    a = square
    n = 0
    root = "" 
    for y in range( 1, (a + 1 ),1 ):
        print( "y = " , y )
        if y*y > a :
            print( "y =  = " , y)
            n = y
            break
    print('n= ' , n)

    n = n - 1 
    a = a - ( ( n) ** 2 )
    print( ' a = ',a )
    root += str(n)
    n = 2*n
    print( 'root = ' , root)
    root += "."

    for looping in range( digits ) :
        if a == 0 :
            root += "0"
            break
        a = 100 * a
        n = 10 * n
        z = 0
        print( ( n + z )  * z )
        print('a = ' , a)
        print('n = ' , n)
        for x in range( 1 , 11, 1 ):
            if  ( ( n + z ) * z ) < a :
                z += 1
                print(   z  )
            if ( ( n + z ) * z ) > a :
                print( " final = " , z)

                break
        if ( ( n + z ) * z ) == a :
            pass
        else :
            z = z - 1

        print(z)
        print('next loop')
        a = a - ( n + z ) *z
        n = n + 2 * z
        root += str(z)
        print( "\n the root is \n " , root  )


    print( "\n the root is \n " )
    return root



