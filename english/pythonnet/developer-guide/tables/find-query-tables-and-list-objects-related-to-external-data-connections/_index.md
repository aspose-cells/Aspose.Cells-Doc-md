---
title: Find Query Tables and List Objects related to External Data Connections
type: docs
weight: 20
url: /python-net/find-query-tables-and-list-objects-related-to-external-data-connections/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

Sometimes you need to find Query Tables and List Objects related to an External Data Connection. Query Tables are linked to an External Data Connection object by Connection Id, while List Objects are linked to a Query Table.

{{% /alert %}} 
## **Find Query Tables and List Objects related to External Data Connections**
The following sample code with the [sample Excel file](5115493.xlsm) explains how to find Query Tables and List Objects related to an External Data Connection.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FindQueryTablesAndListObjectsOfExternalDataConnections.py" >}}

The following is the console output of running the above sample code with this [sample Excel file](5115493.xlsm).

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
