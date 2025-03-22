---
title: Find or Search Data with C++
linktitle: Find or Search Data
type: docs
weight: 50
url: /cpp/find-or-search-data/
description: Learn how to find or search cells in a worksheet that contains specified data through the Aspose.Cells for C++ API.
keywords: Find data, Search data, Find Cells Containing a Formula, Search Cells Containing a Formula, Find Data or Formulas using FindOptions, Search Data or Formulas using FindOptions, Find or Search Cells Containing Specified String Value or Number, Find or Search cells contains specified data
---

{{% alert color="primary" %}}

Microsoft Excel allows users to find cells in a worksheet that contains specified data.

{{% /alert %}}

## **Finding Cells Containing Specified Data**

### **Using Microsoft Excel**

Microsoft Excel allows users to find cells in a worksheet that contains specified data. If you select **Edit** from the **Find** menu in Microsoft Excel, you will see a dialog where you can specify the search value.

Here, we are looking for the value "Oranges". Aspose.Cells also allows developers to find cells in the worksheet containing specified values.

### **Using Aspose.Cells**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The  [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection that represents all cells in the worksheet. The [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection provides several methods for finding cells in a worksheet containing user-specified data. A few of these methods are discussed below in more detail.

{{% alert color="primary" %}}

All Find methods return the references of the cells containing the specified data to search.

{{% /alert %}}

## **Finding Cells Containing a Formula**

Developers can find a specified formula in the worksheet by calling the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection's [**Find**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/find/) method. Typically, the [**Find**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/find/) method accepts three parameters:

- **Object:** The object to search for. The type should be int,double,DateTime,string,bool.
- **Previous cell:** Previous cell with the same object. This parameter can be set to null if searching from the start.
- **FindOptions:** Options for finding the required object.

The examples below use worksheet data for practicing find methods:

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
    U16String inputFilePath = srcDir + u"sampleFindingCellsContainingFormula.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Instantiate FindOptions Object
    FindOptions findOptions;
    findOptions.SetLookInType(LookInType::Formulas);

    // Finding the cell containing the specified formula
    Cell cell = worksheet.GetCells().Find(u"=SUM(A5:A10)", nullptr, findOptions);

    // Printing the name of the cell found after searching worksheet
    std::cout << "Name of the cell containing formula: " << cell.GetName().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Finding Data or Formulas using FindOptions**

It is possible to find specified values using the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection's [**Find**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/find/) method with various [**FindOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/). Typically, the [**Find**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/find/) method accepts the following parameters:

- **Search value**, the data or value to be searched for.
- **Previous cell**, the last cell that contained the same value. This parameter can be set to null when searching from the start.
- **Find options**, the find options.

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
    U16String inputFilePath = srcDir + u"sampleFindingDataOrFormulasUsingFindOptions.xlsx";

    // Instantiate the workbook object
    Workbook workbook(inputFilePath);

    // Calculate formulas in the workbook
    workbook.CalculateFormula();

    // Get Cells collection from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Instantiate FindOptions Object
    FindOptions findOptions;

    // Create a Cells Area
    CellArea ca;
    ca.StartRow = 8;
    ca.StartColumn = 2;
    ca.EndRow = 17;
    ca.EndColumn = 13;

    // Set cells area for find options
    findOptions.SetRange(ca);

    // Set searching properties
    findOptions.SetSearchBackward(false);
    findOptions.SetSearchOrderByRows(true);

    // Set the lookintype, you may specify, values, formulas, comments etc.
    findOptions.SetLookInType(LookInType::Values);

    // Set the lookattype, you may specify Match entire content, endswith, starwith etc.
    findOptions.SetLookAtType(LookAtType::EntireContent);

    // Find the cell with value
    Cell cell = cells.Find(341, nullptr, findOptions);

    if (cell)
    {
        std::cout << "Name of the cell containing the value: " << cell.GetName().ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Record not found " << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Finding Cells Containing Specified String Value or Number**

It is possible to find specified string values by calling the same [**Find**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/find/) method found in the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection with various [**FindOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/).

Specify the [**FindOptions.LookInType**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/lookintype/) and [**FindOptions.LookAtType**](https://reference.aspose.com/cells/cpp/aspose.cells/findoptions/lookattype/) properties. The following example code illustrates how to use these properties to find cells with various number of strings at the **beginning** or at the **center** or at the **end** of the cell's string.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Instantiate the workbook object
    Workbook workbook(srcDir + u"book1.xls");

    // Get Cells collection
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create FindOptions object
    FindOptions opts;
    opts.SetLookInType(LookInType::Values);
    opts.SetLookAtType(LookAtType::EntireContent);

    // Find the cell with the input integer or double
    Cell cell1 = cells.Find(205, nullptr, opts);

    if (cell1)
    {
        std::cout << "Name of the cell containing the value: " << cell1.GetName().ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Record not found " << std::endl;
    }

    // Find the cell with the input string
    Cell cell2 = cells.Find(u"Items A", nullptr, opts);

    if (cell2)
    {
        std::cout << "Name of the cell containing the value: " << cell2.GetName().ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Record not found " << std::endl;
    }

    // Find the cell containing with the input string
    opts.SetLookAtType(LookAtType::Contains);
    Cell cell3 = cells.Find(u"Data", nullptr, opts);

    if (cell3)
    {
        std::cout << "Name of the cell containing the value: " << cell3.GetName().ToUtf8() << std::endl;
    }
    else
    {
        std::cout << "Record not found " << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Find Cells with Specific Style](/cells/cpp/find-cells-with-specific-style/)
- [Find if the cell value starts with single quote mark](/cells/cpp/find-if-the-cell-value-starts-with-single-quote-mark/)
- [Search Data using Original Values](/cells/cpp/search-data-using-original-values/)