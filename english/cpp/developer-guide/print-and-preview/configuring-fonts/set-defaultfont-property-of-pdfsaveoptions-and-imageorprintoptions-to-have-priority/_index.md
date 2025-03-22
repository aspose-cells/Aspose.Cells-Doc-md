---
title: Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority with C++
linktitle: Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority
type: docs
weight: 30
url: /cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
description: Learn to prioritize font settings when saving documents with Aspose.Cells in C++.
---

## **Possible Usage Scenarios**

While setting the **DefaultFont** property of [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), you might expect that saving to PDF or image would set that DefaultFont to all the text in a workbook that has a missing (not installed) font.

Generally, when saving to PDF or image, Aspose.Cells will first try to set the Workbook's default font (i.e., Workbook.DefaultStyle.Font). If the workbook's default font still cannot show/render text properly, then Aspose.Cells will try to render with the font mentioned against the DefaultFont attribute in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/).

To cope with your expectation, we have a Boolean property named "**CheckWorkbookDefaultFont**" in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/). You can set it to **false** to disable trying workbook's default font or let the **DefaultFont** setting in [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) have priority.

## **Set DefaultFont property of PdfSaveOptions/ImageOrPrintOptions**

The following sample code opens an Excel file. The A1 cell (in the first worksheet) has a text set to "Christmas Time Font text". The font name is "Christmas Time Personal Use" that is not installed on the machine. We set **DefaultFont** attribute of [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/)/[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/) to "Times New Roman". We also set **CheckWorkbookDefaultFont** Boolean property to **"false"** which ensures that the text of A1 cell is rendered with "Times New Roman" font and should not use the default font of the workbook ("Calibri" in this case). The code renders the first worksheet to PNG and TIFF image formats. It finally renders to a PDF file format.

{{% alert color="primary" %}}

The default value of **CheckWorkbookDefaultFont** attribute is **true**.

{{% /alert %}}

This is the screenshot of the [template file](49446913.xlsx) used in the example code.

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_1.png)

This is the output PNG image after setting the [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/defaultfont/) property to "Times New Roman".

![todo:image_alt_text](set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority_2.png)

See the output [TIFF](48496672.tiff) image after setting the [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/defaultfont/) property to "Times New Roman".

See the output [PDF](48496673.pdf) file after setting the [**PdfSaveOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/properties/defaultfont) property to "Times New Roman".

## **Sample Code**

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