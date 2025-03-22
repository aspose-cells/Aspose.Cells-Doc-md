---
title: Update Power Query Formula Item with C++
linktitle: Update Power Query Formula Item
type: docs
weight: 120
url: /cpp/update-power-query-formula-item/
description: Learn how to update Power Query Formula Items using Aspose.Cells for C++ to modify data source file locations in Excel files.
---

## **Usage Scenario**

There might be cases where the data source files are moved, and the Excel file is unable to locate the file. In such cases, Aspose.Cells API provides the option to update the Power Query Formula item by using the [*PowerQueryFormulaItem*](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/) class to update the location of the source file.

## **Updating Power Query Formula Item**

Aspose.Cells API provides the ability to update Power Query Formula Items. The following code snippet demonstrates updating the data source file location in the Excel file by using the [**PowerQueryFormulaItem.Value**](https://reference.aspose.com/cells/cpp/aspose.cells.querytables/powerqueryformulaitem/value/) property. The source and output files are attached for your reference.

- [Source File 1](106364953.xlsx)
- [Source File 2](106364954.xlsx)
- [Output File](106364955.xlsx)

## **Sample Code**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load the workbook
    Workbook workbook(srcDir + u"SamplePowerQueryFormula.xlsx");

    // Get the DataMashup object
    DataMashup mashupData = workbook.GetDataMashup();

    // Iterate through PowerQueryFormulas
    auto powerQueryFormulas = mashupData.GetPowerQueryFormulas();
    for (auto& formula : powerQueryFormulas)
    {
        // Iterate through PowerQueryFormulaItems
        auto powerQueryFormulaItems = formula.GetPowerQueryFormulaItems();
        for (auto& item : powerQueryFormulaItems)
        {
            // Check if the item name is "Source"
            if (item.GetName() == u"Source")
            {
                // Update the item value
                U16String newValue = u"Excel.Workbook(File.Contents(\"" + srcDir + u"SamplePowerQueryFormulaSource.xlsx" + u"\"), null, true)";
                item.SetValue(newValue);
            }
        }
    }

    // Save the output workbook
    workbook.Save(outDir + u"SamplePowerQueryFormula_out.xlsx");

    std::cout << "PowerQueryFormula updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```