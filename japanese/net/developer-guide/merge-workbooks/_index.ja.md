---
title: 複数のワークブックを単一のワークブックに結合する
linktitle: ワークブック結合ツール
type: docs
weight: 66
url: /ja/net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

時々、画像、グラフ、データなど、さまざまなコンテンツを組み合わせて単一のワークブックに結合する必要があります。Aspose.Cellsはこの機能をサポートしています。この記事では、Aspose.Cellsを使用してコンソールアプリケーションを作成し、数行のコードを使ってワークブックを結合する方法を示します。

{{% /alert %}}

## **画像とグラフを使用したワークブックの結合**

例のコードは、Aspose.Cellsを使用して2つのワークブックを1つのワークブックに結合します。コードはソースワークブックを読み込み、[**Workbook.combine()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/combine)メソッドを使用してそれらを結合し、出力ワークブックを保存します。

### **ソースワークブック**

- [charts.xlsx](5473097.xlsx)
- [picture.xlsx](5473096.xlsx)

### **出力ワークブック**

- [combined.xlsx](5473095.xlsx)

### **スクリーンショット**

以下は、ソースおよび出力ワークブックのスクリーンショットです。

{{% alert color="primary" %}}

ソースワークブックを好きなものを使用できます。これらの画像は、イメージ説明のためのものです。

{{% /alert %}}

**チャートワークブックの最初のワークシート - 積み重ね** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_1.jpg)

**チャートワークブックの2番目のワークシート - 折れ線** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_2.jpg)

**画像ワークブックの最初のワークシート - 画像** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_3.jpg)

**結合されたワークブックの3つのワークシート - 積み重ね、折れ線、画像** 

![todo:image_alt_text](combine-multiple-workbooks-into-a-single-workbook_4.jpg)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CombineMultipleWorkbooksSingleWorkbook-1.cs" >}}

## **高度なトピック**
- [複数のワークシートを単一のワークシートに結合する](/cells/ja/net/combine-multiple-worksheets-into-a-single-worksheet/)
- [ファイルの結合](/cells/ja/net/merge-files/)
