---  
title: Node.js（C++経由）で指定された有効数字をExcelファイルに保存する方法  
linktitle: Excelファイルに保存する有効桁数を指定する  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/specifying-significant-digits-to-be-stored-in-excel-file/  
description: Aspose.Cells for Node.js via C++を使用して、Excelファイルに保存する有効数字を指定する方法を学びます。  
---  

## **可能な使用シナリオ**  

デフォルトでは、Aspose.Cells for Node.js via C++はExcelファイル内にダブル値の17桁の有効数字を格納しますが、MS-Excelは15桁のみを格納します。Aspose.Cellsのデフォルトの動作を17桁から15桁に変更するには [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) プロパティを使用します。  

## **Excelファイルに保存する有効桁数を指定**  

以下のサンプルコードは、4835値をExcelファイルに保存する際にAspose.Cellsに15桁の有効数字を強制的に使用させるものです。出力されるExcelファイル（22774105.xlsx）を確認してください。拡張子を.zipに変更して解凍すると、15桁のみが保存されているのがわかります。以下のスクリーンショットは [**CellsHelper.getSignificantDigits()**](https://reference.aspose.com/cells/nodejs-cpp/cellshelper/#getSignificantDigits--) プロパティが出力Excelファイルに与える影響を示しています。  

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// By default, Aspose.Cells stores 17 significant digits unlike
// MS-Excel which stores only 15 significant digits
AsposeCells.CellsHelper.setSignificantDigits(15);

// Create workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access cell A1
const c = worksheet.getCells().get("A1");

// Put double value, only 15 significant digits as specified by
// CellsHelper.SignificantDigits above will be stored in excel file just like MS-Excel does
c.putValue(1234567890.123451711);

// Save the workbook
workbook.save(path.join(dataDir, "out_SignificantDigits.xlsx"));
```  

