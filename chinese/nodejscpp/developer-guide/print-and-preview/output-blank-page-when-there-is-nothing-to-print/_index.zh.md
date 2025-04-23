---
title: 使用 C++ 在 Node.js 中输出空白页（如果没有内容需要打印）
linktitle: 当没有要打印的内容时输出空白页
type: docs
weight: 90
url: /zh/nodejs-cpp/output-blank-page-when-there-is-nothing-to-print/
---

## **可能的使用场景**

如果工作表为空，则 Aspose.Cells 在导出为图像时不会打印任何内容。你可以通过使用 [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) 属性改变此行为。当你设置为 **true** 时，它会打印空白页。

## **当没有要打印的内容时输出空白页**

以下示例代码创建了一个空工作簿，包含空白工作表，并在将 [**ImageOrPrintOptions.getOutputBlankPageWhenNothingToPrint()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOutputBlankPageWhenNothingToPrint--) 属性设置为 **true** 后，将空白工作表渲染为图像。因此，生成了空白页，你可以在下面的图片中看到。

![todo:image_alt_text](output-blank-page-when-there-is-nothing-to-print_1.png)

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook
const wb = new AsposeCells.Workbook();

// Access first worksheet - it is empty sheet
const ws = wb.getWorksheets().get(0);

// Specify image or print options
// Since the sheet is blank, we will set OutputBlankPageWhenNothingToPrint to true
// So that empty page gets printed
const opts = new AsposeCells.ImageOrPrintOptions();
opts.setImageType(AsposeCells.ImageType.Png);
opts.setOutputBlankPageWhenNothingToPrint(true);

// Render empty sheet to png image
const sr = new AsposeCells.SheetRender(ws, opts);
sr.toImage(0, path.join(outputDir, "OutputBlankPageWhenNothingToPrint.png"));
```
