---
title: Accessing Cells of a Worksheet with C++
linktitle: Accessing Cells of a Worksheet
type: docs
weight: 10
url: /cpp/accessing-cells-of-a-worksheet/
description: This article shows how to get the maximum display range of worksheet and access cells through the Aspose.Cells for C++ API.
keywords: Get Cell object, Access Cells, Get maximum display range of worksheet.
---

{{% alert color="primary" %}}

We know that all worksheets may contain data that is basically stored in cells (with which a worksheet is made up of). A cell is a basic part of a worksheet that is used to construct the whole worksheet as a sequence of rows and columns. Before we try to access data from a worksheet, we would need to get access to its cells. So, in this topic, we will discuss some basic approaches to access worksheet cells at runtime using Aspose.Cells.

{{% /alert %}}

## **How to Access Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) that represents an Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**WorksheetCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection that represents all cells in the worksheet.

We can use [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection to access cells in a worksheet. Aspose.Cells provides three basic approaches to access cells in a worksheet:

1. Using the cell name.
1. Using a cell's row and column index.
1. Using a cell index in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection

**IMPORTANT:** We have mentioned that the 3rd approach is the fastest and the 1st approach is the slowest one. The performance difference between the approaches is very small so don't worry about performance degradation, whichever approach you use.

### **How to Get Cell Object by Cell Name**

Developers can access any specific cell by passing its cell name to the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection of the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class as an index.

If you create a blank worksheet at the start, the count of [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection is zero. When you use this approach to access a cell, it will check whether this cell exists in the collection or not. If yes, it returns the cell object in the collection otherwise, it creates a new [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) object, adds the object to the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection and then returns the object. This approach is the easiest way to access the cell if you are familiar with Microsoft Excel but it's the slowest one as compared to other approaches.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Using the first worksheet in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its name
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get cell value as string
    U16String value = cell.GetStringValue();

    // Output the value to console
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **How to Get Cell Object by Row & Column Index of the Cell**

Developers can access any specific cell by passing the indices of its row and column to the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection of the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class.

This approach works in the same way as that of the first approach.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell at row 0, column 0
    Cell cell = worksheet.GetCells().Get(0, 0);

    // Get cell value as string
    U16String value = cell.GetStringValue();

    // Print cell value
    std::cout << value.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **How to Get Cell Object by Cell Index in Cells Collection**

A cell can also be accessed by passing the cell's numeric index to the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection.

If you use this approach to access cells, an exception can be thrown if the numeric index of the cell is out of range. This approach is the fastest one to access the cells but an important thing to know is that if you use this approach to access a cell object, the numeric index may change after new cells are added to the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. The cell objects in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection are internally sorted by row and column indices.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Open an existing worksheet
    Workbook workbook(srcDir + u"book1.xls");

    // Using the Sheet 1 in Workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Accessing a cell using its row and column
    Cell cell = worksheet.GetCells().CheckCell(0, 0);

    if (cell)
    {
        U16String value = cell.GetStringValue();
        std::cout << value.ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **How to Get Maximum Display Range of Worksheet**

Aspose.Cells allows developers to access a worksheet's maximum display range. The maximum display range - the range of cells between the first and last cell with content - is useful when you need to copy, select, or display the entire contents of a worksheet in an image.

You can access a worksheet's maximum display range using [**Worksheet.GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/). The following sample code illustrates how to access the [**GetMaxDisplayRange()**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/getmaxdisplayrange/) property.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Path to source file
    U16String filePath = srcDir + u"Book1.xlsx";

    // Instantiating a Workbook object
    Workbook workbook(filePath);

    // Instantiate a workbook from source file
    Workbook wb(filePath);

    // Access the first worksheet
    Worksheet worksheet = wb.GetWorksheets().Get(0);

    // Access the Maximum Display Range
    Range range = worksheet.GetCells().GetMaxDisplayRange();

    // Print the Maximum Display Range RefersTo property
    std::cout << "Maximum Display Range: " << range.GetRefersTo().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```