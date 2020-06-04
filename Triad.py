#!/usr/bin/env python3 
# Name: Carlos Arevalo (caeareva) 
# Group Members: “None”

import numpy
class Triad:
    """
    Calculate angles and distances among a triad of points.

    Author: Carlos Arevalo
    Date: April 10, 2020
    Points can be supplied in any dimensional space as long as they are consistent.
    Points are supplied as tupels in n-dimensions, and there should be three
    of those to make the triad. Each point is positionally named as p, q, r
    and the corresponding angles are then angleP, angleQ and angleR.
    Distances are given by dPQ(), dPR() and dQR()

    Required Modules: numpy, math
    Numpy uses the linear algebra method linalg to calculate the dot product.
    initialized: 3 positional tuples converted to numpay arrays which represent Points in n-space
             p1 = Triad( p=(1,0,0), q=(0,0,0), r=(0,1,0) )
    attributes: p,q,r the 3 tuples representing points in N-space
    methods:  angleP(), angleR(), angleQ() angles measured in radians
          dPQ(), dPR(), dQR() distances in the same units of p,q,r
    """

    def __init__(self, p, q, r):
        """ Construct a Triad.

        Three positional tuples converted to numpy arrays.
        Example construction:
            p1 = Triad( p=(1.,0.,0.), q=(0.,0.,0.), r=(0.,0.,0.) ).
        """
        self.p = numpy.asarray(p)  # converts p tuple to array
        self.q = numpy.asarray(q)  # converts q tuple to array
        self.r = numpy.asarray(r)  # converts r tuple to array

    def dPQ(self):
        """ Provides the distance between point p and point q """
        return numpy.linalg.norm(self.p - self.q)

    def dPR(self):
        """ Provides the distance between point p and point r """
        return numpy.linalg.norm(self.p - self.r)

    def dQR(self):
        """ Provides the distance between point q and point r """
        return numpy.linalg.norm(self.q - self.r)

    def angleP(self):
        """ Provides the angle made at point p by segments pq and pr (radians). """
        return numpy.arccos(numpy.dot((self.q - self.p), (self.r - self.p)) / (
                    numpy.linalg.norm(self.q - self.p) * numpy.linalg.norm(self.r - self.p)))

    def angleQ(self):
        """ Provides the angle made at point q by segments qp and qr (radians). """
        return numpy.arccos(numpy.dot((self.p - self.q), (self.r - self.q)) / (
                    numpy.linalg.norm(self.p - self.q) * numpy.linalg.norm(self.r - self.q)))

    def angleR(self):
        """ Provides the angle made at point r by segments rp and rq (radians). """
        return numpy.arccos(numpy.dot((self.p - self.r), (self.q - self.r)) / (
                    numpy.linalg.norm(self.p - self.r) * numpy.linalg.norm(self.q - self.r)))

def main():
    '''
    Function asks for molecular coordinates, reads over the class functions, and execute equations.
    Then, it prints the solution for bond lengths and angles degrees. The method uses numpy.pi to convert the angles from radians to degrees.
    It could also use the math module without importing it.
    '''
    inputCoord = input("Coordinates: ")  # coordinate input
    # write a function to split the list of coordinates into groupds
    replaceParenthA = inputCoord.replace("(", ",")
    replaceParenthB = replaceParenthA.replace(")", ",")
    element = replaceParenthB.split(",")  # split coordinate
    pass

    # join values to create three 3D vectors (Coordinates): x, y, and z
    carbon = "".join(element[0].split()).strip("=")  # defines carbon coordinates
    nitrogen = "".join(element[4].split()).strip("=")  # defines nitrogen coordinates
    calcium = "".join(element[8].split()).strip("=")  # defines calcium coordinates
    pass

    # map the elements and their respective values (vectors)
    elementDict = {carbon: (float(element[1]), float(element[2]), float(element[3])),
                   nitrogen: (float(element[5]), float(element[6]), float(element[7])),
                   calcium: (float(element[9]), float(element[10]), float(element[11]))}
    p = elementDict[nitrogen]
    q = elementDict[carbon]
    r = elementDict[calcium]
    pass

    # create a Triad with the elements
    theTriad = Triad(p=elementDict[nitrogen], q=elementDict[carbon], r=elementDict[calcium])
    pass

    # print the corresponding bond length for nitrogen and carbon
    Nitro_Carbon_Bond = print("N-C bond length = {0:0.02f}".format(theTriad.dPQ()))  # Nitro_Carbon = theTriad.dPQ()
    # print the corresponding bond length for nitrogen and calcium
    Nitro_Calcium_Bond = print("N-Ca bond length = {0:0.2f}".format(theTriad.dPR()))  # Nitro_Calcium = theTriad.dPR()
    # print the corresponding bond angle for carbon, nitrogen and calcium; Carbon_Nitro_Calcium = (theTriad.angleP())*(180/math.pi)
    Carbon_Nitro_Calcium_Bond_Angle = print(
        "C-N-Ca bond angle = {0:0.1f}".format((theTriad.angleP()) * (180 / numpy.pi)))  # (180/math.pi)))
    pass


main()
