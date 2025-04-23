---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /de/python-net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Manchmal müssen Sie das Bild Ihres Worksheets als transparentes Bild generieren. Sie möchten Transparenz auf alle Zellen anwenden, die keine Füllfarben haben. Aspose.Cells für Python via .NET bietet die [**ImageOrPrintOptions.transparent**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/transparent)-Eigenschaft, um die Transparenz auf das Arbeitsblattbild anzuwenden. Wenn diese Eigenschaft **false** ist, werden Zellen ohne Füllfarben mit Weiß gezeichnet; ist sie **true**, werden Zellen ohne Füllfarben transparent dargestellt.

{{% /alert %}} 

In der folgenden Arbeitsblattansicht wurde keine Transparenz angewendet. Die Zellen ohne Füllfarben sind weiß gezeichnet.

|**Ausgabe ohne Transparenz: Der Zellenhintergrund ist weiß**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Während in der folgenden Arbeitsblattansicht Transparenz angewendet wurde. Die Zellen ohne Füllfarben sind transparent.

|**Ausgabe mit aktivierter Transparenz**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Der folgende Beispielscode generiert ein transparentes Bild aus einem Excel-Arbeitsblatt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-CreateTransparentImage-1.py" >}}

