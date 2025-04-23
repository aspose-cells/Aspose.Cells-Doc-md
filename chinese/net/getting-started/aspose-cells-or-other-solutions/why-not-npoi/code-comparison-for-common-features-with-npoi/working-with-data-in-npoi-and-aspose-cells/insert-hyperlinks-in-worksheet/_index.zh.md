---
title: 在工作表中插入超链接
type: docs
weight: 20
url: /zh/net/insert-hyperlinks-in-worksheet/
---

## **Aspose.Cells - 在工作表中插入超链接**
**在同一文件中的单元格中添加链接**

通过调用超链接集合的Add方法，可以将超链接添加到同一Excel文件中的单元格中。Add方法适用于内部和外部超链接。

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

Worksheet sheet = workbook.Worksheets.Add("Hyperlinks");

HyperlinkCollection hyperlinks = sheet.Hyperlinks;

Style style = new Style();

style.Font.Underline = FontUnderlineType.Single;

style.Font.Color = System.Drawing.Color.Blue;

sheet.Cells[0, 0].Value = "URL Link";

hyperlinks.Add(0, 0, 1, 1, "http://www.aspose.com");

sheet.Cells[0, 0].SetStyle(style);

//link to a file in the current directory

sheet.Cells[1, 0].Value = "File Link";

hyperlinks.Add(1, 0, 1, 1, "book1.xls");

sheet.Cells[1, 0].SetStyle(style);

//e-mail link

sheet.Cells[2, 0].Value = "Email Link";

hyperlinks.Add(2, 0, 1, 1, "mailto:marketplace@aspose.com?subject=Hyperlinks");

sheet.Cells[2, 0].SetStyle(style);

//link to a place in this workbook

Worksheet sheet2 = workbook.Worksheets.Add("Target ISheet");

HyperlinkCollection hyperlinks2 = sheet2.Hyperlinks;

sheet2.Cells[3, 0].Value = "Worksheet Link";

hyperlinks2.Add(3, 0, 1, 1, "Target ISheet!A4");

sheet2.Cells[3, 0].SetStyle(style);

workbook.Save("test.xlsx");


{{< /highlight >}}

**向外部文件添加链接**

通过调用超链接集合的Add方法，可以将超链接添加到同一Excel文件中的单元格中。Add方法适用于内部和外部超链接。其中一个重载方法采用以下参数：

- 单元格名称，将要添加超链接的单元格名称。
- 行数，超链接范围中的行数。
- 列数，超链接范围中的列数。
- URL，目标单元格的地址。

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the first (default) worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Adding an internal hyperlink to the "B9" cell of the other worksheet "Sheet2" in

//the same Excel file

worksheet.Hyperlinks.Add("B3", 1, 1, "Sheet2!B9");

//Saving the Excel file

workbook.Save("C:\\book1.xls");

{{< /highlight >}}
## **NPOI - HSSF XSSF -在工作表中插入超链接**
**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

////cell style for hyperlinks

////by default hyperlinks are blue and underlined

ICellStyle hlink_style = workbook.CreateCellStyle();

IFont hlink_font = workbook.CreateFont();

hlink_font.Underline = FontUnderlineType.Single;

hlink_font.Color = HSSFColor.Blue.Index;

hlink_style.SetFont(hlink_font);

ICell cell;

ISheet sheet = workbook.CreateSheet("Hyperlinks");

//URL

cell = sheet.CreateRow(0).CreateCell(0);

cell.SetCellValue("URL Link");

XSSFHyperlink link = new XSSFHyperlink(HyperlinkType.Url);

link.Address = ("http://poi.apache.org/");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

//link to a file in the current directory

cell = sheet.CreateRow(1).CreateCell(0);

cell.SetCellValue("File Link");

link = new XSSFHyperlink(HyperlinkType.File);

link.Address = ("link1.xls");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

//e-mail link

cell = sheet.CreateRow(2).CreateCell(0);

cell.SetCellValue("Email Link");

link = new XSSFHyperlink(HyperlinkType.Email);

//note, if subject contains white spaces, make sure they are url-encoded

link.Address = ("mailto:poi@apache.org?subject=Hyperlinks");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

//link to a place in this workbook

//Create a target sheet and cell

ISheet sheet2 = workbook.CreateSheet("Target ISheet");

sheet2.CreateRow(0).CreateCell(0).SetCellValue("Target ICell");

cell = sheet.CreateRow(3).CreateCell(0);

cell.SetCellValue("Worksheet Link");

link = new XSSFHyperlink(HyperlinkType.Document);

link.Address = ("'Target ISheet'!A1");

cell.Hyperlink = (link);

cell.CellStyle = (hlink_style);

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
从下面提到的任何社交编码网站下载 **在工作表中插入超链接**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Insert.Hyperlinks.In.Worksheet.Aspose.Cells.zip)

{{% alert color="primary" %}} 

更多详细信息，请访问 [添加超链接以链接数据](/cells/zh/net/adding-hyperlinks-to-link-data-in-aspose-cells/)。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
