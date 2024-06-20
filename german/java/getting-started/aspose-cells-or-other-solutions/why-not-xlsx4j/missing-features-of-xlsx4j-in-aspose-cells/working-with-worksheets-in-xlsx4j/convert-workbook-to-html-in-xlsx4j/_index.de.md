---
title: Arbeitsmappe in HTML konvertieren in xlsx4j
type: docs
weight: 10
url: /de/java/convert-workbook-to-html-in-xlsx4j/
---

## **Aspose.Cells - Arbeitsmappe in HTML konvertieren**
Die Aspose.Cells APIs bieten Unterstützung für die Exportierung von Tabellenkalkulationen im HTML-Format. Hierfür verwendet **Aspose.Cells** die Klasse **HtmlSaveOptions**, mit der Entwickler mehrere Aspekte des Ausgabe-HTML steuern können.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Laufenden Code herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

Besuchen Sie für weitere Details [Excel-Dateien in HTML konvertieren](/cells/de/java/converting-workbook-to-different-formats/).

{{% /alert %}}
