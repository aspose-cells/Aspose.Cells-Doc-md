---
title: 複数のワークブックを単一のワークブックに結合する
linktitle: ワークブック結合ツール
type: docs
weight: 66
url: /ja/python-net/combine-multiple-workbooks-into-a-single-workbook/
---

{{% alert color="primary" %}}

時には、画像やチャート、データなどさまざまな内容のブックを一つにまとめる必要があります。Aspose.Cells for Python via .NETはこの機能をサポートしています。この記事では、Visual Studioでコンソールアプリケーションを作成し、Aspose.Cells for Python via .NETを使用していくつかの簡単なコードでワークブックを結合する方法を示します。

{{% /alert %}}

## **画像とグラフを使用したワークブックの結合**

例のコードは、Aspose.Cells for Python via .NET を使用して二つのワークブックを一つに結合します。コードはソースのワークブックを読み込み、[**Workbook.combine()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/combine)メソッドを使用して結合し、出力のワークブックを保存します。

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Merge-Workbooks-CombineMultipleWorkbooksSingleWorkbook-1.py" >}}

## **高度なトピック**
- [複数のワークシートを単一のワークシートに結合する](/cells/ja/python-net/combine-multiple-worksheets-into-a-single-worksheet/)
- [ファイルの結合](/cells/ja/python-net/merge-files/)

{{< app/cells/assistant language="python-net" >}}
