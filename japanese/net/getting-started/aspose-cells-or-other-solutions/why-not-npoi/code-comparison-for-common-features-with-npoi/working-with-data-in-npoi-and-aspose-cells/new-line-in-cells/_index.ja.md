---
title: 改行 in Cells
type: docs
weight: 30
url: /ja/net/new-line-in-cells/
---
## **Aspose.Cells - Cells の改行**
セル内のテキストを確実に読み取れるようにするために、明示的な改行とテキストの折り返しを適用できます。テキストの折り返しにより、セル内の 1 行が複数の行に変わり、明示的な改行によって、必要な場所に正確に改行が挿入されます。

セル内のテキストを折り返すには、Aspose.Cells.Style.IsTextWrapped プロパティを使用します。

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
## **NPOI - HSSF XSSF - Cells の改行**
CellStyle.setWrapText は、折り返されたテキストに対して true にする必要があります。

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
## **実行中のコードをダウンロード**
ダウンロード**改行 in Cells**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[改行とテキストの折り返し](/cells/ja/net/line-breaks-and-text-wrapping/).

{{% /alert %}}
