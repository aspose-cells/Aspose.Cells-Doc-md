---
title: Hitta frågetabeller och listobjekt relaterade till externa dataanslutningar
type: docs
weight: 20
url: /sv/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

Ibland behöver du ta reda på frågetabeller och listobjekt relaterade till någon extern dataanslutning. Frågetabeller är relaterade till External Data Connection-objekt med anslutnings-ID, medan listobjekt är relaterade till en frågetabell.

{{% /alert %}} 
## **Hitta frågetabeller och listobjekt relaterade till externa dataanslutningar**
 Följande exempelkoder med[exempel på excel-fil](5115493.xlsm) förklara hur du hittar frågetabeller och listobjekt relaterade till extern dataanslutning.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

 Följande är konsolutgången för att köra ovanstående exempelkoder med detta[exempel på excel-fil](5115493.xlsm).

{{< highlight "java" >}}

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
