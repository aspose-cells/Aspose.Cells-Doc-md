---
title: ワークシートのクエリ テーブルの読み取りと書き込み
type: docs
weight: 560
url: /ja/java/reading-and-writing-query-table-of-worksheet/
---
{{% alert color="primary" %}} 

Aspose.Cells提供[Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables)を返すコレクション[クエリ テーブル コレクション](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection).特定のものを取得するには[クエリテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)、 使用[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\) ) プロパティを呼び出して、QueryTable のインデックスを渡します。の[クエリテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)クラスには、QueryTable を調整するための次の 2 つのプロパティがあります。

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

これらは両方ともブール値です。それらは、[データ] > [接続] > [プロパティ] を使用して Microsoft Excel で表示できます。

{{% /alert %}} 
## **ワークシートのクエリ テーブルの読み取りと書き込み**
次のサンプル コードは、最初の[クエリテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)最初のワークシートの両方を印刷します。[クエリテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)プロパティ。次に、[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)に**真実**.

次のスクリーンショットは、[ソースエクセルファイル](5472578.xlsx)コードとそのプロパティで使用され、[クエリテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)値。

![todo:画像_代替_文章](reading-and-writing-query-table-of-worksheet_1.png)

次のスクリーンショットは、[出力エクセルファイル](5472574.xlsx)コードとそのプロパティによって生成され、[クエリテーブル](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)値。ご覧のとおり、Preserved Formatting チェックボックスがオンになっています。

![todo:画像_代替_文章](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **コンソール出力**
上記のサンプル コードのコンソール出力は次のとおりです。

{{< highlight "java" >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}
## **クエリ テーブルの結果範囲を取得する**
Aspose.Cells は、アドレス、つまりクエリ テーブルのセルの結果範囲を読み取るオプションを提供します。次のコードは、クエリ テーブルの結果範囲のアドレスを読み取ることにより、この機能を示しています。サンプルファイルがダウンロードできます[ここ](QueryTXT.xlsx).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
