---
title: ワークシートにハイパーリンクを挿入する
type: docs
weight: 20
url: /ja/net/insert-hyperlinks-in-worksheet/
---

## **Aspose.Cells - ワークシートにハイパーリンクを挿入する**
同一ファイル内のセルにリンクを追加する

セルにハイパーリンクを追加するには、HyperlinkコレクションのAddメソッドを呼び出します。Addメソッドは、内部および外部の両方のハイパーリンクに対して機能します。

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

外部ファイルへのリンクを追加する

ハイパーリンクコレクションのAddメソッドを呼び出すことで、同じExcelファイルのセルにハイパーリンクを追加することが可能です。オーバーロードされたメソッドのバージョンの1つは、次のパラメータを取ります:

- セル名、ハイパーリンクが追加されるセルの名前。
- 行数、このハイパーリンク範囲の行数。
- 列数、このハイパーリンク範囲の列数。
- URL、対象セルのアドレス。

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
## **NPOI - HSSF XSSF - ワークシートにハイパーリンクを挿入する**
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
## **ランニングコードのダウンロード**
以下のいずれかのソーシャルコーディングサイトから**Insert Hyperlinks in Worksheet**をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Insert.Hyperlinks.In.Worksheet.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[Adding Hyperlinks to Link Data](/cells/ja/net/adding-hyperlinks-to-link-data-in-aspose-cells/)を参照してください。

{{% /alert %}}
