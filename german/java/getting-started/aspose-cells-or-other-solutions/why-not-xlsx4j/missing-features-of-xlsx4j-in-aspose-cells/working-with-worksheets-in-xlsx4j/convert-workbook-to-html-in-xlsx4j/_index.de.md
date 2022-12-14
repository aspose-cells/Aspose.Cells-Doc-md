---
title: Konvertieren Sie die Arbeitsmappe in xlsx4j in HTML
type: docs
weight: 10
url: /de/java/convert-workbook-to-html-in-xlsx4j/
---
## **Aspose.Cells – Arbeitsmappe in HTML konvertieren**
 Die Aspose.Cells-APIs bieten Unterstützung für den Export von Tabellenkalkulationen in das HTML-Format. Für diesen Zweck,**Aspose.Cells** nutzt die**HtmlSaveOptions** -Klasse, mit der Entwickler mehrere Aspekte des Ausgabe-HTML steuern können.

**Java**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Laufcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Konvertieren von Excel-Dateien in HTML](/cells/de/java/converting-workbook-to-different-formats/).

{{% /alert %}}
