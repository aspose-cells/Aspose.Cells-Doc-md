---
title: Node.js経由でC++を使ったチャートポイントのリッチテキストカスタムデータラベル
description: Aspose.Cells for Node.js via C++を使用してチャートポイントにリッチテキストカスタムデータラベルを追加する方法を学びます。ガイドでは、異なるフォント、色、配置オプションを使用してラベルの書式設定を行い、チャートの外観と読みやすさを向上させる方法を示します。
keywords: Aspose.Cells for Node.js via C++、チャート作成、リッチテキスト、カスタムデータラベル、フォント、色、配置、外観、読みやすさ。
type: docs
weight: 10
url: /ja/nodejs-cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用してチャートポイントのリッチテキストカスタムデータラベルを作成できます。Aspose.Cellsは[**ChartTextFrame.characters(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#characters-number-number-)メソッドを提供し、これによりテキストの色や太字などのフォントプロパティを設定できる[**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)オブジェクトを返します。

{{% /alert %}}

## チャートポイントのリッチテキストカスタムデータラベル

以下のコードは最初の系列の最初のチャートポイントにアクセスし、そのテキストを設定し、最初の10文字のフォントを赤色に設定し、太字にします。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample_custom_datalabel.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first chart inside the sheet
const chart = worksheet.getCharts().get(0);

// Access the data label of first series first point
const dlbls = chart.getNSeries().get(0).getPoints().get(0).getDataLabels();

// Set data label text
dlbls.setText("Rich Text Label");

// Set the font setting of the first 10 characters
const fntSetting = dlbls.characters(0, 10);
fntSetting.getFont().setColor(AsposeCells.Color.Red);
fntSetting.getFont().setIsBold(true);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
