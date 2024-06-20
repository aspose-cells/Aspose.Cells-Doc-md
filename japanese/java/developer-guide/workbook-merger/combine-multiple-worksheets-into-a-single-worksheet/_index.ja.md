---
title: 複数のワークシートを単一のワークシートにマージする
type: docs
weight: 70
url: /ja/java/combine-multiple-worksheets-into-a-single-worksheet/
description: JavaコードとAspose.Cells for Java APIを使用して複数のワークシートを単一のワークシートに結合する
keywords: 複数のワークシートを単一のワークシートに結合するには、Aspose.Cells APIを使用します。この記事では、ソースブックを読み込み、すべてのソースワークシートのデータを宛先ブック内の単一のワークシートに結合するコード例を示します。
---

{{% alert color="primary" %}}

複数のワークシートを1つのワークシートに結合する必要がある場合があります。Aspose.Cells APIを使用すれば簡単に実現できます。この記事では、ソースブックを読み込み、すべてのソースワークシートのデータを目的のワークブック内の単一のワークシートに結合するコード例を紹介します。

{{% /alert %}}

## **ワークシートを結合する方法**

以下のサンプルは、[**Range.copy()**](https://reference.aspose.com/cells/java/com.aspose.cells/range#copy(com.aspose.cells.Range))メソッドを使用してすべてのソースワークシートを宛先ブック内の単一シートにコピーします。

### **ソースワークブック**

任意のソースブックが使用できます。この例では、3つのワークシートを持つソースブックを使用しています。

**ワークシート1**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_1.jpg)

**ワークシート2**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_2.jpg)

**ワークシート3**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_3.jpg)

### **出力ワークブック**

次のコードを実行すると、すべての3つのワークシートのデータが含まれた単一のワークシートを持つワークブックが作成されます。

**出力ワークシートには今や3つのソースワークシートのデータが含まれています**

![todo:image_alt_text](combine-multiple-worksheets-into-a-single-worksheet_4.jpg)

## **ソースワークブックおよび出力ワークブックのダウンロード**

- [ソースワークブック](5473078.xlsx)
- [出力ワークブック](5473079.xlsx)

### **複数のワークシートを1つのワークシートにマージするためのサンプルコード**

次のコードスニペットは、複数のワークシートを1つのワークシートに結合する方法を示しています。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CombineMultipleWorksheets-CombineMultipleWorksheets.java" >}}

## **追加リソース**

{{% alert color="primary" %}}

[1つのワークブックに複数のワークブックを結合](/cells/ja/java/combine-multiple-workbooks-into-a-single-workbook/)」記事でより詳しい情報を得るために役立つかもしれません。

{{% /alert %}}
