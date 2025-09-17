##Find Query Tables and List Objects related to External Data Connections
## **Find Query Tables and List Objects related to External Data Connections**
Sometimes, you need to find out Query Tables and List Objects related to some External Data Connection. Query Tables are related to External Data Connection object with Connection Id, while List Objects are related to a Query Table.
The following sample code explains how you can find Query Tables and List Objects related to External Data Connection. The code uses the [sample excel file](5472550.xlsm) which you can download from the provided link. You can also see the output of this sample code at the bottom of this article.
## **Console Output**
Here is the console output of the above sample code using this [sample excel file](5472550.xlsm).
connection: AAPL Connection
querytable hp?s=AAPL+Historical+Prices
refersto: =Sheet1!$Q$1:$W$69
connection: BOSL066360W7_SQLEXPRESS Test
querytable BOSL066360W7_SQLEXPRESS Test
Table Table_BOSL066360W7_SQLEXPRESS_Test
refersto: Sheet1!A1:B3
connection: BOSL066360W7_SQLEXPRESS Test1
querytable BOSL066360W7_SQLEXPRESS Test_1
Table Table_BOSL066360W7_SQLEXPRESS_Test_1
refersto: Sheet1!D1:E2
connection: UWTI Connection
querytable hp?s=UWTI+Historical+Prices
refersto: =Sheet1!$H$1:$N$69
