#Simple Options Calculator One

import numpy as np
from scipy.stats import norm

# Need to define Black-Scholes formula for calculating the price of an Option Security.
# Will need variables for Current Stock Price, Years to Maturity, Risk Free Interest Rate, Volitality of underlying Security, Strike Price, and a string Variable for Option Type.

def black_scholes(S, K, T, r, sigma, option_type):
