---
title: Excelワークシートの透過画像を作成
type: docs
weight: 170
url: /ja/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

場合によっては、ワークシートの画像を透明な画像として生成する必要があります。塗りつぶしの色がないすべてのセルに透明度を適用します。 Aspose.Cells は[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)ワークシート イメージに透明度を適用するプロパティ。このプロパティが**間違い**の場合、塗りつぶしの色のないセルは白色で描画されます。**真実**、塗りつぶしの色のないセルは透明に描画されます。

{{% /alert %}} 

次のワークシート イメージでは、透明度が適用されていません。塗りつぶしの色がないセルは白で描画されます。

|**透明度なしの出力: セルの背景は白です**|
|:- |
|![todo:画像_代替_文章](create-transparent-image-of-excel-worksheet_1.png)|

一方、次のワークシート イメージでは、透明度が適用されています。塗りつぶしの色がないセルは透明です。

|**透明度を有効にして出力**|
|:- |
|![todo:画像_代替_文章](create-transparent-image-of-excel-worksheet_2.png)|

次のサンプル コードは、Excel ワークシートから透明なイメージを生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
