#test 1
import numpy as np
import random
from os import system as clear


class Integration:
    """
        This class sets up a numerical integration method for a user-given equation.
         User will choose The integration method,
        rectangle, trapezoidal, or simpsons, give the desired number of sampling
        points, and the offset for the samplings points.

        nSamples (int) - number of samples used for the integration
        domain (list) - gives the domain to be integrated
        dx (float) - the width of the samples, or change in x (delta-x)
        offset(float) - offset for each sample from x = 0.0 (default for midpoint
            is .5*dx)
        sample_points (list) - list of all values to be evaluated in the
            integration process

        lines commented out with a # symbol are for unit testing

    """
    nSamples = 1000
    domain = [0., 1.]
    dx = (domain[1] - domain[0]) / nSamples
    offset = 0.0
    method_choice = 0
    sample_points = []
    calculated_points = []

    def __init__(self):
        return

    def Equation(self, x):
        return np.exp(np.cos(2 * np.pi * x))

    def ChooseIntegration(self):
        """
        This method prompts the user to give their choice for a method of
            integration.
            method_choice (int) - variable returned at end of method. Valid
            returned values are 2-trapezoid,
            3-simpson, 11-left rectangle, 12-right rectangle, 13-midpoint,
            14 - arbitrary
        """
        self.method_choice = int(
            input(
                "Which method?   (choose a number): \n1. Rectangle, \n2. Trapezoid, \n3. Simpson\n"
            ))
        if self.method_choice == 1:
            which_rectangle = int(
                input(
                    "Which rectangle method? \n1. Left Endpoint, \n2. Right Endpoint, \n3. Midpoint, \n4. Arbitrary\n"
                ))
            if which_rectangle == 1:
                self.method_choice = 11
            elif which_rectangle == 2:
                self.method_choice = 12
            elif which_rectangle == 3:
                self.method_choice = 13
            else:
                self.method_choice = 14
        #print(self.method_choice, " test 1")
        return self.method_choice

    def DefineOffset(self, method_choice):
        if self.method_choice > 10:
            if method_choice == 11:  #left endpoint
                self.offset = 0
            elif self.method_choice == 12:  #right endpoint
                self.offset = self.dx
            elif self.method_choice == 13:  #midpoint
                self.offset = .5 * self.dx
            self.method_choice = 1
        else:
            self.offset = 0

    def ConvergenceCriteria():
        return

    def SamplePointGeneration(self):
        if self.method_choice == 1:
            self.sample_points = [
                self.domain[0] + self.offset + self.dx * i
                for i in range(self.nSamples)
            ]
        elif self.method_choice == 2:
            self.sample_points = [
                self.domain[0] + self.offset + self.dx * i
                for i in range(self.nSamples + 1)
            ]

        return self.sample_points

    def ConvergencePlot():
        return

    def IntegrationMethod(self):
        solution = 0

        if self.method_choice == 1:  #rectangle
            y = map(self.Equation, self.sample_points)
            solution = self.dx * sum(y)

        elif self.method_choice == 2:  #Trapezoid

            y = list(map(self.Equation, self.sample_points))
            solution = self.dx * (sum(y) - (y[0] + y[-1]) / 2)
        elif self.method_choice == 3:  #Simpson
            """To calculate Simpson's method, we're going to use the weighted
            averages of the trapezoidal and the midpoint rules S = (2M +T)/3.
            Therefore, this function is recursive, and runs both the trapezoidal
             rule and the midpoint rule"""
            self.method_choice = 1
            self.offset = .5 * self.dx
            M_samples = self.SamplePointGeneration()
            M = self.IntegrationMethod()

            self.method_choice = 2
            self.offset = 0
            T_samples = self.SamplePointGeneration()
            T = self.IntegrationMethod()

            solution = (2 * M + T) / 3

        return solution


"""Main Program:
define X as instance of class integration. Take console input, calculate with
given points."""
X = Integration()
X.ChooseIntegration()
X.DefineOffset(X.method_choice)
X.SamplePointGeneration()
S = X.IntegrationMethod()
#clear('clear')
print("The solution is", S, '\n\n\n')
