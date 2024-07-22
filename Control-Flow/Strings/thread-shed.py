"""
You’ve recently been hired as a cashier at the local sewing hobby shop, Thread Shed. Some of your daily responsibilities
 involve tallying the number of sales during the day, calculating the total amount of money made, and keeping track of
 the names of the customers.

Unfortunately, the Thread Shed has an extremely outdated register system and stores all the transaction information
in one huge unwieldy string called daily_sales.

All day, for each transaction, the name of the customer, amount spent, types of thread purchased, and the date of sale
is all recorded in this same string. Your task is to use your Python skills to iterate through this string and clean up
each transaction and store all the information in easier-to-access lists.

"""

daily_sales = """
Edith Mcbride   ;,;$1.21   ;,;   white ;,; 09/15/17   ,Herbert Tran   ;,;   $7.29;,; white&blue;,
;   09/15/17 ,Paul Clarke ;,;$12.52 ;,;   white&blue ;,; 09/15/17 ,Lucille Caldwell ;,;   $5.13   ;,; white   ;,
; 09/15/17, Eduardo George   ;,;$20.39;,; white&yellow ;,;09/15/17   ,   Danny Mclaughlin;,;$30.82;,; purple ;,
;09/15/17 ,Stacy Vargas;,; $1.85   ;,; purple&yellow ;,;09/15/17,   Shaun Brock;,; $17.98;,;purple&yellow ;,
; 09/15/17 , Erick Harper ;,;$17.41;,; blue ;,; 09/15/17, Michelle Howell ;,;$28.59;,; blue;,;   09/15/17   , 
Carroll Boyd;,; $14.51;,;   purple&blue   ;,; 09/15/17   , Teresa Carter   ;,; $19.64 ;,; white;,;09/15/17   ,   
Jacob Kennedy ;,; $11.40 ;,; white&red   ;,; 09/15/17, Craig Chambers;,; $8.79 ;,; white&blue&red   ;,;09/15/17   , 
Peggy Bell;,; $8.65 ;,;blue   ;,; 09/15/17,   Kenneth Cunningham ;,;   $10.53;,;   green&blue   ;,; 09/15/17   ,   
Marvin Morgan;,;   $16.49;,; green&blue&red   ;,;   09/15/17 ,Marjorie Russell ;,; $6.55 ;,;   green&blue&red;,
;   09/15/17 , Israel Cummings;,;   $11.86   ;,;black;,; 09/15/17,   June Doyle   ;,;   $22.29 ;,; black&yellow ;,
;09/15/17 , Jaime Buchanan   ;,; $8.35;,;   white&black&yellow   ;,;   09/15/17, Rhonda Farmer;,;$2.91 ;,
;   white&black&yellow ;,;09/15/17, Darren Mckenzie ;,;$22.94;,;green ;,;09/15/17,Rufus Malone;,;$4.70   ;,
; green&yellow ;,; 09/15/17   ,Hubert Miles;,;   $3.59 ;,;green&yellow&blue;,;   09/15/17   , Joseph Bridges  ;,
;$5.66   ;,; green&yellow&purple&blue ;,;   09/15/17 , Sergio Murphy   ;,;$17.51   ;,; black   ;,;   09/15/17 , 
Audrey Ferguson ;,; $5.54;,;black&blue   ;,;09/15/17 ,Edna Williams ;,; $17.13;,; black&blue;,;   09/15/17,   
Randy Fleming;,;   $21.13 ;,;black ;,;09/15/17 ,Elisa Hart;,; $0.35   ;,; black&purple;,;   09/15/17   , Ernesto Hunt 
;,; $13.91   ;,;   black&purple ;,; 09/15/17,   Shannon Chavez   ;,;$19.26   ;,; yellow;,; 09/15/17   , Sammy Cain;,
; $5.45;,; yellow&red ;,;09/15/17 ,   Steven Reeves ;,;$5.50 ;,;   yellow;,;   09/15/17, Ruben Jones   ;,; $14.56 ;,
;   yellow&blue;,;09/15/17 , Essie Hansen;,;   $7.33   ;,;   yellow&blue&red ;,; 09/15/17   ,   Rene Hardy   ;,
; $20.22   ;,; black ;,;   09/15/17 ,   Lucy Snyder   ;,; $8.67 ;,;black&red  ;,; 09/15/17 ,Dallas Obrien ;,; $8.31;,
;   black&red ;,;   09/15/17,   Stacey Payne ;,;   $15.70   ;,;   white&black&red ;,;09/15/17 ,   Tanya Cox   ;,
;   $6.74   ;,;yellow   ;,; 09/15/17 , Melody Moran ;,;   $30.84 ;,;yellow&black;,;   09/15/17 , Louise Becker   ;,
; $12.31 ;,; green&yellow&black;,;   09/15/17 , Ryan Webster;,;$2.94 ;,; yellow ;,; 09/15/17 ,Justin Blake ;,
; $22.46   ;,;white&yellow ;,; 09/15/17,   Beverly Baldwin ;,;   $6.60;,; white&yellow&black ;,;09/15/17   ,   
Dale Brady ;,;   $6.27 ;,; yellow   ;,;09/15/17 ,Guadalupe Potter ;,;$21.12   ;,; yellow;,; 09/15/17   , 
Desiree Butler ;,;$2.10   ;,;white;,; 09/15/17 ,Sonja Barnett ;,; $14.22 ;,;white&black;,; 09/15/17, Angelica Garza;,
;$11.60;,;white&black ;,;   09/15/17   ,   Jamie Welch   ;,; $25.27   ;,; white&black&red ;,;09/15/17   ,   
Rex Hudson ;,;$8.26;,;   purple;,; 09/15/17 ,   Nadine Gibbs ;,;   $30.80 ;,;   purple&yellow   ;,; 09/15/17   , 
Hannah Pratt;,;   $22.61   ;,;   purple&yellow ;,;09/15/17,Gayle Richards;,;$22.19 ;,; green&purple&yellow ;,
;09/15/17   ,Stanley Holland ;,; $7.47   ;,; red ;,; 09/15/17 , Anna Dean;,;$5.49 ;,; yellow&red ;,;   09/15/17   , 
Terrance Saunders ;,;   $23.70  ;,;green&yellow&red ;,; 09/15/17 ,   Brandi Zimmerman ;,; $26.66 ;,; red   ;,
;09/15/17 ,Guadalupe Freeman ;,; $25.95;,; green&red ;,;   09/15/17   ,Irving Patterson ;,;$19.55 ;,; green&white&red 
;,;   09/15/17 ,Karl Ross;,;   $15.68;,;   white ;,;   09/15/17 , Brandy Cortez ;,;$23.57;,;   white&red   ;,
;09/15/17, Mamie Riley   ;,;$29.32;,; purple;,;09/15/17 ,Mike Thornton   ;,; $26.44 ;,;   purple   ;,; 09/15/17, 
Jamie Vaughn   ;,; $17.24;,;green ;,; 09/15/17   , Noah Day ;,;   $8.49   ;,;green   ;,;09/15/17 ,Josephine Keller ;,
;$13.10 ;,;green;,;   09/15/17 ,   Tracey Wolfe;,;$20.39 ;,; red   ;,; 09/15/17 , Ignacio Parks;,;$14.70   ;,
; white&red ;,;09/15/17 , Beatrice Newman ;,;$22.45   ;,;white&purple&red ;,;   09/15/17, Andre Norris   ;,
;   $28.46   ;,; red;,;   09/15/17 ,   Albert Lewis ;,; $23.89;,; black&red;,; 09/15/17,   Javier Bailey   ;,
; $24.49   ;,; black&red ;,; 09/15/17   , Everett Lyons ;,;$1.81;,;   black&red ;,; 09/15/17 , Abraham Maxwell;,
; $6.81   ;,;green;,;   09/15/17 ,   Traci Craig ;,;$0.65;,; green&yellow;,; 09/15/17 , Jeffrey Jenkins   ;,;$26.45;,
; green&yellow&blue   ;,;   09/15/17,   Merle Wilson ;,;   $7.69 ;,; purple;,; 09/15/17,Janis Franklin ;,;$8.74   ;,
; purple&black   ;,;09/15/17 , Leonard Guerrero ;,;   $1.86   ;,;yellow ;,;09/15/17,Lana Sanchez;,;$14.75   ;,
; yellow;,; 09/15/17   ,Donna Ball ;,; $28.10  ;,; yellow&blue;,;   09/15/17   , Terrell Barber   ;,; $9.91   ;,
; green ;,;09/15/17   ,Jody Flores;,; $16.34 ;,; green ;,;   09/15/17,   Daryl Herrera ;,;$27.57;,; white;,
;   09/15/17   , Miguel Mcguire;,;$5.25;,; white&blue   ;,;   09/15/17 , Rogelio Gonzalez;,; $9.51;,
;   white&black&blue ;,;   09/15/17   ,   Lora Hammond ;,;$20.56 ;,; green;,;   09/15/17,Owen Ward;,; $21.64   ;,
; green&yellow;,;09/15/17,Malcolm Morales ;,; $24.99   ;,;   green&yellow&black;,; 09/15/17 , Eric Mcdaniel ;,
;$29.70;,; green ;,; 09/15/17 ,Madeline Estrada;,;   $15.52;,;green;,;   09/15/17 , Leticia Manning;,;$15.70 ;,
; green&purple;,; 09/15/17 ,   Mario Wallace ;,; $12.36 ;,;green ;,; 09/15/17,Lewis Glover;,;   $13.66   ;,
; green&white;,;09/15/17,   Gail Phelps   ;,;$30.52 ;,; green&white&blue   ;,; 09/15/17 , Myrtle Morris ;,;   $22.66  
 ;,; green&white&blue;,;09/15/17
 """

