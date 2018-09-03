-- Find the sum of all the multiples of 3 or 5 below 1000.

ns = [x | x <- [1..999], (rem x 5 == 0 || rem x 3 == 0)]
ans = sum ns -- 234168
