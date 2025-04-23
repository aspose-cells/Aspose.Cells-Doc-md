---
title: 将Excel转换为Pdf、图片和其他格式（使用C++）
linktitle: 工作簿转换
type: docs
weight: 65
url: /zh/cpp/convert-workbook-to-different-formats/
description: 使用Aspose.Cells for C++将Excel文件转换为Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML等多种格式。
---

{{% alert color="primary" %}}

Aspose.Cells支持多种格式之间的转换。技术上，转换意味着加载一种文件格式的工作簿并将其保存为另一种格式。

{{% /alert %}}

## **将 Excel 工作簿转换为 PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准的文档格式，软件开发者常被要求找到将Microsoft Excel文件转换为PDF的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Instantiate the Workbook object and open an Excel file
    Workbook workbook(u"Book1.xlsx");

    // Save the document in PDF format
    workbook.Save(u"output.pdf", SaveFormat::Pdf);

    std::cout << "Excel file converted to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将 Excel 工作簿转换为 JPG**
Aspose.Cells支持将Excel文件转换为JPG。
以下代码示例显示了如何将工作簿保存为JPG格式。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    U16String outputFilePath(u"Image1.jpg");
    book.Save(outputFilePath, SaveFormat::Jpg);

    std::cout << "Workbook converted to JPG image successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为图像**
Aspose.Cells支持将Excel文件转换为图像。
以下代码示例显示了如何将工作簿保存为图像。

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"../Data/01_SourceDirectory/");
    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook workbook(srcDir + u"Book1.xlsx");

    workbook.Save(outDir + u"Image1.bmp", SaveFormat::Bmp);
    workbook.Save(outDir + u"Image1.jpg", SaveFormat::Jpg);
    workbook.Save(outDir + u"Image1.png", SaveFormat::Png);
    workbook.Save(outDir + u"Image1.emf", SaveFormat::Emf);
    workbook.Save(outDir + u"Image1.gif", SaveFormat::Gif);

    std::cout << "Workbook converted to images successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为XPS**

XPS文档格式由结构化的XML标记组成，用于定义文档的布局和每个页面的视觉外观，同时还包括用于分发、归档、渲染、处理和打印文档的渲染规则。

XPS的标记语言是XAML的子集，允许在文档中加入矢量图形元素，使用XAML标记WPF基本元素。所用元素以路径和其他几何原语描述。

实际上，XPS文件是一个Unicode ZIP归档，采用开放封装规范，包含组成文档的文件。这些包括每一页的XML标记文件、文本、内嵌字体、光栅图像、二维矢量图形以及数字版权管理信息。可以通过支持ZIP文件的应用程序打开XPS文件，轻松查看其内容。

从Aspose.Cells 6.0.0开始，支持将Microsoft Excel转换为XPS。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputFilePath = srcDir + u"Book1.xls";
    Workbook workbook(inputFilePath);

    Worksheet sheet = workbook.GetWorksheets().Get(0);

    ImageOrPrintOptions options;
    options.SetImageType(ImageType::Png);

    SheetRender sr(sheet, options);
    sr.ToImage(0, outDir + u"out_image.png");

    XpsSaveOptions xpsOptions;
    workbook.Save(outDir + u"out_whole_printingxps.out.xps", xpsOptions);

    std::cout << "Files created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel转换为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）**
Aspose.Cells支持转换Excel文件为Ods、Sxc和Fods文件。以下示例显示如何将[模板](book1.xlsx)转换为Ods、Sxc和Fods文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"book1.xlsx");

    // Save as ods file
    workbook.Save(u"Out.ods");

    // Save as sxc file
    workbook.Save(u"Out.sxc");

    // Save as fods file
    workbook.Save(u"Out.fods");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **将Excel工作簿转换为MHTML文件**

MHTML结合了普通HTML以及外部资源（通常是链接的内容，如图像、动画、音频等）到一个文件中。它们通常用于以.mht文件扩展名的电子邮件。

