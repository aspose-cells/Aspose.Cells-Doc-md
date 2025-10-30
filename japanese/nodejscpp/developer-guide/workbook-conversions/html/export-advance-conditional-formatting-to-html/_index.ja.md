---  
title: DataBar、ColorScale、IconSetの条件付き書式をExcelからHTMLにエクスポート（Node.js経由でC++）  
linktitle: Excel を HTML に変換する際の DataBar、ColorScale、および IconSet 条件付き書式をエクスポート  
type: docs  
weight: 30  
url: /ja/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/  
---  

{{% alert color="primary" %}} 

ExcelファイルをHTMLに変換するとき、DataBar、ColorScale、IconSetの条件付き書式もエクスポートできます。この機能はMicrosoft Excelでは部分的にサポートされていますが、Aspose.Cells for Node.js via C++は完全にサポートしています。

{{% /alert %}}  

## **Excel を HTML に変換する際の DataBar、ColorScale、および IconSet 条件付き書式をエクスポート**  
[サンプルexcelファイル](5115558.xlsx)はDataBar、ColorScale、IconSet条件付き書式設定を含んでいます。指定されたリンクから[サンプルexcelファイル](5115558.xlsx)をダウンロードできます。  

![todo:image_alt_text](conversion_1.png)  

Aspose.Cellsの出力HTMLファイルを使用したDataBar、ColorScale、IconSet条件付き書式設定を示す次のスクリーンショットです。ご覧の通り、これは[サンプルexcelファイル](5115558.xlsx)とまったく同じように見えます。  

![todo:image_alt_text](conversion_2.png)  

### **サンプルコード**  
以下のサンプルコードは、サンプルExcelファイルをHTMLに変換している例です。これは通常の[ExcelからHTMLへの変換]です。  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
