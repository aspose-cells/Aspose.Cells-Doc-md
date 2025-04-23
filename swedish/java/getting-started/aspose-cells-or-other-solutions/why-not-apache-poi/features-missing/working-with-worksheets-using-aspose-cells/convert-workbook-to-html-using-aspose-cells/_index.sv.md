---
title: Konvertera arbetsbok till HTML med Aspose.Cells
type: docs
weight: 20
url: /sv/java/convert-workbook-to-html-using-aspose-cells/
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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ned provkoden**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

För mer information, besök [Konvertera Excel-filer till HTML](/cells/sv/java/konvertera-arbetsbok-till-olika-format/).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
