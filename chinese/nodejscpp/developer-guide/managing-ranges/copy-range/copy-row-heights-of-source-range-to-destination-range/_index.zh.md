---  
title: 使用Node.js via C++复制源范围的行高到目标范围  
linktitle: 将源范围行高度复制到目标范围  
type: docs  
weight: 590  
url: /zh/nodejs-cpp/copy-row-heights-of-source-range-to-destination-range/  
---  

{{% alert color="primary" %}}  

有时，用户需要将源范围的行高复制到目标范围。Aspose.Cells for Node.js via C++提供了[**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/)枚举用于此目的。当你用[**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/)设置[**PasteOptions.getPasteType()**](https://reference.aspose.com/cells/nodejs-cpp/pasteoptions/#getPasteType--)属性时，源范围内所有行的行高将被复制到目标范围。  

{{% /alert %}}  

以下示例代码说明了如何使用[**PasteType.RowHeights**](https://reference.aspose.com/cells/nodejs-cpp/pastetype/)枚举将源范围的行高复制到目标范围。一旦在Microsoft Excel中打开由此代码生成的输出文件，你会看到目标范围的行高与源范围完全一致。  

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

