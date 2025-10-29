---
title: 重采样添加的图片  使用 Node.js 和 C++ 进行 Excel 转 PDF
linktitle: 重采样添加的图片
type: docs
weight: 150
url: /zh/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/
description: 学习如何压缩在 Excel 文件中添加的图片，以减少 PDF 大小并提升转换性能，使用 Aspose.Cells for Node.js via C++。
---

{{% alert color="primary" %}}

当处理含有大量图片的大型 Microsoft Excel 文件时，您可能需要压缩已添加的图片以减小输出 PDF 文件的体积并提升整体转换性能。Aspose.Cells for Node.js via C++ 支持重新采样已添加的图片来减少输出 PDF 的大小，并在一定程度上提升性能。

{{% /alert %}}

请参阅以下示例代码，描述如何使用Aspose.Cells API执行该任务。该示例将Microsoft Excel文件转换为PDF文件，并压缩文件中的图像。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Initialize a new Workbook
// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "input.xlsx"));

// Instantiate the PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();
// Set Image Resample properties
pdfSaveOptions.setImageResample(300, 70);

// Save the PDF file
workbook.save(path.join(dataDir, "OutputFile_out_pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}

使用 [**setImageResample(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#setImageResample-number-number-) 选项可以最小化输出 PDF 的大小，但可能会略微影响图片质量。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
