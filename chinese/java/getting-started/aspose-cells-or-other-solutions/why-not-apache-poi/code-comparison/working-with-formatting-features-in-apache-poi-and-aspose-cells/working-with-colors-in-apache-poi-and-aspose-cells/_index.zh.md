---
title: 在Apache POI和Aspose.Cells中使用颜色
type: docs
weight: 20
url: /zh/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 使用颜色**
Aspose.Cells提供了一个类，[Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)，代表一个Microsoft Excel文件。Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由[Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)类表示。Worksheet类提供了一个Cells集合。Cells集合中的每个项代表[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)类的对象。

Aspose.Cells在Cell类中提供了setStyle方法，用于设置单元格的格式。此外，Style类的Style对象可用于配置字体设置。

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
## **Apache POI SS - HSSF XSSF - 使用颜色**
CellStyle类可用于设置背景和填充模式设置。

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

更多详情，请访问[颜色和背景模式](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns)。

{{% /alert %}}
