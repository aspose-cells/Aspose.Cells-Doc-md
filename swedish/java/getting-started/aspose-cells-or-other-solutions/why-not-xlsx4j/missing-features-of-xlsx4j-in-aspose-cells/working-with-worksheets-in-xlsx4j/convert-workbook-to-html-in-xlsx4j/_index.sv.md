---
title: Konvertera arbetsbok till HTML i xlsx4j
type: docs
weight: 10
url: /sv/java/convert-workbook-to-html-in-xlsx4j/
---
## **Aspose.Cells - Konvertera arbetsbok till HTML**
 API:erna Aspose.Cells ger stöd för export av kalkylblad till HTML-format. För det här syftet,**Aspose.Cells** använder**HtmlSaveOptions** klass som tillåter utvecklare att kontrollera flera aspekter av utdata-HTML.

**Java**

{{< highlight "java" >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Ladda ner Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **Ladda ner exempelkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 För mer information, besök[Konvertera Excel-filer till HTML](/cells/sv/java/converting-workbook-to-different-formats/).

{{% /alert %}}
