---
title: 外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける
type: docs
weight: 20
url: /ja/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---

## **外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける**

時々、外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける必要があります。 クエリテーブルは、接続IDを持つ外部データ接続オブジェクトと関連しており、リストオブジェクトはクエリテーブルに関連しています。

次のサンプルコードは、外部データ接続に関連するクエリテーブルとリストオブジェクトを見つける方法を説明しています。 このコードでは、提供されたリンクからダウンロードできる[サンプルExcelファイル](5472550.xlsm)を使用しています。 また、この記事の最下部にこのサンプルコードの出力を見ることもできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **コンソール出力**

以下は、この[サンプルExcelファイル](5472550.xlsm)を使用して上記のサンプルコードのコンソール出力です。

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
{{< app/cells/assistant language="java" >}}
