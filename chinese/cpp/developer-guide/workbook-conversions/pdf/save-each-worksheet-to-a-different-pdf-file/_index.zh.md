---
title: 将每个工作表保存为不同的 PDF 文件，使用 C++
linktitle: 将每个工作表保存为不同的PDF文件
type: docs
weight: 130
url: /zh/cpp/save-each-worksheet-to-a-different-pdf-file/
description: 了解如何使用 Aspose.Cells for C++ 将 Excel 文件中的每个工作表保存为单独的 PDF 文件。
---

{{% alert color="primary" %}} 

 Aspose.Cells 支持将包含图片、图表等的 XLS 文件转换为 PDF 文档。Aspose.Cells for C++ 可以独立完成将电子表格转换为 PDF ，无需使用 Aspose.PDF for C++。转换过程中不需要创建或使用任何临时文件，全部在内存中完成。

{{% /alert %}} 

## **将每个工作表保存为不同的PDF文件**
 如果您需要将模板 Excel 文件中的每个工作表保存为不同的 PDF 文件，您可以轻松实现。可以尝试每次设置一个工作表索引为 [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) 选项进行渲染到 PDF。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Get the Excel file path
    U16String filePath = srcDir + u"input.xlsx";

    // Instantiate a new workbook and open the Excel file from its location
    Workbook workbook(filePath);

    // Get the count of the worksheets in the workbook
    int sheetCount = workbook.GetWorksheets().GetCount();

    // Define PdfSaveOptions
    PdfSaveOptions pdfSaveOptions;

    // Take PDFs of each sheet
    for (int j = 0; j < sheetCount; j++)
    {
        Worksheet ws = workbook.GetWorksheets().Get(j);

        // Set worksheet to output
        SheetSet sheetSet(Vector<int32_t>{ ws.GetIndex() });
        pdfSaveOptions.SetSheetSet(sheetSet);

        // Save the workbook with the current worksheet as PDF
        workbook.Save(srcDir + u"worksheet-" + ws.GetName() + u".out.pdf", pdfSaveOptions);
    }

    std::cout << "PDFs generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

如果你的电子表格包含公式，最好在渲染为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)。这样可以确保公式依赖的值被重新计算，且正确的值被渲染到PDF中。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
