---
title: 使用 C++ 将 Excel 转换为 PDF
linktitle: 将Excel转换为PDF
type: docs
weight: 220
url: /zh/cpp/convert-excel-to-pdf/
description: 了解如何使用 Aspose.Cells 和 C++ 将 Excel 工作簿转换为 PDF 格式。
---

{{% alert color="primary" %}}

 Aspose.Cells 支持将 Excel 工作簿转换为 PDF。在此示例中，我们将看到完整的将 Excel 工作簿转换为 PDF 的过程。

{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准的文档格式，软件开发者常被要求找到将Microsoft Excel文件转换为PDF的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

{{% alert color="primary" %}}

 Aspose.Cells for C++ 直接在输出文件中写入 API 和版本号信息。例如，在将文档渲染为 PDF 时，Aspose.Cells for C++ 将在 **PDF 生成者** 字段填充一个值，例如 ‘Aspose.Cells v23.2’。

请注意，您可以使用 [**PdfSaveOptions.GetProducer()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getproducer/) 属性在输出文档中更改此信息。

{{% /alert %}}

### **直接转换**

 Aspose.Cells for C++ 支持将电子表格独立转换为 PDF，只需使用 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的 [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法保存为 PDF 文件。[**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法提供了 [**SaveFormat.Pdf**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举成员，可将原生 Excel 文件转换为 PDF 格式。

按以下步骤直接将Excel电子表格转换为PDF格式：

 1. 通过调用其空构造函数实例化 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的对象。
1. 您可以打开/加载现有模板文件，或者如果您是从头开始创建工作簿，则跳过此步骤。
 1. 使用 Aspose.Cells 的 API 在电子表格上进行任何操作（输入数据、应用格式、设置公式、插入图片或其他绘图对象等）。
 1. 当电子表格代码完成后，调用 [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) 类的 [**Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) 方法保存电子表格。

 文件格式应为 PDF，因此请从 [**SaveFormat**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) 枚举中选择 *Pdf*（预定义值）生成最终的 PDF 文档。

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
    U16String inputFilePath = srcDir + u"Book1.xls";

    // Path of output PDF file
    U16String outputFilePath = outDir + u"output.pdf";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Save the document in PDF format
    workbook.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Document saved successfully in PDF format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **高级转换**

 您还可以选择使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 类设置转换的不同属性。设置 [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 类的不同属性可以让您控制输出 PDF 文件的打印、字体、权限和压缩设置。

 最重要的属性是 [**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/)，它允许您设置 PDF 标准的符合级别。目前，您可以将文档保存为 PDF 1.4、PDF 1.5、PDF 1.6、PDF 1.7、PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab 和 PDF/A-3u 格式。注意，使用 PDF/A 格式时，输出文件大小会比普通 PDF 文件大。

#### **将工作簿保存为PDF/A兼容文件**

 以下代码片段演示了如何使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 类将 Excel 文件保存为符合 PDF/A 规范的 PDF 格式。

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

    // Instantiate new workbook
    Workbook workbook;

    // Insert a value into the A1 cell in the first worksheet
    workbook.GetWorksheets().Get(0).GetCells().Get(0, 0).PutValue(U16String(u"Testing PDF/A"));

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set the compliance type
    pdfSaveOptions.SetCompliance(PdfCompliance::PdfA1b);

    // Save the file
    workbook.Save(outDir + u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file created successfully with PDF/A-1b compliance!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

 请注意，[**GetCompliance()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcompliance/) 属性是在 Aspose.Cells for C++ 5.3.0 版本中新增的。

{{% /alert %}}

#### **设置PDF创建时间**

 使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 类，可以获取或设置 PDF 的创建时间。以下代码演示了如何使用 [**PdfSaveOptions.GetCreatedTime()**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/getcreatedtime/) 属性设置 PDF 文件的创建时间。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputPath = srcDir + u"Book1.xlsx";

    // Load excel file containing charts
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions options;
	options.SetCreatedTime(Date{ 2025,01,01 });

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(srcDir + u"output.pdf", options);

    std::cout << "Workbook saved to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **设置ContentCopyForAccessibility选项**

 使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 类，可以获取或设置 PDF [**GetAccessibilityExtractContent()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/getaccessibilityextractcontent/) 选项以控制转换后 PDF 的内容访问权限。

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
    U16String inputPath = srcDir + u"BookWithSomeData.xlsx";

    // Load excel file containing some data
    Workbook workbook(inputPath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOpt;

    // Create an instance of PdfSecurityOptions
    PdfSecurityOptions securityOptions;

    // Set AccessibilityExtractContent to false
    securityOptions.SetAccessibilityExtractContent(false);

    // Set the security option in the PdfSaveOptions
    pdfSaveOpt.SetSecurityOptions(securityOptions);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    workbook.Save(outDir + u"outFile.pdf", pdfSaveOpt);

    std::cout << "Workbook saved to PDF format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

#### **导出自定义属性到PDF**

 使用 [**PdfSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/pdfsaveoptions/) 类，可以将源工作簿中的自定义属性导出到 PDF。提供了 [**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/pdfcustompropertiesexport/) 枚举器，用于指定导出属性的方式。这些属性可以在 Adobe Acrobat Reader 中点击 文件然后属性选项查看，如下图所示。测试时可以下载模板文件 "sourceWithCustProps.xlsx" [此处](sourceWithCustProps.xlsx)，输出 PDF 文件 "outSourceWithCustProps" 可在 [此处](outSourceWithCustProps.pdf) 查看分析。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Load excel file containing custom properties
    U16String inputFilePath(u"sourceWithCustProps.xlsx");
    Workbook workbook(inputFilePath);

    // Create an instance of PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Set CustomPropertiesExport property to PdfCustomPropertiesExport::Standard
    pdfSaveOptions.SetCustomPropertiesExport(PdfCustomPropertiesExport::Standard);

    // Save the workbook to PDF format while passing the object of PdfSaveOptions
    U16String outputFilePath(u"outSourceWithCustProps.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    Aspose::Cells::Cleanup();
}
```

### **转换属性**

 我们不断努力提升转换功能，每个新版本都在改善。Aspose.Cells 的 Excel 转 PDF 转换仍存在一些限制。例如，MapChart 在转换为 PDF 时不支持，部分绘图对象支持不佳。

 以下表格列出了使用 Aspose.Cells 在导出为 PDF 时全部或部分支持的功能。此表不是最终版本，也未涵盖所有电子表格属性，但指出了哪些功能不支持或部分支持转换为 PDF。

| **文档元素** | **属性** | **支持** | **备注** |
| :- | :- | :- | :- |
| 对齐 |  | 支持 |  |
| 背景设置 |  | 支持 |  |
| 边框 | 颜色 | 支持 |  |
| 边框 | 线条样式 | 支持 |  |
| 边框 | 线宽 | 支持 |  |
| 单元格数据 |  | 支持 |  |
| 注释 |  | 支持 |  |
| 条件格式 |  | 支持 |  |
| 文档属性 |  | 支持 |  |
| 绘图对象 |  | 部分支持 | 阴影和3D效果在支持方面有限；WordArt 和 SmartArt 支持不完全。 |
| 字体 | 大小 | 支持 |  |
| 字体 | 颜色 | 支持 |  |
| 字体 | 样式 | 支持 |  |
| 字体 | 下划线 | 支持 |  |
| 字体 | 效果 | 支持 |  |
| 图片 |  | 支持 |  |
| 超链接 |  | 支持 |  |
| 图表 |  | 部分支持 | MapChart 不支持。 |
| 合并单元格 |  | 支持 |  |
| 分页符 |  | 支持 |  |
| 页面设置 | 页眉/页脚 | 支持 |  |
| 页面设置 | 页边距 | 支持 |  |
| 页面设置 | 页面方向 | 支持 |  |
| 页面设置 | 页面大小 | 支持 |  |
| 页面设置 | 打印区域 | 支持 |  |
| 页面设置 | 打印标题 | 是 |  |
| 页面设置 | 缩放 | 是 |  |
| 行高/列宽 |  | 是 |  |
| RTL（从右到左）语言 |  | 是 |  |

{{% alert color="primary" %}}

如果你的电子表格包含公式，最好在渲染为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)。这样可以确保公式依赖的值被重新计算，且正确的值被渲染到PDF中。

{{% /alert %}}

## **高级主题**
- [使用命名目标添加PDF书签](/cells/zh/cpp/add-pdf-bookmarks-with-named-destinations/)
- [在保存为PDF时仅更改特定Unicode字符的字体](/cells/zh/cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [将XLSX文件转换为PDF格式](/cells/zh/cpp/convert-xlsx-file-to-pdf-format/)
- [将 Excel 文件转换为兼容 PDFA-1a 格式的 PDF](/cells/zh/cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将带有图片或图表的XLS文件转换为PDF](/cells/zh/cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表工作表创建PdfBookmarkEntry](/cells/zh/cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [将所有工作表列调整到单个PDF页面上](/cells/zh/cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [在使用DrawObjectEventHandler类呈现到PDF时获取DrawObject和边界](/cells/zh/cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [在呈现Excel文件时获取字体替换的警告](/cells/zh/cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [在将Excel渲染为PDF时忽略错误](/cells/zh/cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页面数量-从Excel转换为PDF](/cells/zh/cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [保存为PDF时打印注释](/cells/zh/cpp/print-comments-while-saving-to-pdf/)
- [在将Excel转换为PDF时呈现Office加载项](/cells/zh/cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [将每个Excel工作表呈现为一个PDF页面-从Excel转换为PDF](/cells/zh/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [通过Aspose.Cells在输出PDF中呈现Unicode补充字符](/cells/zh/cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [重新采样添加的图像-从Excel转换为PDF](/cells/zh/cpp/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存为不同的PDF文件](/cells/zh/cpp/save-each-worksheet-to-a-different-pdf-file/)
- [以标准或最小尺寸保存Excel到PDF](/cells/zh/cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [将指定的工作表保存为 PDF](/cells/zh/cpp/save-specified-worksheets-to-pdf/)
- [安全的PDF文件](/cells/zh/cpp/secure-pdf-documents/)
- [指定如何在输出PDF和图像中跨越字符串](/cells/zh/cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
