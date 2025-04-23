---
title: Node.js経由でC++を使用してチャートシリーズの値のフォーマットコードを設定する
description: Aspose.Cells for Node.js via C++でチャートシリーズの値のフォーマットコードの設定方法を学びます。このガイドは、適切なフォーマットコードを使用してチャートシリーズのデータをフォーマットし、正確かつ専門的にデータを表示するのに役立ちます。
keywords: Aspose.Cells for Node.js、チャートシリーズ、値のフォーマットコード、フォーマット、データ提示、正確性、専門性。
linktitle: 数値形式
type: docs
weight: 100
url: /ja/nodejs-cpp/set-the-values-format-code-of-chart-series/
---

## **可能な使用シナリオ**
[Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--) プロパティを使用してチャートシリーズの値のフォーマットコードを設定できます。このプロパティは、ワークシート内の範囲に基づくシリーズだけでなく、値の配列で作成されたシリーズでも便利に機能します。

## **チャートシリーズの値の形式コードを設定する**
次のサンプルコードは、以前はシリーズがなかった空のチャートにシリーズを追加します。値の配列を使用してシリーズを追加します。シリーズを追加した後、[Series.getValuesFormatCode()](https://reference.aspose.com/cells/nodejs-cpp/series/#getValuesFormatCode--)プロパティとコード$#,##0を使用してフォーマットし、数字10000は$10,000に変換されます。スクリーンショットは、実行後の[sample Excelファイル](51740712.xlsx)と[出力Excelファイル](51740713.xlsx)への効果を示しています。

![todo:image_alt_text](set-the-values-format-code-of-chart-series_1.png)

## **サンプルコード**
```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "51740712.xlsx");

// Load the source Excel file 
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Add series using an array of values
chart.getNSeries().add("{10000, 20000, 30000, 40000}", true);

// Access the series and set its values format code
const series = chart.getNSeries().get(0);
series.setValuesFormatCode("$#,##0");

// Save the output Excel file
workbook.save(path.join(dataDir, "51740713.xlsx"));
```
