# Learn Python

<!-- Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.
 -->

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

* Both contain a series of values that can be of any type.
* Their main difference is that lists are mutable, whereas tuples are not.
* Consequently, tuples will work as keys in dictionaries(and lists not), because dictionary keys need to be immutable(which also means hashable)

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

* Set: **unordered** collection of **unique** elements  
  * can't contain duplicates
  * hashable  
    * conseuqently, uses hash lookup(which is why sets are unordered, like dictionaries)
      * **Performance**: this makes __contain__(in) a lot more efficient with sets than lists
        * O(1)constant
      * doesn't allow for indexes
  * can only contain mutable/hashable items
    * although sets are mutable themselves
  * Example: >>> x = set([1,2,3,22,2,2,2]) => {1, 2, 3, 22}

* List: **ordered** collection of elements  
  * ok with duplicates
  * mutable and consequently not hashable
  * can contain any type of object
  * **Performance**: O(n)linear
  * Example >>> x = [1,2,3,22,2,2,2] => [1,2,3,22,2,2,2]
---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

* **`lambda`** is a way to create small, anonymous functions, i.e., functions without a name
  * almost always used only once
  * used often in combination with filter(), reduce(), and map()
  * format: lambda <arguments> : <expression>
* **Example**: sorting strings in list by length of string
  * >>> myList = ['first','second','third']
  * >>> sorted(myList,key=lambda string : len(string)) => ['first', 'third', 'second']


---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

* List comprehensions: elegant and compact way to define and create a list, often with properties of sets
  * Essentially, instead of creating block of code with for loop and append, etc., you can define new list of values in 1 line!
* **ExampleListComprehensionMap** convert Celsius to Fahrenheit
  * >>> Celsius = [39.2, 36.5, 37.3, 37.8]
  * >>> Fahrenheit = [ x(float(9)/5) + 32 for x in Celsius ]
  * >>> print Fahrenheit => [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
* **ExampleMapFunction**
  * >>> Celsius = [39.2, 36.5, 37.3, 37.8]
  * >>> Fahrenheit = map(lambda x: (float(9)/5)x + 32, Celsius)
  * >>> print Fahrenheit => [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
  * **ExampleListComprehensionFilter** filter out numbers divisible by 7 between 1 and 100
    * >>> result = [ x for x in range(1,100) if x % 7 == 0 )
    * >>> result => [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]  
* **ExampleFilterFunction** filter out numbers divisible by 7 between 1 and 100
  * >>> myList = range(1,100)
  * >>> result = filter(lambda x: x % 7 == 0, myList)
  * >>> result => [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98]
* **ExampleSetComprenhenion** calculate primes up 100 and incorporating set comprehensions to remove duplicates
  * >>> from math import sqrt
  * >>> n = 100
  * >>> sqrt_n = int(sqrt(n))
  * >>> no_p = { i for i in range(2,sqrt_n) for j in range(2*i,n,i) }
  * >>> no_p => {4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30, 32, 33, 34, 35, 36, 38, 39, 40, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 60, 62, 63, 64, 65, 66, 68, 69, 70, 72, 74, 75, 76, 77, 78, 80, 81, 82, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 98, 99}
  * >>> p = { x for x in range(2,n) if x not in no_p }
  * >>> p => {0, 1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
* **ExampleDictComprehension** mapping of integers between 1 and 5 and their squares
  * nums = {n: n**2 for n in range(1,5)}
  * nums => {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```
* 937 days

b.  
```
date_start = '12-31-2013'  
date_stop = '05-28-2015'  
```

* 513 days

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

* 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

* Done

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

* Done

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

* Done

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)

* Done
