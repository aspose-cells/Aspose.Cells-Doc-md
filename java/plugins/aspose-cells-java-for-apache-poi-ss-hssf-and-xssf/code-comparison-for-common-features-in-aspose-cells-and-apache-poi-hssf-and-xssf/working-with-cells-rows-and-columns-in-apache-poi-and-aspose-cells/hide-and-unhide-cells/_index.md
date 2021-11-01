---
title: Hide and Unhide Cells
type: docs
weight: 30
url: /java/hide-and-unhide-cells/
---

## **Aspose.Cells - Hide and Unhide Rows and Columns**
Aspose.Cells provides a class, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), that represents a Microsoft Excel file. The Workbook class contains aWorksheetCollection that allows access to each worksheet in the Excel file. A worksheet is represented by the[Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) class. The Worksheet class provides a Cells collection that represents all cells in the worksheet. The Cells collection provides several methods for managing rows or columns in a worksheet. 

**Java**

{{< highlight java >}}

 Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

Cells cells = worksheet.getCells();

cells.hideRow(2); //Hiding the 3rd row of the worksheet

cells.hideColumn(1); //Hiding the 2nd column of the worksheet

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Hide / Unhide Cells**
To Hide a row or column, Apache POI SS provide Row.setZeroHeight(boolean) method.

**Java**

{{< highlight java >}}

 InputStream inStream = new FileInputStream("workbook.xls");

Workbook workbook = WorkbookFactory.create(inStream);

Sheet sheet = workbook.createSheet();

Row row = sheet.createRow(0);

row.setZeroHeight(true);

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/hideunhidecells)

{{% alert color="primary" %}} 

For more details, visit [Hiding and Showing Rows and Columns](http://docs.aspose.com:8082/docs/display/cellsjava/Hiding+and+Showing+Rows+and+Columns).

{{% /alert %}}
