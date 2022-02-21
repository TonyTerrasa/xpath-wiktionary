# Order Up

Once we have a query, we can find the elements at an order in the document with the following syntax:

```
(//query)[n]
```
OR
```
(//query)[position() = n]
```

 This will give us the $n^{th}$ occurance of the query in the document. 
 
 Therefore:
 * `(/query)[1]` gives the first
 * `(/query)[8]` gives the 8th
 * `(/query)[last()]` gives the last

**The parentheses are important**


You can see this [Stack Overflow discussion](https://stackoverflow.com/questions/3674569/how-to-select-specified-node-within-xpath-node-sets-by-index-with-selenium) for more details. 

# Questions


1) What are the first and last titles in our sample file?
2) What are the title of the 746th page? 
3) What (distinct) users edited the pages in the range 130-328 inclusive? 
