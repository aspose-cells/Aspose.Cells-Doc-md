---
title: 条件付き書式の DataBars 画像を生成する
type: docs
weight: 170
url: /ja/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

場合によっては、条件付き書式設定 DataBar の画像を生成する必要があります。 Aspose.Cells を使用できます[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)メソッドを使用してこれらの画像を生成します。この記事では、Aspose.Cells を使用して DataBar イメージを生成する方法を示します。

{{% /alert %}}

## **例**

次のサンプル コードは、セル C1 の DataBar イメージを生成します。まず、セルの書式条件オブジェクトにアクセスし、そのオブジェクトから DataBar オブジェクトにアクセスし、そのオブジェクトを使用します。[**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) セルの画像を生成するメソッド。最後に、イメージをディスクに保存します。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
