---
title: Golang経由のC++で複数のワークブックを1つのワークブックに結合する
linktitle: ワークブック結合ツール
type: docs
weight: 66
url: /ja/go-cpp/combine-multiple-workbooks-into-a-single-workbook/
description: Aspose.Cellsを使用したGolang経由のC++で複数のワークブックを1つのワークブックに結合する方法を学びます。
---

{{% alert color="primary" %}}

時には、画像やチャート、データなど様々な内容を持つワークブックを1つに結合する必要があります。Aspose.Cellsはこの機能をサポートしています。この記事では、Visual Studioでコンソールアプリケーションを作成し、数行のコードでワークブックを結合する方法を示します。

{{% /alert %}}

## **画像とグラフを使用したワークブックの結合**

例のコードは、Aspose.Cellsを使用して2つのワークブックを1つのワークブックに結合します。コードはソースワークブックを読み込み、[**Workbook::Combine()**](https://reference.aspose.com/cells/go-cpp/workbook/combine/)メソッドを使用してそれらを結合し、出力ワークブックを保存します。

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

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-MergeWorkbooks.go" >}}
## **高度なトピック**
- [複数のワークシートを単一のワークシートに結合する](/cells/ja/cpp/combine-multiple-worksheets-into-a-single-worksheet/)
- [ファイルの結合](/cells/ja/cpp/merge-files/)
