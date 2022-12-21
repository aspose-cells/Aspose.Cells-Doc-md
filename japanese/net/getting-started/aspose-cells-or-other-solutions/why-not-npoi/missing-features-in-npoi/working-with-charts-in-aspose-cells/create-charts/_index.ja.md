---
title: チャートを作成する
type: docs
weight: 20
url: /ja/net/create-charts/
---
## **Aspose.Cells - チャートの作成**
Aspose.Cells を使用して、さまざまなチャートをスプレッドシートに追加することができます。Aspose.Cells は、多くの柔軟なチャート オブジェクトを提供します。

**C#**

{{< highlight "cs" >}}

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

// Adding NSeries (chart data source) to the chart ranging from "A1" cell to "B3"

SeriesCollection serieses = chart.NSeries;

serieses.Add("A1:B3", true);

// Saving the Excel file

workbook.Save("Chart_Aspose.xls");

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**チャートを作成する**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Create.Charts.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[チャートの作成方法](/cells/ja/net/create-charts/).

{{% /alert %}}
