<h1>Determining Whether a Year is a Leap Year</h1>
<p>In this tutorial, we will learn how to write a simple Python program to determine whether a given year is a leap year or not.</p>
<h2>What is a Leap Year?</h2>
<p>A leap year is a year that is divisible by 4 with no remainder and either:</p>
<ul>
    <li>Not divisible by 100, or</li>
    <li>Divisible by 400 with no remainder</li>
</ul>
<p>Leap years occur every 4 years, with the exception of years that are divisible by 100 but not by 400. This means that 1900 was not a leap year, but 2000 was.</p>
<h2>Setting Up the Code</h2>
<p>First, we will start by setting up the basic structure of our code. We will begin by importing the <code>int</code> function, which we will use to convert the user's input to an integer. Then, we will define a variable called <code>year</code> and assign it the value of the user's input, converted to an integer using the <code>int</code> function.</p>
<pre><code># Receives user input
year = int(input('which year do you want to check?'))
</code></pre>
<h2>Checking for Leap Years</h2>
<p>Next, we will add an <code>if</code> statement to check whether the year is a leap year or not. We will use the modulo operator (<code>%</code>) to check for a remainder after dividing the year by 4, 100, and 400.</p>
<pre><code># A leap year is said to be divisible by 4 with no remainder 
# and divisible by 100 with remainder 
# or divisible by 400 with no remainder 
# and divisible by 100 with remainder
if year % 4 == 0 and year % 100 != 0:
    print('this is a leap year')
elif year % 100 !=0 and year % 400 == 0:
    print('this is a leap year')
else:
    print('this is not a leap year')
</code></pre>
<p>In the first <code>if</code> statement, we are checking whether the year is divisible by 4 with no remainder and not divisible by 100. If both of these conditions are true, then the year is a leap year, and we print "this is a leap year".</p>
<p>In the <code>elif</code> statement, we are checking whether the year is not divisible by 100 with a remainder and divisible by 400 with no remainder. If both of these conditions are true, then the year is a leap year, and we print "this is a leap year".</p>
<p>Finally, if neither of the above conditions are true, we print "this is not a leap year".</p>
<h2>Testing the Code</h2>

<p>Now that we have written our code, we can test it by running it in a Python interpreter. Simply run the code and follow the prompts to input a year. If the year is a leap year, the code will print "this is a leap year". If it is not a leap year, the code will print "this is not a leap year".</p>
<p>For example:</p>
<pre><code>which year do you want to check? 2020
this is a leap year
</code></pre>
<h2>Conclusion</h2>
<p>In this tutorial, we learned how to write a simple Python program to determine whether a given year is a leap year or not. We used the modulo operator to check for remainders after dividing the year by 4, 100, and 400, and used <code>if</code> and <code>elif</code> statements to determine whether the year met the conditions for being a leap year. Finally, we tested the code by running it in a Python interpreter and inputting a year.</p>
