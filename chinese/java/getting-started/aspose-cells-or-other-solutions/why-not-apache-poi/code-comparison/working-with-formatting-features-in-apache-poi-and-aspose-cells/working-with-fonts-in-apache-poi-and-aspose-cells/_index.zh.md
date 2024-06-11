---
title: 在Apache POI和Aspose.Cells中使用字体
type: docs
weight: 30
url: /zh/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 使用字体**
Aspose.Cells提供了一个表示Microsoft Excel文件的类[Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)。Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供了Cells集合。Cells集合中的每个项目表示Cell类的对象。

Java

{{< highlight java >}}

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
Apache POI SS提供Font类来设置各种字体设置。

Java

{{< highlight java >}}

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

有关更多详细信息，请访问[处理字体设置](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings)。

{{% /alert %}}
