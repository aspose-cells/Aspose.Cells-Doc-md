---
title: Node.jsを通じたC++でのShapeまたはChartのThreeDFormatの操作方法
linktitle: 図形またはグラフの3 D形式の操作
type: docs
weight: 250
url: /ja/nodejs-cpp/working-with-the-threedformat-of-shape-or-chart/
---

## **可能な使用シナリオ**
Aspose.Cells for Node.js via C++は、[Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) プロパティと [ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) クラスを提供し、形状やチャートの3Dフォーマットについて操作します。[ThreeDFormat](https://reference.aspose.com/cells/nodejs-cpp/threedformat) クラスには、アプリケーションの要件に応じて異なる結果を得るために設定できるさまざまなプロパティが含まれています。

## **図形またはグラフの3-D形式の操作**
次のサンプルコードは、[ソースExcelファイル](5115419.xlsx)をロードし、最初のワークシートの最初の形状にアクセスし、[Shape.getThreeDFormat()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getThreeDFormat--) プロパティのサブプロパティを設定し、その後ワークブックを保存し、[出力Excelファイル](5115410.xlsx)として保存します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load excel file containing a shape
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access first shape
const sh = ws.getShapes().get(0);

// Apply different three dimensional settings
const n3df = sh.getThreeDFormat();
n3df.setContourWidth(17);
n3df.setExtrusionHeight(32);

// Save the output excel file in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
