---
title: 将工作表转换为图像以及使用C++按页转换工作表为图像
linktitle: 将工作表转换为图像以及按页将工作表转换为图像
type: docs
weight: 80
url: /zh/cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/
description: 了解如何使用Aspose.Cells和C++将工作表转换为图像文件，以及将具有多页的工作表按页转换为图像文件。
---

{{% alert color="primary" %}}

本文旨在为开发者提供详细了解如何将工作表转换为图像文件，以及将多页工作表按照每页转换为图像文件的方法。

有时，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用。您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。简单来说，您希望将工作表呈现为图像。Aspose.Cells 支持将 Microsoft Excel 文件中的工作表转换为图像。Aspose.Cells 还支持将工作簿转换为多个图像文件，每页一个。

你可能会使用Office自动化实现此功能，但Office自动化有其自身的缺点。涉及多个原因和问题：例如安全性、稳定性、伸缩性/速度、价格和功能。简而言之，有很多原因，其中主要原因是微软自己强烈建议不要使用Office自动化。

{{% /alert %}}

## **使用 Aspose.Cells 将工作表转换为图像文件**

本文介绍了如何在 Visual Studio 中创建控制台应用程序，使用 Aspose.Cells API 将工作表转换为图像，并将每个工作表转换为单个图像的几行最简代码。

你需要在程序/项目中包含[**Aspose.Cells.Rendering**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/)命名空间。它包含多个有价值的类，例如[**SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/workbookrender/)等。[**Aspose.Cells.Rendering.SheetRender**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/)类代表用于渲染工作表为图像的工作表，并具有一个重载的[**ToImage**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetrender/toimage/)方法，可以直接将工作表转换为带有任何属性或选项设置的图像文件。它可以返回一个`System.Drawing.Bitmap`对象，您可以将图像文件保存到磁盘/流中。支持多种图像格式，例如BMP、PNG、GIF、JPG、JPEG、TIFF、EMF等。

本文解释了如何：

- 将工作表转换为图像
- 将工作表中的每个页面转换为图像

此任务显示如何使用Aspose.Cells将模板工作簿中的工作表转换为图像文件。

### **设置项目**

1. 首先，[下载 Aspose.Cells for C++](https://downloads.aspose.com/cells/cpp)。
1. 在您的开发计算机上安装。所有[Aspose](http://www.aspose.com/)组件安装后，都在评估模式下运行。评估模式没有时间限制，只会在生成的文档中注入水印。现在启动Visual Studio并创建一个新的控制台应用程序。此示例使用C++控制台应用程序。为创建的项目添加对Aspose.Cells的引用。

### **将工作表转换为图像文件**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook.xlsx**（1个工作表）。接下来，将模板文件的工作表Sheet1转换为名为SheetImage.jpg的图像文件。

以下是组件用来完成任务的代码。它将**Testbook.xlsx**中的Sheet1转换为图像文件，以说明这种转换有多么简便。

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

std::string convert_u16_to_string(const U16String& u16str);

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheettoImageFile.xlsx");
    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions imgOptions;
    imgOptions.SetOnePagePerSheet(true);
    imgOptions.SetImageType(ImageType::Jpeg);

    SheetRender sr(sheet, imgOptions);
    sr.ToImage(0, outDir + u"outputConvertWorksheettoImageFile.jpg");

    std::cout << "Worksheet converted to image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **使用Aspose.Cells按页将工作表转换为图像文件**

此示例演示如何使用Aspose.Cells将模板工作簿中具有多个页面的工作表转换为每页一个图像文件。

### **按页转换工作表为图像**

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook2.xlsx**（1个工作表）。

现在，将模板文件的工作表Sheet1转换为图像文件（每页一个文件）。由于我已经创建了执行复制任务的控制台应用程序，因此我将跳过创建控制台应用程序的步骤，直接转移到工作表转换步骤。

以下是组件完成任务所使用的代码。它将Testbook2.xlsx中的Sheet1按页转换为图像文件。

```cpp
#include <iostream>
#include <string>
#include <sstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

std::u16string intToU16String(int value) {
    std::u16string result;
    if (value == 0) {
        result.push_back(u'0');
        return result;
    }
    while (value > 0) {
        result.insert(result.begin(), static_cast<char16_t>(u'0' + (value % 10)));
        value /= 10;
    }
    return result;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook book(srcDir + u"sampleConvertWorksheetToImageByPage.xlsx");

    Worksheet sheet = book.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetHorizontalResolution(200);
    options.SetVerticalResolution(200);
    options.SetImageType(ImageType::Tiff);

    SheetRender sr(sheet, options);
    for (int j = 0; j < sr.GetPageCount(); j++)
    {
        std::u16string pageNum = intToU16String(j + 1);
        U16String fileName = outDir + U16String(u"outputConvertWorksheetToImageByPage_") + U16String(pageNum.c_str()) + U16String(u".tif");
        sr.ToImage(j, fileName);
    }

    std::cout << "Worksheet converted to images by page successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
