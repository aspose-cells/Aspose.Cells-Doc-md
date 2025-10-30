---
title: Node.js経由のC++で行と列のグループ化と解除
linktitle: 行と列のグループ化および展開
type: docs
weight: 50
url: /ja/nodejs-cpp/grouping-and-ungrouping-rows-and-columns/
description: Aspose.Cells for Node.js via C++を使用してExcelで行と列をグループ化および解除する方法を確認します。
--- 

## **紹介**

Microsoft Excelファイルでは、データの概要を作成して、1回のマウスクリックで詳細のレベルを表示したり非表示にしたりできます。

**アウトライン記号**の1、2、3、+、および-をクリックして、ワークシートのセクションの要約または見出しを迅速に表示したり、個々の要約または見出しの詳細を表示する際に使用できます。下の図で示されているように、個々の要約または見出しの詳細を表示するためにシンボルを使用できます。

|**行と列のグループ化**|
| :- |
|![todo:image_alt_text](grouping-and-ungrouping-rows-and-columns_1.png)|

## **行と列のグループ管理**

Aspose.Cellsは、Microsoft Excelファイルを表す [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) クラスにはExcelファイル内の各ワークシートにアクセスできる [**WorksheetCollection**](https://reference.aspose.com/cells/nodejs-cpp/worksheetcollection) が含まれます。ワークシートは [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスは、そのワークシート内のすべてのセルを表す [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) コレクションを提供します。

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) コレクションは、ワークシート内の行または列を管理するためのいくつかのメソッドを提供し、その中のいくつかを詳細に説明します。

### **行と列のグループ化**

[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) コレクションの [**groupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupRows-number-number-boolean-) および [**groupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#groupColumns-number-number-) メソッドを呼び出すことで、行や列をグループ化できます。両方のメソッドは次のパラメータを取ります：

- 最初の行/列インデックス、グループ内の最初の行または列
 - グループ内の最後の行/列のインデックス、最後の行または列。
- 非表示かどうか、グループ化後に行または列を非表示にするかどうかを指定するブールパラメータ。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading the Excel file into a buffer
const fs = require("fs");
const fileContent = fs.readFileSync(filePath);

// Opening the Excel file through the buffer
const workbook = new AsposeCells.Workbook(fileContent);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows (from 0 to 5) and making them hidden by passing true
worksheet.getCells().groupRows(0, 5, true);

// Grouping first three columns (from 0 to 2) and making them hidden by passing true
worksheet.getCells().groupColumns(0, 2, true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

#### **グループ設定**

Microsoft Excelでは、以下を表示するためのグループ設定を構成できます:

- 詳細の下の要約行。
- 詳細の右側の要約列。

これらのグループ設定は、[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) クラスの [**getOutline()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#getOutline--) プロパティを使用して構成できます。

### **詳細の下にサマリー行**

詳細の下にサマリ行を表示するかどうかを制御するには、[**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) クラスの [**getSummaryRowBelow()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryRowBelow--) プロパティを **true** か **false** に設定します。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

// Setting SummaryRowBelow property to false
worksheet.getOutline().setSummaryRowBelow(false);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

### **詳細の右側にサマリー列**

詳細の右側にサマリ列を表示するかどうかも、[**Outline**](https://reference.aspose.com/cells/nodejs-cpp/outline) クラスの [**getSummaryColumnRight()**](https://reference.aspose.com/cells/nodejs-cpp/outline/#getSummaryColumnRight--) プロパティを **true** か **false** に設定することで制御できます。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);
const worksheet = workbook.getWorksheets().get(0);

// Grouping first six rows and first three columns
worksheet.getCells().groupRows(0, 5, true);
worksheet.getCells().groupColumns(0, 2, true);

worksheet.getOutline().setSummaryColumnRight(true);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```

## **行と列のグループ解除**

グループ化された行や列を解除するには、[**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) コレクションの [**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) および [**ungroupColumns(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupColumns-number-number-) メソッドを呼び出します。両方のメソッドには2つのパラメータが必要です：

- 最初の行または列のインデックス、グループ化を解除する最初の行/列。
- 最後の行または列のインデックス、グループ化を解除する最後の行/列。

[**ungroupRows(number, number, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/cells/#ungroupRows-number-number-boolean-) には、Booleanの第3パラメータを取るオーバーロードがあります。それを **true** に設定すると、すべてのグループ情報が削除されます。そうでなければ、外側のグループ情報だけが削除されます。

```javascript
const path = require("path");
const fs = require("fs");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Reading Excel file into buffer
const buffer = fs.readFileSync(filePath);

// Instantiating a Workbook object with file content
const workbook = new AsposeCells.Workbook(buffer);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Ungrouping first six rows (from 0 to 5)
worksheet.getCells().ungroupRows(0, 5);

// Ungrouping first three columns (from 0 to 2)
worksheet.getCells().ungroupColumns(0, 2);

// Saving the modified Excel file
workbook.save(path.join(dataDir, "output.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