"""
It looks like each transaction is separated from the next transaction by a ,, and then each piece of data within a 
transaction is separated by the artifact ;,;.

If we want to split up daily_sales into a list of individual transactions, we are going to want to split by ,, but first,
we need to replace the artifact ;,; to something without a comma, so we don’t split any transactions themselves.

Replace all the instances of ;,; in daily_sales with some other character and save the result to daily_sales_replaced.
"""

daily_sales_replaced = daily_sales.replace(";,;", "|")

"""
Now we can split the string into a list of each individual transaction. Split daily_sales_replaced around commas and 
save it to a new list daily_transactions.
"""

daily_transactions = daily_sales_replaced.split(",")

"""
Output: ['Edith Mcbride   |$1.21   |   white | \n09/15/17   ', 'Herbert Tran   |   $7.29| \nwhite&blue|   09/15/17 
', 'Paul Clarke |$12.52 \n|   white&blue | 09/15/17 ', 'Lucille Caldwell   \n|   $5.13   | white   | 09/15/17', 
'\nEduardo George   |$20.39| white&yellow \n|09/15/17   ', '   Danny Mclaughlin|$30.82|   \npurple |09/15/17 ', 
'Stacy Vargas| $1.85   | \npurple&yellow |09/15/17', '   Shaun Brock| \n$17.98|purple&yellow | 09/15/17 ', 
' \nErick Harper |$17.41| blue | 09/15/17', ' \nMichelle Howell |$28.59| blue|   09/15/17   ', ' \nCarroll Boyd| 
$14.51|   purple&blue   |   \n09/15/17   ', ' Teresa Carter   | $19.64 | \nwhite|09/15/17   ', '   Jacob Kennedy | 
$11.40   \n| white&red   | 09/15/17', ' Craig Chambers| \n$8.79 | white&blue&red   |09/15/17   ', ' Peggy Bell| $8.65 
|blue   | 09/15/17', '   Kenneth Cunningham |   $10.53|   green&blue   | \n09/15/17   ', '   Marvin Morgan|   $16.49| 
\ngreen&blue&red   |   09/15/17 ', 'Marjorie Russell \n| $6.55 |   green&blue&red|   09/15/17 ', '\nIsrael Cummings|  
 $11.86   |black|  \n09/15/17', '   June Doyle   |   $22.29 |  \nblack&yellow |09/15/17 ', ' Jaime Buchanan   |   
 \n$8.35|   white&black&yellow   |   09/15/17', '   \nRhonda Farmer|$2.91 |   white&black&yellow   \n|09/15/17', 
 ' Darren Mckenzie |$22.94|green \n|09/15/17', 'Rufus Malone|$4.70   | green&yellow \n| 09/15/17   ', 'Hubert Miles|  
  $3.59   \n|green&yellow&blue|   09/15/17   ', ' Joseph Bridges  |$5.66   | green&yellow&purple&blue \n|   09/15/17 
  ', ' Sergio Murphy   |$17.51   |   \nblack   |   09/15/17 ', ' Audrey Ferguson | \n$5.54|black&blue   |09/15/17 ', 
  'Edna Williams | \n$17.13| black&blue|   09/15/17', '   Randy Fleming|   $21.13 |black |09/15/17 ', 'Elisa Hart| 
  $0.35   | black&purple|   09/15/17   ', '\nErnesto Hunt | $13.91   |   black&purple |   \n09/15/17', '   Shannon 
  Chavez   |$19.26   | \nyellow| 09/15/17   ', ' Sammy Cain| $5.45|   \nyellow&red |09/15/17 ', '   Steven Reeves 
  |$5.50   \n|   yellow|   09/15/17', ' Ruben Jones   | \n$14.56 |   yellow&blue|09/15/17 ', ' Essie Hansen|   $7.33  
   |   yellow&blue&red\n| 09/15/17   ', '   Rene Hardy   | $20.22   | \nblack |   09/15/17 ', '   Lucy Snyder   | 
   $8.67   \n|black&red  | 09/15/17 ', 'Dallas Obrien |   \n$8.31|   black&red |   09/15/17', '   Stacey Payne \n|   
   $15.70   |   white&black&red |09/15/17   \n', '   Tanya Cox   |   $6.74   |yellow   | \n09/15/17 ', ' Melody Moran 
   |   $30.84   \n|yellow&black|   09/15/17 ', ' Louise Becker   | \n$12.31 | green&yellow&black|   09/15/17 ', 
   '\nRyan Webster|$2.94 | yellow | 09/15/17 \n', 'Justin Blake | $22.46   |white&yellow |   \n09/15/17', '   Beverly 
   Baldwin |   $6.60|   \nwhite&yellow&black |09/15/17   ', '   Dale Brady   \n|   $6.27 | yellow   |09/15/17 ', 
   'Guadalupe Potter |$21.12   | yellow| 09/15/17   ', ' \nDesiree Butler |$2.10   |white| 09/15/17  \n', 
   'Sonja Barnett | $14.22 |white&black|   \n09/15/17', ' Angelica Garza|$11.60|white&black   \n|   09/15/17   ', 
   '   Jamie Welch   | $25.27   | \nwhite&black&red |09/15/17   ', '   Rex Hudson   \n|$8.26|   purple| 09/15/17 ', 
   '   Nadine Gibbs \n|   $30.80 |   purple&yellow   | 09/15/17   ', ' \nHannah Pratt|   $22.61   |   purple&yellow   
   \n|09/15/17', 'Gayle Richards|$22.19 | \ngreen&purple&yellow |09/15/17   ', 'Stanley Holland \n| $7.47   | red | 
   09/15/17 ', ' Anna Dean|$5.49 | yellow&red |   09/15/17   ', '\nTerrance Saunders |   $23.70  |green&yellow&red 
   \n| 09/15/17 ', '   Brandi Zimmerman | $26.66 | \nred   |09/15/17 ', 'Guadalupe Freeman | $25.95| \ngreen&red |   
   09/15/17   ', 'Irving Patterson \n|$19.55 | green&white&red |   09/15/17 ', 'Karl Ross|   $15.68|   white |   
   09/15/17 ', ' Brandy Cortez |$23.57|   white&red   |09/15/17', ' \nMamie Riley   |$29.32| purple|09/15/17 ', 
   'Mike Thornton   | $26.44 |   purple   | 09/15/17', ' \nJamie Vaughn   | $17.24|green | 09/15/17   ', ' \nNoah Day 
   |   $8.49   |green   |09/15/17   \n', 'Josephine Keller |$13.10 |green|   09/15/17 ', '   Tracey Wolfe|$20.39 | 
   red   | 09/15/17 ', '\nIgnacio Parks|$14.70   | white&red |09/15/17 \n', ' Beatrice Newman |$22.45   
   |white&purple&red \n|   09/15/17', ' Andre Norris   |   $28.46   |   \nred|   09/15/17 ', '   Albert Lewis | 
   $23.89|   \nblack&red| 09/15/17', '   Javier Bailey   |   \n$24.49   | black&red | 09/15/17   ', ' Everett Lyons 
   |$1.81|   black&red | 09/15/17 ', '   \nAbraham Maxwell| $6.81   |green|   09/15/17   \n', '   Traci Craig |$0.65| 
   green&yellow| \n09/15/17 ', ' Jeffrey Jenkins   |$26.45| \ngreen&yellow&blue   |   09/15/17', '   Merle Wilson \n| 
     $7.69 | purple| 09/15/17', 'Janis Franklin   \n|$8.74   | purple&black   |09/15/17 ', '  \nLeonard Guerrero |   
     $1.86   |yellow  \n|09/15/17', 'Lana Sanchez|$14.75   | yellow|   \n09/15/17   ', 'Donna Ball | $28.10  | 
     \nyellow&blue|   09/15/17   ', ' Terrell Barber   | \n$9.91   | green |09/15/17   ', 'Jody Flores| \n$16.34 | 
     green |   09/15/17', '   Daryl Herrera \n|$27.57| white|   09/15/17   ', ' Miguel Mcguire|$5.25| white&blue   |  
      09/15/17 ', '   \nRogelio Gonzalez| $9.51|   white&black&blue   \n|   09/15/17   ', '   Lora Hammond |$20.56 | 
      \ngreen|   09/15/17', 'Owen Ward| $21.64   |   \ngreen&yellow|09/15/17', 'Malcolm Morales |   \n$24.99   |   
      green&yellow&black| 09/15/17 ', '   \nEric Mcdaniel |$29.70| green | 09/15/17 \n', 'Madeline Estrada|   
      $15.52|green|   09/15/17 \n', ' Leticia Manning|$15.70 | green&purple| \n09/15/17 ', '   Mario Wallace | $12.36 
      |green | \n09/15/17', 'Lewis Glover|   $13.66   |   \ngreen&white|09/15/17', '   Gail Phelps   |$30.52   \n| 
      green&white&blue   | 09/15/17 ', ' Myrtle Morris \n|   $22.66   | green&white&blue|09/15/17']"""

