---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 170
url: /de/net/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Manchmal müssen Sie das Bild Ihres Arbeitsblatts als transparentes Bild generieren. Sie möchten Transparenz auf alle Zellen anwenden, die keine Füllfarben haben. Aspose.Cells bietet die [**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent)-Eigenschaft, um Transparenz auf das Arbeitsblattbild anzuwenden. Wenn diese Eigenschaft **false** ist, werden Zellen ohne Füllfarben mit weißer Farbe gezeichnet, und wenn sie **true** ist, werden Zellen ohne Füllfarben transparent gezeichnet.

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

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
