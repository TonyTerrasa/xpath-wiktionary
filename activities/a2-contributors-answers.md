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

We can use the `distinct-values` function to find unique entries in the `contributor` elements. 

```
count(distinct-values(//contributor))
```

This will give us `241` unique contributors.


## 3) How many contributors have usernames that start with "W"? Are there any that start with "w"?

We can use the `starts-with` function to check what letter an element starts with. Don't forget to look for **distinct** values. 
```
count(distinct-values(//contributor[starts-with(username, "W")]))
```

This gives us `7`

The `starts-with` function is case-sensitive which means that it sees "W" and "w" as different letters. If we do 
```
count(distinct-values(//contributor[starts-with(username, "w")]))
``` "w"

We get `0` contributors whose usernames start "w"



