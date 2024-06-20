---
title: Konvertera arbetsbok till HTML i xlsx4j
type: docs
weight: 10
url: /sv/java/convert-workbook-to-html-in-xlsx4j/
---

## **Aspose.Cells - Konvertera arbetsbok till HTML**
Aspose.Cells API:er ger stöd för att exportera kalkylblad till HTML-format. För detta ändamål använder **Aspose.Cells** **HtmlSaveOptions**-klassen vilket låter utvecklare kontrollera flera aspekter av utdata-HTML.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Ladda ned körbar kod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

För mer information, besök [Konvertera Excel-filer till HTML](/cells/sv/java/konvertera-arbetsbok-till-olika-format/).

{{% /alert %}}
