# !/usr/bin/env python3
# Name: Carlos Arevalo (caeareva)
# Group Members: “None”

'''
Program requires an input coordinate string because the methods are not recorded.
Then, the program will output bond lengths and angle.

Input: C = (39.447, 94.657, 11.824) N = (39.292, 95.716, 11.027) Ca = (39.462, 97.101, 11.465)

Program output:
Coordinates: C = (39.447, 94.657, 11.824) N = (39.292, 95.716, 11.027) Ca = (39.462, 97.101, 11.465)
N-C bond length = 1.33
N-Ca bond length = 1.46
C-N-Ca bond angle = 124.0
'''

import math

class Triad:
    """
    Calculate angles and distances among a triad of points.

    Author: David Bernick
    Date: March 21, 2013
    Points can be supplied in any dimensional space as long as they are consistent.
    Points are supplied as tupels in n-dimensions, and there should be three
    of those to make the triad. Each point is positionally named as p,q,r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()

    Required Modules: math
    initialized: 3 positional tuples representing Points in n-space
             p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods:  angleP(), angleR(), angleQ() angles measured in radians
          dPQ(), dPR(), dQR() distances in the same units of p,q,r
    """

    def __init__(self, p, q, r):
        """ Construct a Triad.

        Example construction:
            p1 = Triad( p=(1.,0.,0.), q=(0.,0.,0.), r=(0.,0.,0.) ).
        """
        self.p = p
        self.q = q
        self.r = r

    # private helper methods
    def d2(self, a, b):  # calculate squared distance of point a to b
        """ Calculates squared distance of point a to b """
        return float(sum((ia - ib) * (ia - ib) for ia, ib in zip(a, b)))

    def dot(self, a, b):  # dotProd of standard vectors a,b
        """ dotProd of standard vectors a,b """
        return float(sum(ia * ib for ia, ib in zip(a, b)))

    def ndot(self, a, b, c):  # dotProd of vec. a,c standardized to b
        """ dotProd of vec. a,c standardized to b """
        return float(sum((ia - ib) * (ic - ib) for ia, ib, ic in zip(a, b, c)))

    # calculate lengths(distances) of segments PQ, PR and QR
    def dPQ(self):
        """ Provides the distance between point p and point q """
        return math.sqrt(self.d2(self.p, self.q))

    def dPR(self):
        """ Provides the distance between point p and point r """
        return math.sqrt(self.d2(self.p, self.r))

    def dQR(self):
        """ Provides the distance between point q and point r """
        return math.sqrt(self.d2(self.q, self.r))

    def angleP(self):
        """ Provides the angle made at point p by segments pq and pr (radians). """
        return math.acos(
            self.ndot(self.q, self.p, self.r) / math.sqrt(self.d2(self.q, self.p) * self.d2(self.r, self.p)))

    def angleQ(self):
        """ Provides the angle made at point q by segments qp and qr (radians). """
        return math.acos(
            self.ndot(self.p, self.q, self.r) / math.sqrt(self.d2(self.p, self.q) * self.d2(self.r, self.q)))

    def angleR(self):
        """ Provides the angle made at point r by segments rp and rq (radians). """
        return math.acos(
            self.ndot(self.p, self.r, self.q) / math.sqrt(self.d2(self.p, self.r) * self.d2(self.q, self.r)))

def main():
    '''
    Function asks for molecular coordinates, reads over the class functions, and execute equations.
    Then, it prints the solution for bond lengths and angles degrees.
    '''
    inputCoord = input("Enter coordinates: ")  # coordinate input
    # write a function to split the list of coordinates into groupds
    replaceParenthA = inputCoord.replace("(", ",")
    replaceParenthB = replaceParenthA.replace(")", ",")
    element = replaceParenthB.split(",")  # split coordinate
    pass

    # join values to create three 3D vectors (Coordinates)
    carbon = "".join(element[0].split()).strip("=")  # defines carbon coordinates
    nitrogen = "".join(element[4].split()).strip("=")  # defines nitrogen coordinates
    calcium = "".join(element[8].split()).strip("=")  # defines calcium coordinates
    pass

    # map the elements and their respective values (vectors)
    elementDict = {carbon: (float(element[1]), float(element[2]), float(element[3])),
                   nitrogen: (float(element[5]), float(element[6]), float(element[7])),
                   calcium: (float(element[9]), float(element[10]), float(element[11]))}
    pass

    # create a Triad with the elements
    theTriad = Triad(p=elementDict[nitrogen], q=elementDict[carbon], r=elementDict[calcium])
    Nitro_Carbon = theTriad.dPQ()
    Nitro_Calcium = theTriad.dPR()
    Carbon_Nitro_Calcium = (theTriad.angleP()) * (180 / math.pi)
    pass

    # print the corresponding bond length for nitrogen and carbon
    Nitro_Carbon_Bond = print("N-C bond length = {0:0.02f}".format(Nitro_Carbon))
    # print the corresponding bond length for nitrogen and calcium
    Nitro_Calcium_Bond = print("N-Ca bond length = {0:0.2f}".format(Nitro_Calcium))
    # print the corresponding bond angle for carbon, nitrogen and calcium
    Carbon_Nitro_Calcium_Bond_Angle = print("C-N-Ca bond angle = {0:0.1f}".format(Carbon_Nitro_Calcium))
    pass

main()