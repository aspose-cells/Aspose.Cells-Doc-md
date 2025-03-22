---
title: Insert or Delete Rows in an Excel Worksheet with C++
linktitle: Insert or Delete Rows
type: docs
weight: 20
url: /cpp/insert-or-delete-rows-in-an-excel-worksheet/
description: This article provides the C++ code to insert and delete rows in an Excel worksheet.
keywords: c++ insert or delete rows in excel worksheet, c++ insert or delete rows in excel, c++ insert rows in excel, c++ delete rows in excel, insert or delete rows in excel worksheet with c++, insert or delete rows in excel with c++, insert rows in excel with c++, delete rows in excel with c++
---

{{% alert color="primary" %}}

When creating a new worksheet, or working with an existing worksheet, you might need to add extra rows or columns to accommodate data. At other times, you might need to delete rows or columns from specified positions in the worksheet.

{{% /alert %}}

Aspose.Cells offers two methods for inserting and deleting rows: [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) and [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/). These methods are optimized for performance and do the job very quickly.

To insert or remove a number of rows, we recommend that you always use the [**Cells.InsertRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrows/) and [**Cells.DeleteRows**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterows/) methods instead of using the [**Cells.InsertRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/insertrow/) or [**DeleteRow**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/deleterow/) methods in a loop.

Aspose.Cells works in the same way as Microsoft Excel does. When rows or columns are added, the worksheet content is shifted down and to the right. When rows or columns are removed, the worksheet content is shifted up or to the left. Any references in other worksheets and cells are updated when rows are added or removed.

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
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_book1.out.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Insert 10 rows at row index 2 (insertion starts at 3rd row)
    sheet.GetCells().InsertRows(2, 10);

    // Delete 5 rows now. (8th row - 12th row)
    sheet.GetCells().DeleteRows(7, 5);

    // Save the excel file
    workbook.Save(outputFilePath);

    std::cout << "Rows inserted and deleted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```