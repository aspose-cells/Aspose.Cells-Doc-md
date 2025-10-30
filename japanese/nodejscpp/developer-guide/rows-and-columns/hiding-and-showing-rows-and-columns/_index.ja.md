---
title: Node.js経由のC++を使った行と列の非表示と表示
linktitle: 行と列の非表示および表示
type: docs
weight: 60
url: /ja/nodejs-cpp/hiding-and-showing-rows-and-columns/
description: Aspose.Cells for Node.js via C++を使ってワークシートの行と列を非表示・表示する方法を学びます。
---

{{% alert color="primary" %}}

時々、ワークシートに特定の行または列を非表示にして後で表示することが理にかなっています。Microsoft Excelはこの機能を提供し、Aspose.Cellsも同様です。

{{% /alert %}}

## **行と列の可視性の制御**

Aspose.Cells for Node.js via C++は、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスを提供します。 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)クラスには、Excelファイル内の各ワークシートにアクセスできる[**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection)が含まれています。ワークシートは[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)クラスは、そのシート内のすべてのセルを表す[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションを提供します。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)コレクションには、ワークシートの行や列を管理するためのいくつかのメソッドがあります。以下にいくつかを説明します。

### **行と列の非表示**

開発者は、[**hideRow(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRow-number-)と[**hideColumn(number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumn-number-)のメソッドを呼び出すことで、行や列を非表示にできます。どちらのメソッドも、特定の行や列のインデックスをパラメータとして受け取り、その行または列を非表示にします。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with Uint8Array
const workbook = new AsposeCells.Workbook(new Uint8Array(fileBuffer));

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Hiding the 3rd row of the worksheet
worksheet.getCells().hideRow(2);

// Hiding the 2nd column of the worksheet
worksheet.getCells().hideColumn(1);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.out.xls"));
```

{{% alert color="primary" %}}

また、行または列を非表示にすることもできます。その際は、行の高さまたは列の幅をそれぞれ0に設定することができます。

{{% /alert %}}

### **行と列の表示**

開発者は、[**unhideRow(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRow-number-number-)と[**unhideColumn(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumn-number-number-)のメソッドを呼び出すことで、非表示になっている行や列を表示させることができます。どちらのメソッドも、2つのパラメータを取ります：

- **行または列のインデックス** - 特定の行または列を表示するために使用される行または列のインデックス。
- **行の高さまたは列の幅** - 非表示にする行または列に割り当てられた行の高さまたは列の幅。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");
// Read the Excel file into a Buffer (Uint8Array)
const fileBuffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file buffer
const workbook = new AsposeCells.Workbook(fileBuffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unhiding the 3rd row and setting its height to 13.5
worksheet.getCells().unhideRow(2, 13.5);

// Unhiding the 2nd column and setting its width to 8.5
worksheet.getCells().unhideColumn(1, 8.5);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

{{% alert color="primary" %}}

隠された列を表示状態に戻す際に、以前設定した幅や元の幅に復元する必要がある場合は、負の幅を使用して列の非表示を解除してください。例：worksheet.cells.unhideColumn(5, -1)

{{% /alert %}}

### **複数の行および列の非表示**

開発者は、[**hideRows(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideRows-number-number-)と[**hideColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#hideColumns-number-number-)のメソッドを呼び出し、複数の行や列を一度に非表示にできます。これらの両方のメソッドは、開始行または列のインデックスと隠す行または列の数をパラメータとして受け取ります。

```javascript
const fs = require("fs");
const path = require("path");
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

// Hiding 3, 4, and 5 rows in the worksheet
worksheet.getCells().hideRows(2, 3);

// Hiding 2 and 3 columns in the worksheet
worksheet.getCells().hideColumns(1, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "outputxls"));
```

{{% alert color="primary" %}}

また、[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)クラスの[**unhideRows(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideRows-number-number-number-)と[**unhideColumns(number, number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#unhideColumns-number-number-number-)メソッドを使って複数の行や列を表示状態にすることも可能です。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
