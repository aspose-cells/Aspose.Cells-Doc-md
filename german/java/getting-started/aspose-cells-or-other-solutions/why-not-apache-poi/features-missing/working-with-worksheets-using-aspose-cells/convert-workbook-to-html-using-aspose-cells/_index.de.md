---
title: Arbeitsmappe in HTML konvertieren mit Aspose.Cells
type: docs
weight: 20
url: /de/java/convert-workbook-to-html-using-aspose-cells/
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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

Besuchen Sie für weitere Details [Excel-Dateien in HTML konvertieren](/cells/de/java/converting-workbook-to-different-formats/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