Aspose.Cells支持读取和写入MHTML文件。

下面的代码示例显示了如何将工作簿保存为MHTML文件。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Specify the HTML Saving Options
    HtmlSaveOptions sv(SaveFormat::MHtml);

    // Instantiate a workbook and open the template XLSX file
    Workbook wb(filePath);

    // Save the MHT file
    wb.Save(filePath + u".out.mht", sv);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为HTML**

Aspose.Cells API 提供了导出电子表格为 HTML 格式的支持。为此，Aspose.Cells 使用 [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) 类，提供控制输出 HTML 各个方面的灵活性。

下面的代码示例显示了如何将工作簿保存为HTML文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"ConvertingToHTMLFiles_out.html";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in HTML format
    wb.Save(outputFilePath, SaveFormat::Html);

    std::cout << "File converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **为HTML设置图像首选项**

从 8.0.2 版本起，Aspose.Cells 已将 [**GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/) 公开给 [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/) 类，使开发者在将电子表格保存为 HTML 格式时可以指定图片偏好。

以下是一些可以应用的图像设置的详细信息：

- [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/)：指定图像类型。请注意，所有形状，包括图表，在输出HTML中呈现为图像。
- [**GetQuality()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getquality/)：指定当 [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) 设置为Jpeg时，图像的质量在0到100之间。
- [**GetVerticalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getverticalresolution/)：获取或设置图像的垂直分辨率（每英寸点数）。
- [**GetHorizontalResolution()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gethorizontalresolution/)：获取或设置图像的水平分辨率（每英寸点数）。
- [**TiffCompression**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/tiffcompression/)：在 [**ImageType**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/imagetype/) 被指定为 Tiff 时，获取或设置图片的压缩类型。
- [**GetTransparent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/gettransparent/)：指示当ImageFormat指定为Png时，图像的背景是否应该是透明的。

下面的代码示例演示了如何使用[**HtmlSaveOptions.GetImageOptions()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getimageoptions/)来指定不同的首选项。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"Book1.xlsx";

    Workbook book(filePath);
    HtmlSaveOptions saveOptions(SaveFormat::Html);

    saveOptions.GetImageOptions().SetImageType(ImageType::Png);

    book.Save(outDir + u"output.html", saveOptions);

    std::cout << "Spreadsheet converted to HTML successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为Markdown**

Aspose.Cells API支持导出电子表格为Markdown格式。导出活动工作表为Markdown时，将 [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**MarkdownSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/markdownsaveoptions/) 类来指定导出工作表到Markdown的其他设置。

