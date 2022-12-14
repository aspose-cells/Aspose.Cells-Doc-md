---
title: 在 Apache POI 和 Aspose.Cells 中使用字体
type: docs
weight: 30
url: /zh/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - 使用字体**
Aspose.Cells提供了一个类，[工作簿](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)表示 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。工作表由[工作表](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)班级。 Worksheet 类提供了一个 Cells 集合。 Cells 集合中的每个项目代表[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)班级。

**Java**

{{< highlight "java" >}}

 //Adding some value to cell

Cell cell = cells.get("A1");

cell.setValue("This is Aspose test of fonts!");

//Setting the font name to "Courier New"

Style style = cell.getStyle();

Font font = style.getFont();

font.setName("Courier New");

font.setSize(24);

font.setBold(true);

font.setUnderline(FontUnderlineType.SINGLE);

font.setColor(Color.getBlue());

font.setStrikeout(true);

//font.setSubscript(true);

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 使用字体**
Apache POI SS 提供字体类来设置各种字体设置。

**Java**

{{< highlight "java" >}}

 // Create a new font and alter it.

Font font = wb.createFont();

font.setFontHeightInPoints((short)24);

font.setFontName("Courier New");

font.setItalic(true);

font.setStrikeout(true);

// Fonts are set into a style so create a new one to use.

CellStyle style = wb.createCellStyle();

style.setFont(font);

// Create a cell and put a value in it.

Cell cell = row.createCell(1);

cell.setCellValue("This is a test of fonts");

cell.setCellStyle(style);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/fonts)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[处理字体设置](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
