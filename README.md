# Numerical-methods-showcase
Pieces of sample code and outputs for numerical methods

Hello, this is a readme to explain the numerical methods employed in the Conical_Pendulum function.
This includes
  1) small explaination and example of what an algorithm is
  2) a list of all the methods I tried out and how I tested them
  3) how to use and tweek this showcase code yourself
  4) reason for why I choose the improved Euler method on the x1[i+1] step
 
Section 1: 
First is a small explaination on algorithms:
simply put, it's a set of rules I make my computer follow in order to do some calculation
for example if I want to solve the differential equation   dy/dx = -5*y   using numerical methods.
I might use this set of instructions:

  start with y[x=0] = y_0
  y[x+h] = y[x] + (dy/dx)[x]*h = y[x] + (-5*y[x])*h
  repeat until x = 10
  
  where h is a small step but finite step in an array of x values
  here I run this from x = 0   to    x = 10   with h = 0.01 for example
  and I would use some for loop and make use of the indices in the x array in order to calculate the next successive value in y

this is an example of an algorithm (this one's called the Euler method), it's just a set of instructions I tell my computer via code (Python, Matlab, etc...)


Section 2:
I tested different algorithms by using them to solve the pendulum equation d^2x/dt^2 = -G*sin(x)  where x is the angle from vertical of a pendulum (no small angle approximation)
all with the same time step and same time domain (I did t=0 to t=50 with step size ts = 0.01), since I know that the actualsolution should be something akin to a sine wave,
any output that was not a sine wave tells me that the method (algorithm) is faulty.

Tried 6 different algorithms in total
  1) Euler method
  2) Improved Euler on v[i+1] (v is x2 in some cell blocks)
  3) Improved Euler on x[i+1] (x is x1 in some cell blocks)
  4) Runge-Kutta on v[i+1]
  5) Runge-Kutta on x[i+1]
  6) Collatz Runge-Kutta
  
Explaining all these methods here would be too long, methods one through five is found here 
cite: elementary differential equations and boundary value problems (Boyce 2001)
and the sixth method is found in this paper
https://watermark.silverchair.com/6-4-368.pdf?token=AQECAHi208BE49Ooan9kkhW_Ercy7Dm3ZL_9Cf3qfKAc485ysgAAAqIwggKeBgkqhkiG9w0BBwagggKPMIICiwIBADCCAoQGCSqGSIb3DQEHATAeBglghkgBZQMEAS4wEQQM5MhOa-eJz9geVJQbAgEQgIICVfXrDKKS1yZCTNmbBMaXugstqvbKu3Wfyp2AMi0GA9aduXHGSeMENeNrXwDYL-FzhkqWKsDztETEnb19khQXxlEE9bW2_dXz6_WpHk5ud1MlkuHyRpFgnoPiyOI3yK4KBWOsK2-hbEYyfShQaqMT1_dS5YHb-DVL7HVw2ClLEmm9KcnwQLUjDvSfJ3unXT3yNJQF8xjgUZ6mev_Ec898iPaiew8updQjv0pXRLrXE1VHdb2yb11RD06nvqKFiApWvpsgEGVS_5OS96_a5Rpr7bhfNtfddiNUK_IosYNSWdju-IvN6k2uGN_D__dCdkKRBlDoABxdwyUFe3tpMa7fRM8TCZaHmLMcqB4_Pj_rBVpFSI2lZLmBOcXia8tLqClY6FEtaYGNDLShCQ2UTiPbzpFSLF6_iAbU7zPb6SdMWcrD40awT5wMU15SxyFO2Ihnfx3jmFFryVubQBsb-Xzja7T7bEsRcv0p77GjeE4myufe6bXQCEcKJIUXYRSdWdpE2rgfXvO08fLBnAjNWfFtfgwKpmzdSSDVaiTiU_7Cro6JQeFJFekX0hGgtnB7dmugznQorL6TuX_89aCOXjteliHZc2FVLvZ7NxmioJcPdjPTL7JYVqVawGefmzs64Vq_vgFBPXB4xOXSici0jH4_8Npt8a6UdqXD5Ei0LLbMJiB_0CvFL_lFa20lYmCHO2xR3aH7tmLrF0ywLXFs8mfjJGCvckuwGTF8UrOK770FnvjGhlIrioU56WijhferrUhv-D3JILZc3EJfMygX2osWDwvPAl_5Ag
by R.E Scraton

Note that the 1st source only provides examples of the methods on 1st order differential equations so I took some liberties in how I applied these methods to the 2nd order
differential equation  d^2x/dt^2 = -G*sin(x)  where x is the angle from vertical of a pendulum

method 6 is from a paper that specified a way to apply the Runge-Kutta method to 2nd order differential equations


Section 3:
Download the Numerical_showcase.py file and load it up in your favorite Python IDE (I use Spyder)
In the file there are 6 cell blocks each using a different a different algorithm to solve the pendulum equation
In Spyder hitting ctrl+enter will run the cell block that your text cursor is currently in
and the plots of the outputs will appear in the plots tab of the top right panel of Spyder
by default all the cell blocks have the same time domain t = 0 to t = 50 with ts = 0.1
this is to ensure a fair comparision between the methods

run some of the cell blocks and check the outputs, you should see a sine wave if the algorithm is good
when you run with the default time array you should notice that only the improved Euler on x1[i+1] and the Collatz Runge-Kutta are good
you will also notice that the regular Euler method is the worst one with an output that is not even close to a sine wave

An exercise you can do is to decrease the time step (makes it more precise) for the regular Euler method before it can match the results of the good methods
(improved Euler on x1[i+1] and Collatz)
You can can up the time step up upping the amount of steps in the t = numpy.linspace(0,50,501) command, the last number (501 in this case) is the number of steps between
t = 0  and   t = 50,   change the time array to t = numpy.linspace(0,50,50001), with 50001 steps you should see the regular Euler method outputting a sine wave with a
slight amplitude change.
This is compared to the methods improved Euler on x1[i+1] and Collatz Runge-Kutta that can produce near perfect sine waves with just 501 steps


Section 4:
If the improved Euler on x1[i+1] and Collatz Runge-Kutta are similar, why did I choose the former?
Because the improved Euler on x1[i+1] is easier to implement and the Collatz Runge-Kutta is deceiving in its operations per for loop
the improved Euler on x1[i+1] only calculates 3 values per loop
while the Collatz Runge-Kutta calculates 5 values per loop
This makes the improved Euler method on x1[i+1] faster in runtime even though they both run through the same amount of loops

