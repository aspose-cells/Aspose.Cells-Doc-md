---  
title: Aspose.Cells for Node.js via C++を使用して共有ワークブックを作成  
linktitle: Aspose.Cellsで共有ブックを作成する  
type: docs  
weight: 40  
url: /ja/nodejs-cpp/create-shared-workbook-with-aspose-cells/  
description: Aspose.Cells for Node.js via C++を使った共有ワークブックの作り方を学ぶ  
---  

## **可能な使用シナリオ**  

Microsoft Excelは、以下のスクリーンショットのようにワークブックを共有できます。共有すると、複数のユーザーがネットワーク上で編集可能になります。Aspose.Cells for Node.js via C++は[**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--)プロパティを使って共有ワークブックを作成可能です。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_1.png)  

## **Aspose.Cellsで共有ブックを作成する**  

以下のサンプルコードは、[**WorkbookSettings.getShared()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getShared--)プロパティを**true**に設定して共有ワークブックを作成します。Microsoft Excelで[出力Excelファイル](55541786.xlsx)を開くと、「共有」ステータスとともに出力済みのワークブック名が表示されます。  

![todo:image_alt_text](create-shared-workbook-with-aspose-cells_2.png)  

## **サンプルコード**  

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create Workbook object
const wb = new AsposeCells.Workbook();

// Share the Workbook
wb.getSettings().setShared(true);

// Save the Shared Workbook
wb.save("outputSharedWorkbook.xlsx");
```  

