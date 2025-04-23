---
title: 限制生成的页数——Excel转PDF的C++方案
linktitle: 限制生成的页面数量  将Excel转换为PDF
type: docs
weight: 180
url: /zh/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: 了解如何在将Excel电子表格转换为PDF时限制生成的页数，使用编号Aspose.Cells for Node.js via C++。 
---

{{% alert color="primary" %}}

有时候，您希望将某个范围的页面打印到输出PDF文件中。编号Aspose.Cells for Node.js via C++具有设置限制导出页面数量的能力。

{{% /alert %}}

## **限制生成的页面数量**

以下示例显示了如何将Microsoft Excel文件的页面范围（第3页和第4页）呈现为PDF。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "TestBook.xlsx"));
// Instantiate the PdfSaveOption
const options = new AsposeCells.PdfSaveOptions();

// Print only Page 3 and Page 4 in the output PDF
// Starting page index (0-based index)
options.setPageIndex(3);
// Number of pages to be printed
options.setPageCount(2);

// Save the PDF file
workbook.save(path.join(dataDir, "outPDF1.out.pdf"), options);
```

{{% alert color="primary" %}}

如果电子表格包含公式，建议在渲染为PDF之前调用[**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。这样可以确保依赖公式的值被重新计算，并在输出文件中显示正确的值。

{{% /alert %}}
