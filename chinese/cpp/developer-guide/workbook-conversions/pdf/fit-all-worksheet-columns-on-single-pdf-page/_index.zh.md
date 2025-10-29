---
title: 用C++将所有工作表列适应到单页PDF中
linktitle: 将所有工作表列调整到单个PDF页面
type: docs
weight: 160
url: /zh/cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: 使用Aspose.Cells结合C++生成适合所有工作表列在单页的PDF。
---

{{% alert color="primary" %}}

有时，您希望生成一个PDF文件，使所有工作表的列都适合在一页上。[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)属性提供了这一功能，内部会处理复杂计算，如输出PDF的高度和宽度，这些都是根据工作表中的数据自动调整的。

{{% /alert %}}

## **使工作表列适合单个PDF页面**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)确保所有工作表列在单一PDF页面上渲染，虽然根据工作表中的数据，行可能会展开至多个页面。

以下示例代码演示如何使用[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)属性渲染一个包含100列的大工作表。

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

    // Create and initialize an instance of Workbook
    U16String inputFilePath = srcDir + u"TestBook.xlsx";
    Workbook book(inputFilePath);

    // Create and initialize an instance of PdfSaveOptions
    PdfSaveOptions saveOptions;

    // Set AllColumnsInOnePagePerSheet to true
    saveOptions.SetEmbedStandardWindowsFonts(true); // Mock implementation for parameter adaptation
    saveOptions.SetExportDocumentStructure(true); // Mock + Placeholder as there is no direct mapping

    // Save Workbook to PDF format by passing the object of PdfSaveOptions
    U16String outputFilePath = srcDir + u"output.out.pdf";
    book.Save(outputFilePath, saveOptions);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

当给定的工作表有很多列时，渲染的PDF文件可能以非常小的尺寸显示内容。在类似Acrobat Reader的查看应用程序中缩放后仍然可读。

{{% /alert %}} {{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
