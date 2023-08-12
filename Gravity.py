import gzip
import os


import math
print("###################################################################################################################################")
print("#                                                                                                                                 #")
print("#                                                                                                                                 #")
print("#                                                                                                                                 #")
print("")
print("                                      ################  May i use your gravity? ##############              ")
print("")
print("")
print("")
print("")
print("                         Purpose: To find the gravity of each planet                                         ")
print("")
print("")
print("                   We will be using gravity formulas and laws to find the gravity force of celestial body ")
print("")
print("")
print("")
print("")
print("")
print("")
print("select: 1 -> sun,2 -> Mercury,3 -> Venus, 4 ->Mars,5 -> Earth,6 -> Jupiter, 7 -> Saturn, 8 -> Uranus, 9 -> Neptune")
print("")
print("")
print("")
print("")
print("")
print("")


def planets(planet):

    if planet == 1:
        print("You have selected the star which thinks it shines,but just passes hot gas")
        print("These are the values for sun: Mass=1.989 * 10**30, Gravitational constant= 6.67 * 10**-11,Radius=696,340,000")
        m=1.989 * 10**30
        G=6.67 * 10**-11
        R=696340000
        #print(m,G,R)
        #print("%f NM-2 X %f / %f*%f",1.989 * 10^30,6.67 *10^-11/696,340,000^92)
        calculatedgravity=calculate(m,G,R)
    elif planet == 2:
        print("You have selected mercury")
        print("These are the values of mercury:mass=3.30 * 10**23,gravitational constant=6.67 * 10**-11.Radius=24937000")
        M=3.30 * 10**23  
        g=6.67 * 10**-11
        r= 24937000
        #print(M,g,r)
        #print("%f NM-2 X %f / %f*%f",3.30 * 10**23,6.67*10**-11/24937000**2)
        calculatedgravity=calculate(M,g,r)
    elif planet == 3:
        print("you have selected the planet of rotten eggs")
        print("These are the values of venus:mass=4.867*10**24,gravitational constant 6.67 * 10**-11,Radius=605180000")
        ma=4.867*10**24
        gr=6.67 * 10**-11
        radius=605180000
        #print(ma,gr,radius)
        #print("%f NM-2 X %f / %f*%f",3.30 * 10**23,6.67*10**-11/605180000**2)
        calculatedgravity=calculate(ma,gr,radius)

    elif planet == 4:
        print("you have selected the land of no iron deficiences")
        print("These are the values of mars:mass=6.39 * 10**23,gravitational constant 6.67 * 10^-11,Radius=3389500")
        mass=6.39 * 10**23
        gravity=6.67 * 10**-11
        rad=3389500
        #print(mass,gravity,rad)
        #print("%f NM-2 X %f / %f*%f",6.39 * 10^23,6.67*10**-11/33895^2)
        calculatedgravity=calculate(mass,gravity,rad)
    
    elif planet == 5:
        print("So.. you wanna know the gravity of the blue planet..Why?")
        print("These are the values of Earth :MASS 5.97219X10^24,GRAVITATIONAL CONSTANT: 6.67X10^-11, RADIUS=6371000")
        mass_earth=5.97219 * 10 ** 24
        gravityfalls=6.67 * 10 ** -11
        radical=6371000
        #print(mass_earth,gravityfalls,radical)
        #print("%f NM-2 X %f / %f*%f",5.97219 * 10^24,6.67 * 10^-11/6371000^2)
        calculatedgravity=calculate(mass_earth,gravityfalls,radical)
        
    elif planet == 6:
        print("you have selected the  gas planet")
        print("These are the values of jupiter :MASS 1.898 * 10^27,GRAVITATIONAL CONSTANT 6.67 * 10^-11,RADIUS=69911000")
        mass_jupiter=1.898 * 10**27
        gravitational_constant=6.67 * 10**-11
        Radius_jupiter=69911000
        #print(mass_jupiter,gravitational_constant,Radius_jupiter)
        #print("%f NM-2 X %f / %f*%f",1.898 * 10^27,6.67 * 10^-11/69911000^2)
        calculatedgravity=calculate(mass_jupiter,gravitational_constant,Radius_jupiter)
    

    elif planet == 7:
        print("you have selected the planet of hula-hoops.No she is not engaged")
        print("These are the values of saturn :MASS 5.683 * 10^26 ,GRAVITATIONAL CONSTANT  6.67 * 10^-11,RADIUS=69911000")
        mass_saturn=5.683 * 10**26
        gravity_saturn=6.67 * 10**-11
        Radius_saturn=58232000 
        #print(mass_saturn,gravity_saturn,Radius_saturn)
        #print("%f NM-2 X %f / %f*%f",5.683 * 10**26,6.67 * 10**-11/58232000**2)
        calculatedgravity=calculate(mass_saturn,gravity_saturn,Radius_saturn)

    elif planet == 8:
        print("No, the cold never bothered her anyway")
        print("These are the values of uranus:MASS 8.681 * 10^25  ,GRAVITATIONAL CONSTANT  6.67 * 10^-11,RADIUS=25362000 ")
        mass_uranus=8.681 * 10 ** 25 
        gravity_uranus=6.67  * 10 ** -11
        Radius_uranus=58232000 
        #print(mass_uranus,gravity_uranus,Radius_uranus)
        #print("%f 10^25 NM^-2 X %f 10^-11 / %f 10^2",8.681 ,6.67, 25362000)
        calculatedgravity=calculate(mass_uranus,gravity_uranus,Radius_uranus)

    elif planet == 9:
        print("Yeah she's very distant in personality")
        print("These are the values of neptune:MASS 8.681 * 10^25  ,GRAVITATIONAL CONSTANT  6.67 * 10^-11,RADIUS=25362000 ")
        mass_neptune=1.024 * 10 **  26
        gravity_neptune =6.67 * 10 ** -11
        Radius_neptune= 25362000 
        print(mass_neptune,gravity_neptune,Radius_neptune)
        calculatedgravity=calculate(mass_neptune,gravity_neptune,Radius_neptune)

    else:
        print("Is this from a different multiverse? If so, sorry we don't have that here.")    
                
            
    
def calculate(mass,gravity_constant,radius):
   # print("Inside calculate",mass,gravity_constant,radius)
    gravity=(gravity_constant*mass)/float(radius)**2
    print("")
    print("")
    print("")
    print("")
    print("             Accelaration due to gravity is:              ",gravity)
    return gravity

while True:
  planet = int(input("Which celestial body do you want to know gravity of(Choose from above)?"))
  os.system('clear')
  planets(planet)