"""
Now, iterate through and append each split string (which are lists now) to our new daily_transactions_split list.
"""

daily_transactions_split = []

for transaction in daily_transactions:
    daily_transactions_split.append(transaction.split("|"))

"""
Output: [['Edith Mcbride   ', '$1.21   ', '   white ', ' \n09/15/17   '], ['Herbert Tran   ', '   $7.29', 
' \nwhite&blue', '   09/15/17 '], ['Paul Clarke ', '$12.52 \n', '   white&blue ', ' 09/15/17 '], ['Lucille Caldwell   
\n', '   $5.13   ', ' white   ', ' 09/15/17'], ['\nEduardo George   ', '$20.39', ' white&yellow \n', '09/15/17   '], 
['   Danny Mclaughlin', '$30.82', '   \npurple ', '09/15/17 '], ['Stacy Vargas', ' $1.85   ', ' \npurple&yellow ', 
'09/15/17'], ['   Shaun Brock', ' \n$17.98', 'purple&yellow ', ' 09/15/17 '], [' \nErick Harper ', '$17.41', 
' blue ', ' 09/15/17'], [' \nMichelle Howell ', '$28.59', ' blue', '   09/15/17   '], [' \nCarroll Boyd', ' $14.51', 
'   purple&blue   ', '   \n09/15/17   '], [' Teresa Carter   ', ' $19.64 ', ' \nwhite', '09/15/17   '], ['   Jacob 
Kennedy ', ' $11.40   \n', ' white&red   ', ' 09/15/17'], [' Craig Chambers', ' \n$8.79 ', ' white&blue&red   ', 
'09/15/17   '], [' Peggy Bell', ' $8.65 ', 'blue   ', ' 09/15/17'], ['   Kenneth Cunningham ', '   $10.53', 
'   green&blue   ', ' \n09/15/17   '], ['   Marvin Morgan', '   $16.49', ' \ngreen&blue&red   ', '   09/15/17 '], 
['Marjorie Russell \n', ' $6.55 ', '   green&blue&red', '   09/15/17 '], ['\nIsrael Cummings', '   $11.86   ', 
'black', '  \n09/15/17'], ['   June Doyle   ', '   $22.29 ', '  \nblack&yellow ', '09/15/17 '], [' Jaime Buchanan   
', '   \n$8.35', '   white&black&yellow   ', '   09/15/17'], ['   \nRhonda Farmer', '$2.91 ', '   white&black&yellow  
 \n', '09/15/17'], [' Darren Mckenzie ', '$22.94', 'green \n', '09/15/17'], ['Rufus Malone', '$4.70   ', 
 ' green&yellow \n', ' 09/15/17   '], ['Hubert Miles', '   $3.59   \n', 'green&yellow&blue', '   09/15/17   '], 
 [' Joseph Bridges  ', '$5.66   ', ' green&yellow&purple&blue \n', '   09/15/17 '], [' Sergio Murphy   ', 
 '$17.51   ', '   \nblack   ', '   09/15/17 '], [' Audrey Ferguson ', ' \n$5.54', 'black&blue   ', '09/15/17 '], 
 ['Edna Williams ', ' \n$17.13', ' black&blue', '   09/15/17'], ['   Randy Fleming', '   $21.13 ', 'black ', 
 '09/15/17 '], ['Elisa Hart', ' $0.35   ', ' black&purple', '   09/15/17   '], ['\nErnesto Hunt ', ' $13.91   ', 
 '   black&purple ', '   \n09/15/17'], ['   Shannon Chavez   ', '$19.26   ', ' \nyellow', ' 09/15/17   '], 
 [' Sammy Cain', ' $5.45', '   \nyellow&red ', '09/15/17 '], ['   Steven Reeves ', '$5.50   \n', '   yellow', 
 '   09/15/17'], [' Ruben Jones   ', ' \n$14.56 ', '   yellow&blue', '09/15/17 '], [' Essie Hansen', '   $7.33   ', 
 '   yellow&blue&red\n', ' 09/15/17   '], ['   Rene Hardy   ', ' $20.22   ', ' \nblack ', '   09/15/17 '], 
 ['   Lucy Snyder   ', ' $8.67   \n', 'black&red  ', ' 09/15/17 '], ['Dallas Obrien ', '   \n$8.31', '   black&red ', 
 '   09/15/17'], ['   Stacey Payne \n', '   $15.70   ', '   white&black&red ', '09/15/17   \n'], ['   Tanya Cox   ', 
 '   $6.74   ', 'yellow   ', ' \n09/15/17 '], [' Melody Moran ', '   $30.84   \n', 'yellow&black', '   09/15/17 '], 
 [' Louise Becker   ', ' \n$12.31 ', ' green&yellow&black', '   09/15/17 '], ['\nRyan Webster', '$2.94 ', ' yellow ', 
 ' 09/15/17 \n'], ['Justin Blake ', ' $22.46   ', 'white&yellow ', '   \n09/15/17'], ['   Beverly Baldwin ', 
 '   $6.60', '   \nwhite&yellow&black ', '09/15/17   '], ['   Dale Brady   \n', '   $6.27 ', ' yellow   ', 
 '09/15/17 '], ['Guadalupe Potter ', '$21.12   ', ' yellow', ' 09/15/17   '], [' \nDesiree Butler ', '$2.10   ', 
 'white', ' 09/15/17  \n'], ['Sonja Barnett ', ' $14.22 ', 'white&black', '   \n09/15/17'], [' Angelica Garza', 
 '$11.60', 'white&black   \n', '   09/15/17   '], ['   Jamie Welch   ', ' $25.27   ', ' \nwhite&black&red ', 
 '09/15/17   '], ['   Rex Hudson   \n', '$8.26', '   purple', ' 09/15/17 '], ['   Nadine Gibbs \n', '   $30.80 ', 
 '   purple&yellow   ', ' 09/15/17   '], [' \nHannah Pratt', '   $22.61   ', '   purple&yellow   \n', '09/15/17'], 
 ['Gayle Richards', '$22.19 ', ' \ngreen&purple&yellow ', '09/15/17   '], ['Stanley Holland \n', ' $7.47   ', 
 ' red ', ' 09/15/17 '], [' Anna Dean', '$5.49 ', ' yellow&red ', '   09/15/17   '], ['\nTerrance Saunders ', 
 '   $23.70  ', 'green&yellow&red \n', ' 09/15/17 '], ['   Brandi Zimmerman ', ' $26.66 ', ' \nred   ', '09/15/17 '], 
 ['Guadalupe Freeman ', ' $25.95', ' \ngreen&red ', '   09/15/17   '], ['Irving Patterson \n', '$19.55 ', 
 ' green&white&red ', '   09/15/17 '], ['Karl Ross', '   $15.68', '   white ', '   09/15/17 '], [' Brandy Cortez ', 
 '$23.57', '   white&red   ', '09/15/17'], [' \nMamie Riley   ', '$29.32', ' purple', '09/15/17 '], ['Mike Thornton   
 ', ' $26.44 ', '   purple   ', ' 09/15/17'], [' \nJamie Vaughn   ', ' $17.24', 'green ', ' 09/15/17   '], 
 [' \nNoah Day ', '   $8.49   ', 'green   ', '09/15/17   \n'], ['Josephine Keller ', '$13.10 ', 'green', '   09/15/17 
 '], ['   Tracey Wolfe', '$20.39 ', ' red   ', ' 09/15/17 '], ['\nIgnacio Parks', '$14.70   ', ' white&red ', 
 '09/15/17 \n'], [' Beatrice Newman ', '$22.45   ', 'white&purple&red \n', '   09/15/17'], [' Andre Norris   ', 
 '   $28.46   ', '   \nred', '   09/15/17 '], ['   Albert Lewis ', ' $23.89', '   \nblack&red', ' 09/15/17'], 
 ['   Javier Bailey   ', '   \n$24.49   ', ' black&red ', ' 09/15/17   '], [' Everett Lyons ', '$1.81', '   black&red 
 ', ' 09/15/17 '], ['   \nAbraham Maxwell', ' $6.81   ', 'green', '   09/15/17   \n'], ['   Traci Craig ', '$0.65', 
 ' green&yellow', ' \n09/15/17 '], [' Jeffrey Jenkins   ', '$26.45', ' \ngreen&yellow&blue   ', '   09/15/17'], 
 ['   Merle Wilson \n', '   $7.69 ', ' purple', ' 09/15/17'], ['Janis Franklin   \n', '$8.74   ', ' purple&black   ', 
 '09/15/17 '], ['  \nLeonard Guerrero ', '   $1.86   ', 'yellow  \n', '09/15/17'], ['Lana Sanchez', '$14.75   ', 
 ' yellow', '   \n09/15/17   '], ['Donna Ball ', ' $28.10  ', ' \nyellow&blue', '   09/15/17   '], [' Terrell Barber  
  ', ' \n$9.91   ', ' green ', '09/15/17   '], ['Jody Flores', ' \n$16.34 ', ' green ', '   09/15/17'], ['   Daryl 
  Herrera \n', '$27.57', ' white', '   09/15/17   '], [' Miguel Mcguire', '$5.25', ' white&blue   ', '   09/15/17 '], 
  ['   \nRogelio Gonzalez', ' $9.51', '   white&black&blue   \n', '   09/15/17   '], ['   Lora Hammond ', '$20.56 ', 
  ' \ngreen', '   09/15/17'], ['Owen Ward', ' $21.64   ', '   \ngreen&yellow', '09/15/17'], ['Malcolm Morales ', 
  '   \n$24.99   ', '   green&yellow&black', ' 09/15/17 '], ['   \nEric Mcdaniel ', '$29.70', ' green ', ' 09/15/17 
  \n'], ['Madeline Estrada', '   $15.52', 'green', '   09/15/17 \n'], [' Leticia Manning', '$15.70 ', 
  ' green&purple', ' \n09/15/17 '], ['   Mario Wallace ', ' $12.36 ', 'green ', ' \n09/15/17'], ['Lewis Glover', 
  '   $13.66   ', '   \ngreen&white', '09/15/17'], ['   Gail Phelps   ', '$30.52   \n', ' green&white&blue   ', 
  ' 09/15/17 '], [' Myrtle Morris \n', '   $22.66   ', ' green&white&blue', '09/15/17']]"""

