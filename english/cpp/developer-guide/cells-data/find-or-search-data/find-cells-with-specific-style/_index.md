---
title: Find Cells with Specific Style with C++
linktitle: Find Cells with Specific Style
type: docs
weight: 190
url: /cpp/find-cells-with-specific-style/
description: Learn how to find or search cells with a particular style applied through the Aspose.Cells for C++ API.
keywords: Find cells with a particular style applied, Search cells with a particular style applied
---

{{% alert color="primary" %}}

Sometimes, you need to find cells with a particular style applied. You can use Aspose.Cells to find all cells with a common style. Aspose.Cells provides the [**FindOptions.Style**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/style/) property which you can use to specify the style to search cells for.

{{% /alert %}}

The code in this example finds all cells that have the same style as that of cell A1. After the code has been executed, all the cells that have the same style as A1 contain the text "Found".

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String filePath = srcDir + u"TestBook.xlsx";

    Workbook workbook(filePath);
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Style style = worksheet.GetCells().Get(u"A1").GetStyle();

    FindOptions options;
    options.SetStyle(style);

    Cell nextCell;

    do
    {
        nextCell = worksheet.GetCells().Find(U16String(), nextCell, options);
        if (nextCell.GetRow() == -1)
            break;
        nextCell.PutValue(u"Found");
    } while (true);

    U16String outputPath = outDir + u"output.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```