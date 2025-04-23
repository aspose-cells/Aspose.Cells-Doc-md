---
title: 使用C++配置渲染电子表格的字体
linktitle: 配置字体以渲染电子表格
type: docs
weight: 10
url: /zh/cpp/configuring-fonts-for-rendering-spreadsheets/
description: 学习如何使用Aspose.Cells for C++配置字体，以便渲染电子表格为图像、PDF和XPS格式。
---

## **可能的使用场景**

Aspose.Cells API提供将电子表格渲染为图像格式以及转换为PDF和XPS格式的功能。为了最大程度地保证转换的准确性，必须确保电子表格中使用的字体已在操作系统的默认字体目录中。如果缺少必要的字体，Aspose.Cells会尝试用可用的字体替代。

## **选择字体**

以下是Aspose.Cells后台的流程：

1. API试图在文件系统中找到与电子表格中使用的确切字体名称匹配的字体。
1. 如果API找不到相同名字的字体，它会尝试使用工作簿的 [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) 属性中指定的默认字体。
1. 如果API找不到在工作簿的 [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) 属性中定义的字体，它会尝试使用 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) 或 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) 属性中指定的字体。
1. 如果API找不到在 [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) 或 [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/) 属性中定义的字体，它会尝试使用 [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) 属性中指定的字体。
1. 如果API找不到在 [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/) 属性中定义的字体，它会尝试从所有可用字体中选择最合适的字体。
1. 最后，如果API在文件系统中找不到任何字体，它会用Arial字体渲染电子表格。

## **设置自定义字体文件夹**

Aspose.Cells API会在操作系统的默认字体目录搜索所需的字体。如果未找到所需字体，API会在自定义（用户定义的）目录中搜索。 [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) 类提供了多种设置自定义字体目录的方法，详见下文：

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/)：如果只有一个要设置的文件夹，则此方法很有用。
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/)：当字体存储在多个文件夹中，且用户希望分别设置所有文件夹时，此方法非常实用。
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/)：此机制在用户希望从多个文件夹加载字体、单个字体文件或字体数据（字节数组）时非常有用。

{{% alert color="primary" %}}

这两种方法都接受一个布尔类型的第二参数。传入 **true** 会指示Aspose.Cells API搜索子文件夹中的字体文件。

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

请在应用程序开始时（在调用任何其他Aspose.Cells API对象之前）使用上述任意方法。

{{% /alert %}}

{{% alert color="primary" %}}

如果使用所有上述方法设置字体源，则只有最后一次设置将生效。

{{% /alert %}}

## **字体替换机制**

Aspose.Cells API还提供指定替代字体以进行渲染的机制。当所需字体未在目标计算机上可用时，此机制十分有用。用户可以提供一份字体名称列表作为原始字体的替代。为此，Aspose.Cells引入了 [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/) 方法，它接受两个参数。第一个参数是字符串类型，表示需要替换的字体名称；第二个参数是字符串数组，用户可以提供一份字体名称的替代列表。

以下是一个简单的使用场景：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **信息收集**

除上述方法外，Aspose.Cells还提供了收集已设置的字体源和替代信息的方法：

1. [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) 方法返回一个 [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) 类型的数组，列出指定的字体源。如果未设置任何源，[**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) 方法将返回空数组。
1. [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) 方法接受一个字符串类型参数，允许用户指定已设置替代项的字体名称。如果未为该字体设置替代项，[**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) 方法将返回 null。

## **高级主题**
- [在将电子表格呈现为图像时设置默认字体](/cells/zh/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [设置 PdfSaveOptions 和 ImageOrPrintOptions 的 DefaultFont 属性具有优先级](/cells/zh/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [支持的字体格式](/cells/zh/cpp/supported-font-formats/)
