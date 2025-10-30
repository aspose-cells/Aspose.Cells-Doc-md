---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /ja/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

時には、ワークシートの画像を透過画像として生成する必要があります。塗りつぶし色のないすべてのセルに透過性を適用したい場合、Aspose.Cells for Python via .NETは[**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent)プロパティを提供しており、これを使用してワークシート画像に透過性を適用できます。このプロパティが**false**の場合、塗りつぶし色のないセルは白色で描画され、**true**の場合は透明に描画されます。

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

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
