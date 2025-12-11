---
title: Update Power Query Formula Item with C++
linktitle: Update Power Query Formula Item
type: docs
weight: 120
url: /cpp/update-power-query-formula-item/
description: Learn how to update Power Query Formula Items using Aspose.Cells for C++ to modify data source file locations in Excel files.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Usage Scenario**

There might be cases where the data source files are moved, and the Excel file is unable to locate the file. In such cases, Aspose.Cells API provides the option to update the Power Query Formula **Item** by using the *PowerQueryFormulaItem* class to update the location of the source file.

## **Updating Power Query Formula Item**

Aspose.Cells API provides the ability to update Power Query Formula Items. The following code snippet demonstrates updating the data source file location in the Excel file by using the **PowerQueryFormulaItem.GetValue()** property. The source and output files are attached for your reference.

- [Source File 1](106364953.xlsx)
- [Source File 2](106364954.xlsx)
- [Output File](106364955.xlsx)

## **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook(srcDir + u"SamplePowerQueryFormula.xlsx");
    DataMashup mashupData = workbook.GetDataMashup();

    PowerQueryFormulaCollection powerQueryFormulas = mashupData.GetPowerQueryFormulas();
    for (int i = 0; i < powerQueryFormulas.GetCount(); ++i)
    {
        PowerQueryFormula formula = powerQueryFormulas.Get(i);
        PowerQueryFormulaItemCollection powerQueryFormulaItems = formula.GetPowerQueryFormulaItems();
        for (int j = 0; j < powerQueryFormulaItems.GetCount(); ++j)
        {
            PowerQueryFormulaItem item = powerQueryFormulaItems.Get(j);
            if (item.GetName() == u"Source")
            {
                U16String newValue = u"Excel.Workbook(File.Contents(\"" + srcDir + u"SamplePowerQueryFormulaSource.xlsx" + u"\"), null, true)";
                item.SetValue(newValue);
            }
        }
    }

    workbook.Save(outDir + u"SamplePowerQueryFormula_out.xlsx");
    std::cout << "PowerQueryFormula updated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
