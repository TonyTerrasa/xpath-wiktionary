# Order Up

## 1) What are the first and last titles in our sample file?
Just as in the example, we can use: 
```
(//title)[position() = 1]
(//title)[position() = last()]
```
OR
```
(//title)[1]
(//title)[last()]
```

The first is: "Wiktionary:Welcome, newcomers"

The last is: "defining vocabulary"

## 2) What are the title of the 746th page? 
Use
```
(//title)[746]
```
OR
```
(//title)[position() = 746]
```
This gives us: "outer space"

## 3) What (distinct) users edited the pages in the range 130-328 inclusive? 

First, we can get the range of usernames using: 
```
(//username)[position() >= 130 and position() <= 328]
```
Notice that we use the `=` because we want to include the 130th and the 328th element. 

Finally, we use the `distinct-values()` function:
```
distinct-values((//username)[position() >= 130 and position() <= 328])
```
This gives:

```
LatinGuy87
DerbethBot
Equinox
SurjectionBot
WingerBot
Vininn126
Ultimateria
Inner Focus
Rudi Laschenkohl
Sarilho1
Fytcha
Oxlade2000
Vox Sciurorum
Allahverdi Verdizade
Monsegu 2
Rukhabot
NadandoBot
ExcarnateSojourner
Jberkel
Surjection
Mahagaja
La más guay
Zff19930930
Supevan
350bot
Embryomystic
Hans-Friedrich Tamke
StuckInLagToad
Sgconlaw
AutoDooz
Urszag
İtidal
User1267183728390127891247
BandiniRaffaele2
Эарендил
AmazingJus
Gabbe
Minorax
Chuck Entz
-sche
Kristian-Clausal
Whitekiko
DanielWhernchend
Lambiam
Killarnee
Astova
AdamBMorgan
Erutuon
Numberguy6
Inqilābī
Linguoboy
Svlioras
Indian subcontinent
Yellow is the colour
SodhakSH
DCDuring
Veikk0.ma
Returning2stadia
J3133
Ajmint
Roger the Rodger
Gidriano
Biolongvistul
沈澄心
1234qwer1234qwer4
```

