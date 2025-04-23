---  
title: Node.jsとC++を使用してワークシートタブの色を設定する方法  
linktitle: ワークシートタブの色を設定  
type: docs  
weight: 120  
url: /ja/nodejs-cpp/set-worksheet-tab-color/  
description: この資料は、Node.jsとC++を使用してExcelのワークシートタブの色をプログラムで設定するサンプルコードを示します。  
keywords: Excelタブの色を設定するNode.jsとC++のコード例  
---  

{{% alert color="primary" %}}  

Aspose.Cells を使用すると、個々のワークシートタブの色を変更して目立たせることができます。たとえば、Expenses を赤、Sales を緑、Assets を青などにすることができます。

{{% /alert %}}  
## **Microsoft Excel でワークシートのタブの色を設定する**  
1. 現在のワークシートの下部にあるタブシートでタブを右クリックします。  
1. **タブの色**を選択します。  
1. パレットから色を選択します。  
1. **OK** をクリックします。  
## **Aspose.Cellsでワークシートのタブの色を設定する**  
以下のサンプルコードは、Aspose.Cellsでタブの色を設定する方法を示しています。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Instantiate a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xlsx"));

// Get the first worksheet in the book
const worksheet = workbook.getWorksheets().get(0);

// Set the tab color
worksheet.setTabColor(AsposeCells.Color.Red);

// Save the Excel file
workbook.save(path.join(dataDir, "worksheettabcolor.out.xls"));
```  

