---
title: 外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する
type: docs
weight: 20
url: /ja/net/find-query-tables-and-list-objects-related-to-external-data-connections/
---
{{% alert color="primary" %}} 

外部データ接続に関連するクエリ テーブルとリスト オブジェクトを見つける必要がある場合があります。クエリ テーブルは接続 ID を持つ外部データ接続オブジェクトに関連付けられ、リスト オブジェクトはクエリ テーブルに関連付けられます。

{{% /alert %}} 
## **外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する**
以下のサンプルコードは[サンプルエクセルファイル](5115493.xlsm)外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する方法を説明します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-FindQueryTablesAndListObjectsOfExternalDataConnections.cs" >}}

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FindQueryTablesAndListObjectsOfExternalDataConnections-PrintTables.cs" >}}

以下は、これを使用して上記のサンプル コードを実行した場合のコンソール出力です。[サンプルエクセルファイル](5115493.xlsm).

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
