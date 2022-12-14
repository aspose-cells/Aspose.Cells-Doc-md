---
title: Erstellen Sie ein transparentes Bild des Excel-Arbeitsblatts
type: docs
weight: 80
url: /de/java/create-transparent-image-of-excel-worksheet/
---
{{% alert color="primary" %}}

 Manchmal müssen Sie das Bild Ihres Arbeitsblatts als transparentes Bild generieren. Sie möchten Transparenz auf alle Zellen anwenden, die keine Füllfarben haben. Aspose.Cells bietet die[**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) -Eigenschaft, um Transparenz auf das Arbeitsblattbild anzuwenden. Wenn diese Eigenschaft ist**FALSCH** , dann werden Zellen ohne Füllfarben mit weißer Farbe gezeichnet und wenn ja**Stimmt**, Zellen ohne Füllfarben werden transparent gezeichnet.

{{% /alert %}}

Im folgenden Arbeitsblattbild wurde keine Transparenz angewendet. Die Zellen ohne Füllfarben werden weiß gezeichnet.

**Arbeitsblattbild ohne Anwenden von Transparenz**

![todo: Bild_alt_Text](create-transparent-image-of-excel-worksheet_1.png)

Während im folgenden Arbeitsblattbild Transparenz angewendet wurde. Die Zellen ohne Füllfarben sind transparent.

**Arbeitsblattbild nach dem Anwenden von Transparenz**

![todo: Bild_alt_Text](create-transparent-image-of-excel-worksheet_2.png)

Sie können den folgenden Beispielcode verwenden, um ein transparentes Bild Ihres Excel-Arbeitsblatts zu generieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
