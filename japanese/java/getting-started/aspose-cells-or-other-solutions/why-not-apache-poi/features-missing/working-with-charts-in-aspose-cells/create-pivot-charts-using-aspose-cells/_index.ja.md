---
title: Aspose.Cells を使用してピボット グラフを作成する
type: docs
weight: 40
url: /ja/java/create-pivot-charts-using-aspose-cells/
---
## **Aspose.Cells - ピボット チャートの作成**
ピボット テーブルは、レコードのインタラクティブな要約です。たとえば、ワークシートのリストに何百もの請求書エントリがあるとします。ピボット テーブルは、顧客、製品、または日付ごとに請求書を合計できます。 Microsoft Excel では、ボタンを新しい位置にドラッグすることで、ピボット テーブル内の情報をすばやく再配置できます。
ピボット チャートは、ピボット テーブル内のデータをインタラクティブにグラフィカルに表現したものです。ピボット グラフは、Excel 2000 で導入されました。ピボット テーブルを使用すると、小計と合計が自動的に作成されるため、データをさらに理解しやすくなります。

Aspose.Cells は、ピボット テーブルとピボット チャートをサポートします。

**Java**

{{< highlight "java" >}}

 // Instantiating an Workbook object

Workbook workbook = new Workbook(dataDir + "AsposePivotTable.xls");

// Adding a new sheet

int sheetIndex = workbook.getWorksheets().add(SheetType.CHART);

Worksheet sheet3 = workbook.getWorksheets().get(sheetIndex);

// Naming the sheet

sheet3.setName("PivotChart");

// Adding a column chart

int chartIndex = sheet3.getCharts().add(ChartType.COLUMN, 0, 5, 28, 16);

Chart chart = sheet3.getCharts().get(chartIndex);

// Setting the pivot chart data source

chart.setPivotSource("PivotTable!PivotTable1");

chart.setHidePivotFieldButtons(false);

{{< /highlight >}}
## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[ピボット テーブルとピボット チャートを作成する](/cells/ja/java/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}
