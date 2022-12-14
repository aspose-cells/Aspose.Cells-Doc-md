---
title: Legen Sie die Standardschriftart fest, während Sie die Tabelle in Bilder rendern
type: docs
weight: 840
url: /de/java/set-default-font-while-rendering-spreadsheet-to-images/
---
{{% alert color="primary" %}} 

 Bitte verwenden Sie die[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) -Eigenschaft zum Festlegen der Standardschriftart beim Rendern von Tabellenkalkulationen in Bilder. Diese Eigenschaft ist nur wirksam, wenn die Standardschriftart der Arbeitsmappe Ihre Zeichen nicht darstellen konnte. Die mit angegebene Standardschriftart[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) -Eigenschaft wird für alle Zellen verwendet, die ungültige oder nicht vorhandene Schriftarten haben.

{{% /alert %}} 
## **Legen Sie die Standardschriftart fest, während Sie die Tabelle in Bilder rendern**
Der folgende Beispielcode erstellt eine Arbeitsmappe, fügt Text in Zelle A4 des ersten Arbeitsblatts hinzu und legt seine Schriftart auf eine ungültige oder nicht vorhandene Schriftart fest. Dann nimmt es zwei Bilder des Arbeitsblatts. Das erste Bild wird aufgenommen, indem die eingestellt wird[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) Eigentum zu*Kurier Neu* und das zweite Bild wird durch Einstellen von aufgenommen[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) Eigentum zu*Times New Roman*.

 Dies ist das Ausgabebild nach der Einstellung von[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) Eigentum zu*Kurier Neu*.

![todo: Bild_alt_Text](set-default-font-while-rendering-spreadsheet-to-images_1.png)

 Dies ist das Ausgabebild nach der Einstellung von[ImageOrPrintOptions.DefaultFont](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#DefaultFont) Eigentum zu*Times New Roman*.

![todo: Bild_alt_Text](set-default-font-while-rendering-spreadsheet-to-images_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-SetDefaultFontWhileRenderingSpreadsheetToImages-.java" >}}
