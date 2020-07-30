---
title : "Convert Workbook to HTML in xlsx4j" 
description : "" 
weight : 20681 
toc : false
type: docs
url: /java/plugins/xlsx4j/missingfeaturesinapscls/worksheets/convert+workbook+to+html+in+xlsx4j/
---

# Aspose.Cells for Java : Convert Workbook to HTML in xlsx4j


## Aspose.Cells - Convert Workbook to HTML

The Aspose.Cells APIs provides support for exporting spreadsheets to HTML format. For this purpose, **Aspose.Cells** uses the **HtmlSaveOptions** class which allows developers to control several aspects of the output HTML.

**Java**

{{< code lang="java" >}}
//Specify the HTML Saving Options
HtmlSaveOptions save = new HtmlSaveOptions(SaveFormat.HTML);

//Instantiate a workbook and open the template XLSX file
Workbook book = new Workbook(dataDir + "book1.xls");

//Save the HTML file
book.save(dataDir + "AsposeHTMLSpreadsheet.html", save);
{{< /code >}}

## Download Running Code

*   [CodePlex](http://asposecellsjavaxlsx4j.codeplex.com/releases/view/618923)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaxlsx4j.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose.Cells-for-Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/converttohtml/AsposeConvertToHTML.java)

For more details, visit [Converting Excel Files to HTML](http://www.aspose.com/docs/display/cellsjava/Converting+Excel+Files+to+HTML).

