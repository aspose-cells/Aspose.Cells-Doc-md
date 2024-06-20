---
title: 在Apache POI和Aspose.Cells中使用边框
type: docs
weight: 10
url: /zh/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 使用边框**
Aspose.Cells提供一个代表Microsoft Excel文件的类[Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)，Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供一个Cells集合，Cells集合中的每个项表示Cell类的对象。

Aspose.Cells提供了Cell类中的setStyle方法，用于设置单元格的格式样式。同时，Style类的Style对象用于配置字体设置。

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
## **Apache POI SS - HSSF XSSF - 使用边框**
CellStyle类提供了使用Apache POI SS - HSSF和XSSF设置边框设置的功能。

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[向单元格添加边框](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells)。

{{% /alert %}}
