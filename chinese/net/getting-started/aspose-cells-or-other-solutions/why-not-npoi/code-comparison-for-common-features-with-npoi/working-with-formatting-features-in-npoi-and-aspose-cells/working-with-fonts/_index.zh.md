---
title: 使用字体
type: docs
weight: 30
url: /zh/net/working-with-fonts/
---
## **Aspose.Cells - 使用字体**
**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Worksheets.Add();

Worksheet worksheet = workbook.Worksheets[0];

// Adding some value to cell

Cell cell = worksheet.Cells["A1"];

cell.PutValue("This is Aspose test of fonts!");

// Setting the font name to "Times New Roman"

Style style = cell.GetStyle();

Font font = style.Font;

font.Name = "Courier New";

font.Size = 24;

font.IsBold = true;

font.Underline = FontUnderlineType.Single;

font.Color = Color.Blue;

font.IsStrikeout = true;

cell.SetStyle(style);

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats


{{< /highlight >}}
## **NPOI - HSSF XSSF - 使用字体**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

// Create a Worksheet

ISheet ws = wb.CreateSheet("Sheet1");

// Create a new font and alter it

IFont font = wb.CreateFont();

font.FontHeightInPoints = 24;

font.FontName = "Courier New";

font.IsItalic = true;

font.IsStrikeout = true;            

// Fonts are set into a style so create a new one to use.

ICellStyle style = wb.CreateCellStyle();

style.SetFont(font);

IRow row = ws.CreateRow(0);

// Create a cell and put a value in it.

ICell cell = row.CreateCell(1);

cell.SetCellValue("Thisi s a test of fonts");

cell.CellStyle = style;

FileStream sw = File.Create("test.xlsx");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
下载**使用字体**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.1/Working.with.Fonts.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[数据格式化功能](http://www.aspose.com/docs/display/cellsjava/Working+with+Data+Formatting).

{{% /alert %}}
