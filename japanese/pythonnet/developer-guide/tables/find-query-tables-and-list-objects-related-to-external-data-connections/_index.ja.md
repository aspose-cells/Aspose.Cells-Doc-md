---
title: 外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける
type: docs
weight: 20
url: /ja/python-net/find-query-tables-and-list-objects-related-to-external-data-connections/
---

{{% alert color="primary" %}} 

時々、外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける必要があります。 クエリテーブルは、接続IDを持つ外部データ接続オブジェクトと関連しており、リストオブジェクトはクエリテーブルに関連しています。

{{% /alert %}} 
## **外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける**
[サンプルエクセルファイル](5115493.xlsm)を使用して、外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける方法について説明する以下のサンプルコードを参照してください。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Tables-FindQueryTablesAndListObjectsOfExternalDataConnections.py" >}}


上記のサンプルコードをこの[サンプルエクセルファイル](5115493.xlsm)で実行した場合のコンソール出力は次のとおりです。

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

