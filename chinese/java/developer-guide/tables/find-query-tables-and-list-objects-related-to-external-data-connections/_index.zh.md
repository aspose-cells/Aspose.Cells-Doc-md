---
title: 查找与外部数据连接相关的查询表和列表对象
type: docs
weight: 20
url: /zh/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **查找与外部数据连接相关的查询表和列表对象**

有时您需要找出与某些外部数据连接相关的查询表和列表对象。查询表与连接ID相关联，而列表对象与查询表相关。

以下示例代码解释了如何找到与外部数据连接相关的查询表和列表对象。该代码使用[示例Excel文件](5472550.xlsm)，您可以从提供的链接中下载。您还可以在本文底部看到此示例代码的输出。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **控制台输出**

这是使用此【示例Excel文件】（5472550.xlsm）的代码的控制台输出。

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
