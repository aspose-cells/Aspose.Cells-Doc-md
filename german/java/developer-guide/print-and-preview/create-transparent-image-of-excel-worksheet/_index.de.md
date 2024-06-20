---
title: Create Transparent Image of Excel Worksheet
type: docs
weight: 80
url: /de/java/create-transparent-image-of-excel-worksheet/
---

{{% alert color="primary" %}}

Manchmal müssen Sie das Bild Ihres Arbeitsblatts als transparentes Bild generieren. Sie möchten die Transparenz auf alle Zellen anwenden, die keine Füllfarben haben. Aspose.Cells bietet die Eigenschaft [**ImageOrPrintOptions.setTransparent()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent) zur Anwendung von Transparenz auf das Arbeitsblattbild. Wenn diese Eigenschaft **false** ist, werden Zellen ohne Füllfarben mit weißer Farbe gezeichnet, und wenn sie **true** ist, werden Zellen ohne Füllfarben transparent gezeichnet.

{{% /alert %}}

In der folgenden Arbeitsblattansicht wurde keine Transparenz angewendet. Die Zellen ohne Füllfarben sind weiß gezeichnet.

**Arbeitsblattbild ohne Anwendung von Transparenz**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)

Während in der folgenden Arbeitsblattansicht Transparenz angewendet wurde. Die Zellen ohne Füllfarben sind transparent.

**Arbeitsblattbild nach Anwendung der Transparenz**

![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)

Sie können den folgenden Beispielcode verwenden, um ein transparentes Bild Ihres Excel-Arbeitsblatts zu generieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-CreateTransparentImage-1.java" >}}
