---  
title: Node.js経由C++を使用した共有数式の最大行数指定  
linktitle: 共有式の最大行数を指定  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/specify-maximum-rows-of-shared-formula/  
description: Aspose.Cells for Node.js via C++ を使用して共有数式の最大行数を指定する方法を学びます。  
---  

## **可能な使用シナリオ**  

 共有数式のデフォルト最大行数は64です。これを任意の数値（例：1000）に変更できます。共有数式の行数によってパフォーマンスが変動します。そのため、Aspose.Cellsは[**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--)プロパティを提供し、これを使って最大行数を設定できます。共有数式の総行数がこれを超えると、複数の共有数式に分割されます。以下のスクリーンショットは、その設定例を示しています。  

![todo:image_alt_text](specify-maximum-rows-of-shared-formula_1.png)  

## **共有式の最大行数を指定**  

 [**WorkbookSettings.getMaxRowsOfSharedFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getMaxRowsOfSharedFormula--)プロパティの使用例を示すサンプルコードです。最大行数を5に設定し、セルD1に100行分の共有数式を追加し、[出力Excelファイル](61767856.xlsx)に保存します。出力Excelの内容を展開し、*sheet1.xml*を確認すると、各5行ごとに分割された共有数式が見えます。  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Create a new workbook
const wb = new AsposeCells.Workbook();

// Set the max rows of shared formula to 5
wb.getSettings().setMaxRowsOfSharedFormula(5);

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Access cell D1
const cell = ws.getCells().get("D1");

// Set the shared formula in 100 rows
cell.setSharedFormula("=Sum(A1:A2)", 100, 1);

// Save the output Excel file
wb.save("outputSpecifyMaximumRowsOfSharedFormula.xlsx");
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
