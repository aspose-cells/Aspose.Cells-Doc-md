---  
title: Node.js経由のC++を使ってチャートのデータラベルの形状をテキストに合わせてリサイズする  
linktitle: チャートのデータラベルの形状をテキストに合わせるようにサイズ変更する  
description: Aspose.Cells for Node.js via C++を使用して、チャートのデータラベルの形状をテキストに合わせてリサイズする方法を学びましょう。ガイドでは、テキストが適切に表示され切り捨てや重なりがないように、ラベルのサイズと形状を調整する方法を説明します。  
keywords: Aspose.Cells for Node.js via C++、チャート作成、データラベル、形状リサイズ、テキストフィット、切り捨て、重なり。  
type: docs  
weight: 220  
url: /ja/nodejs-cpp/resize-chart-s-data-label-shape-to-fit-text/  
---  

{{% alert color="primary" %}}  
Excelアプリケーションでは、チャートのデータラベルの**テキストに合わせて形状を変更**するオプションが提供されており、これによりテキストが形状内に収まるように形状のサイズが拡大されます。  
{{% /alert %}}  

## **Microsoft Excelのインタフェース上で、チャートのデータラベルを選択して、**フォーマットデータラベル**メニューを右クリックします。**サイズとプロパティ**タブで、**配置**を展開して、**テキストに合わせて形状を変更**オプションを含む関連プロパティを表示します。**  

 このオプションは、チャート上の任意のデータラベルを選択し、右クリックして**データラベルの書式設定**メニューからアクセスできます。**サイズとプロパティ**タブの下にある**整列**を展開すると、必要な関連プロパティが表示されます、その中に**テキストに合わせて形状をリサイズ**オプションがあります。  

## ** Aspose.Cells for Node.js via C++を使ったチャートのデータラベルの形状をテキストに合わせてリサイズする方法**  

 Excelの機能に似せて、データラベルの形状をテキストにフィットさせるために、Aspose.Cells APIはブール型の[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--)プロパティを公開しています。以下のコード例は、その[**DataLabels.isResizeShapeToFitText()**](https://reference.aspose.com/cells/nodejs-cpp/charttextframe/#isResizeShapeToFitText--)プロパティの簡単な使用例を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");

// Create an instance of Workbook containing the Chart
const workbook = new AsposeCells.Workbook(filePath);

// Access the Worksheet that contains the Chart
const sheet = workbook.getWorksheets().get(0);

for (let c = 0; c < sheet.getCharts().getCount(); c++) 
{
// Access the Chart
const chart = sheet.getCharts().get(c);

for (let index = 0; index < chart.getNSeries().getCount(); index++) {
// Access the DataLabels of indexed NSeries
const labels = chart.getNSeries().get(index).getDataLabels();

// Set ResizeShapeToFitText property to true
labels.setIsResizeShapeToFitText(true);
}

// Calculate Chart
chart.calculate();
}

// Save the result
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

