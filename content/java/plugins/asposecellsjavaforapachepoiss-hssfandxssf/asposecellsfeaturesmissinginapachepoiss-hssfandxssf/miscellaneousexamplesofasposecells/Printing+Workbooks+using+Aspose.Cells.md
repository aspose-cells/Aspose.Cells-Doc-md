+++
title = "Printing Workbooks using Aspose.Cells" 
description = "" 
weight = 20652 
+++

Aspose.Cells for Java : Printing Workbooks using Aspose.Cells  

# Aspose.Cells for Java : Printing Workbooks using Aspose.Cells


## Aspose.Cells - Printing Workbooks

After you finish creating your spreadsheet, you will probably want to print a hard copy of the sheet for your need. When you are printing, MS Excel assumes you want to print the entire worksheet area unless you specify your selection.

Printing Worksheet

**Java**

{{< code lang="java" >}}
//Instantiate a new workbook
Workbook book = new Workbook(dataDir + "AsposeDataInput.xls");

//Create an object for ImageOptions
ImageOrPrintOptions  imgOptions = new ImageOrPrintOptions ();

//Get the first worksheet
Worksheet sheet = book.getWorksheets().get(0);

//Create a SheetRender object with respect to your desired sheet
SheetRender sr = new SheetRender(sheet, imgOptions);

//Print the worksheet
sr.toPrinter("Samsung ML-1520 Series");
{{< /code >}}

Printing Workbook

**Java**

{{< code lang="java" >}}
//Create a WorkbookRender object with respect to your workbook
WorkbookRender wr = new WorkbookRender(book, imgOptions);

//Print the workbook
wr.toPrinter("Samsung ML-1520 Series");
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintWorkbook.java)

For more details, visit [Printing Workbooks](http://docs.aspose.com:8082/docs/display/cellsjava/Printing+Workbooks).

