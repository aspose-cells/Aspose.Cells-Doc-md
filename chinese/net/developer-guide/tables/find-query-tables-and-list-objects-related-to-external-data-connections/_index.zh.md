---
title: 查找与外部数据连接相关的查询表和列表对象
type: docs
weight: 20
url: /zh/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

有时您需要找出与某些外部数据连接相关的查询表和列表对象。查询表与连接ID相关联，而列表对象与查询表相关。

{{% /alert %}} 
## **查找与外部数据连接相关的查询表和列表对象**
以下示例代码和[示例Excel文件](5115493.xlsm)解释了如何找出与外部数据连接相关的查询表和列表对象。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

以下是运行上述示例代码与这个[示例Excel文件](5115493.xlsm)的控制台输出。

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
