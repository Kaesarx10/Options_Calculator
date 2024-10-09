#Simple Options Calculator One

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
