---  
title: 使用 Node.js 和 C++ 将每个工作表保存为不同的 PDF 文件  
linktitle: 将每个工作表保存为不同的PDF文件  
type: docs  
weight: 130  
url: /zh/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/  
---  

{{% alert color="primary" %}}  
Aspose.Cells 支持将包含图片、图表等的 XLS 文件转换为 PDF。Aspose.Cells for Node.js via C++ 可以单独完成表格到 PDF 的转换，无需使用 Aspose.PDF for Node.js via C++。该转换过程无需创建或使用任何临时文件，全部操作可在内存中完成。  
{{% /alert %}}  

## **将每个工作表保存为不同的PDF文件**  
 如果您需要将模板 Excel 文件中的每个工作表保存为不同的 PDF 文件，您可以轻松实现。可以尝试每次设置一个工作表索引为 [**PdfSaveOptions.SheetSet**](https://reference.aspose.com/cells/nodejs-cpp/pdfs saveoptions/#sheetSet) 选项进行渲染到 PDF。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Get the Excel file path
const filePath = path.join(dataDir, "input.xlsx");

// Instantiate a new workbook and open the Excel file from its location
const workbook = new AsposeCells.Workbook(filePath);

// Get the count of the worksheets in the workbook
const sheetCount = workbook.getWorksheets().getCount();

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Take PDFs of each sheet
for (let j = 0; j < sheetCount; j++) {
const ws = workbook.getWorksheets().get(j);

// set worksheet to output
const sheetSet = new AsposeCells.SheetSet([ws.getIndex()]);
pdfSaveOptions.setSheetSet(sheetSet);

workbook.save(path.join(dataDir, `worksheet-${ws.getName()}.out.pdf`), pdfSaveOptions);
}
```  

{{% alert color="primary" %}}  
如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。  
{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
