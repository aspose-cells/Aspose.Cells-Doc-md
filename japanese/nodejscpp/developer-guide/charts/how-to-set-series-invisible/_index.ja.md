---
title: Node.jsをC++経由でシリーズを非表示に設定する方法
linktitle: シリーズを非表示にする方法
description: Aspose.Cells for Node.js via C++を使用してExcelチャートでシリーズを非表示に設定する方法を学びましょう。 
keywords: Excelチャート、系列、非表示、IsFiltered Node.jsをC++経由で。
type: docs
weight: 74
url: /ja/nodejs-cpp/how-to-set-series-invisible/
---

## Excelチャートでシリーズを非表示にする方法

Excelチャートでは、チャートを右クリックして「データの選択」をクリックし、表示・非表示の設定をチェック・解除できます。以下の[サンプルファイル](SeriesFiltered.xlsx)をダウンロードし、図のように操作してこの機能を実現できます。次に、Aspose.Cellsライブラリを使った方法をご説明します。

![todo:image_alt_text](series-invisible.png)

## Aspose.Cellsでシリーズを非表示に設定する方法 

Aspose.Cellsを使ってシリーズを非表示に設定するコードは以下の通りです：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SeriesFiltered.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const charts = workbook.getWorksheets().get(0).getCharts();
const chart = charts.get("Chart 1");
const nSeriesFiltered = chart.getFilteredNSeries();
const nSeries = chart.getNSeries();
nSeries.get(1).setIsColorVaried(true);
nSeries.get(0).setIsColorVaried(true);
workbook.save(path.join(dataDir, "output.xlsx"));
```

以下の[入力ファイル](SeriesFiltered.xlsx)と[出力ファイル](output.xlsx)を取得できます。

図のように、最初に表示されていた2つのシリーズが、出力ファイルで非表示になっています。
![todo:image_alt_text](output.png)
{{< app/cells/assistant language="nodejs-cpp" >}}
