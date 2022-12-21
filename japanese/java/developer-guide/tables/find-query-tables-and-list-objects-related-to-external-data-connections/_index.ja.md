---
title: 外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する
type: docs
weight: 20
url: /ja/java/find-query-tables-and-list-objects-related-to-external-data-connections/
---
## **外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する**

外部データ接続に関連するクエリ テーブルとリスト オブジェクトを見つける必要がある場合があります。クエリ テーブルは接続 ID を持つ外部データ接続オブジェクトに関連付けられ、リスト オブジェクトはクエリ テーブルに関連付けられます。

次のサンプル コードでは、外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する方法について説明します。コードは、[サンプルエクセルファイル](5472550.xlsm)提供されたリンクからダウンロードできます。このサンプル コードの出力は、この記事の最後にも記載されています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-tables-FindReferenceCellsFromExternalConnection-FindReferenceCellsFromExternalConnection.java" >}}

## **コンソール出力**

これを使用した上記のサンプル コードのコンソール出力は次のとおりです。[サンプルエクセルファイル](5472550.xlsm).

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
