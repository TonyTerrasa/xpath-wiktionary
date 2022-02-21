# How Many?: Answers 

Below are the answers for activity 1

## 1) How many pages are there in this file?

You can find the answer with:
```
count(//page)
```

You get `900`

## 2) How would you find the number of words in this file? How many are there?


Notice that not ever page is a word defintion. For example the first page is titled "Wiktionary:GNU Free Documentation License."

Notice that pages that define words have no spaces or colons (":") in the title. We can use the `not()` and `contains()` function to filter for only words. 

You can filter our spaces with:
```
count(//page[not(contains(title, " "))])
```

You can also filter out colons with:

```
count(//page[not(contains(title, " ")) and not(contains(title, ":"))])
```



The number of pages with no spaces or colons in the title is `821`
