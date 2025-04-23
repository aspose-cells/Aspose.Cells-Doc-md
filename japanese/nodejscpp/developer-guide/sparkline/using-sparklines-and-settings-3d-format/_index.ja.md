---
title: Node.jsをC++経由で使用して、スパークラインと3Dフォーマットの設定を使用する方法
linktitle: スパークラインと設定3Dフォーマットの使用
type: docs
weight: 40
url: /ja/nodejs-cpp/using-sparklines-and-settings-3d-format/
description: Aspose.Cells for Node.js via C++を使用して、Excelファイルにスパークラインと3Dフォーマットを適用する方法を学びます。 
---

## **スパークラインの使用**
Microsoft Excel 2010では、これまで以上に情報をさまざまな方法で分析できます。新しいデータ分析および可視化ツールを使用して重要なデータトレンドを追跡および強調することができます。スパークラインは、表内に配置してデータとグラフを同時に表示できるミニチャートです。スパークラインを適切に使用すると、データ分析が迅速かつ的確になります。また、情報のシンプルな表示を提供し、多くの複雑なチャートでワークシートが過度に混雑するのを避けることもできます。

Aspose.Cells for Node.js via C++は、スプレッドシートのスパークラインを操作するためのAPIを提供します。
### **Microsoft Excelでのスパークライン**
Microsoft Excel 2010にスパークラインを挿入するには:

1. スパークラインが表示されるセルを選択します。視覚的にわかりやすくするため、データの横のセルを選択します。
1. リボンの**挿入**を選択し、**スパークライン**グループで**列**を選択します。
1. ワークシートに含まれるソースデータのセル範囲を選択または入力します。チャートが表示されます。

スパークラインは、例えばソフトボールリーグの勝敗記録などのトレンドを見るのに役立ちます。スパークラインは、リーグ内の各チームのシーズン全体を要約することさえできます。
### **Aspose.Cells for Node.js via C++を使用したスパークライン**
開発者は、Aspose.Cells for Node.js via C++が提供するAPIを使用して、テンプレートファイル内のスパークラインを作成、削除、または読み取ることができます。スパークラインを管理するクラスは[SparklineGroupCollection](https://reference.aspose.com/cells/nodejs-cpp/sparklinegroupcollection/)モジュールに含まれており、これらの機能を使用する前にこのモジュールをロードする必要があります。

指定されたデータ範囲にカスタムグラフィックスを追加することで、開発者は選択したセル領域に異なる種類の小さなチャートを追加する自由があります。

以下の例は、スパークライン機能を示しています。この例では次のことを示しています:

1. 簡単なテンプレートファイルを開きます。
1. ワークシートのスパークライン情報を読み取ります。
1.指定されたデータ範囲に新しいスパークラインをセル領域に追加します。
1. Excelファイルをディスクに保存します。


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a Workbook
// Open a template file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));
// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);

// Use the following lines if you need to read the Sparklines
// Read the Sparklines from the template file (if it has)
const sparklinesCount = sheet.getSparklineGroups().getCount();

for (let i = 0; i < sparklinesCount; i++)
{
const group = sheet.getSparklineGroups().get(i);
// Display the Sparklines group information e.g type, number of sparklines items
console.log(`sparkline group: type:${group.getType()}, sparkline items count:${group.getSparklines().getCount()}`);
const sparklineCount = sparklineGroup.getSparklines().getCount();
for (let j = 0; j < sparklineCount; j++) 
{
const sparkline = sparklineGroup.getSparklines().get(j);
// Display the individual Sparkines and the data ranges
console.log(`sparkline: row:${sparkline.getRow()}, col:${sparkline.getColumn()}, dataRange:${sparkline.getDataRange()}`);
}
}


// Add Sparklines
// Define the CellArea D2:D10
const ca = AsposeCells.CellArea.createCellArea(1, 4, 7, 4);
// Add new Sparklines for a data range to a cell area
const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Column, "Sheet1!B2:D8", false, ca);
const group = sheet.getSparklineGroups().get(idx);
// Create CellsColor
const clr = workbook.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Save the excel file
workbook.save(path.join(dataDir, "Book1.out.xlsx"));
```
## **3Dフォーマットの設定**
シナリオに合った結果を得るために、3Dチャーティングスタイルが必要な場合があります。Aspose.Cells for Node.js via C++は、Microsoft Excel 2007の3Dフォーマットを適用するための関連APIも提供しています。

Microsoft Excel 2007の3Dフォーマットを適用する方法を示す完全な例が以下に示されています。例のコードを実行すると、ワークシートに3D効果のある列グラフが追加されます。


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "3d_format.out.xlsx");

// Instantiate a new Workbook
const book = new AsposeCells.Workbook();

// Add a Data Worksheet
const dataSheet = book.getWorksheets().add("DataSheet");

// Add Chart Worksheet
const sheet = book.getWorksheets().add("MyChart");

// Put some values into the cells in the data worksheet
dataSheet.getCells().get("B1").putValue(1);
dataSheet.getCells().get("B2").putValue(2);
dataSheet.getCells().get("B3").putValue(3);
dataSheet.getCells().get("A1").putValue("A");
dataSheet.getCells().get("A2").putValue("B");
dataSheet.getCells().get("A3").putValue("C");

// Define the Chart Collection
const charts = sheet.getCharts();
// Add a Column chart to the Chart Worksheet
const chartSheetIdx = charts.add(AsposeCells.ChartType.Column, 5, 0, 25, 15);

// Get the newly added Chart
const chart = book.getWorksheets().get(2).getCharts().get(0);

// Set the background/foreground color for PlotArea/ChartArea
chart.getPlotArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setBackgroundColor(AsposeCells.Color.White);
chart.getPlotArea().getArea().setForegroundColor(AsposeCells.Color.White);
chart.getChartArea().getArea().setForegroundColor(AsposeCells.Color.White);

// Hide the Legend
chart.setShowLegend(false);

// Add Data Series for the Chart
chart.getNSeries().add("DataSheet!B1:B3", true);
// Specify the Category Data
chart.getNSeries().setCategoryData("DataSheet!A1:A3");

// Get the Data Series
const ser = chart.getNSeries().get(0);

// Apply the 3-D formatting
const spPr = ser.getShapeProperties();
const fmt3d = spPr.getFormat3D();

// Specify Bevel with its height/width
const bevel = fmt3d.getTopBevel();
bevel.setType(AsposeCells.BevelPresetType.Circle);
bevel.setHeight(2);
bevel.setWidth(5);

// Specify Surface material type
fmt3d.setSurfaceMaterialType(AsposeCells.PresetMaterialType.WarmMatte);

// Specify surface lighting type
fmt3d.setSurfaceLightingType(AsposeCells.LightRigType.ThreePoint);

// Specify lighting angle
fmt3d.setLightingAngle(20);

// Specify Series background/foreground and line color
ser.getArea().setBackgroundColor(AsposeCells.Color.Maroon);
ser.getArea().setForegroundColor(AsposeCells.Color.Maroon);
ser.getBorder().setColor(AsposeCells.Color.Maroon);

// Save the Excel file
book.save(filePath);
```
