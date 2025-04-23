---
title: Excelファイルの行と列の挿入と削除
linktitle: Excelファイルの行と列の挿入と削除
type: docs
weight: 70
url: /ja/nodejs-cpp/inserting-and-deleting-rows-and-columns/
description: この記事では、Aspose.Cells for Node.js via C++ APIを使った行および列の挿入と削除方法を紹介します。
keywords: Aspose.Cells Node.js via C++で行や列の管理、挿入、削除
---

## **紹介**

ワークシートをゼロから作成するか、既存のワークシートで作業する場合、さらなるデータを収容するために追加の行や列を必要とする場合があります。逆に、ワークシート内の特定の位置から行や列を削除する必要がある場合もあります。 
これらの要件を満たすために、Aspose.Cells for Node.js via C++は非常にシンプルなクラスとメソッドのセットを提供します。以下に説明します。

### **行と列の管理**

Aspose.Cells for Node.js via C++はMicrosoft Excelファイルを表すクラス[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)を提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイルの各ワークシートにアクセスできる[**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)コレクションがあります。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、そのシート内のすべてのセルを表す[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションを提供します。

[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--)コレクションは、ワークシートの行と列を管理するいくつかのメソッドを提供します。詳細は以下に説明します。

{{% alert color="primary" %}}

行や列を追加すると、ワークシート内の内容が下または右にシフトされ、削除すると上または左にシフトされます。

{{% /alert %}}


## **行と列の挿入**

### **行の挿入方法**

[**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) コレクションの[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) メソッドを呼び出すことで、ワークシートの任意の位置に行を挿入できます。[**insertRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRow-number-) メソッドは新しい行が挿入される行のインデックスを取ります。

```javascript
const path = require("path");
const fs = require("fs");
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

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRow(2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

### **複数の行を挿入する方法**

ワークシートに複数の行を挿入するには、[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) コレクションの[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) メソッドを呼び出します。[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) メソッドは2つのパラメータを取ります:

- 行インデックス、新しい行が挿入される行のインデックス。
- 行数、挿入する必要がある行の合計数。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

const fileData = fs.readFileSync(filePath);
const workbook = new AsposeCells.Workbook(fileData);

const worksheet = workbook.getWorksheets().get(0);
worksheet.getCells().insertRows(2, 10);

workbook.save(path.join(dataDir, "output.out.xls"));
```

### **書式付きで行を挿入する方法**

書式オプションを指定して行を挿入するには、パラメータとして[**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions)を取る[**insertRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertRows-number-number-boolean-) オーバーロードを使用します。[**InsertOptions**](https://reference.aspose.com/cells/nodejs-cpp/insertoptions)クラスの[**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/)プロパティを[**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) 列挙型で設定します。[**CopyFormatType**](https://reference.aspose.com/cells/nodejs-cpp/copyformattype/) 列挙型には次の3つのメンバーがあります。

- SameAsAbove: 上の行と同じ書式を適用します。
- SameAsBelow: 下の行と同じ書式を適用します。
- Clear: 書式をクリアします。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "book1.xls");
const fstream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fstream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Setting Formatting options
const insertOptions = new AsposeCells.InsertOptions();
insertOptions.setCopyFormatType(AsposeCells.CopyFormatType.SameAsAbove);

// Inserting a row into the worksheet at 3rd position
worksheet.getCells().insertRows(2, 1, insertOptions);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "InsertingARowWithFormatting.out.xls"));
```

### **列の挿入方法**

開発者は、[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) コレクションの[**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) メソッドを呼び出すことで、ワークシートの任意の位置に列を挿入することもできます。[**insertColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#insertColumn-number-boolean-) メソッドは、新しい列が挿入される列のインデックスを取ります。

```javascript
const fs = require('fs');
const path = require('path');
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Creating a file stream containing the Excel file to be opened
const fileStream = fs.readFileSync(filePath);

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fileStream);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Inserting a column into the worksheet at 2nd position
worksheet.getCells().insertColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

## **行と列の削除**

### **複数の行を削除する方法**

ワークシートから複数の行を削除するには、[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) コレクションの[**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) メソッドを呼び出します。[**deleteRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteRows-number-number-) メソッドは2つのパラメータを取ります:

- 行インデックス、削除される行のインデックス。
- 行数、削除する必要がある行の合計数。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Read file contents as Uint8Array
const fileContent = fs.readFileSync(filePath);
const fileBuffer = new Uint8Array(fileContent);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting 10 rows from the worksheet starting from 3rd row
worksheet.getCells().deleteRows(2, 10);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));
```


### **列を削除する方法**

ワークシートから任意の位置に列を削除するには、[**getCells()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getCells--) コレクションの[**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) メソッドを呼び出します。[**deleteColumn(number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#deleteColumn-number-boolean-) メソッドは削除する列のインデックスを取ります。

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Creating a file stream containing the Excel file to be opened
const filePath = path.join(dataDir, "Book1.xlsx");

// Instantiating a Workbook object
// Opening the Excel file through the file stream
const workbook = new AsposeCells.Workbook(fs.readFileSync(filePath));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Deleting a column from the worksheet at 5th position
worksheet.getCells().deleteColumn(4);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xlsx"));

// Closing resources is handled automatically by Node.js, no specific close needed.
```
