---
title: Find Query Tables and List Objects related to External Data Connections
type: docs
weight: 20
url: /net/find-query-tables-and-list-objects-related-to-external-data-connections/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sometimes, you need to find out Query Tables and List Objects related to some External Data Connection. Query Tables are related to External Data Connection object with Connection Id, while List Objects are related to a Query Table.

{{% /alert %}} 
## **Find Query Tables and List Objects related to External Data Connections**
The following sample codes with [sample excel file](5115493.xlsm) explain how to find Query Tables and List Objects related to External Data Connection.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

The following is the console output of running the above sample codes with this [sample excel file](5115493.xlsm).

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
{{< app/cells/assistant language="csharp" >}}
