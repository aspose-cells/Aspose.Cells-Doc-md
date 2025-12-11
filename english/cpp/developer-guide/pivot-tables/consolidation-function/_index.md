---
title: Consolidation Function with C++
linktitle: Consolidation Function
type: docs
weight: 20
url: /cpp/consolidation-function/
description: Learn how to apply a ConsolidationFunction to data fields of a pivot table using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Consolidation function**

Aspose.Cells can be used to apply a **ConsolidationFunction** to data fields (or value fields) of a pivot table. In Microsoft Excel, you can right‑click the value field and then select the **Value Field Settings...** option and then select the tab **Summarize Values By**. From there, you can select any ConsolidationFunction of your choice, such as Sum, Count, Average, Max, Min, Product, Distinct Count, etc.

Aspose.Cells provides the [**ConsolidationFunction**](https://reference.aspose.com/cells/cpp/aspose.cells/consolidationfunction/) enumeration to support the following consolidation functions.

- ConsolidationFunction::Average
- ConsolidationFunction::Count
- ConsolidationFunction::CountNums
- ConsolidationFunction::DistinctCount
- ConsolidationFunction::Max
- ConsolidationFunction::Min
- ConsolidationFunction::Product
- ConsolidationFunction::StdDev
- ConsolidationFunction::StdDevp
- ConsolidationFunction::Sum
- ConsolidationFunction::Var
- ConsolidationFunction::Varp

### **Applying ConsolidationFunction to Data Fields of Pivot Table**

The following code applies the **Average** consolidation function to the first data field (or value field) and the **DistinctCount** consolidation function to the second data field (or value field).

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.xlsx";

    // Create workbook from source Excel file
    Workbook workbook(inputFilePath);

    // Access the first worksheet of the workbook
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first pivot table of the worksheet
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Apply Average consolidation function to first data field
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Average);

    // Apply DistinctCount consolidation function to second data field
    pivotTable.GetDataFields().Get(1).SetFunction(ConsolidationFunction::DistinctCount);

    // Calculate the data to make the changes take effect
    pivotTable.CalculateData();

    // Saving the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Pivot table updated and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}
DistinctCount consolidation function is supported by Microsoft Excel 2013 only.
{{% /alert %}}

{{< app/cells/assistant language="cpp" >}}