transactions_clean = []
for transaction in daily_transactions_split:
    temp_list = []
    for item in transaction:
        temp_list.append(item.replace("\n", "").strip())
    transactions_clean.append(temp_list)

"""
Output: [['Edith Mcbride', '$1.21', 'white', '09/15/17'], ['Herbert Tran', '$7.29', 'white&blue', '09/15/17'], 
['Paul Clarke', '$12.52', 'white&blue', '09/15/17'], ['Lucille Caldwell', '$5.13', 'white', '09/15/17'], 
['Eduardo George', '$20.39', 'white&yellow', '09/15/17'], ['Danny Mclaughlin', '$30.82', 'purple', '09/15/17'], 
['Stacy Vargas', '$1.85', 'purple&yellow', '09/15/17'], ['Shaun Brock', '$17.98', 'purple&yellow', '09/15/17'], 
['Erick Harper', '$17.41', 'blue', '09/15/17'], ['Michelle Howell', '$28.59', 'blue', '09/15/17'], ['Carroll Boyd', 
'$14.51', 'purple&blue', '09/15/17'], ['Teresa Carter', '$19.64', 'white', '09/15/17'], ['Jacob Kennedy', '$11.40', 
'white&red', '09/15/17'], ['Craig Chambers', '$8.79', 'white&blue&red', '09/15/17'], ['Peggy Bell', '$8.65', 'blue', 
'09/15/17'], ['Kenneth Cunningham', '$10.53', 'green&blue', '09/15/17'], ['Marvin Morgan', '$16.49', 
'green&blue&red', '09/15/17'], ['Marjorie Russell', '$6.55', 'green&blue&red', '09/15/17'], ['Israel Cummings', 
'$11.86', 'black', '09/15/17'], ['June Doyle', '$22.29', 'black&yellow', '09/15/17'], ['Jaime Buchanan', '$8.35', 
'white&black&yellow', '09/15/17'], ['Rhonda Farmer', '$2.91', 'white&black&yellow', '09/15/17'], ['Darren Mckenzie', 
'$22.94', 'green', '09/15/17'], ['Rufus Malone', '$4.70', 'green&yellow', '09/15/17'], ['Hubert Miles', '$3.59', 
'green&yellow&blue', '09/15/17'], ['Joseph Bridges', '$5.66', 'green&yellow&purple&blue', '09/15/17'], 
['Sergio Murphy', '$17.51', 'black', '09/15/17'], ['Audrey Ferguson', '$5.54', 'black&blue', '09/15/17'], 
['Edna Williams', '$17.13', 'black&blue', '09/15/17'], ['Randy Fleming', '$21.13', 'black', '09/15/17'], 
['Elisa Hart', '$0.35', 'black&purple', '09/15/17'], ['Ernesto Hunt', '$13.91', 'black&purple', '09/15/17'], 
['Shannon Chavez', '$19.26', 'yellow', '09/15/17'], ['Sammy Cain', '$5.45', 'yellow&red', '09/15/17'], 
['Steven Reeves', '$5.50', 'yellow', '09/15/17'], ['Ruben Jones', '$14.56', 'yellow&blue', '09/15/17'], 
['Essie Hansen', '$7.33', 'yellow&blue&red', '09/15/17'], ['Rene Hardy', '$20.22', 'black', '09/15/17'], 
['Lucy Snyder', '$8.67', 'black&red', '09/15/17'], ['Dallas Obrien', '$8.31', 'black&red', '09/15/17'], 
['Stacey Payne', '$15.70', 'white&black&red', '09/15/17'], ['Tanya Cox', '$6.74', 'yellow', '09/15/17'], 
['Melody Moran', '$30.84', 'yellow&black', '09/15/17'], ['Louise Becker', '$12.31', 'green&yellow&black', 
'09/15/17'], ['Ryan Webster', '$2.94', 'yellow', '09/15/17'], ['Justin Blake', '$22.46', 'white&yellow', '09/15/17'], 
['Beverly Baldwin', '$6.60', 'white&yellow&black', '09/15/17'], ['Dale Brady', '$6.27', 'yellow', '09/15/17'], 
['Guadalupe Potter', '$21.12', 'yellow', '09/15/17'], ['Desiree Butler', '$2.10', 'white', '09/15/17'], 
['Sonja Barnett', '$14.22', 'white&black', '09/15/17'], ['Angelica Garza', '$11.60', 'white&black', '09/15/17'], 
['Jamie Welch', '$25.27', 'white&black&red', '09/15/17'], ['Rex Hudson', '$8.26', 'purple', '09/15/17'], 
['Nadine Gibbs', '$30.80', 'purple&yellow', '09/15/17'], ['Hannah Pratt', '$22.61', 'purple&yellow', '09/15/17'], 
['Gayle Richards', '$22.19', 'green&purple&yellow', '09/15/17'], ['Stanley Holland', '$7.47', 'red', '09/15/17'], 
['Anna Dean', '$5.49', 'yellow&red', '09/15/17'], ['Terrance Saunders', '$23.70', 'green&yellow&red', '09/15/17'], 
['Brandi Zimmerman', '$26.66', 'red', '09/15/17'], ['Guadalupe Freeman', '$25.95', 'green&red', '09/15/17'], 
['Irving Patterson', '$19.55', 'green&white&red', '09/15/17'], ['Karl Ross', '$15.68', 'white', '09/15/17'], 
['Brandy Cortez', '$23.57', 'white&red', '09/15/17'], ['Mamie Riley', '$29.32', 'purple', '09/15/17'], 
['Mike Thornton', '$26.44', 'purple', '09/15/17'], ['Jamie Vaughn', '$17.24', 'green', '09/15/17'], ['Noah Day', 
'$8.49', 'green', '09/15/17'], ['Josephine Keller', '$13.10', 'green', '09/15/17'], ['Tracey Wolfe', '$20.39', 'red', 
'09/15/17'], ['Ignacio Parks', '$14.70', 'white&red', '09/15/17'], ['Beatrice Newman', '$22.45', 'white&purple&red', 
'09/15/17'], ['Andre Norris', '$28.46', 'red', '09/15/17'], ['Albert Lewis', '$23.89', 'black&red', '09/15/17'], 
['Javier Bailey', '$24.49', 'black&red', '09/15/17'], ['Everett Lyons', '$1.81', 'black&red', '09/15/17'], 
['Abraham Maxwell', '$6.81', 'green', '09/15/17'], ['Traci Craig', '$0.65', 'green&yellow', '09/15/17'], 
['Jeffrey Jenkins', '$26.45', 'green&yellow&blue', '09/15/17'], ['Merle Wilson', '$7.69', 'purple', '09/15/17'], 
['Janis Franklin', '$8.74', 'purple&black', '09/15/17'], ['Leonard Guerrero', '$1.86', 'yellow', '09/15/17'], 
['Lana Sanchez', '$14.75', 'yellow', '09/15/17'], ['Donna Ball', '$28.10', 'yellow&blue', '09/15/17'], 
['Terrell Barber', '$9.91', 'green', '09/15/17'], ['Jody Flores', '$16.34', 'green', '09/15/17'], ['Daryl Herrera', 
'$27.57', 'white', '09/15/17'], ['Miguel Mcguire', '$5.25', 'white&blue', '09/15/17'], ['Rogelio Gonzalez', '$9.51', 
'white&black&blue', '09/15/17'], ['Lora Hammond', '$20.56', 'green', '09/15/17'], ['Owen Ward', '$21.64', 
'green&yellow', '09/15/17'], ['Malcolm Morales', '$24.99', 'green&yellow&black', '09/15/17'], ['Eric Mcdaniel', 
'$29.70', 'green', '09/15/17'], ['Madeline Estrada', '$15.52', 'green', '09/15/17'], ['Leticia Manning', '$15.70', 
'green&purple', '09/15/17'], ['Mario Wallace', '$12.36', 'green', '09/15/17'], ['Lewis Glover', '$13.66', 
'green&white', '09/15/17'], ['Gail Phelps', '$30.52', 'green&white&blue', '09/15/17'], ['Myrtle Morris', '$22.66', 
'green&white&blue', '09/15/17']]"""

