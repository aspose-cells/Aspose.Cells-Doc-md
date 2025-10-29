---  
title: 每个 Excel 工作表渲染一页PDF  使用 Node.js 和 C++ 进行 Excel 转 PDF 转换  
linktitle: 将Excel工作表渲染为一份PDF页面  Excel转PDF转换  
type: docs  
weight: 100  
url: /zh/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/  
---  

{{% alert color="primary" %}}  

当处理大型 Microsoft Excel 文件（例如具有多个工作表、每个包含50列和300行或更多数据的工作簿）时，您可能希望 PDF 输出能每个工作表显示一页，而不考虑工作表的大小。这意味着每个页面的尺寸可能差异很大。这可以通过使用 Aspose.Cells for Node.js via C++ 实现。  

{{% /alert %}}  

请查看以下示例代码，将多个工作表的Excel文件转换为PDF。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Implement one page per worksheet option
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
pdfSaveOptions.setOnePagePerSheet(true);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile.out.pdf"), pdfSaveOptions);
```  

{{% alert color="primary" %}}  

如果将 [PdfSaveOptions.getOnePagePerSheet()](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getOnePagePerSheet--) 选项设置为**true**，所有工作表内容将被渲染到一个 PDF 页面中。  

{{% /alert %}} {{% alert color="primary" %}}  

如果您的电子表格包含公式，最好在将电子表格渲染为 PDF 之前调用 [Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。这可以确保公式相关的数值被重新计算，正确的值会在 PDF 中显示。  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
