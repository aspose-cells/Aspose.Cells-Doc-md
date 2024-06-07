---
title: 单元格中的新行
type: docs
weight: 30
url: /zh/net/new-line-in-cells/
---

## **Aspose.Cells - 单元格中的新行**
为确保单元格中的文本可读，可以应用显式换行和文本换行。文本换行将一个单行变成多行，而显式换行可将换行符插入到您想要的位置。

要在单元格中换行，请使用 Aspose.Cells.Style.IsTextWrapped 属性。

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

Worksheet sheet = workbook.Worksheets[0];

sheet.Cells[2,2].Value = "Use \n with word wrap on to create a new line";

//Get Cell's Style

Style style = sheet.Cells[2, 2].GetStyle();

//Set Text Wrap property to true

style.IsTextWrapped = true;

//Set Cell's Style

sheet.Cells[2, 2].SetStyle(style);

workbook.Save("test.xlsx");

{{< /highlight >}}
## **NPOI - HSSF XSSF - 单元格中的换行**
CellStyle.setWrapText应设置为true以自动换行。

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet = workbook.CreateSheet("Sheet1");

IRow row = sheet.CreateRow(2);

ICell cell = row.CreateCell(2);

cell.SetCellValue("Use \n with word wrap on to create a new line");

//to enable newlines you need set a cell styles with wrap=true

ICellStyle cs = workbook.CreateCellStyle();

cs.WrapText = true;

cell.CellStyle = cs;

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
从以下任一社交编码站点下载 **New Line in Cells**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

了解更多详情，请访问 [换行和文本包装](/cells/zh/net/line-breaks-and-text-wrapping/)。

{{% /alert %}}
