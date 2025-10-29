---
title: 设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性以提升优先级，使用 C++ 和 Node.js
linktitle: 设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性具有优先级
type: docs
weight: 30
url: /zh/nodejs-cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: 了解如何用 Aspose.Cells for Node.js via C++ 设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性。确保在字体缺失时正确渲染字体。
---

## **可能的使用场景**

在设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) 的 **DefaultFont** 属性时，您可能希望保存为 PDF 或图像时将该 DefaultFont 设置为工作簿中所有没有安装的字体的文本。

通常，在保存为 PDF 或图片时，Aspose.Cells for Node.js via C++ 会优先尝试设置工作簿的默认字体（即 `Workbook.DefaultStyle.Font`）。如果工作簿的默认字体仍无法正确显示/渲染文本，Aspose.Cells 将尝试使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) 中默认字体属性所指定的字体进行渲染。

为了符合您的期望，我们在 [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) 中提供了一个名为"**CheckWorkbookDefaultFont**"的布尔属性。您可以将其设置为 **false** 以禁用尝试工作簿的默认字体，或者让 [**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/) 中的 **DefaultFont** 设置具有优先级。

## **设置PdfSaveOptions/ImageOrPrintOptions的DefaultFont属性**

以下示例代码打开一个Excel文件。第一个工作表的A1单元格内设置了一段文本“Christmas Time Font text”。字体名为“Christmas Time Personal Use”，该字体未安装在机器上。我们将[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)的**DefaultFont**属性设置为“Times New Roman”。同时将布尔属性**CheckWorkbookDefaultFont**设置为“false”，确保A1单元格的文本使用“Times New Roman”字体渲染，而不是使用默认字体（此处为“Calibri”）。该代码将第一个工作表渲染为PNG和TIFF图像格式，最后输出为PDF文件。

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont**属性的默认值为**true**。

{{% /alert %}}

这是示例代码中使用的[模板文件](49446913.xlsx)的屏幕截图。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

设置[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)属性为“Times New Roman”后生成的PNG图像示意。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

设置[**ImageOrPrintOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getDefaultFont--)属性为“Times New Roman”后，输出的[TIF](48496672.tiff)图像。

在设置 [**PdfSaveOptions.getDefaultFont()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getDefaultFont--) 属性为 "Times New Roman" 后，查看输出 [PDF](48496673.pdf) 文件。

## **示例代码**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const sourceDir = path.join(__dirname, "data");
const outputDir = path.join(__dirname, "output");

// Open an Excel file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx"));

// Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const imgOpt = new AsposeCells.ImageOrPrintOptions();
imgOpt.setImageType(AsposeCells.ImageType.Png);
imgOpt.setCheckWorkbookDefaultFont(false);
imgOpt.setDefaultFont("Times New Roman");
const sr = new AsposeCells.SheetRender(workbook.getWorksheets().get(0), imgOpt);
sr.toImage(0, path.join(outputDir, "out1_imagePNG.png"));

// Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
imgOpt.setImageType(AsposeCells.ImageType.Tiff);
const wr = new AsposeCells.WorkbookRender(workbook, imgOpt);
wr.toImage(path.join(outputDir, "out1_imageTIFF.tiff"));

// Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
// So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
const saveOptions = new AsposeCells.PdfSaveOptions();
saveOptions.setDefaultFont("Times New Roman");
saveOptions.setCheckWorkbookDefaultFont(false);
workbook.save(path.join(outputDir, "out1_pdf.pdf"), saveOptions);
```
{{< app/cells/assistant language="nodejs-cpp" >}}
