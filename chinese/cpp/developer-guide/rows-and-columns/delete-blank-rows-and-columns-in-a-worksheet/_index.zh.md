---
title: 用C++删除工作表中的空白行和空白列
linktitle: 在工作表中删除空行和空列
type: docs
weight: 300
url: /zh/cpp/delete-blank-rows-and-columns-in-a-worksheet/
description: 使用Aspose.Cells和C++删除工作表中的空行和空列。
---

{{% alert color="primary" %}}

可以从工作表中删除所有空白行和列。这在例如从微软Excel文件生成PDF文件时非常有用，只转换包含数据或相关对象的行和列。

使用以下Aspose.Cells方法来删除空行和空列:

1. 要删除空行，请使用[**Cells.DeleteBlankRows()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankrows/)方法。请注意，对于将要被删除的空行，不仅需要[**Row.IsBlank**](https://reference.aspose.com/cells/cpp/aspose.cells/row/isblank/)为true，还必须在这些行中的任何单元格没有可见的注释定义，也不应该和任何数据透视表的范围相交。
2. 要删除空白列，使用 [**Cells.DeleteBlankColumns()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleteblankcolumns/) 方法。

{{% /alert %}}

## C++ 代码删除空白行

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

    // Open an existing Excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";
    Workbook workbook(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = workbook.GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the Blank Rows from the worksheet
    sheet.GetCells().DeleteBlankRows();

    // Save the Excel file
    U16String outputFilePath = outDir + u"mybook.out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Blank rows deleted and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## C++ 代码删除空白列

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"SampleInput.xlsx";

    // Create a smart pointer to a new Workbook instance
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Create a Worksheets object with reference to the sheets of the Workbook
    WorksheetCollection sheets = wb->GetWorksheets();

    // Get the first Worksheet from WorksheetCollection
    Worksheet sheet = sheets.Get(0);

    // Delete the blank columns from the worksheet
    sheet.GetCells().DeleteBlankColumns();

    // Save the excel file
    U16String outputFilePath = srcDir + u"mybook.out.xlsx";
    wb->Save(outputFilePath);

    std::cout << "Blank columns deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
