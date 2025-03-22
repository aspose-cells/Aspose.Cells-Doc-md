---
title: Creating Subtotals with C++
linktitle: Creating Subtotals
type: docs
weight: 800
url: /cpp/creating-subtotals/
description: Learn how to create subtotals for any repeating values in a spreadsheet by using the Aspose.Cells for C++ API.
keywords: Apply Subtotals, Set Subtotals, Add subtotals, Create Subtotals, How to add subtotals to a worksheet 
---

{{% alert color="primary" %}}

You can automatically create subtotals for any repeating values in a spreadsheet. Aspose.Cells provides API features that help you add subtotals to spreadsheets programmatically.

{{% /alert %}}

## **Using Microsoft Excel**

To add subtotals in Microsoft Excel:

1. Create a simple data list in the first worksheet of the workbook (as shown in the figure below) and save the file as Book1.xls.
1. Select any cell within your list.
1. From the **Data** menu, select **Subtotals**. The Subtotals dialog will be displayed. Define what function to use and where to place the subtotals.

## **Using the Aspose.Cells API**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in the Excel file.

A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class. The class provides a wide range of methods for managing worksheets and other objects. Each worksheet consists of a [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) collection. To add subtotals to a worksheet, use the [**Subtotal**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/subtotal/) method of the [**Cells**](https://reference.aspose.com/cells/cpp/aspose.cells/cells/) class. Provide parameter values to the method to specify how the subtotal should be calculated and placed.

In the examples below, we have added subtotals to the first worksheet of the template file (Book1.xls) using the Aspose.Cells API. When the code is executed, a worksheet with subtotals is created.

The code snippets that follow show how to add subtotals to a worksheet with Aspose.Cells for C++.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Instantiate a new workbook and open the template file
    Workbook workbook(inputFilePath);

    // Get the Cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Create a cell area i.e., B3:C19
    CellArea ca = CellArea::CreateCellArea(2, 1, 18, 2); // StartRow: 2, StartColumn: 1, EndRow: 18, EndColumn: 2

    // Apply subtotal; the consolidation function is Sum and it will be applied to the second column (C) in the list
    cells.Subtotal(ca, 0, ConsolidationFunction::Sum, Vector<int32_t>({ 1 }));

    // Save the Excel file
    workbook.Save(outDir + u"output.out.xls");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Advance topics**
- [Applying Subtotal and Changing Direction of Outline Summary Rows below Detail](/cells/cpp/applying-subtotal-and-changing-direction-of-outline-summary-rows-below-detail/)
