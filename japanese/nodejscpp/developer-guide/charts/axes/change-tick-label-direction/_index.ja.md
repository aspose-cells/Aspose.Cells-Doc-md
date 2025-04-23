---
title: Node.jsとC++を使用したティックラベルの方向変更方法
linktitle: 目盛りラベル方向の変更
description: Aspose.Cells for Node.jsでのティックラベルの向きを変更する方法について学びます。ガイドでは、軸上のティックラベルの向き（水平、垂直、角度付）を調整する方法を説明します。
keywords: Aspose.Cells for Node.js、ティックラベル、方向、向き、軸、水平、垂直、角度
type: docs
weight: 170
url: /ja/nodejs-cpp/change-tick-label-direction/
---

## **目盛りラベル方向の変更**

Aspose.Cellsは、[**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--)プロパティを使用してチャートのティックラベルの向きを変更する機能を提供します。[**TickLabels.getDirectionType()**](https://reference.aspose.com/cells/nodejs-cpp/ticklabels/#getDirectionType--)プロパティは[**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype)列挙値を受け入れます。[**ChartTextDirectionType**](https://reference.aspose.com/cells/nodejs-cpp/charttextdirectiontype)列挙には次のメンバーが含まれます：

－ 水平
－ 垂直
－ Rotate90
－ Rotate270
－ スタック

次の画像は、ソースファイルと出力ファイルを比較したものです。

### **ソースファイル画像**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **出力ファイル画像**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

次のコードスニペットは、Rotate90から水平への目盛りラベルの方向を変更します。

## **サンプルコード**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");
const filePath = path.join(sourceDir, "SampleChangeTickLabelDirection.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

const worksheet = workbook.getWorksheets().get(0);

// Load the chart from source worksheet
const chart = worksheet.getCharts().get(0);

chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Horizontal);

// Output the file
workbook.save(path.join(outputDir, "outputChangeChartDataLableDirection.xlsx"));
```

ソースファイルと出力ファイルは、以下のリンクからダウンロードできます。

[ソースファイル](105480221.xlsx)

[出力ファイル](105480223.xlsx)
