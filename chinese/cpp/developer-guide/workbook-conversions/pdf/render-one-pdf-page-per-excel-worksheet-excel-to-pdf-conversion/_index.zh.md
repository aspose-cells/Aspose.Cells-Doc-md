---
title: 为每个Excel工作表渲染一页PDF  使用C++将Excel转换为PDF
type: docs
weight: 100
url: /zh/cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: 使用Aspose.Cells将每个工作表转换为一页的PDF格式。
---

{{% alert color="primary" %}} 

当处理大型Microsoft Excel文件（例如包含多张工作表，每张50列和300行以上数据的工作簿）时，您可能希望PDF输出显示每个工作表一页，而不考虑工作表的大小。这意味着每一页的页面大小可能会大不相同。这可以通过使用Aspose.Cells for C++实现。

{{% /alert %}} 

请查看以下示例代码，将多个工作表的Excel文件转换为PDF。

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

    // Initialize a new Workbook and open an Excel file
    U16String inputFilePath = srcDir + u"input.xlsx";
    Workbook workbook(inputFilePath);

    // Implement one page per worksheet option
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetOnePagePerSheet(true);

    // Save the PDF file
    U16String outputFile = srcDir + u"OutputFile.out.pdf";
    workbook.Save(outputFile, pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

如果将[PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/)选项设置为**true**，所有工作表内容都将渲染到一页PDF中。

{{% /alert %}} {{% alert color="primary" %}} 

如果您的电子表格包含公式，建议在将电子表格渲染为PDF前调用[Workbook::CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)，确保依赖公式的值被重新计算，并在PDF中显示正确的值。

{{% /alert %}}
