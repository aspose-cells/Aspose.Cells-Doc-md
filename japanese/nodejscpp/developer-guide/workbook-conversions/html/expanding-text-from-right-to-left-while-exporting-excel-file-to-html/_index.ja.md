---  
title: ExcelファイルをHTMLにエクスポートする際に、右から左へのテキスト展開  
linktitle: Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開  
type: docs  
weight: 60  
url: /ja/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/  
---  

{{% alert color="primary" %}}  

Aspose.Cells は、Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開する機能を v8.9.0.0 以降でサポートしています。元の Excel ファイルに右から左に展開するテキストが含まれている場合、Aspose.Cells はそれを適切に HTML にエクスポートします。  

{{% /alert %}}  
## **Excel ファイルを HTML にエクスポートする際にテキストを右から左に展開**  
[サンプルexcelファイル](5115502.xlsx)をHTMLに変換するサンプルコードは次のとおりです。このスクリーンショットは、サンプルExcelがMicrosoft Excel 2013でどのように表示されるかを示しています。  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_1.png)  

このスクリーンショットは、古いバージョンで生成された[output HTML](5115509)を示しています。  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_2.png)  

このスクリーンショットは、新しいバージョンで生成された[output HTML](5115508)を示しています。  

![todo:image_alt_text](expanding-text-from-right-to-left-while-exporting-excel-file-to-html_3.png)  

スクリーンショットに示されるように、新しいバージョンでは右寄せされたテキストを Microsoft Excel と同様に適切に左に展開します。  


```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load source excel file inside the workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save workbook in html format
wb.save(path.join(dataDir, `ExpandTextFromRightToLeft_out_${AsposeCells.CellsHelper.getVersion()}.html`), AsposeCells.SaveFormat.Html);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
