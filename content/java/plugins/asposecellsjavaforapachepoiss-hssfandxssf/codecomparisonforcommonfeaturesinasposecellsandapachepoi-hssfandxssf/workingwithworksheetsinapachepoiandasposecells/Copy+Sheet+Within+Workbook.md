+++
title = "Copy Sheet Within Workbook" 
description = "" 
weight = 20596 
+++

Aspose.Cells for Java : Copy Sheet Within Workbook  

# Aspose.Cells for Java : Copy Sheet Within Workbook


## Microsoft Excel - Moving or Copying Sheets within Workbook

Following are the steps involved for copying and moving worksheets within or between workbooks.

1.  To move or copy sheets within or between workbooks, open the workbook that will receive the sheets.
2.  Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.
3.  On the **Edit** menu, click **Move or Copy Sheet**.
4.  In the To book box, click the workbook to receive the sheets.
5.  To move or copy the selected sheets to a new workbook, click **new book**.
6.  In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.
7.  To copy the sheets instead of moving them, select the **Create a copy** check box.

## Aspose.Cells - Copy Sheet Within Workbook

Aspose.Cells provides an overloaded method, `WorksheetCollection.addCopy()`, that is used to add a worksheet to the collection and copy data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet.

The following example shows how to copy an existing worksheet within a workbook.

Copy sheets using Aspose.Cells

**Java**

{{< code lang="java" >}}
//Create a new Workbook by excel file path
Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.
WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.
sheets.addCopy("Sheet1");
{{< /code >}}

## Apache POI SS - Copy Sheet Within Workbook

`Workbook.cloneSheet()` is used to to copy sheets with workbook.

Copy sheets using Apache POI SS

**Java**

{{< code lang="java" >}}
Workbook wb = new HSSFWorkbook();
wb.createSheet("new sheet");
wb.createSheet("second sheet");
Sheet cloneSheet = wb.cloneSheet(0);
{{< /code >}}

## Download Running Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## Download Sample Code

*   [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook/)
*   [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

For more details, visit [Copying and Moving Worksheets](http://docs.aspose.com:8082/docs/display/cellsjava/Copying+and+Moving+Worksheets).

