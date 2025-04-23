---
title: セル内の改行
type: docs
weight: 30
url: /ja/net/new-line-in-cells/
---

## **Aspose.Cells - セル内の改行**
セル内のテキストが読み取れるようにするために、明示的な改行とテキストの折り返しを適用することができます。テキストの折り返しは、セル内の一行を複数行に変換し、明示的な改行は望む場所に改行を挿入します。

セル内のテキストを折り返すには、Aspose.Cells.Style.IsTextWrappedプロパティを使用します。

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
## **NPOI - HSSF XSSF - セル内の改行**
CellStyle.setWrapTextは、折り返されたテキストに対してtrueである必要があります。

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
## **ランニングコードのダウンロード**
以下に示すいずれかのソーシャルコーディングサイトから、 **セル内の新しい行**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/New.Line.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[改行とテキストの折り返し](/cells/ja/net/line-breaks-and-text-wrapping/)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
