import numpy as np
import random
from matplotlib import pyplot as plt
import time


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
    domain = [0., 1.9]
    dx = (domain[1] - domain[0]) / nSamples
    offset = 0.0
    method_choice = 0
    which_rectangle = "z"
    sample_points = []
    calculated_points = []
    error = 1
    solution = 0
    n = []
    er = []

    def __init__(self):
        return

    def Equation(self, x):
        """If you change this function, you must define your own analytic answer
            in Integration.ConvergencePlot(), otherwise you'll end up with an infinite
            loop, and it will suck."""
        return np.exp(np.cos(np.pi * 2 * x))

    def ChooseIntegration(self):
        """
        This method prompts the user to give their choice for a method of
            integration.
            method_choice (int) - variable returned at end of method. Valid
            returned values are 2-trapezoid,
            3-simpson, a-left rectangle, b-right rectangle, c-midpoint,
            d - arbitrary
        """
        self.method_choice = int(
            input(
                "Which method?   (choose a number): \n1. Rectangle, \n2. Trapezoid, \n3. Simpson\n"
            ))
        if self.method_choice == 1:
            self.which_rectangle = input(
                "Which rectangle method? \na - Left Endpoint, \nb - Right Endpoint, \nc - Midpoint, \nd - Arbitrary\n"
            )
            if self.which_rectangle == "a":
                return
            elif self.which_rectangle == "b":
                return
            elif self.which_rectangle == "c":
                return
            else:
                self.which_rectangle = "d"
        #print(self.method_choice, " test 1")
        #return self.method_choice

    def DefineOffset(self):
        """This function defines the offset of the sample point used by the rectangle
        method.
            which_rectangle(str) - taken from Integration.ChooseIntegration()

        """
        if self.method_choice == 1:
            if self.which_rectangle == "a":  #left endpoint
                self.offset = 0
            elif self.which_rectangle == "b":  #right endpoint
                self.offset = self.dx
            elif self.which_rectangle == "c":  #midpoint
                self.offset = .5 * self.dx
            elif self.which_rectangle == "d":
                self.offset = random.random() * self.dx

        else:
            self.offset = 0

    #    print("Offset", self.offset)

    def SamplePointGeneration(self):
        """This method will generate the x coordinates for each sampling point to be used
        in the integration.

            sample_points (list) - used to store each x to be mapped in Integration.IntegrationMethod()
        """
        if self.method_choice == 1 or self.method_choice == "a" or self.method_choice == "b" or self.method_choice == "c":
            self.sample_points = [
                self.domain[0] + self.offset + self.dx * i
                for i in range(self.nSamples)
            ]
        elif self.method_choice == 2:
            self.sample_points = [
                self.domain[0] + self.offset + self.dx * i
                for i in range(self.nSamples + 1)
            ]
        #    print("---------SAMPLES--------\n", self.sample_points)

    def IntegrationMethod(self):

        if self.method_choice == 1:  #rectangle
            y = map(self.Equation, self.sample_points)
            self.solution = self.dx * sum(y)

        elif self.method_choice == 2:  #Trapezoid

            y = list(map(self.Equation, self.sample_points))
            self.solution = self.dx * (sum(y) - (y[0] + y[-1]) / 2)

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
            #    print("midpoint", M, " Trapezoid", T)
            self.solution = (2 * M + T) / 3
            self.method_choice = 3
        return self.solution

    def ConvergencePlot(self):

        self.nSamples = 2
        """This is the error function. To test for convergence, choose an epsilon for converge_to, and add the analytic answer
        to 16 digits or so.

        """
        converge_to = 1e-9

        #for i in range(0, 10):
        #    if self.error < converge_to:
        #        break
        #    else:
        while self.error > converge_to:
            t1 = time.time()
            self.n.append(self.nSamples)
            self.dx = (self.domain[1] - self.domain[0]) / self.nSamples
            self.SamplePointGeneration()
            A = self.IntegrationMethod()
            self.nSamples = self.nSamples * 2
            #    print(A)
            """ Here you must give the analytic answer to the function you are integrating if you want to have a
            """
            self.error = abs(A - 2.27687334373138)
            self.er.append(self.error)
            print("Error: ", self.error, "... N = ", self.nSamples)
            t2 = time.time()
            print("\t", t2 - t1, " seconds")

    def Error_Plots(self):

        print(len(self.n), len(self.er))
        plt.plot(self.n, self.er)
        plt.scatter(self.n, self.er, label="Your function")
        plt.legend()
        plt.xscale('log')
        plt.xlabel("Number of Sampling points")
        plt.yscale('log')
        plt.ylabel('Error')

        plt.show()


"""Main Program:
define X as instance of class integration. Take console input, calculate with
given points."""
t0 = time.time()
X = Integration()
X.ChooseIntegration()
X.DefineOffset()
X.SamplePointGeneration()
S = X.IntegrationMethod()
#clear('clear')
print("The solution is", S, '\n\n\n')
X.ConvergencePlot()

tf = time.time()
tt = tf - t0
print(tt, "seconds")

X.Error_Plots()
