# fuzz
Fuzz a data Fuzzer/Obfuscator

I use this what I am trying to break stuff - which currently seems like everyday !!

#test.csv

This is my test file
```text
id,first_name,last_name,email,country,ip_address,City,Country,CCard,Race,Company
2,Janice,Gilbert,jgilbert0@odnoklassniki.ru,Russia,200.90.119.195,Pyt-Yakh,Lebanon,3577598273371963,Melanesian,Yakijo
3,Mary,Adams,madams1@youtube.com,China,35.18.31.5,Lücheng,Portugal,3586021087796977,Black,or,African,American,Jamia
4,Frank,Lopez,flopez2@blog.com,Belarus,179.220.143.145,Dashkawka,United,States,5602233033286350,Pakistani,Vinte
5,Marie,Martin,mmartin3@va.gov,Russia,161.72.215.42,Boguchar,China,5411850139268049,Blackfeet,Twimbo
6,Joyce,Price,jprice4@artisteer.com,Sweden,105.57.32.169,Horred,Mongolia,5100176874230168,Creek,Skippad
7,William,Riley,wriley5@shutterfly.com,Colombia,138.135.110.89,Guapi,Indonesia,374622899402654,Navajo,Yadel
8,Rose,Cunningham,rcunningham6@friendfeed.com,Colombia,54.204.6.137,Buenaventura,Indonesia,3581970954021361,Indonesian,Gigaclub
9,Beverly,Kim,bkim7@twitter.com,China,181.185.247.178,Meilisi,Philippines,5602237467769419,Apache,Jatri
10,Lois,Coleman,lcoleman8@imageshack.us,China,152.211.220.240,Zhihe,Jamaica,5577254622341886,Seminole,Twimm
```



#Useage1 Simple extract

Extract fields 1,5,6 from the file called people.csv. And impose a data loss of 0%, 0%, 0%, please not the default options mean CSV seperated and FULL Loss - but as we having a loss of 0 - no data will be lost.

   cat people.csv | python fuzz.py -d 1,5,6 -l 0,0,0 

And you should see 

```text
id,first_name,last_name
2,Janice,Gilbert
3,Mary,Adams
4,Frank,Lopez
5,Marie,Martin
6,Joyce,Price
7,William,Riley
8,Rose,Cunningham
9,Beverly,Kim
10,Lois,Coleman
```

#Useage2 Full Data loss

We want to loose some fields at random 

   cat people.csv | python fuzz.py -d 1,5,6 -l 0,50,30 

So First_Name will have 50% data loss, and Last_Name will have 30% data loss. There is a Default option of ALL data loss i.e the whole field

This produces

```
id,first_name,last_name
2,,Gilbert
3,Mary,Adams
4,Frank,Lopez
5,Marie,Martin
6,,
7,,Riley
8,,Cunningham
9,,Kim
10,Lois,Coleman
```


#Useage3 Partial Data loss

You need to pass the **Type** of data loss, by passing nothing it is implied that it is **ALL**.

We will keep the loss rates the same - and see what the output looks like


   cat people.csv | python fuzz.py -d 1,5,6 -l 0,50,30  -t partial

**Note** Type is case in sensative it looks for P or p.

```txt
id,first_name,last_name
2,Janice,Gilbert
3,Mary,Adams
4,Frank,Lo
5,  ri ,Martin
6,Joyce,   ce
7,W l  am,Riley
8,Rose,Cunningham
9,Be   ly,Kim
10,Lois,Coleman
```
