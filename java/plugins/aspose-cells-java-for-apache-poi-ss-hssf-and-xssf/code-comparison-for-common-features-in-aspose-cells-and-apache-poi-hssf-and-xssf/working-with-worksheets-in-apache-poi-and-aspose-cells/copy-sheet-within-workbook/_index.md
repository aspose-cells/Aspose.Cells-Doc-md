---
title: Copy Sheet Within Workbook
type: docs
weight: 40
url: /java/copy-sheet-within-workbook/
---

## **Microsoft Excel - Moving or Copying Sheets within Workbook**
Following are the steps involved for copying and moving worksheets within or between workbooks.

1. To move or copy sheets within or between workbooks, open the workbook that will receive the sheets.
1. Switch to the workbook that contains the sheets you want to move or copy, and then select the sheets.
1. On the **Edit** menu, click **Move or Copy Sheet**.
1. In the To book box, click the workbook to receive the sheets.
1. To move or copy the selected sheets to a new workbook, click **new book**.
1. In the **Before sheet** box, click the sheet before which you want to insert the moved or copied sheets.
1. To copy the sheets instead of moving them, select the **Create a copy** check box.
## **Aspose.Cells - Copy Sheet Within Workbook**
{{% alert color="primary" %}} 

Aspose.Cells provides an overloaded method, WorksheetCollection.addCopy(), that is used to add a worksheet to the collection and copy data from an existing worksheet. One version of the method takes the index of the source worksheet as a parameter. The other version takes the name of the source worksheet.

The following example shows how to copy an existing worksheet within a workbook.

{{% /alert %}} 

Copy sheets using Aspose.Cells

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - Copy Sheet Within Workbook**
{{% alert color="primary" %}} 

Workbook.cloneSheet() is used to to copy sheets with workbook.

{{% /alert %}} 

Copy sheets using Apache POI SS

**Java**

{{< highlight java >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

For more details, visit [Copying and Moving Worksheets](http://docs.aspose.com:8082/docs/display/cellsjava/Copying+and+Moving+Worksheets).

{{% /alert %}}
