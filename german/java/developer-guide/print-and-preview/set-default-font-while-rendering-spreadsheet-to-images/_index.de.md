---
title: Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen
type: docs
weight: 840
url: /de/java/set-default-font-while-rendering-spreadsheet-to-images/
---

{{% alert color="primary" %}} 

Bitte verwenden Sie die Eigenschaft [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont), um den Standardfont beim Rendern von Tabellenkalkulationen in Bilder festzulegen. Diese Eigenschaft ist nur wirksam, wenn der Standardfont der Arbeitsmappe Ihre Zeichen nicht rendern konnte. Der mit der Eigenschaft [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) angegebene Standardfont wird für alle Zellen verwendet, die ungültige oder nicht vorhandene Schriften haben.

{{% /alert %}} 
## **Standardfont beim Rendern von Tabellenkalkulationen in Bilder festlegen**
Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt etwas Text in Zelle A4 des ersten Arbeitsblatts hinzu und setzt seine Schriftart auf ungültige oder nicht vorhandene Schriftart. Dann werden zwei Bilder des Arbeitsblatts erstellt. Das erste Bild wird erstellt, indem die Eigenschaft [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) auf *Courier New* gesetzt wird, und das zweite Bild wird erstellt, indem die Eigenschaft [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) auf *Times New Roman* gesetzt wird.

Dies ist das Ausgabebild, nachdem die Eigenschaft [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) auf *Courier New* gesetzt wurde.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

Dies ist das Ausgabebild, nachdem die Eigenschaft [ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) auf *Times New Roman* gesetzt wurde.

![todo:image_alt_text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
{{< app/cells/assistant language="java" >}}
