---
title: Node.jsとC++を使用した日付軸の管理方法
description: Aspose.Cells for Node.js via C++を使用した日付軸の管理方法について学びます。ガイドでは、さまざまな日付フォーマット、時間スケール、ティックラベルの頻度について理解を深めます。
keywords: Aspose.Cells for Node.js、日付軸、管理、日付フォーマット、時間スケール、ティックラベル頻度
type: docs
weight: 200
url: /ja/nodejs-cpp/date-axis/
---

## **可能な使用シナリオ**
 ワークシートデータからチャートを作成し、日付を使っている場合、その日付が横軸（カテゴリ軸）にプロットされると、Aspose.Cells for Node.js via C++は自動的にカテゴリ軸を日付（時間スケール）軸に変更します。
日付軸は、特定の間隔や基本単位（日数、月、年など）で、ワークシートの日付を年代順に表示します。ワークシート上の日付が順次に並んでいない場合や基本単位が同じでない場合でも、表示されます。
 デフォルトでは、Aspose.Cellsはワークシートのデータ内の任意の2つの日付間の最小差に基づいて日付軸の基本単位を決定します。例として、株価データの最小差が7日間の場合、Excelは基本単位を日として設定しますが、長期のパフォーマンス表示のために月や年に変更できます。

## **Microsoft Excelのように日付軸を処理する**
新しいExcelファイルを作成し、最初のワークシートにチャートの値を配置するサンプルコードをご覧ください。 
その後、チャートを追加し、[**Axis**](https://reference.aspose.com/cells/nodejs-cpp/axis/)の種類を設定します。 
[**Axis.getCategoryType()**](https://reference.aspose.com/cells/nodejs-cpp/axis/#getCategoryType--)のタイプを設定し、その後基本単位を日に設定します。

![todo:image_alt_text](excel.png)

## **サンプルコード**
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
// Get the first worksheet
const worksheet = workbook.getWorksheets().get(0);
// Add the sample values to cells
worksheet.getCells().get("A1").putValue("Date");
// 14 means datetime format
const style = worksheet.getCells().getStyle();
style.setNumber(14);
// Put values to cells for creating chart
worksheet.getCells().get("A2").setStyle(style);
worksheet.getCells().get("A2").putValue(new Date(Date.UTC(2022, 5, 26)));
worksheet.getCells().get("A3").setStyle(style);
worksheet.getCells().get("A3").putValue(new Date(Date.UTC(2022, 4, 22)));
worksheet.getCells().get("A4").setStyle(style);
worksheet.getCells().get("A4").putValue(new Date(Date.UTC(2022, 7, 3)));
worksheet.getCells().get("B1").putValue("Price");
worksheet.getCells().get("B2").putValue(40);
worksheet.getCells().get("B3").putValue(50);
worksheet.getCells().get("B4").putValue(60);
// Add a chart to the worksheet
const chartIndex = worksheet.getCharts().add(AsposeCells.ChartType.Column, 9, 6, 21, 13);
// Access the instance of the newly added chart
const chart = worksheet.getCharts().get(chartIndex);
// Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
chart.setChartDataRange("A1:B4", true);         
// Set the Axis type to Date time
chart.getCategoryAxis().setCategoryType(AsposeCells.CategoryType.TimeScale);
// Set the base unit for CategoryAxis to days
chart.getCategoryAxis().setBaseUnitScale(AsposeCells.TimeUnit.Days);
// Set the direction for the axis text to be vertical
chart.getCategoryAxis().getTickLabels().setDirectionType(AsposeCells.ChartTextDirectionType.Vertical);
// Fill the PlotArea area with nothing 
chart.getPlotArea().getArea().getFillFormat().setFillType(AsposeCells.FillType.None);
// Set max value of Y axis.
chart.getValueAxis().setMaxValue(70);
// Set major unit.
chart.getValueAxis().setMajorUnit(10);
// Save the file
workbook.save("DateAxis.xlsx");
```
