#Simple Options Calculator One

import time
import numpy as np
from scipy.stats import norm

# Need to define Black-Scholes formula for calculating the price of an Option Security.
# Will need variables for Current Stock Price, Years to Maturity, Risk Free Interest Rate, Volitality of underlying Security, Strike Price, and a string Variable for Option Type.

def black_scholes(S, K, T, r, sigma, option_type):
	Parameters:
	S (float): Current Stock Price
	K (float): Option Strike Price
	T (float): Time to Maturity (in Yrs)
	r (float): Rist-Free Interst Rate
	sigma (float): Volatility of the underlying security (annual)
	option_type (str): 'call', or 'put'

	Returns:
	tuple: Option Price and Computation Time in Seconds
	
# must start timer to obtain computaional time.
	start_time = time.time()

# Before calculation the Complete Formula where price C = S*N(d1)-K*e^(-rT) * N(d2), d1 and d2 are defined
# d1 represents the normalized distance between the current stock price and the strike price, adjusted for the time value of money and the volatility of the security
# Growth rate is incoporated through rate r, and volatility incorporated through sigma.
# This is the probability the Option will be in the money at the expiration, adjusted for time value of money. 
# d1 = [ ln(S/K) + (r+(sigma^2)/2) * T ] / [ sigma * T^(1/2) ]

	d1 = (np.log(S/K) + (r + .5*sigma**2) * T ) / (sigma * np.sqrt(T))

# d2 is derived by subtracting the product sigmaand the square root of T, from d1. 
# d2 = d1 - sigma * T^(1/2)
# This is used to calculate the probability that the option will be excercised, considering the discounting effect of the risk-free rate.

	d2 = d1 - sigma * np.sqrt(T)

