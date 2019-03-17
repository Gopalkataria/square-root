# finding root only of irrational numbers ( = or < 2 digit )

def root( square , digits = 5 ):
    
    a = square
    n = 0
    root = "" 
    for y in range( 1, (a + 1 ),1 ):
##        print( "y = " , y )
        if y*y > a :
##            print( "y =  = " , y)
            n = y
            break
##    print('n= ' , n)

    n = n - 1 
    a = a - ( ( n) ** 2 )
##    print( ' a = ',a )
    root += str(n)
    n = 2*n
##    print( 'root = ' , root)
    root += "."

    for looping in range( digits ) :
        if a == 0 :
            root += "0"
            break
        a = 100 * a
        n = 10 * n
        z = 0
##        print( ( n + z )  * z )
##        print('a = ' , a)
##        print('n = ' , n)
        for x in range( 1 , 11, 1 ):
            #print()
            if  ( ( n + z ) * z ) < a :
                z += 1
                #print(  n ,",", z ,",", ( n + z )  * z )
            if ( ( n + z ) * z ) > a :
##                print()
##                print(  n ,",", z ,",", ( n + z )  * z )
##                print( " final = " , z)

                break
        if ( ( n + z ) * z ) == a :
            pass
        else :
            z = z - 1

##        print(z)
##        print('next loop')
        a = a - ( n + z ) *z
        n = n + 2 * z
        root += str(z)
##        print( a )
        
##    print( ' root = ' , root )

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



