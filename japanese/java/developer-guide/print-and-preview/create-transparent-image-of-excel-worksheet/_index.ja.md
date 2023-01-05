---
title: Excelワークシートの透過画像を作成
type: docs
weight: 80
url: /ja/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

場合によっては、ワークシートの画像を透明な画像として生成する必要があります。塗りつぶしの色がないすべてのセルに透明度を適用します。 Aspose.Cells は[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)ワークシート イメージに透明度を適用するプロパティ。このプロパティが**間違い**の場合、塗りつぶしの色のないセルは白色で描画されます。**真実**、塗りつぶしの色のないセルは透明に描画されます。

{{% /alert %}}

次のワークシート イメージでは、透明度が適用されていません。塗りつぶしの色がないセルは白で描画されます。

**透明度を適用しないワークシート イメージ**

![todo:画像_代替_文章](create-transparent-image-of-excel-worksheet_1.png)

一方、次のワークシート イメージでは、透明度が適用されています。塗りつぶしの色がないセルは透明です。

**透明度適用後のワークシート イメージ**

![todo:画像_代替_文章](create-transparent-image-of-excel-worksheet_2.png)

次のサンプル コードを使用して、Excel ワークシートの透明なイメージを生成できます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
