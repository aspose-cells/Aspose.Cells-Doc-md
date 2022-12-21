---
title: 複数のワークブックを 1 つのワークブックに結合する
linktitle: ワークブックの合併
type: docs
weight: 66
url: /ja/net/combine-multiple-workbooks-into-a-single-workbook/
---
{{% alert color="primary" %}}

場合によっては、ワークブックを画像、グラフ、データなどのさまざまなコンテンツと組み合わせて 1 つのワークブックにする必要があります。 Aspose.Cells はこの機能をサポートしています。この記事では、Visual Studio でコンソール アプリケーションを作成し、Aspose.Cells を使用して数行の単純なコードとワークブックを組み合わせる方法を示します。

{{% /alert %}}

## **ワークブックと画像およびチャートの結合**

サンプル コードは、Aspose.Cells を使用して 2 つのワークブックを 1 つのワークブックに結合します。コードはソース ワークブックをロードし、[**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)メソッドを使用してそれらを結合し、出力ワークブックを保存します。

### **ソース ワークブック**

- [グラフ.xlsx](5473097.xlsx)
- [画像.xlsx](5473096.xlsx)

### **出力ワークブック**

- [結合.xlsx](5473095.xlsx)

### **スクリーンショット**

以下は、ソース ワークブックと出力ワークブックのスクリーンショットです。

{{% alert color="primary" %}}

任意のソース ワークブックを使用できます。これらの画像は、説明のみを目的としています。

{{% /alert %}}

**グラフ ワークブックの最初のワークシート - 積み上げ** 

![todo:画像_代替_文章](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**グラフ ワークブックの 2 番目のワークシート - 線** 

![todo:画像_代替_文章](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**ピクチャ ワークブックの最初のワークシート - ピクチャ** 

![todo:画像_代替_文章](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**結合されたブック内の 3 つのワークシートすべて - 積み上げ、線、画像** 

![todo:画像_代替_文章](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **先行トピック**
- [複数のワークシートを 1 つのワークシートに結合する](/cells/ja/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [ファイルをマージ](/cells/ja/net/merge-files/)
