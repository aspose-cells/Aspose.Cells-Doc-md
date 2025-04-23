---
title: 行や範囲をコピーしながらチャートのデータソースを宛先ワークシートに変更する方法（Node.js経由でC++）
linktitle: 行または範囲をコピーする際、チャートを新しいワークシートにコピーすると、チャートのデータソースは変更されません。
description: Aspose.Cells for Node.js via C++で行や範囲をコピーしながらチャートのデータソースを宛先ワークシートに変更する方法を学びます。このガイドは、チャートのデータ範囲を更新し、それを宛先ワークシートにリンクする方法を示します。
keywords: Aspose.Cells for Node.js via C++、チャーティング、データソース、宛先ワークシート、行、範囲、コピー、更新、データ範囲、リンク
type: docs
weight: 440
url: /ja/nodejs-cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/
---

## **可能な使用シナリオ**

チャートを含む行や範囲を新しいワークシートにコピーするとき、チャートのデータソースは変わりません。たとえば、チャートのデータソースが`=Sheet1!$A$1:$B$4`である場合、行または範囲を新しいワークシートにコピーしても、データソースは`=Sheet1!$A$1:$B$4`のままです。これはMicrosoft Excelでも同じ動作です。しかし、データソースを新しい宛先ワークシートにしたい場合は、[**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--)プロパティを`true`に設定し、[**Cells.copyRows(Cells, number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#copyRows-cells-number-number-number-)メソッドを呼び出すことで実現可能です。たとえば、宛先シートがDestSheetの場合、チャートのデータソースは`=Sheet1!$A$1:$B$4`から`=DestSheet!$A$1:$B$4`に変わります。

## **行や範囲をコピーする際に、チャートのデータソースを宛先ワークシートに変更する**

次のサンプルコードは、チャートを含む行や範囲を新しいワークシートにコピーする際に、[**CopyOptions.getReferToDestinationSheet()**](https://reference.aspose.com/cells/nodejs-cpp/copyoptions/#getReferToDestinationSheet--)プロパティの使用例を示しています。このコードは[サンプルExcelファイル](5113699.xlsx)を使用し、[出力Excelファイル](5113697.xlsx)を生成します。

![todo:image_alt_text](change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load sample excel file
const wb = new AsposeCells.Workbook(filePath);

// Access the first sheet which contains chart
const source = wb.getWorksheets().get(0);

// Add another sheet named DestSheet
const destination = wb.getWorksheets().add("DestSheet");

// Set CopyOptions.ReferToDestinationSheet to true
const options = new AsposeCells.CopyOptions();
options.setReferToDestinationSheet(true);

// Copy all the rows of source worksheet to destination worksheet which includes chart as well
// The chart data source will now refer to DestSheet
destination.getCells().copyRows(source.getCells(), 0, 0, source.getCells().getMaxDisplayRange().getRowCount(), options);

// Save workbook in xlsx format
wb.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```
