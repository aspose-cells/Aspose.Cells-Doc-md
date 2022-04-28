---
title: Freeze Panes in Apache POI and Aspose.Cells
type: docs
weight: 80
url: /java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Freeze Panes**
Aspose.Cells provides a class, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) that represents a Microsoft Excel file. The Workbook class contains a WorksheetCollection that allows access to each worksheet in an Excel file.

A worksheet is represented by the [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) class. The Worksheet class provides a wide range of properties and methods for managing worksheets. To configure freeze panes, call the Worksheet class' freezePanesmethod. THe FreezePanes method takes the following parameters:

- **Row**, the row index of the cell that the freeze will start from.
- **Column**, the column index of the cell that the freeze will start from.
- **Frozen rows**, the number of visible rows in the top pane.
- **Frozen columns**, the number of visible columns in the left pane

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Freeze Panes**
sheet.createFreezePane is available to achieve FreezePane functionality while using Apache POI SS - HSSF and XSSF

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

For more details, visit [Freeze Panes](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
