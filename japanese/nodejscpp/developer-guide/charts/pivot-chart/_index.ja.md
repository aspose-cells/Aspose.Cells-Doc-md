---
title: Aspose.Cells for Node.js via C++を使ったPivotChartの追加方法
linktitle: ピボットチャート
type: docs
weight: 100
url: /ja/nodejs-cpp/how-to-add-pivot-chart/
description: Aspose.Cells for Node.js via C++を使用してPivotChartを追加する方法。
keywords: Node.js（C++経由）でPivotChartの管理
---
## PivotChartとは

ピボットチャートは、ピボットテーブルのデータを視覚的に表現したものです。ピボットチャートは、要約の概要、分析、探索、および提示のための方法を提供します。主な特徴と側面は以下の通りです：

1. 動的データ表現：ピボットチャートは、ピボットテーブルの変更に応じて自動的に更新されます。フィールドの追加や削除により、ピボットチャートもそれに応じて更新されます。

1. インタラクティブ：ピボットチャートはインタラクティブで、フィルタリング、並べ替え、詳細表示が可能です。これにより、データセットのさまざまな側面を簡単に探索できます。

1. 柔軟なレイアウト：ユーザーはフィールドをドラッグアンドドロップしてピボットチャートのレイアウトを変更でき、データの視覚化に柔軟性を持たせることができます。

1. 様々なチャートタイプ：棒グラフ、折れ線グラフ、円グラフなど、さまざまなタイプのチャートで作成可能です。データの性質や洞察したい内容に応じて選択します。

1. 要約：ピボットチャートは大量のデータを要約し、合計値、平均値、カウント、その他の統計情報を表示できます。

1. フィルタリング：特定の条件を満たすデータのみを表示するフィルタリング機能もあります。

<br>
ピボットチャートは、ビジネスインテリジェンスやデータ分析によく使われ、複雑なデータセットの明確で簡潔なビジュアル概要を提供します。データ駆動の意思決定に強力なツールです。

## Aspose.Cells for Node.js via C++を使用したPivotChartの追加方法

### **ピボットテーブルの追加**

Aspose.Cells for Node.js via C++を使用してピボットテーブルを作成するには：

1. セルオブジェクトの`putValue`メソッドを使ってワークシートにデータを追加します。既にデータが入力されたテンプレートファイルを使用することも可能です。そのデータはピボットテーブルのデータソースとして利用されます。
1. `PivotTables`コレクションの`add`メソッドを呼び出してピボットテーブルをワークシートに追加します。
1. `PivotTables`コレクションからインデックスを渡して新しい`PivotTable`オブジェクトにアクセスします。`.PivotTable`オブジェクトにカプセル化されたピボットテーブルのいずれかを使用して管理します。

以下にコード例を示します。

```javascript
try {
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Obtaining the reference of the first worksheet
const sheet = workbook.getWorksheets().get(0);
// Name the sheet
sheet.setName("Data");
const cells = sheet.getCells();

// Setting the values to the cells
cells.get("A1").putValue("Employee");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Product");
cells.get("D1").putValue("Continent");
cells.get("E1").putValue("Country");
cells.get("F1").putValue("Sale");

const namesAndValues = [
["David", 1, "Maxilaku", "Asia", "China", 2000],
["David", 2, "Maxilaku", "Asia", "India", 500],
["David", 3, "Chai", "Asia", "Korea", 1200],
["David", 4, "Maxilaku", "Asia", "India", 1500],
["James", 1, "Chang", "Europe", "France", 500],
["James", 2, "Chang", "Europe", "France", 1500],
["James", 3, "Chang", "Europe", "Germany", 800],
["James", 4, "Chang", "Europe", "Italy", 900],
["James", 4, "Chang", "Europe", "France", 500],
["Miya", 1, "Geitost", "America", "U.S.", 1600],
["Miya", 2, "Chai", "America", "U.S.", 600],
["Miya", 3, "Geitost", "America", "Brazil", 2000],
["Miya", 2, "Geitost", "America", "U.S.", 500],
["Miya", 3, "Maxilaku", "America", "Canada", 900],
["Miya", 4, "Geitost", "America", "U.S.", 700],
["Miya", 5, "Geitost", "America", "U.S.", 1400],
["Miya", 6, "Ikuru", "Europe", "Italy", 1350],
["Miya", 7, "Ikuru", "Europe", "France", 300],
["Miya", 8, "Ikuru", "Europe", "Italy", 500],
["Miya", 9, "Ikuru", "America", "New Zealand", 1000],
["Miya", 10, "Ipoh Coffee", "Oceania", "Australia", 1500],
["Miya", 11, "Chocolade", "Oceania", "Australia", 500],
["Miya", 12, "Chocolade", "Oceania", "New Zealand", 1500],
["Miya", 13, "Chocolade", "Oceania", "S.Africa", 1600],
["Miya", 14, "Chocolade", "Africa", "Egypt", 1000],
["Miya", 15, "Chocolade", "Africa", "Egypt", 1200],
["Miya", 16, "Chocolade", "Africa", "Egypt", 1300],
];

namesAndValues.forEach((item, index) => {
const rowIndex = index + 2;
cells.get(`A${rowIndex}`).putValue(item[0]);
cells.get(`B${rowIndex}`).putValue(item[1]);
cells.get(`C${rowIndex}`).putValue(item[2]);
cells.get(`D${rowIndex}`).putValue(item[3]);
cells.get(`E${rowIndex}`).putValue(item[4]);
cells.get(`F${rowIndex}`).putValue(item[5]);
```

### **ピボットチャートの追加**

Aspose.Cells for Node.js via C++を使用してピボットチャートを作成するには：

1. チャートを追加します。
1. グラフの `PivotSource` を既存のピボットテーブルを指すように設定します。
1. 他の属性を設定します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiating an Workbook object
// Opening the excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "pivotTable_test.xlsx"));
// Adding a new sheet
const sheetIndex = workbook.getWorksheets().add(AsposeCells.SheetType.Chart);
const sheet3 = workbook.getWorksheets().get(sheetIndex);
sheet3.setName("PivotChart");
// Adding a column chart
const index = sheet3.getCharts().add(AsposeCells.ChartType.Column, 0, 5, 28, 16);
// Setting the pivot chart data source
sheet3.getCharts().get(index).setPivotSource("PivotTable!PivotTable1");
sheet3.getCharts().get(index).setHidePivotFieldButtons(false);
// Saving the Excel file
workbook.save(path.join(dataDir, "pivotChart_test_out.xlsx"));
```

{{< app/cells/assistant language="nodejs-cpp" >}}
