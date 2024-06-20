---
title: ワークシートのズームファクターを設定します
type: docs
weight: 80
url: /ja/net/set-worksheet-zoom-factor/
---

## **Aspose.Cells - ワークシートのズームファクターを設定**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

worksheet.Zoom = 75;

//Saving the Excel file

workbook.Save("../../data/newWorksheet.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - ワークシートのズームファクターを設定**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

sheet1.SetZoom(3, 4); // 75 percent

FileStream sw = File.Create("../../data/newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下に記載されているソーシャルコーディングサイトのいずれかから**ワークシートのズームファクター**をダウンロードしてください:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Zoom.Factor.zip)

{{% alert color="primary" %}} 

詳細については、[ワークシートの操作](/cells/ja/net/working-with-worksheets-in-npoi-and-aspose-cells/)ページを参照してください。

{{% /alert %}}
