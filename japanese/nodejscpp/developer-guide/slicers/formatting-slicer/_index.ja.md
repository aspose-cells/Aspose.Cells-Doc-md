---  
title: Node.jsをC++経由でスライサーをフォーマット  
linktitle: スライサーの書式を設定する  
type: docs  
weight: 20  
url: /ja/nodejs-cpp/formatting-slicer/  
---  

## **可能な使用シナリオ**  

Microsoft Excelでスライサーの列数やスタイルを設定してフォーマットできます。Aspose.Cells for Node.js via C++は、[**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--)や[**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--)のプロパティを使用してこれも行えます。  

## **スライサーの書式設定**  

以下のコードをご覧ください。スライサーを含む[sample Excelファイル](67338473.xlsx)を読み込み、スライサーにアクセスしてその列数やスタイルタイプを設定し、[output Excelファイル](67338474.xlsx)として保存します。スクリーンショットは、サンプルコードの実行後のスライサーの見た目を示しています。  

![todo:image_alt_text](formatting-slicer_1.png)  

## **サンプルコード**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleFormattingSlicer.xlsx");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook(filePath);

// Access first worksheet.
const ws = wb.getWorksheets().get(0);

// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);

// Set the number of columns of the slicer.
slicer.setNumberOfColumns(2);

// Set the type of slicer style.
slicer.setStyleType(AsposeCells.SlicerStyleType.SlicerStyleLight6);

// Save the workbook in output XLSX format.
wb.save("outputFormattingSlicer.xlsx", AsposeCells.SaveFormat.Xlsx);
```  

