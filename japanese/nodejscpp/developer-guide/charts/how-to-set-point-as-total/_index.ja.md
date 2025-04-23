---  
title: Node.js経由でC++を使用し、ポイントを合計に設定する方法  
linktitle: 合計としてポイントを設定する方法  
description: Aspose.Cells for Node.js via C++を使用してWaterFallチャートのポイントを合計に設定する方法を学びましょう。  
keywords: WaterFallチャート、ポイント、合計として設定、Node.jsをC++経由で  
type: docs  
weight: 72  
url: /ja/nodejs-cpp/how-to-set-point-as-total/  
---  

## Excelチャートの「ポイントを合計に設定」とは

例えばWaterFallチャートなど、一部のExcelチャートでは、あるポイントデータが前のポイントの合計になっており、「ポイントを合計として設定」する必要があります。サンプルコードとイラストを下に示します。

## WaterFallチャートには"ポイントを合計に設定"が必要です 

![todo:image_alt_text](set-as-total1.png)

この図はExcelのWaterFallチャートを示しています。4つのデータポイントは「Total」から始まり、すべての前のデータポイントを合計するために使用されます。この図では設定が正確ではありません。「Total 2024」のポイントを選択すると、「合計に設定」オプションがExcelでチェックされていないことがわかります。修正が必要なサンプルExcelファイル([SampleSheet.xlsx](SampleSheet.xlsx))を添付し、Aspose.Cells for Node.js via C++を使用して正しく設定します。

## Aspose.Cells for Node.js via C++を使用して"ポイントを合計に設定"する方法 

正しい設定を行うためのコードは以下の通りです：

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);
const chart = worksheet.getCharts().get("Graphiq5");

// set some points as total column 
// In this example, we set points 0, 4, 8, 12 as total
chart.getNSeries().get(0).getLayoutProperties().setSubtotals([0, 4, 8, 12]);
workbook.save(path.join(dataDir, "output.xlsx"));
```

次の正しい[出力ファイル](output.xlsx)を取得できます。

図のように、4つの"合計"データポイントが正しく設定されているのが確認でき、前のチャートとの違いもわかります。

![todo:image_alt_text](set-as-total2.png)  
