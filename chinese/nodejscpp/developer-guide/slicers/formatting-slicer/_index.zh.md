---  
title: 使用Node.js通过C++格式化切片器  
linktitle: 格式化切片器  
type: docs  
weight: 20  
url: /zh/nodejs-cpp/formatting-slicer/  
---  

## **可能的使用场景**  

您可以通过设置列数或样式等方式在Microsoft Excel中格式化切片器。Aspose.Cells for Node.js via C++还允许您使用[**Slicer.getNumberOfColumns()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getNumberOfColumns--)和[**Slicer.getStyleType()**](https://reference.aspose.com/cells/nodejs-cpp/slicer/#getStyleType--)属性进行此操作。  

## **格式化切片器**  

请参阅以下代码，它加载了包含切片器的[sample Excel file](67338473.xlsx)。它访问该切片器并设置其列数和样式类型，然后将其保存为[output Excel file](67338474.xlsx)。截图展示了在执行示例代码后切片器的外观。  

![todo:image_alt_text](formatting-slicer_1.png)  

## **示例代码**  

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

