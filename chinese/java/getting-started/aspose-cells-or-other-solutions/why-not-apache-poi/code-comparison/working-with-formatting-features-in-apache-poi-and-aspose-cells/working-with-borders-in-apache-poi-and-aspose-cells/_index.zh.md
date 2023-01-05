---
title: 在 Apache POI 和 Aspose.Cells 中使用边框
type: docs
weight: 10
url: /zh/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - 使用边框**
Aspose.Cells提供了一个类，[工作簿](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)表示 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。工作表由[工作表](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)班级。 Worksheet 类提供了一个 Cellscollection。 Cells 集合中的每个项目代表[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)班级。

Aspose.Cells 中提供了setStyle方法[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)用于设置单元格格式样式的类。此外，样式对象的[风格](http://docs.aspose.com:8082/docs/display/cellsjava/Style)使用类并提供用于配置字体设置的属性。

**Java**

{{< highlight "java" >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 使用边界**
CellStyle 类提供使用 Apache POI SS - HSSF 和 XSSF 设置边框的功能。

**Java**

{{< highlight "java" >}}

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

欲了解更多详情，请访问[为 Cells 添加边框](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
