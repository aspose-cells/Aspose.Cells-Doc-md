---
title: グラフを画像に変換
type: docs
weight: 10
url: /ja/net/convert-chart-to-images/
---

## **Aspose.Cells - グラフを画像に変換**
グラフは視覚的に魅力があり、ユーザーがデータの比較、パターン、傾向を見るのが簡単です。
Chart クラスの toImage メソッドは、チャートを画像ファイルに変換し、ディスクまたはストリームに保存できます。

**C#**

{{< highlight cs >}}

 // Instantiating a Workbook object

Workbook workbook = new Workbook();

// Obtaining the reference of the first worksheet

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet sheet = worksheets[0];

// Adding some sample value to cells

Cells cells = sheet.Cells;

Cell cell = cells["A1"];

cell.Value = 50;

cell = cells["A2"];

cell.Value = 100;

cell = cells["A3"];

cell.Value = 150;

cell = cells["B1"];

cell.Value = 4;

cell = cells["B2"];

cell.Value = 20;

cell = cells["B3"];

cell.Value = 50;

ChartCollection charts = sheet.Charts;

// Adding a chart to the worksheet

int chartIndex = charts.Add(ChartType.Pyramid, 5, 0, 15, 5);

Chart chart = charts[chartIndex];

//Save the chart image file.

chart.ToImage("AsposeChartImage.png", ImageFormat.Png);

{{< /highlight >}}
## **ランニングコードのダウンロード**
以下のソーシャルコーディングサイトから **グラフを画像に変換** をダウンロードしてください。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Convert.Chart.To.Images.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、[グラフを画像に変換](/cells/ja/net/converting-chart-to-image-in-svg-format/)をご覧ください。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
