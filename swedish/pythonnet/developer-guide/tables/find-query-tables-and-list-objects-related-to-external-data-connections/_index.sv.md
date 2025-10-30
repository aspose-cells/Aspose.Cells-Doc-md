---
title: Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar
type: docs
weight: 20
url: /sv/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

Ibland behöver du ta reda på frågetabeller och lista objekt relaterade till någon extern dataanslutning. Frågetabeller är relaterade till objekt för extern dataanslutning med anslutnings-ID, medan lista objekt är relaterade till en frågetabell.

{{% /alert %}} 
## **Hitta frågetabeller och lista objekt relaterade till externa dataanslutningar**
Följande kodexemplar med [provexkelfil](5115493.xlsm) förklarar hur man hittar frågetabeller och lista objekt relaterade till extern dataanslutning.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FindQueryTablesAndListObjectsOfExternalDataConnections.py" >}}


Det följande är konsolutdatan från att köra ovanstående kodexemplar med denna [provexkelfil](5115493.xlsm).

{{< highlight java >}}

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


{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
