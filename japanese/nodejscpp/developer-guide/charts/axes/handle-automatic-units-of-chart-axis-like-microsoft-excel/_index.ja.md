---  
title: Microsoft Excelと同様の自動単位のチャート軸の処理をNode.jsとC++で行う方法  
linktitle: Microsoft Excelのようにチャートの軸の自動単位を処理する  
description: Aspose.Cells for Node.js via C++におけるチャート軸の自動単位の扱い方を学びましょう。ガイドは、自動単位の設定とカスタマイズ方法、科学表記の表示やスケール調整について説明します。  
keywords: Aspose.Cells for Node.js via C++、チャート軸、自動単位、Microsoft Excel、設定、カスタマイズ、科学表記、スケーリング。  
type: docs  
weight: 120  
url: /ja/nodejs-cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/  
---  

## **可能な使用シナリオ**  
初期のAspose.Cells for Node.js via C++では、チャートを画像やPDFにレンダリングしたときに自動単位を正しく処理できませんでしたが、現在は対応しています。コードの変更は不要です。チャートを画像やPDFに変換するだけでMicrosoft Excelと同じようにチャート軸がレンダリングされます。  

## **Microsoft Excelのようにチャートの軸の自動単位を処理する**  
次のサンプルコードは、[サンプルExcelファイル](61767755.xlsx)を読み込み、[出力PDFチャート](61767752.pdf)を生成します。スクリーンショットは、チャート軸の自動単位を赤い長方形で示し、サンプルExcelファイルのチャートと出力されたPDFのチャートを比較しています。両者は完全に一致しています。  

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)  

## **サンプルコード**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx");

// Load the sample Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first chart
const chart = worksheet.getCharts().get(0);

// Render chart to pdf
chart.toPdf("outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf");
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
