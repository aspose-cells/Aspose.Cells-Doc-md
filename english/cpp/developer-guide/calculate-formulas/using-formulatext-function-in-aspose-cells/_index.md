---
title: Using FormulaText Function in Aspose.Cells with C++
linktitle: Using FormulaText Function
description: This article introduces how to use the FormulaText function in Aspose.Cells library to process formulas in Microsoft Excel. By loading an existing Excel file or creating a new Excel file, we can use the method provided by Aspose.Cells to get and set the formula text of the cell and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, FormulaText functions
type: docs
weight: 60
url: /cpp/using-formulatext-function-in-aspose-cells/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

FormulaText is an Excel 2013 and later function. It is not supported by previous versions like Excel 2010 or 2007 etc. As its name suggests, it prints the text of the formula which is present in a given cell. This article will show you how to make use of this function using Aspose.Cells.

{{% /alert %}} 

The following sample code shows the usage of FormulaText with Aspose.Cells. The code first writes a formula in cell A1 and then prints the text of the formula using FormulaText in cell A2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**
Here is the console output of the above sample code.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
