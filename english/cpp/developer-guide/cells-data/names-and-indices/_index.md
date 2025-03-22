---
title: Conversion between cell name and row/column index with C++
linktitle: Cell Name and Index Conversion
type: docs
weight: 10
url: /cpp/names-and-indices/
description: Learn how to get Conversion between cell name and row/column index through the Aspose.Cells for C++ API.
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
---

## **Get Cell Name from Row and Column Indices**
It is possible to find a cell's name given the row and column index. This article explains how.
Aspose.Cells provides the `CellsHelper::CellIndexToName` method which allows developers to get a cell's name if they provide the row and column index.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use `CellsHelper::CellIndexToName` to access the cell's name given a known row and column index. The code generates the following output.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Initialize row and column indices
    int32_t row = 3;
    int32_t column = 5;

    // Convert cell index to cell name
    U16String name = CellsHelper::CellIndexToName(row, column);

    // Output the cell name
    std::cout << "Cell name: " << name.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Get Row and Column Indices from Cell Name**
It is possible to find a row and column index of the cell from its name. This article explains how.
Aspose.Cells provides the `CellsHelper::CellNameToIndex` method which allows developers to get a row and column index from the cell's name.

{{% alert color="primary" %}} 

Microsoft Excel starts counting row and column indices from 1. Unlike Microsoft Excel, Aspose.Cells starts counting row and column indices from 0.

{{% /alert %}} 

The following sample code illustrates how to use `CellsHelper::CellNameToIndex` to get the row and column index from the cell's name. The code generates the following output.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Define the cell name
    U16String name = u"C4";

    // Variables to store row and column indices
    int32_t row = 0;
    int32_t column = 0;

    // Convert cell name to row and column indices
    CellsHelper::CellNameToIndex(name, row, column);

    // Output the row and column indices
    std::cout << "Row: " << row << ", Column: " << column << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Create safe sheet names**
Sometimes there is a need of assigning the sheet name at runtime. In this scenario, there may be sheet names which may contain some additional characters like `<>+()?`. There is a need to replace any such character, which is not allowed as a sheet name with some preset character provided by user. Similarly the length may increase to more than 31 characters which needs to be truncated. Aspose.Cells provides a feature to handle all these issues. Following sample code demonstrates this feature:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Long name will be truncated to 31 characters
    U16String name1 = CellsHelper::CreateSafeSheetName(u"this is first name which is created using CellsHelper.CreateSafeSheetName and truncated to 31 characters");

    // Any invalid character will be replaced with _
    U16String name2 = CellsHelper::CreateSafeSheetName(u" <> + (adj.Private ? \" Private\" : \")", u'_'); //? shall be replaced with _

    // Display first name
    std::cout << name1.ToUtf8() << std::endl;

    // Display second name
    std::cout << name2.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Output:

```
this is first name which is cre
<> + (adj.Private _ " Private"
```