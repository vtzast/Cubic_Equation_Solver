from math import sqrt, cos, acos, pi

def quadratic_equation_solver(a,b,c):
    if a == 0:
        if b == 0:
            if c == 0:
                print('The equation has an infinite number of roots!')
                print('The equation is in the form 0x=0')
            else:
                print('The equation does not have any roots!')
                print('The equation is in the form 0x=b')
        else:
            x = -c/b
            print('The equation has one root: x =',x)
    else:
        d = b**2 - 4 *a*c
        if d < 0:
            z1 = complex(round(-b/(2*a),2),round(sqrt(-d)/(2*a),2))
            z2 = z1.conjugate()
            print("The equation does not have any real roots!")
            print('But, two distinct (non-real) complex roots:',
                  'z1 =',z1,'and','z2 =',z2)
        elif d == 0:
            x = -b/(2*a)
            print("The equation has one real root, a double root! x =",x)
        else:
            x1 = (-b + sqrt(d))/(2*a)
            x2 = (-b - sqrt(d))/(2*a)
            print('The equation has two real roots:', 'x1 =', round(x1,2),
            'and','x2 =',round(x2,2)) 


cube_root = lambda x: x**(1./3.) if 0 <= x else -(-x)**(1./3.)


def cubic_equation_solver(A,B,C,D): 
    if A == 0:
        quadratic_equation_solver(B,C,D)
    else:
        d = 18*A*B*C*D - 4*(B**3)*D + (B**2)*(C**2) - 4*A*(C**3) - 27*(A**2)*(D**2)
        P = B**2 - 3*A*C
        Q = 9*A*B*C - 2*(B**3) - 27*(A**2)*D  
        if d > 0:
            D1 = (2*(B/A)**3 - 9*((B/A)*(C/A)) + 27 *(D/A))/54
            D2 = ((B/A)**2 - 3*(C/A))/9
            theta = acos(D1/sqrt(D2**3))
            x1 = -2*sqrt(D2)*cos(theta/3) - B/3 
            x2 = -2*sqrt(D2)*cos((theta + 2*pi)/3) - B/3
            x3 = -2*sqrt(D2)*cos((theta - 2*pi)/3) - B/3  
            print('The cubic equation has three distinct real roots',
            'x1 =',round(x1,2),'x2 =',round(x2,2),'and x3 =',round(x3,2))
        elif d < 0: 
            N = cube_root(Q/2 + sqrt((Q**2)/4 - P**3)) + \
            cube_root(Q/2 - sqrt((Q**2)/4 - P**3))
            x = -B/(3*A) + N/(3*A)
            z1 = complex(round((-B/(3*A) - (N/2)/(3*A)),2),
            round(sqrt((3/4)*N**2 - 3*P)/(3*A),2))
            z2 = z1.conjugate()
            print('The cubic equation has one real root x =',round(x,2),'and' +
            ' two (non-real) complex roots','z1 =',z1,'and z2 =',z2)
        else:
            print('The cubic equation has a multiple root, and all of ' + \
            'its roots are real!')
            if P == 0:
                x = -B/(3*A)
                print('In this case the cubi equation has one triple root x =',x)
            else:
                xd = (9*A*D - B*C)/(2*P)
                xs = (4*A*B*C - 9*A**2*D - B**3)/(A*P)
                print('In this case the cubic equation has a double root xd =',xd,
                'and a single root xs =',xs)
