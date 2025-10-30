---  
title: Node.jsとC++で行列や列の書式設定  
linktitle: 行と列  
type: docs  
weight: 100  
url: /ja/nodejs-cpp/adjusting-row-height-and-column-width/  
description: Aspose.Cells for Node.js via C++は、行の高さや列の幅を変更したり、行や列に書式を適用したりすることをサポートします。  
keywords: 行の高さと列の幅を設定し、行の高さと列の幅を調整し、行の高さや列の幅を変更し、行と列の書式を設定する方法  
---  

{{% alert color="primary" %}}  
スプレッドシートで行や列にデータを追加する際、行の高さや列の幅を変更する必要がある場合があります。時には、行や列に書式を適用するときに、現在の高さや幅を変えてデータを見やすくすることもあります。通常、Microsoft ExcelのWYSIWYG環境で行高や列幅を調整しますが、Aspose.Cellsを用いると、Runtime中にこれらの操作を行うことができます。  
{{% /alert %}}  

## **行で操作する**  

### **行の高さの調整方法**  

Aspose.Cellsは、[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)というMicrosoft Excelファイルを表すクラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)があります。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表され、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスはすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションを提供します。  

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションは、ワークシート内の行や列を管理するための複数のメソッドを提供します。以下に詳細を説明します。  

### **行の高さを設定する方法**  

単一の行の高さを設定するには、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-)メソッドを呼び出します。[**setRowHeight(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setRowHeight-number-number-)メソッドは次のパラメータを取ります：

- **行インデックス**：高さを変更する行のインデックス。  
- **行の高さ**：行に適用する行の高さ。

```javascript
try {
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Creating a file stream containing the Excel file to be opened
const fstream = fs.createReadStream(filePath);

// Reading the file stream into a buffer
const chunks = [];
fstream.on('data', chunk => chunks.push(chunk));
fstream.on('end', () => {
const buffer = Buffer.concat(chunks);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of the second row to 13
worksheet.getCells().setRowHeight(1, 13);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream.close();
```  

### **ワークシート内のすべての行の高さを設定する方法**  

全ての行の同じ高さを設定したい場合は、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**getStandardHeight()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardHeight--)プロパティを使用して行えます。  

**例:**  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the height of all rows in the worksheet to 15
worksheet.getCells().setStandardHeight(15);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// (Note: Closing the file stream is unnecessary in this context as it's a 
// synchronous read performed using fs.readFileSync, which does not require
// explicit closure, but if using fs.createReadStream, you would handle it accordingly)
```  

## **列で操作する**  

### **列の幅を設定する方法**  

列の幅を設定するには、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-)メソッドを呼び出します。[**setColumnWidth(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidth-number-number-)メソッドは次のパラメータを取ります：  

- **列インデックス**：幅を変更する列のインデックス。  
- **列の幅**：設定したい列の幅。  

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of the second column to 17.5
worksheet.getCells().setColumnWidth(1, 17.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
fstream; // Note: No explicit close needed for fs.readFileSync
```  

### **ピクセル単位で列幅を設定する方法**  

列の幅を設定するには、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-)メソッドを呼び出します。[**setColumnWidthPixel(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#setColumnWidthPixel-number-number-)メソッドは次のパラメータを取ります：  

- **列インデックス**：幅を変更する列のインデックス。  
- **列の幅**、ピクセル単位での所望の列の幅。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
const outDir = path.join(__dirname, "output");

// Load source Excel file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the width of the column in pixels
worksheet.getCells().setColumnWidthPixel(7, 200);

workbook.save(path.join(outDir, "SetColumnWidthInPixels_Out.xlsx"));
```  

### **ワークシート内のすべての列の幅を設定する方法**  

全列に対して同じ幅を設定したい場合は、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションの[**getStandardWidth()**](https://reference.aspose.com/cells/nodejs-cpp/cells/#getStandardWidth--)プロパティを使用します。  

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
// Opening the Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting the width of all columns in the worksheet to 20.5
worksheet.getCells().setStandardWidth(20.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));

// Closing the file stream to free all resources
// No explicit close needed in Node.js
```  

## **高度なトピック**  
- [行と列の自動調整](/cells/ja/nodejs-cpp/autofit-rows-and-columns/)  
- [Aspose.Cellsを使用したテキストを列に変換する](/cells/ja/nodejs-cpp/convert-text-to-columns-using-aspose-cells/)  
- [行と列のコピー](/cells/ja/nodejs-cpp/copying-rows-and-columns/)  
- [ワークシート内の空白の行と列を削除](/cells/ja/nodejs-cpp/delete-blank-rows-and-columns-in-a-worksheet/)  
- [行と列のグループ化および解除](/cells/ja/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/)  
- [行と列の非表示および表示](/cells/ja/nodejs-cpp/hiding-and-showing-rows-and-columns/)  
- [Excelワークシートに行を挿入または削除](/cells/ja/nodejs-cpp/insert-or-delete-rows-in-an-excel-worksheet/)  
- [Excelファイルの行と列の挿入と削除](/cells/ja/nodejs-cpp/inserting-and-deleting-rows-and-columns/)  
- [ワークシート内の重複する行を削除する](/cells/ja/nodejs-cpp/remove-duplicate-rows-in-a-worksheet/)  
- [ワークシート内の空白の列と行を削除する際に、他のワークシートの参照を更新する](/cells/ja/nodejs-cpp/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
