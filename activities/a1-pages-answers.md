# Pages and Basics: Answers 

Below are the answers for activity 1

## 1) How many pages are there in this file?

You can find the answer with:
```
count(//page)
```

You get `900`

## 2) How would you find the number of words in this file? How many are there?


Notice that not ever page is a word defintion. For example the first page is titled "Wiktionary:GNU Free Documentation License."

Notice that pages that define words have no spaces or colons (":") in the title. We can use the `not()` and `contains()` functions to filter for only words. 

You can filter out spaces with:
```
count(//page[not(contains(title, " "))])
```

You can also filter out colons with:

```
count(//page[not(contains(title, " ")) and not(contains(title, ":"))])
```

The number of pages with no spaces or colons in the title is `821`


## 3) What is the length of the longest entry title? What is that entry?

To find the lengths of all of the title elements, we can us the `string-length()` function. Try running the following:

```
//title/string-length()
```
You get the length of each title element like:
```
29
41
53
33
10
4
9
34
...
```

To find the maximum, we use the `max` function. 

```
max(//title/string-length())
```

This gives us `53`. 

Finally, we can find the title that is this length with:
```
//title[string-length() = max(//title/string-length())]
```

The result of this XPath is: 
```
<title xmlns="http://www.mediawiki.org/xml/export-0.10/">Wiktionary:Text of the GNU Free Documentation License</title>
<title xmlns="http://www.mediawiki.org/xml/export-0.10/">Wiktionary:Wiktionary idiom dictionary considerations</title>
```

There are actually 2 titles which are `53` characters long. 

## 4) When was of the page with the highest id number last edited?


The highest page id can be found: 
```
max(//page/id)
```

**It is important that you include both `page`and `id`.** If you search for `//id` you will be including the `id`s of the revisions as well. 



The page with the highest id can be found: 
```
//page[id = max(//page/id)]
```

Then, we look for the path 
```
//page[id = max(//page/id)]/revision/timestamp
```

This will give us: 
```
<timestamp xmlns="http://www.mediawiki.org/xml/export-0.10/">2020-12-06T16:50:49Z</timestamp>
```

This means, it was last edited on December 6, 2020 at 16:50


