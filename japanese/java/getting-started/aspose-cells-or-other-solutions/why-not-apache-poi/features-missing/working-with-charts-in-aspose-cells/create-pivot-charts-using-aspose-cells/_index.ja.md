---
title: Aspose.Cellsを使用してピボットグラフを作成する
type: docs
weight: 40
url: /ja/java/create-pivot-charts-using-aspose-cells/
---

## **Aspose.Cells - ピボットチャートを作成する**
ピボットテーブルは、レコードのインタラクティブな集計です。たとえば、ワークシートのリストには数百の請求書エントリがあります。ピボットテーブルは、顧客、製品、または日付別に請求書を合計することができます。Microsoft Excelを使用すると、ピボットテーブル内の情報をボタンをドラッグするだけで素早く再配置することが可能です。
ピボットチャートは、ピボットテーブルのデータのインタラクティブなグラフィカルな表現です。ピボットチャートはExcel 2000で導入されました。ピボットテーブルが自動的に小計と合計を作成するため、ピボットチャートを使用することでデータを理解することがさらに容易になります。

Aspose.Cells は、ピボットテーブルとピボットチャートをサポートしています。

**Java**

{{< highlight java >}}

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
## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/charts/AsposePivotChart.java)

{{% alert color="primary" %}} 

詳細については、[ピボットテーブルとピボットチャートの作成](/cells/ja/java/create-pivot-tables-and-pivot-charts/) をご覧ください。

{{% /alert %}}
