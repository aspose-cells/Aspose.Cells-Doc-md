---
title: 使用边框
type: docs
weight: 10
url: /zh/net/working-with-borders/
---
## **Aspose.Cells - 使用边框**
**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Worksheets.Add();

Worksheet worksheet = workbook.Worksheets[0];

// Style the cell with borders all around.

Style style = workbook.CreateStyle();

style.SetBorder(BorderType.BottomBorder, CellBorderType.Thin, Color.Black);

style.SetBorder(BorderType.LeftBorder, CellBorderType.Thin, Color.Green);

style.SetBorder(BorderType.RightBorder, CellBorderType.Thin, Color.Blue);

style.SetBorder(BorderType.TopBorder, CellBorderType.MediumDashed, Color.Black);

Cell cell = worksheet.Cells["A1"];

cell.SetStyle(style);            

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats


{{< /highlight >}}
## **NPOI - HSSF XSSF - 使用边界**
**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook();

// Create a Worksheet

ISheet ws = wb.CreateSheet("Sheet1");

ICellStyle style = wb.CreateCellStyle();

//Setting the line of the top border

style.BorderTop = BorderStyle.Thick;

style.TopBorderColor = 256;

style.BorderLeft = BorderStyle.Thick;

style.LeftBorderColor = 256;

style.BorderRight = BorderStyle.Thick;

style.RightBorderColor = 256;

style.BorderBottom = BorderStyle.Thick;

style.BottomBorderColor = 256;

IRow row = ws.CreateRow(0);

ICell cell = row.CreateCell(1);

cell.CellStyle = style;

FileStream sw = File.Create("test.xlsx");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
下载**使用边框**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.1/Working.With.Borders.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[数据格式化功能](http://www.aspose.com/docs/display/cellsjava/Working+with+Data+Formatting).

{{% /alert %}}
