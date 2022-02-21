# Contributors 


## 1) How would you get contributor elements from the database? How many contributor elements are there?

We can access the `contributor` elements by using: 

```
//contributor
```

We can count them with:


```
count(//contributor)
```

The answer are `900`. Notice that this is the same as the number of pages. 


## 2) Sometimes, one contributor edits multiple pages. How many unique or distinct contributors are there?

We can use the `distinct-values()` function to find unique entries in the `contributor` elements. 

```
count(distinct-values(//contributor))
```

This will give us `241` unique contributors.


## 3) How many contributors have usernames that start with "W"? Are there any that start with "w"?

We can use the `starts-with()` function to check what letter an element starts with. Don't forget to look for **distinct** values. 
```
count(distinct-values(//contributor[starts-with(username, "W")]))
```

This gives us `7`

The `starts-with()` function is case-sensitive which means that it sees "W" and "w" as different letters. If we do 
```
count(distinct-values(//contributor[starts-with(username, "w")]))
``` 

We get `0` contributors whose usernames start "w"


## 4) What is the shortest/smallest username?
This question similar to question 3 in activity 1

To find the lengths of all of the title elements, we can us the `string-length()` function. Try running the following:

```
//username/string-length()
```
You get the length of each username element like:
```
8
17
10
7
8
10
9
10
7
16
8
16
...
```

To find the smallest, we use the `min()` (minimum) function. 

```
min(//username/string-length())
```

This gives us `3`. 

Finally, we can find the title that is this length with:
```
//username[string-length() = min(//username/string-length())]
```

The result of this XPath is: 
```
<username xmlns="http://www.mediawiki.org/xml/export-0.10/">Rua</username>
<username xmlns="http://www.mediawiki.org/xml/export-0.10/">沈澄心</username>
<username xmlns="http://www.mediawiki.org/xml/export-0.10/">沈澄心</username>
```

There are actually 3 usernames which are `3` characters long. You may not be able to see some of the characters depending on the fonts you have installed on you computer.

