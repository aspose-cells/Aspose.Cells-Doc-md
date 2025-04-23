---  
title: Node.jsを使用してC++経由でワークシート内のセル範囲を移動する  
linktitle: ワークシート内のセルの範囲を移動する  
type: docs  
weight: 370  
url: /ja/nodejs-cpp/move-range-of-cells-in-a-worksheet/  
description: Aspose.Cells for Node.js via C++を使用して、ワークシート内のセル範囲を移動する方法を学びます。  
---  

{{% alert color="primary" %}}  
この記事では、ワークシート内のセルの範囲を移動する方法を示しています。  
{{% /alert %}}  

## **ワークシート内のセルの範囲を移動する**  
例のコードは、タスクをデモンストレーションするためにテンプレートファイルを使用しています。  

**入力ファイル**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)  

次に、範囲A1:B5をC1:D5に移動した生成されたファイルをご覧ください。  

**出力ファイル**  

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xlsx");
// Instantiate the workbook object. Open the Excel file
const workbook = new AsposeCells.Workbook(filePath);

const cells = workbook.getWorksheets().get(0).getCells();

const range = cells.createRange("A1", "B5");
//move the range to right.
range.moveTo(0, 2);
```  

