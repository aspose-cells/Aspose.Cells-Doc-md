---
title: 将PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性设置为优先，使用C++
linktitle: 设置PdfSaveOptions和ImageOrPrintOptions的DefaultFont属性具有优先级
type: docs
weight: 30
url: /zh/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: 学习在使用Aspose.Cells保存文档时优先设置字体。
---

## **可能的使用场景**

在设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 和 [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) 的 **DefaultFont** 属性时，您可能希望保存为 PDF 或图像时将该 DefaultFont 设置为工作簿中所有没有安装的字体的文本。

通常，在保存为PDF或图像时，Aspose.Cells会优先尝试设置工作簿的默认字体（即Workbook.DefaultStyle.Font）。如果工作簿的默认字体仍无法正确显示/渲染文本，则Aspose.Cells将尝试使用[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)中的DefaultFont属性中提到的字体进行渲染。

为了符合您的预期，我们在{0}/{1}}中添加了布尔属性“**CheckWorkbookDefaultFont**”。您可以将其设置为**false**，以禁用尝试使用工作簿的默认字体，或让{2}/{3}中的**DefaultFont**设置优先执行。

## **设置PdfSaveOptions/ImageOrPrintOptions的DefaultFont属性**

以下示例代码打开一个Excel文件。第一个工作表的A1单元格内设置了一段文本“Christmas Time Font text”。字体名为“Christmas Time Personal Use”，该字体未安装在机器上。我们将[**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)的**DefaultFont**属性设置为“Times New Roman”。同时将布尔属性**CheckWorkbookDefaultFont**设置为“false”，确保A1单元格的文本使用“Times New Roman”字体渲染，而不是使用默认字体（此处为“Calibri”）。该代码将第一个工作表渲染为PNG和TIFF图像格式，最后输出为PDF文件。

{{% alert color="primary" %}}

**CheckWorkbookDefaultFont**属性的默认值为**true**。

{{% /alert %}}

这是示例代码中使用的[模板文件](49446913.xlsx)的屏幕截图。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

设置[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性为“Times New Roman”后生成的PNG图像示意。

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

设置[**ImageOrPrintOptions.GetDefaultFont()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)属性为“Times New Roman”后，输出的[TIF](48496672.tiff)图像。

设置[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)属性为“Times New Roman”后，输出的[PDF](48496673.pdf)文件。

## **示例代码**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Input and output directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outputDir(u"..\\Data\\02_OutputDirectory\\");

    // Open an Excel file
    Workbook workbook(sourceDir + u"sampleSetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.xlsx");

    // Rendering to PNG file format while setting the CheckWorkbookDefaultFont attribute to false.
    // So, "Times New Roman" font would be used for any missing (not installed) font in the workbook.
    ImageOrPrintOptions imgOpt;
    imgOpt.SetImageType(ImageType::Png);
    imgOpt.SetCheckWorkbookDefaultFont(false);
    imgOpt.SetDefaultFont(u"Times New Roman");

    // Create a SheetRender instance for the first worksheet and render to PNG.
    SheetRender sr(workbook.GetWorksheets().Get(0), imgOpt);
    sr.ToImage(0, outputDir + u"out1_imagePNG.png");

    // Rendering to TIFF file format while setting the CheckWorkbookDefaultFont attribute to false.
    imgOpt.SetImageType(ImageType::Tiff);
    WorkbookRender wr(workbook, imgOpt);
    wr.ToImage(outputDir + u"out1_imageTIFF.tiff");

    // Rendering to PDF file format while setting the CheckWorkbookDefaultFont attribute to false.
    PdfSaveOptions saveOptions;
    saveOptions.SetDefaultFont(u"Times New Roman");
    saveOptions.SetCheckWorkbookDefaultFont(false);

    // Save the workbook as PDF
    workbook.Save(outputDir + u"out1_pdf.pdf", saveOptions);

    std::cout << "Files exported successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
