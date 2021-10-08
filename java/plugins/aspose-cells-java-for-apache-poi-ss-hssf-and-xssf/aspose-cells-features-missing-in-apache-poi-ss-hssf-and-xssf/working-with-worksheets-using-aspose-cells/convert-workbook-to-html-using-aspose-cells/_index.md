---
title: Convert Workbook to HTML using Aspose.Cells
type: docs
weight: 20
url: /java/convert-workbook-to-html-using-aspose-cells/
---

## **Aspose.Cells - Convert Workbook to HTML**
The Aspose.Cells APIs provides support for exporting spreadsheets to HTML format. For this purpose, **Aspose.Cells** uses the **HtmlSaveOptions** class which allows developers to control several aspects of the output HTML.

**Java**

{{< highlight java >}}

 //Specify the HTML Saving Options

HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file

Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file

book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);

{{< /highlight >}}
## **Download Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://archive.codeplex.com/?p=asposecellsjavaapachepoi)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeConvertToHTML.java)

{{% alert color="primary" %}} 

For more details, visit [Converting Excel Files to HTML](http://www.aspose.com/docs/display/cellsjava/Converting+Excel+Files+to+HTML).

{{% /alert %}}
