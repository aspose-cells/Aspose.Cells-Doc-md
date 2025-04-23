---  
title: Node.jsとC++を使用したExcelからJSONへの変換  
linktitle: ExcelをJSONに変換  
type: docs  
weight: 300  
url: /ja/nodejs-cpp/convert-excel-to-json/  
description: ExcelファイルをJSONに変換する方法を学びます（Aspose.Cells for Node.js via C++を使用）。  
keywords: WorkbookをJSONにエクスポート（Node.jsとC++を使用） ※ExcelをJSONに変換  
---  

{{% alert color="primary" %}}  
Aspose.Cellsは、WorkbookをJSON（JavaScript Object Notation）ファイルに変換することをサポートしています。  
{{% /alert %}}  

## **ExcelワークブックをJSONに変換**  

Excel WorkbookをJSONに変換する方法については、Aspose.Cells for Node.js via C++ライブラリが最適なソリューションを提供します。Aspose.Cells APIは、スプレッドシートをJSON形式に変換するサポートを提供します。ワークブックをJSONにエクスポートするには、[**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat/)を[**Workbook.save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-)メソッドの第2パラメータとして渡します。また、[**JsonSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/jsonsaveoptions/)クラスを使用して、ワークシートのエクスポート設定を追加で指定することもできます。  

以下のコード例は、ExcelワークブックをJSONにエクスポートする例です。変換されたJSONファイルは、[ソースファイル](sample.xlsx)をコードにより変換した結果を参考にしてください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json");
```  

以下のコード例は、JsonSaveOptionsクラスを使用して追加設定を指定し、ExcelワークブックをJSONにエクスポートする例です。変換されたJSONファイルは、[ソースファイル](sample.xlsx)をコードにより変換した結果を参考にしてください。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Create an options of saving the file.
const options = new AsposeCells.JsonSaveOptions();

// Set the exporting range.
options.setExportArea(AsposeCells.CellArea.createCellArea("B1", "C4"));

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save("sample_out.json", options);
```  


