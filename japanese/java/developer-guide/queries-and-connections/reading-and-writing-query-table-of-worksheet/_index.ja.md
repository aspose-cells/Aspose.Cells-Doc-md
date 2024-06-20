---
title: ワークシートのクエリテーブルの読み取りと書き込み
type: docs
weight: 560
url: /ja/java/reading-and-writing-query-table-of-worksheet/
---

{{% alert color="primary" %}} 

Aspose.Cellsは[Worksheet.getQueryTables()](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#QueryTables)コレクションを提供し、[QueryTableCollection](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTableCollection)を返します。特定の[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)を取得するには、[QueryTableCollection.get()](https://reference.aspose.com/cells/java/com.aspose.cells/querytablecollection#Item%20\(int\))プロパティを使用し、QueryTableのインデックスを渡します。[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)クラスには、クエリテーブルを調整するための次の2つのプロパティがあります。

- [QueryTable.getAdjustColumnWidth()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#AdjustColumnWidth)
- [QueryTable.getPreserveFormatting()](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)

これらは両方ともブール値です。Microsoft Excelでそれらを表示するには、[データ] > [接続] > [プロパティ]を選択します。

{{% /alert %}} 
## **ワークシートのクエリテーブルの読み取りと書き込み**
次のサンプルコードは、最初の[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)を最初のワークシートから読み取り、その[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)の両方のプロパティを出力します。その後、[QueryTable.PreserveFormatting](https://reference.aspose.com/cells/java/com.aspose.cells/querytable#PreserveFormatting)を**true**に設定します。

次のスクリーンショットは、コードで使用される[source excel file](5472578.xlsx)と、その[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)の両方の値を示しています。

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_1.png)

次のスクリーンショットは、コードによって生成された[output excel file](5472574.xlsx)とその[QueryTable](https://reference.aspose.com/cells/java/com.aspose.cells/QueryTable)の両方の値を示しています。Preserved Formattingのチェックがされていることがわかります。

![todo:image_alt_text](reading-and-writing-query-table-of-worksheet_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-ReadingAndWritingQueryTable.java" >}}
## **コンソール出力**
上記のサンプルコードのコンソール出力は次の通りです

{{< highlight java >}}

 Adjust Column Width: true

Preserve Formatting: false

{{< /highlight >}}

## **クエリテーブル結果の範囲を取得**
Aspose.Cellsは、クエリテーブルの結果範囲のアドレスを読み取るオプションを提供します。次のコードは、クエリテーブルの結果範囲のアドレスを読み取るこの機能を示しています。サンプルファイルは[こちら](QueryTXT.xlsx)からダウンロードできます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ReadingAndWritingQueryTable-RetrieveQueryTableResultRange.java" >}}
