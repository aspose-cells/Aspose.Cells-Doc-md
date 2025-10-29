---
title: 使用ImageOrPrint选项和C++将工作表转换为图像
linktitle: 转换工作表为图像
type: docs
weight: 90
url: /zh/cpp/converting-worksheet-to-image-using-imageorprint-options/
description: 了解如何使用Aspose.Cells和C++将工作表转换为图像文件，并应用不同的图像和打印选项。
---

{{% alert color="primary" %}}

本文旨在详细说明如何将工作表转换为图像文件，以及为图像应用不同的图像和打印选项，例如分辨率、TIFF压缩、图像格式和页面质量。

{{% /alert %}}

## **将工作表保存为图像-不同方法**

有时，你可能需要将工作表以图片的形式呈现。你可能需要在应用程序或网页中显示工作表图像，将它们插入Word文档、PDF文件、PowerPoint演示文稿，或在其他场景中使用。简而言之，你希望将工作表渲染为图像，以便在其他地方使用。Aspose.Cells支持将Excel文件中的工作表转换为图像。此外，支持设置不同的选项，如图像格式、分辨率（垂直和水平）、图像质量以及其他图像和打印选项。

你可能会考虑Office自动化，但它也有其缺点。涉及多个原因和问题，例如安全性、稳定性、扩展性、速度、价格和功能。简而言之，原因很多，其中微软自己强烈建议不要使用软件方案进行Office自动化。

本文介绍如何在Visual Studio中创建控制台应用程序，并使用少量代码和Aspose.Cells API执行工作表到图像的转换，应用不同的图像和打印选项。

你需要在程序/项目中包含[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)命名空间。它包含多个有价值的类，例如[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)等。

'[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)'类代表用于渲染工作表为图像的工作表。它具有一个重载的[**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)方法，可以直接将工作表转换为指定属性或选项的图像文件。它可以返回一个位图对象，您可以将图像文件保存到磁盘或流中。支持多种图像格式，如BMP、PNG、GIF、JPEG、TIFF、EMF等。

## **使用Aspose.Cells结合ImageOrPrint选项将工作表转换为图像**

### **在Microsoft Excel中创建模板工作簿**

我在MS Excel中创建了一个新工作簿，并在第一个工作表添加了一些数据。现在，我将把模板文件的“Sheet1”工作表转换为图像文件“SheetImage.tiff”，并应用不同的图像选项，如水平和垂直分辨率、Tiff压缩等。

### **下载并安装Aspose.Cells**

首先，您需要[下载](https://downloads.aspose.com/cells/cpp) Aspose.Cells for C++。将其安装在您的开发计算机上。所有[ Aspose](http://www.aspose.com/)组件安装后，都以评估模式运行。评估模式没有时间限制，只会在生成的文档中添加水印。

### **创建一个项目**

启动Visual Studio并创建一个新的控制台应用程序。此示例将演示一个C++控制台应用程序。

### **添加引用**

此项目将使用Aspose.Cells。因此，必须在项目中添加对Aspose.Cells的引用。例如，添加引用到`...\Program Files\Aspose\Aspose.Cells for C++\Bin\Aspose.Cells.lib`。

### **将工作表转换为图像文件**

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

## **转换选项**

可以将特定页面保存为图像。以下代码将工作簿中的第一个和第二个工作表转换为JPG图像。

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

## **使用WorkbookRender进行图像转换**

TIFF图像可以包含多个帧。你可以将整个工作簿保存为具有多个帧或页面的单一TIFF图像：

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
