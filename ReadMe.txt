1. General Notes
The python code relies on the mpmath module to take care of the large number of digits. Note that I set the precision to 1,000,100 instead of just 1M. This was necessary to take care of compounding rounding errors in the last digits.


https://en.wikipedia.org/wiki/Jonathan_Borwein
https://en.wikipedia.org/wiki/Peter_Borwein

see also
https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula]\

2. Python Code
A. The source came from Scientific American article
"Ramanujan and Pi" by Jonathan M. Borwein and Peter B. Borwein
pg. 112-118, February 1988, where they present an iterative method based on fourth roots that converges 
very quickly to Pi. They claim that 15 times through the loop will yield 2 billion digits.
You may see the mathematical presentation of the calculation in the two jpgs: Alpha_Calc and Y_Calc.

The program takes 2 minutes and 11 seconds to calculate 1M digits on an Intel i5 at 2.9GHz.
The python code is 1MillionDigitsofPi.py

B. A second, faster, method based on Borwein Nonic (ninth order) algorithm is presented in 1MillionDigitsofPi_Borwein.py 
This code produces 1M digits in 12 seconds. The formula may be found here
http://www.hvks.com/Numerical/Downloads/HVE%20Practical%20implementation%20of%20PI%20Algorithms.pdf

3. Checking
Having generated 1,000,000 digits, it was necessary to check the calculation. I retrieved 1 million digits from the website https://www.piday.org/million/. I saved the html file and then used notepad to strip out the html and save the actual digits as a txt file. I created an Access database and imported the text file created by my python code and the text file taken from piday. The comparison agrees to the last decimal place.

4. Why
Just for fun. There is no use for all these digits. NASA estimates that with 40 digits you can calculate the circumference of the visible universe (r= 46 billion light years) and your answer would be off by no more than diameter of a hydrogen atom.
https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/
