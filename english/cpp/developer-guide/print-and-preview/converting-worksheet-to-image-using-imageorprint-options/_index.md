---
title: Converting Worksheet to Image using ImageOrPrint Options with C++
linktitle: Converting Worksheet to Image
type: docs
weight: 90
url: /cpp/converting-worksheet-to-image-using-imageorprint-options/
description: Learn how to convert a worksheet to an image file and apply different image and print options using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

This document is designed to provide a detailed understanding of how to convert a worksheet to an image file and apply different image and print options for the image, such as resolution, TIFF compression, image format, and page quality.

{{% /alert %}}

## **Saving Worksheets to Images - Different Approaches**

Sometimes, you might require presenting your worksheets as a pictorial representation. You may need to present the worksheet images in your applications or web pages, insert them into a Word document, a PDF file, a PowerPoint presentation, or use them in some other scenario. Simply put, you want a worksheet rendered as an image so that you can use it elsewhere. Aspose.Cells supports converting worksheets in Excel files to images. Additionally, Aspose.Cells supports setting different options like image format, resolution (both vertical and horizontal), image quality, and other image and print options.

You might consider Office Automation, but it has its own drawbacks. There are several reasons and issues involved, such as security, stability, scalability, speed, price, and features. In short, there are many reasons, with the top one being that Microsoft themselves strongly recommends against Office automation from software solutions.

This article shows how to create a console application in Visual Studio, perform the conversion of a worksheet to an image using different image and print options with a few and simplest lines of code using Aspose.Cells API.

You need to include the [**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/) namespace in your program/project. It has several valuable classes, for example, [**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/), [**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/), [**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/), etc.

The [**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/) class represents a worksheet to render images for the worksheet. It has an overloaded [**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/) method that can directly convert a worksheet to image file(s) specified with your desired attributes or options. It can return a bitmap object, and you can save an image file to the disk/stream. Several image formats are supported, such as BMP, PNG, GIF, JPEG, TIFF, EMF, and so on.

## **Using Aspose.Cells to Convert Worksheet to Image using ImageOrPrint Options**

### **Creating a Template Workbook in Microsoft Excel**

I created a new workbook in MS Excel and added some data in the first worksheet. Now, I will convert the template file’s worksheet “Sheet1” to an image file “SheetImage.tiff” and will apply different image options like horizontal and vertical resolutions, TiffCompression, etc.

### **Download and Install Aspose.Cells**

First, you need to [download](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++. Install it on your development computer. All [Aspose](http://www.aspose.com/) components, when installed, work in evaluation mode. The evaluation mode has no time limit and only injects watermarks into produced documents.

### **Create a Project**

Start Visual Studio and create a new console application. This example will show a C++ console application.

### **Add References**

This project will use Aspose.Cells. So, you have to add a reference to the Aspose.Cells component in your project. For example, add a reference to `...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`.

### **Convert Worksheet to an Image File**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleWorksheetToAnImage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(300);
    options.SetVerticalResolution(300);
    options.SetTiffCompression(TiffCompression::CompressionLZW);
    options.SetImageType(ImageType::Tiff);
    options.SetPrintingPage(PrintingPageType::Default);

    SheetRender sr(sheet, options);

    int pageIndex = 3;
    int pageNumber = pageIndex + 1;
    std::wstring pageStr = std::to_wstring(pageNumber);
    U16String pageNumberStr(reinterpret_cast<const char16_t*>(pageStr.c_str()));
    U16String outputPath = outDir + U16String(u"outputWorksheetToAnImage_") + pageNumberStr + U16String(u".tiff");
    sr.ToImage(pageIndex, outputPath);

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Conversion Options**

It is possible to save specific pages to an image. The following code converts the first and second worksheets in a workbook to JPG images.

```c++
#include <iostream>
#include <fstream>
#include <sstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"sampleSpecificPagesToImages.xlsx";
    Workbook workbook(inputPath);

    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetImageType(Aspose::Cells::Drawing::ImageType::Jpeg);

    SheetRender sr(worksheet, imgOptions);

    int32_t pageIndex = 3;

    Vector<uint8_t> imageData = sr.ToImage(pageIndex);

    std::wstringstream ws;
    ws << (pageIndex + 1);
    U16String pageNumStr(reinterpret_cast<const char16_t*>(ws.str().c_str()));

    U16String outputPath = outDir + u"outputSpecificPagesToImage_" + pageNumStr + u".jpg";
    std::ofstream outputFile(outputPath.ToUtf8(), std::ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Page rendered successfully to: " << outputPath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Image Conversion using WorkbookRender**

A TIFF image can contain more than one frame. You can save the whole workbook to a single TIFF image with multiple frames or pages:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook wb(srcDir + u"sampleUseWorkbookRenderForImageConversion.xlsx");

    // Set image options
    ImageOrPrintOptions opts;
    opts.SetImageType(ImageType::Tiff);

    // Render workbook to image
    WorkbookRender wr(wb, opts);
    wr.ToImage(outDir + u"outputUseWorkbookRenderForImageConversion.tiff");

    std::cout << "Workbook rendered to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
