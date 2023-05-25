---
title: Excelワークシートの透明画像を作成
type: docs
weight: 170
url: /ja/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

場合によっては、ワークシートの画像を透明な画像として生成する必要があります。塗りつぶし色のないすべてのセルに透明度を適用したいとします。 Aspose.Cells は、[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)ワークシート画像に透明度を適用するプロパティ。このプロパティが *false** の場合、塗りつぶし色のないセルは白色で描画され、*true** の場合、塗りつぶし色のないセルは透明で描画されます。

{{% /alert %}} 

次のワークシート画像では、透明度は適用されていません。塗りつぶし色のないセルは白く描画されます。

|**透明度なしで出力: セルの背景は白になります**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

次のワークシート画像では、透明度が適用されています。塗りつぶし色のないセルは透明です。

|**透明度を有効にして出力する**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

次のサンプル コードは、Excel ワークシートから透明な画像を生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