"""
Create three empty lists. customers, sales, and thread_sold. We are going to collect the individual data points 
for each transaction in these lists.

Now, iterate through transactions_clean and for each transaction:

Append the customers name to customers.
Append the amount of the sale to sales.
Append the threads sold to thread_sold.
"""

customer = []
sales = []
thread_sold = []

for transaction in transactions_clean:
    customer.append(transaction[0])
    sales.append(transaction[1])
    thread_sold.append(transaction[-2])

"""
Now we want to know how much Thread Shed made in a day.

First, define a variable called total_sales and set it equal to 0. Now, consider the list sales. It is a list of 
strings that we want to sum. In order for us to sum these values, we will have to remove the $, and set them equal to 
floats.

Iterate through sales and for each item, strip off the $, set it equal to a float, and add it to total_sales.
"""

total_sales = 0

for sale in sales:
    total_sales += float(sale.strip("$"))

print(total_sales)  # Should be 1498.7400000000005

"""
Finally, we want to determine how many of each color thread we sold today. Let’s start with a single color, 
and then we’ll generalize it.

First, print out thread_sold and inspect it.


Output:

['white', 'white&blue', 'white&blue', 'white', 'white&yellow', 'purple', 'purple&yellow', 'purple&yellow', 'blue', 
'blue', 'purple&blue', 'white', 'white&red', 'white&blue&red', 'blue', 'green&blue', 'green&blue&red', 
'green&blue&red', 'black', 'black&yellow', 'white&black&yellow', 'white&black&yellow', 'green', 'green&yellow', 
'green&yellow&blue', 'green&yellow&purple&blue', 'black', 'black&blue', 'black&blue', 'black', 'black&purple', 
'black&purple', 'yellow', 'yellow&red', 'yellow', 'yellow&blue', 'yellow&blue&red', 'black', 'black&red', 
'black&red', 'white&black&red', 'yellow', 'yellow&black', 'green&yellow&black', 'yellow', 'white&yellow', 
'white&yellow&black', 'yellow', 'yellow', 'white', 'white&black', 'white&black', 'white&black&red', 'purple', 
'purple&yellow', 'purple&yellow', 'green&purple&yellow', 'red', 'yellow&red', 'green&yellow&red', 'red', 'green&red', 
'green&white&red', 'white', 'white&red', 'purple', 'purple', 'green', 'green', 'green', 'red', 'white&red', 
'white&purple&red', 'red', 'black&red', 'black&red', 'black&red', 'green', 'green&yellow', 'green&yellow&blue', 
'purple', 'purple&black', 'yellow', 'yellow', 'yellow&blue', 'green', 'green', 'white', 'white&blue', 
'white&black&blue', 'green', 'green&yellow', 'green&yellow&black', 'green', 'green', 'green&purple', 'green', 
'green&white', 'green&white&blue', 'green&white&blue']


We see that thread_sold is a list of strings, some are single colors and some are multiple colors separated by the & 
character. The end product we want here is a list that contains an item for each color thread sold, so no strings 
that have multiple colors in them. First, define an empty list thread_sold_split. Next, iterate through thread_sold. 
For each item, check if it is a single color or multiple colors. If it is a single color, append that color to 
thread_sold_split. If it is multiple colors, first split the string around the & character and then add each color 
individually to thread_sold_split. 

Now we have a list thread_sold_split that contains an entry with the color of 
every thread sold today.

Define a function called color_count that takes one argument, color. The function should iterate through 
thread_sold_split and count the number of times the item is equal to argument, color. Then, it should return this 
count.
"""

thread_sold_split = []

for thread in thread_sold:
    if "&" not in thread:
        thread_sold_split.append(thread)
    else:
        multi_thread = thread.split("&")
        for item in multi_thread:
            thread_sold_split.append(item)


def colour_count(colour):
    count = 0
    for thread_colour in thread_sold_split:
        if thread_colour == colour:
            count += 1
    return count


print(colour_count("white"))  # Should return 28

"""
Define a list called colors that stores all of the colored threads that Thread Shed offers:

colours = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

Now, using the string method .format() and the function color_count(), iterate through the list colors and print a 
sentence that says how many threads of each color were sold today."""

colours = ['red', 'yellow', 'green', 'white', 'black', 'blue', 'purple']

for colour in colours:
    colour_total_count = colour_count(colour)
    print("Thread Shed sold {} threads of {} thread today.".format(colour_total_count, colour))

"""
Output:
Thread Shed sold 24 threads of red thread today.
Thread Shed sold 34 threads of yellow thread today.
Thread Shed sold 30 threads of green thread today.
Thread Shed sold 28 threads of white thread today.
Thread Shed sold 26 threads of black thread today.
Thread Shed sold 22 threads of blue thread today.
Thread Shed sold 17 threads of purple thread today.
"""
