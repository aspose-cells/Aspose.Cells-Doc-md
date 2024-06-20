---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /ja/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

ワークシートの画像を透明なイメージとして生成する必要があることがあります。塗りつぶし色のないすべてのセルに透明性を適用したい場合があります。Aspose.Cells は、ワークシート画像に透明性を適用するための[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)プロパティを提供しています。このプロパティが**false**の場合、塗りつぶし色のないセルは白色で描画され、**true**の場合、塗りつぶし色のないセルは透明に描画されます。

{{% /alert %}}

以下のワークシートイメージでは、透明性が適用されていません。埋められていないセルは白色で描画されます。

**透明度を適用しないワークシート画像**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

以下のワークシート画像では、透明度が適用されました。塗りつぶしのないセルは透明です。

**透明度を適用した後のワークシート画像**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

次のサンプルコードを使用して、Excelワークシートの透明な画像を生成できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