以下示例演示如何使用 [**SaveFormat.Markdown**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员将活动工作表导出为Markdown。请参考由代码生成的 [输出Markdown文件](md_sample.txt)。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Markdown file
    U16String outputFilePath = outDir + u"Book1.md";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as Markdown
    workbook.Save(outputFilePath, SaveFormat::Markdown);

    std::cout << "Workbook saved as Markdown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为JSON**

Aspose.Cells支持将工作簿转换为JSON（JavaScript对象表示法）文件。

以下示例演示如何使用 [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员将活动工作表导出为JSON。请参阅代码示例，了解如何将 [源文件](Book1.xlsx) 转换为由代码生成的 [输出JSON文件](Book1.Json)。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output json file
    U16String outputFilePath = outDir + u"book1.json";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the workbook as JSON
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel转换为XML**
Aspose.Cells 支持将工作簿转换为 Excel 2003 电子表格 XML 和普通 XML 数据。

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath = u"Book1.xlsx";
    Workbook workbook(inputFilePath);

    // Save as Excel 2003 Spreadsheet XML
    U16String outputFilePath1 = u"Spreadsheet.xml";
    workbook.Save(outputFilePath1);

    // Save as plain XML data
    U16String outputFilePath2 = u"data.xml";
    XmlSaveOptions xmlSaveOptions;
    workbook.Save(outputFilePath2, xmlSaveOptions);

    std::cout << "Files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为TIFF**
Aspose.Cells 支持将工作簿转换为 TIFF 文件。

下面的代码片段显示了如何将Excel转换为TIFF：

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open a template excel file
    U16String inputFilePath(u"Book1.xlsx");
    Workbook book(inputFilePath);

    // Save file to TIFF
    U16String outputFilePath(u"out.tiff");
    book.Save(outputFilePath);

    std::cout << "File saved successfully to TIFF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为DOCX**

Aspose.Cells API支持将电子表格导出为DOCX格式。导出工作簿为DOCX时，将 [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**DocxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/docxsaveoptions/) 类来指定导出到DOCX的其他设置。

以下示例演示如何使用 [**SaveFormat.Docx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员将活动工作表导出为DOCX。请参考由代码生成的 [输出DOCX文件](Book1.docx)。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output docx file
    U16String outputFilePath = outDir + u"Book1.docx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save as DOCX
    workbook.Save(outputFilePath, SaveFormat::Docx);

    std::cout << "File saved successfully as DOCX!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将Excel工作簿转换为PPTX**

Aspose.Cells支持将电子表格转换为PPTX格式。导出到PPTX时，将 [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**PptxSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pptxsaveoptions/) 类来指定其他导出设置。

以下示例演示如何使用 [**SaveFormat.Pptx**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员将活动工作表导出为PPTX。请查看由代码生成的 [输出PPTX文件](Book1.pptx)。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output PowerPoint file
    U16String outputFilePath = outDir + u"Book1.pptx";

    // Create workbook from the input Excel file
    Workbook workbook(inputFilePath);

    // Save the workbook as a PowerPoint file
    workbook.Save(outputFilePath, SaveFormat::Pptx);

    std::cout << "Workbook saved as PowerPoint successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将 Excel 工作簿转换为 EPUB**

Aspose.Cells API支持将电子表格转换为EPUB格式。要导出工作簿为EPUB，将 [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) 类来指定导出到EPUB的其他设置。

以下示例演示如何使用 [**SaveFormat.Epub**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员将活动工作表导出为EPUB。

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output EPUB file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.epub";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in EPUB format
    wb.Save(outputFilePath, SaveFormat::Epub);

    std::cout << "File converted to EPUB format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将 Excel 工作簿转换为 AZW3**

Aspose.Cells API支持将电子表格转换为AZW3格式。要导出工作簿到AZW3，传递 [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 作为 [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法的第二个参数。也可以使用 [**EBookSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells.saving/ebooksaveoptions/) 类指定其他导出设置。

以下示例演示如何将活动工作表导出为AZW3，使用 [**SaveFormat.Azw3**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String filePath = srcDir + u"sample.xlsx";

    // Path of output AZW3 file
    U16String outputFilePath = outDir + u"ConvertingToEPUBFiles_out.azw3";

    // Load the sample excel file into a workbook object
    Workbook wb(filePath);

    // Save the workbook in AZW3 format
    wb.Save(outputFilePath, SaveFormat::Azw3);

    std::cout << "File converted to AZW3 format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [将XLSB的修订版转换为XLSM](/cells/zh/cpp/convert-revision-of-xlsb-to-xlsm/)
- [HTML](/cells/zh/cpp/convert-excel-to-html/)
- [图像](/cells/zh/cpp/convert-excel-to-image/)
- [Json](/cells/zh/cpp/convert-workbook-to-json/)
- [将Excel工作簿转换为Ods、Sxc和Fods（OpenOffice / LibreOffice Calc）](/cells/zh/cpp/convert-excel-to-ods/)
- [Pdf](/cells/zh/cpp/convert-excel-workbook-to-pdf/)
- [转换Excel为CSV、TSV和Txt](/cells/zh/cpp/convert-excel-to-csv-tsv-and-txt/)
- [跟踪文档转换进度](/cells/zh/cpp/track-document-conversion-progress/)
- [将CSV、TSV和TXT转换为Excel](/cells/zh/cpp/convert-csv-tsv-and-txt-to-excel/)
