---
title: Working with Colors in Apache POI and Aspose.Cells
type: docs
weight: 20
url: /java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Working with Colors**
Aspose.Cells provides a class, [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook), that represents a Microsoft Excel file. The Workbook class contains a WorksheetCollection that allows access to each worksheet in the Excel file. A worksheet is represented by the [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) class. The Worksheet class provides a Cellscollection. Each item in the Cells collection represents an object of the [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) class.

Aspose.Cells provides the setStyle method in the Cell class that is used to set a cell's formatting. Also, the Style object of the Style class can be used to configure font settings.

**Java**

{{< highlight java >}}

 //Accessing cell from the worksheet

Cell cell = cells.get("B2");

Style style = cell.getStyle();

//Setting the foreground color to yellow

style.setBackgroundColor(Color.getYellow());

//Setting the background pattern to vertical stripe

style.setPattern(BackgroundType.VERTICAL_STRIPE);

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

// === Setting Foreground ===

//Adding custom color to the palette at 55th index

Color color = Color.fromArgb(212,213,0);

workbook.changePalette(color,55);

//Accessing cell from the worksheet

cell = cells.get("B3");

//Adding some value to the cell

cell.setValue("Hello Aspose!");

//Setting the custom color to the font

style = cell.getStyle();

Font font = style.getFont();

font.setColor(color);

cell.setStyle(style);


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Working with Colors**
CellStyle class is available to set background and fillpattern settings.

**Java**

{{< highlight java >}}

 // Aqua background

CellStyle style = wb.createCellStyle();

style.setFillBackgroundColor(IndexedColors.AQUA.getIndex());

style.setFillPattern(CellStyle.BIG_SPOTS);

Cell cell = row.createCell((short) 1);

cell.setCellValue("X");

cell.setCellStyle(style);

// Orange "foreground", foreground being the fill foreground not the font color.

style = wb.createCellStyle();

style.setFillForegroundColor(IndexedColors.ORANGE.getIndex());

style.setFillPattern(CellStyle.SOLID_FOREGROUND);

cell = row.createCell((short) 2);

cell.setCellValue("X");

cell.setCellStyle(style);

{{< /highlight >}}
## **Download Running Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/releases/view/618615)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [CodePlex](https://asposecellsjavaapachepoi.codeplex.com/SourceControl/latest#src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors/)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

For more details, visit [Colors and Background Patterns](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}
