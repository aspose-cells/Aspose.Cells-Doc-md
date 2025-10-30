---
title: Node.jsでPivotOptionsを使ったPivotChartの管理方法（C++を経由）
linktitle: Pivot Options
type: docs
weight: 10
url: /ja/nodejs-cpp/how-to-manage-pivotchart-with-pivotoptions/
description: Node.js（C++経由）でPivotOptionsを使ったPivotChartの管理方法
keywords: Node.js（C++経由）でPivotChartの管理
---
## PivotChartとは

ExcelのPivotChartは、PivotTableから作成されたデータの視覚的な表現です。これにより、ユーザーは情報を要約してチャート形式で表示し、データをダイナミックに視覚化して分析することができます。PivotChartは対話型であり、データの異なる視点を簡単に表示するように修正できるため、Excelでのデータ分析とプレゼンテーションにおける強力なツールとなっています。

## PivotOptionsを使用してPivotChartを管理する方法

Aspose.Cells for Node.js via C++を使用して、[**PivotOptions**](https://reference.aspose.com/cells/nodejs-cpp/pivotoptions/)を使ったPivotChartの管理が可能です。

サンプルファイルとコード:
[サンプルファイル](Sample.xlsx)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const chart = workbook.getWorksheets().get(0).getCharts().get(0);
const opt = chart.getPivotOptions();

// Hide ZoneFilter in PivotChart
opt.setDropZoneFilter(false); // HideZoneFilter

// You can set more properties, try them!
// opt.setDropZoneCategories(false); // HideZoneCategories
// opt.setDropZoneData(false); // HideZoneData
// opt.setDropZoneSeries(false); // HideZoneSeries
// opt.setDropZonesVisible(false); // Hide All

// Save the file and see the effect.
workbook.save(path.join(dataDir, "HideZoneFilter.xlsx"));
```

上記の例のコードを使用すると、次の効果が表示された結果ファイルを確認できます。

**![Output](Output.png)**
{{< app/cells/assistant language="nodejs-cpp" >}}
