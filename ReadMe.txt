1. Source
The source came from Scientific American article
"Ramanujan and Pi" by Jonathan M. Borwein and Peter B. Borwein
[https://en.wikipedia.org/wiki/Jonathan_Borwein
https://en.wikipedia.org/wiki/Peter_Borwein

see also
https://en.wikipedia.org/wiki/Bailey%E2%80%93Borwein%E2%80%93Plouffe_formula]

pg. 112-118
where they present an iteravite methond based on fourth roots that converges 
very quickly to Pi. They claim that 15 times through the loop will yeild 2 billion digits.
You may see the mathematical presentation of the calculation in the two jpgs: Alpha_Calc and Y_Calc.

2. Python Code
The python code relies on the mpmath module to take care of the large number of digits. Note that I set the precision to 1,000,100 instead of just 1M. This was necessary to take care of compounding rounding errors in the last digits.

3. Checking
Having generated 1,000,000 digits it was necessary to check the calculation. I retreived 1 million digits from the website https://www.piday.org/million/. I saved the html file and then used notepad to strip out the html and save the actual digits as a txt file.

4. Why
Just for fun. There is no use for all these digits. NASA estimates that with 40 digits you can calculate the circumference of the visible universe(r= 46 Billion light years) and your answer would be off by no more than than diameter of a hydrogen atom.
https://www.jpl.nasa.gov/edu/news/2016/3/16/how-many-decimals-of-pi-do-we-really-need/
