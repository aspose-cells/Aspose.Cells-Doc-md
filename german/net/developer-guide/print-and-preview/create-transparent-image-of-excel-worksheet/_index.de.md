---
title: Erstellen Sie ein transparentes Bild eines Excel-Arbeitsblatts
type: docs
weight: 170
url: /de/net/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

Manchmal müssen Sie das Bild Ihres Arbeitsblatts als transparentes Bild generieren. Sie möchten Transparenz auf alle Zellen anwenden, die keine Füllfarben haben. Aspose.Cells bietet die[**ImageOrPrintOptions.Transparent**](https://reference.aspose.com/cells/net/aspose.cells.rendering/imageorprintoptions/properties/transparent) Eigenschaft, um Transparenz auf das Arbeitsblattbild anzuwenden. Wenn diese Eigenschaft *falsch** ist, werden Zellen ohne Füllfarben mit weißer Farbe gezeichnet, und wenn sie *wahr** ist, werden Zellen ohne Füllfarben transparent gezeichnet.

{{% /alert %}} 

Im folgenden Arbeitsblattbild wurde keine Transparenz angewendet. Die Zellen ohne Füllfarben werden weiß gezeichnet.

|**Ausgabe ohne Transparenz: Der Zellenhintergrund ist weiß**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|

Während im folgenden Arbeitsblattbild Transparenz angewendet wurde. Die Zellen ohne Füllfarben sind transparent.

|**Ausgabe mit aktivierter Transparenz**|
| :- |
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|

Der folgende Beispielcode generiert ein transparentes Bild aus einem Excel-Arbeitsblatt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreateTransparentImage-1.cs" >}}
