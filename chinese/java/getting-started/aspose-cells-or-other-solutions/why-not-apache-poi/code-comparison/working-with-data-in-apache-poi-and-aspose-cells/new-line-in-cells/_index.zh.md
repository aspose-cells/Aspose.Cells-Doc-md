---
title: 单元格中的新行
type: docs
weight: 30
url: /zh/java/new-line-in-cells/
---

## **Aspose.Cells - 单元格中的新行**
为确保单元格中的文本可读，可以应用显式换行和文本换行。文本换行将一个单行变成多行，而显式换行可将换行符插入到您想要的位置。

要在单元格中自动换行，请使用Style.setTextWrapped方法。

**Java**

{{< highlight java >}}

 // Add Text to the First Cell with Explicit Line Breaks

cell.get(0, 0).setValue("I am using \nthe latest version of \nAspose.Cells \nto test this functionality");

//Get Cell's Style

Style style = cell.get(0, 0).getStyle();

//Set Text Wrap property to true

style.setTextWrapped(true);

//Set Cell's Style

cell.get(0, 0).setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 单元格中的新行**
CellStyle.setWrapText应设置为true以自动换行。

**Java**

{{< highlight java >}}

 Row row = sheet.createRow(2);

Cell cell = row.createCell(2);

cell.setCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

CellStyle cs = wb.createCellStyle();

cs.setWrapText(true);

cell.setCellStyle(cs);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/newlineincells)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[换行和文本自动换行](/java/line-breaks-and-text-wrapping)。

{{% /alert %}}
