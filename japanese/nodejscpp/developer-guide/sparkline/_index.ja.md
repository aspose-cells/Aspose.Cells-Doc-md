---
title: Node.js経由でC++を使ってスパークラインを挿入
linktitle: スパークライン
type: docs
weight: 160
url: /ja/nodejs-cpp/creating-sparklines/
description: Aspose.Cells for Node.js via C++を使用してExcelのスパークラインを作成します。
---

## **スパークラインを挿入する**
{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++を使用したスパークラインは、ワークシートのセル内に表示される小さなチャートで、データの視覚的表現を提供します。季節的な増減、経済サイクル、最大値・最小値の強調など、値のシリーズのトレンドを示すために使用します。最も効果的に見せるためには、データの近くにスパークラインを配置します。スパークラインには、ライン、コラム、スタックの3種類があります。

{{% /alert %}} 

Aspose.Cells for Node.js via C++を使ってスパークラインを簡単に作成する例コードは次の通りです：



```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const book = new AsposeCells.Workbook(filePath);
const sheet = book.getWorksheets().get(0);

sheet.getCells().get("A1").putValue(5);
sheet.getCells().get("B1").putValue(2);
sheet.getCells().get("C1").putValue(1);
sheet.getCells().get("D1").putValue(3);

// Define the CellArea
const ca = AsposeCells.CellArea.createCellArea(0, 4, 0, 4);

const idx = sheet.getSparklineGroups().add(AsposeCells.SparklineType.Line, `${sheet.getName()}!A1:D1`, false, ca);

const group = sheet.getSparklineGroups().get(idx);
group.getSparklines().add(`${sheet.getName()}!A1:D1`, 0, 4);

// Customize Sparklines

// Create CellsColor
const clr = book.createCellsColor();
clr.setColor(AsposeCells.Color.Orange);
group.setSeriesColor(clr);

// Set the high points are colored green and the low points are colored red
group.setShowHighPoint(true);
group.setShowLowPoint(true);
group.getHighPointColor().setColor(AsposeCells.Color.Green);
group.getLowPointColor().setColor(AsposeCells.Color.Red);
// Set line weight 
group.setLineWeight(1.0);

// Saving the Excel file
book.save(path.join(dataDir, "output.xlsx"));
```

## **高度なトピック**
- [スパークラインの使用と 3D フォーマットの設定](/cells/ja/nodejs-cpp/using-sparklines-and-settings-3d-format/)
{{< app/cells/assistant language="nodejs-cpp" >}}
