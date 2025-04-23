---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ja/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

時々、ワークシートの画像を透明なイメージとして生成する必要があります。埋められていないセルに透明性を適用したい場合があります。Aspose.Cellsは透明性をワークシートイメージに適用するための[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)プロパティを提供しています。このプロパティが **false** の場合、埋められていないセルは白色で描画され、 **true** の場合、埋められていないセルは透明に描画されます。

{{% /alert %}} 

以下のワークシートイメージでは、透明性が適用されていません。埋められていないセルは白色で描画されます。

|**透明度なしの出力: セルの背景は白です**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

以下のワークシート画像では、透明度が適用されました。塗りつぶしのないセルは透明です。

|**透明度を有効にした出力**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

次のサンプルコードは、Excelワークシートから透明な画像を生成します。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
