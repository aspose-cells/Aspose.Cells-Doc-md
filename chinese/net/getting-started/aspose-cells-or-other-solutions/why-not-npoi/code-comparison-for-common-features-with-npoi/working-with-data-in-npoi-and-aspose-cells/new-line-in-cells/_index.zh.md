---
title: Cells 中的新行
type: docs
weight: 30
url: /zh/net/new-line-in-cells/
---
## **Aspose.Cells - Cells 中的新线**
为确保可以读取单元格中的文本，可以应用明确的换行符和文本换行。文本换行将单元格中的一行变成多行，明确的换行符正好放在你想要的地方。

要在单元格中换行文本，请使用 Aspose.Cells.Style.IsTextWrapped 属性。

**C#**

{{< highlight "cs" >}}

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
## **NPOI - HSSF XSSF - Cells 中的新行**
CellStyle.setWrapText 应适用于环绕文本。

**C#**

{{< highlight "cs" >}}

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
下载**Cells 中的新行**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[换行和文字换行](/cells/zh/net/line-breaks-and-text-wrapping/).

{{% /alert %}}
