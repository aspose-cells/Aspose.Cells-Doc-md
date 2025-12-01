---
title: Propagate Formula in Table or List Object automatically while entering data in new rows with C++
linktitle: Sets Table Formula
type: docs
weight: 260
url: /cpp/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
description: Learn how to propagate formulas in tables or list objects automatically when entering new data using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes, you want a formula in your Table or List Object to automatically propagate to new rows while entering new data. This is the default behavior of Microsoft Excel. To achieve the same functionality with Aspose.Cells, use the [ListColumn::GetFormula](https://reference.aspose.com/cells/cpp/aspose.cells.tables/listcolumn/getformula/) method.

## **Propagate Formula in Table or List Object automatically while entering data in new rows**
The following sample code creates a Table or List Object in such a way that the formula in column B will automatically propagate to new rows when you enter new data. Please check the [output excel file](5115469.xlsx) generated with this code. If you enter any number in cell A3, you will see that the formula in cell B2 automatically propagates to cell B3.

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

    // Create workbook object
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Add column headings in cell A1 and B1
    sheet.GetCells().Get(0, 0).PutValue(u"Column A");
    sheet.GetCells().Get(0, 1).PutValue(u"Column B");

    // Add list object, set its name and style
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(0, 0, 1, sheet.GetCells().GetMaxColumn(), true));
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium2);
    listObject.SetDisplayName(u"Table");

    // Set the formula of second column so that it propagates to new rows automatically while entering data
    listObject.GetListColumns().Get(1).SetFormula(u"=[Column A] + 1");

    // Save the workbook in xlsx format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
