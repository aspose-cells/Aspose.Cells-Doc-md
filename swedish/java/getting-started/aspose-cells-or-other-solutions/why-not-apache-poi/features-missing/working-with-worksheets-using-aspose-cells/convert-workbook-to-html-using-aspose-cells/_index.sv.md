---
title: Konvertera arbetsbok till HTML med Aspose.Cells
type: docs
weight: 20
url: /sv/java/convert-workbook-to-html-using-aspose-cells/
---
## **Aspose.Cells - Konvertera arbetsbok till HTML**
 API:erna Aspose.Cells ger stöd för export av kalkylblad till formatet HTML. För detta ändamål,**Aspose.Cells** använder**HtmlSaveOptions** klass som tillåter utvecklare att kontrollera flera aspekter av utdata HTML.

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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Ladda ner provkod**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

 För mer information, besök[Konvertera Excel-filer till HTML](/cells/sv/java/converting-workbook-to-different-formats/).

{{% /alert %}}
