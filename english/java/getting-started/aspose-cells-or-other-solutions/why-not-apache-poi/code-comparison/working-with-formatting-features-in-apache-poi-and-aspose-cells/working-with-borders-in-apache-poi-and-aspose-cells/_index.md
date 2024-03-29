---
title: Working with Borders in Apache POI and Aspose.Cells
type: docs
weight: 10
url: /java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Working with Borders**
Aspose.Cells provides a class, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) that represents a Microsoft Excel file. The Workbook class contains a WorksheetCollection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) class. The Worksheet class provides a Cellscollection. Each item in the Cells collection represents an object of the [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) class.

Aspose.Cells provides the setStyle method in the [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) class used to set a cell's formatting style. Also, the Style object of the [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) class is used and provides properties for configuring font settings.

**Java**

{{< highlight java >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Working with Borders**
CellStyle class provides features to set borders settings using Apache POI SS - HSSF and XSSF.

**Java**

{{< highlight java >}}

 //Setting the line of the top border

style.setBorder(BorderType.TOP_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the bottom border

style.setBorder(BorderType.BOTTOM_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the left border

style.setBorder(BorderType.LEFT_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the right border

style.setBorder(BorderType.RIGHT_BORDER,CellBorderType.THICK,Color.getBlack());

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

For more details, visit [Adding Borders to Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
