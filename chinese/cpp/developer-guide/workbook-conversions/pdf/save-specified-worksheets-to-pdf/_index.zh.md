---  
title: 使用 C++ 将特定工作表导出为 PDF  
linktitle: 将指定的工作表保存为 PDF  
type: docs  
weight: 140  
url: /zh/cpp/save-specified-worksheets-to-pdf/  
description: 使用 Aspose.Cells 与 C++ 导出特定工作表为 PDF。  
---  

 默认情况下，Aspose.Cells 会将工作簿中所有 **可见** 工作表保存为一个 PDF 文件。使用 [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) 选项，可以保存指定的工作表为 PDF。例如，可以保存活动工作表为 PDF，保存所有工作表（包括隐藏和不可见工作表）为 PDF，或保存自定义的多个工作表为 PDF。

## **将活动工作表保存为 PDF**

 如果只想导出活动工作表为 PDF，可以将 [**SheetSet.GetActive()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getactive/) 传递给 [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) 选项实现。

 源文件 [sheetset-example.xlsx](sheetset-example.xlsx) 的工作表 `Sheet2` 为活动工作表。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set active sheet to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetActive());

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## ** 保存所有工作表为 PDF**

 [**SheetSet.GetVisible()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getvisible/) 表示工作簿中的可见工作表，[**SheetSet.GetAll()**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) 表示包括所有工作表（包括隐藏/不可见工作表）。如果要导出所有工作表为 PDF，可以直接传递 [**SheetSet.GetAll**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/sheetset/getall/) 给 [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) 选项。

源文件[sheetset-example.xlsx](sheetset-example.xlsx)包含所有四个工作表，其中隐藏了工作表`Sheet3`。

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Set all sheets to output
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(SheetSet::GetAll());

    // Save the PDF file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF file generated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **将指定的工作表保存为 PDF**

 如果想导出多个自定义工作表为 PDF，可以通过传递多个工作表索引到 [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) 选项实现。

```c++
#include <iostream>
#include "Aspose.Cells.h"
#include "Aspose.Cells/PdfSaveOptions.h"
#include "Aspose.Cells/SheetSet.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template Excel file
    U16String inputFilePath(u"sheetset-example.xlsx");
    Workbook workbook(inputFilePath);

    // Set custom multiple sheets (Sheet1, Sheet3) to output
    Vector<int32_t> sheetIndexes = {0, 2};
    SheetSet sheetSet(sheetIndexes);

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the PDF file with PdfSaveOptions
    U16String outputFilePath(u"output.pdf");
    workbook.Save(outputFilePath, pdfSaveOptions);

    std::cout << "Excel file saved as PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## ** 将工作表重新排序为 PDF**

 如果希望在不修改源文件的情况下，将工作表（如反转顺序）重新排序后导出为 PDF，可以将重新排序的工作表索引传递给 [**PdfSaveOptions.GetSheetSet()**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/getsheetset/) 选项。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Open the template excel file
    Workbook workbook(u"sheetset-example.xlsx");

    // Reorder sheets (Sheet1, Sheet2, Sheet3, Sheet4) to (Sheet4, Sheet3, Sheet2, Sheet1)
    Vector<int32_t> sheetIndexes = { 3, 2, 1, 0 };
    SheetSet sheetSet(sheetIndexes);

    // Create PdfSaveOptions and assign the sheet set
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetSheetSet(sheetSet);

    // Save the pdf file with PdfSaveOptions
    workbook.Save(u"output.pdf", pdfSaveOptions);

    std::cout << "PDF saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
