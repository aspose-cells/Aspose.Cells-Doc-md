---
title: Find Query Tables and List Objects related to External Data Connections with Golang via C++
linktitle: Find Query Tables and List Objects
type: docs
weight: 20
url: /go-cpp/find-query-tables-and-list-objects-related-to-external-data-connections/
description: Learn how to find Query Tables and List Objects related to External Data Connections using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Sometimes, you need to find out Query Tables and List Objects related to an External Data Connection. Query Tables are related to an External Data Connection object with a Connection ID, while List Objects are related to a Query Table.

{{% /alert %}}

## **Find Query Tables and List Objects related to External Data Connections**
The following sample codes with [sample Excel file](5115493.xlsm) explain how to find Query Tables and List Objects related to an External Data Connection.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindQueryTablesAndListObjectsRelatedToExternalDataConnections.go" >}}

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindQueryTablesAndListObjectsRelatedToExternalDataConnections-1.go" >}}

The following is the console output of running the above sample codes with this [sample Excel file](5115493.xlsm).

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

{{< app/cells/assistant language="go" >}}


