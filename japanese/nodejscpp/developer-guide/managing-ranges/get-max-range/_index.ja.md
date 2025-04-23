---  
title: Node.jsを使った最大範囲の取得（C++経由）  
linktitle: ワークシート内の最大範囲を取得する  
type: docs  
weight: 360  
url: /ja/nodejs-cpp/get-max-range-in-a-worksheet/  
description: この記事では、Aspose.Cells for Node.js via C++を使ってExcelファイルの最大範囲、最大データ範囲、最大表示範囲を取得する方法について説明します。  
---  

{{% alert color="primary" %}}  

ワークシートからデータを読み取る場合、最大範囲を知る必要があります。  

ワークシートからすべてのデータをコピーする場合、最大範囲を知る必要があります。  

HTMLおよびPDFに指定された範囲をエクスポートする際、最大範囲を把握する必要があります。  

Aspose.Cells for Node.js via C++はいくつかの方法でワークシートの最大範囲を見つけることができます。  

{{% /alert %}}  

## **最大範囲を取得する**  
Aspose.Cellsでは、[**row**](https://reference.aspose.com/cells/nodejs-cpp/row/)と[**column**](https://reference.aspose.com/cells/nodejs-cpp/column/)オブジェクトが初期化されている場合、空の行や列にデータがなくても、これらの行と列が最大範囲としてカウントされます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Loads the workbook
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxRow();
let maxColumn = sheet.getCells().getMaxColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxRow();
maxColumn = sheet.getCells().getMaxColumn();
// The range is updated to A1:B10.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **最大データ範囲を取得する**  
ほとんどの場合、空のセルが範囲外にある場合でも、すべてのデータを含むすべての範囲を取得する必要があります。  
また、シェイプ、テーブル、ピボットテーブルに関する設定は無視されます。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "SampleSheet.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();
const sheet = worksheets.get(0);

// Gets the max data range.
let maxRow = sheet.getCells().getMaxDataRow();
let maxColumn = sheet.getCells().getMaxDataColumn();
// The range is A1:B3.
let range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);

sheet.getCells().get("A10").putValue(null);

maxRow = sheet.getCells().getMaxDataRow();
maxColumn = sheet.getCells().getMaxDataColumn();
// The range is still A1:B3.
range = sheet.getCells().createRange(0, 0, maxRow + 1, maxColumn + 1);
```  

## **最大表示範囲を取得する**  
ワークシートからすべてのデータをHTML、PDF、または画像にエクスポートする場合、データ、スタイル、グラフィック、表、およびピボットテーブルを含むすべての可視オブジェクトを含むエリアを取得する必要があります。  
以下のコードは、最大表示範囲をHTMLにレンダリングする方法を示しています：  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Instantiate a new Workbook.
const workbook = new AsposeCells.Workbook(filePath);

// Get all the worksheets in the book.
const worksheets = workbook.getWorksheets();

// Gets the max display range.
const range = worksheets.get(0).getCells().getMaxDisplayRange();

// Save the range to html
const saveOptions = new AsposeCells.HtmlSaveOptions();
saveOptions.setExportActiveWorksheetOnly(true);
saveOptions.setExportArea(AsposeCells.CellArea.createCellArea(range.getFirstRow(), range.getFirstColumn(), range.getFirstRow() + range.getRowCount() - 1, range.getFirstColumn() + range.getColumnCount() - 1));

// Save the range.
workbook.save("html.html", saveOptions);
```  

以下は[ソースエクセルファイル](Book1.xlsx)です。  

