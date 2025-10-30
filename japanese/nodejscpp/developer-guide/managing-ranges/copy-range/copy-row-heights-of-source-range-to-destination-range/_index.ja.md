---  
title: ソース範囲の行の高さを宛先範囲にコピーする（Node.jsとC++）  
linktitle: ソース範囲の行の高さを宛先範囲にコピー  
type: docs  
weight: 590  
url: /ja/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

ユーザーは、ソース範囲の行の高さを宛先範囲にコピーする必要がある場合があります。Aspose.Cells for Node.js via C++はこの目的のために[**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/)列挙型を提供しています。[**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--)プロパティに[**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/)を設定すると、ソース範囲内のすべての行の高さが宛先範囲にコピーされます。  

{{% /alert %}}  

以下のサンプルコードは、[**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/)列挙型を使用して、ソース範囲の行の高さを宛先範囲にコピーする方法を示しています。このコードで生成されたExcelファイルをMicrosoft Excelで開くと、宛先範囲の行の高さがソース範囲と完全に一致していることがわかります。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook();

// Source worksheet
const srcSheet = workbook.getWorksheets().get(0);

// Add destination worksheet
const dstSheet = workbook.getWorksheets().add("Destination Sheet");

// Set the row height of the 4th row. This row height will be copied to destination range
srcSheet.getCells().setRowHeight(3, 50);

// Create source range to be copied
const srcRange = srcSheet.getCells().createRange("A1:D10");

// Create destination range in destination worksheet
const dstRange = dstSheet.getCells().createRange("A1:D10");

// PasteOptions, we want to copy row heights of source range to destination range
const opts = new AsposeCells.PasteOptions();
opts.setPasteType(AsposeCells.PasteType.RowHeights);

// Copy source range to destination range with paste options
dstRange.copy(srcRange, opts);

// Write informative message in cell D4 of destination worksheet
dstSheet.getCells().get("D4").putValue("Row heights of source range copied to destination range");

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
