---
title: Calculate Formulas with C++
linktitle: Calculate Formulas
description: This article introduces how to use Aspose.Cells library to calculate formulas in Microsoft Excel with C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to calculate the formula and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, formulas, calculations, Direct Calculation of Formula, Calculate Formulas repeatedly, add formulas.
type: docs
weight: 125
url: /cpp/calculate-formulas/
---

## **Adding Formulas & Calculating Results**

Aspose.Cells has an embedded formula calculation engine. Not only can it re-calculate formulas imported from designer templates, but it also supports calculating the results of formulas added at runtime.

Aspose.Cells supports most of the formulas or functions that are part of Microsoft Excel (Read [a list of the functions supported by the calculation engine](/cells/cpp/supported-formula-functions/)). Those functions can be used through the APIs or designer spreadsheets. Aspose.Cells supports a huge set of mathematical, string, boolean, date/time, statistical, database, lookup, and reference formulas.

Use the [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) property or [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) methods of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class to add a formula to a cell. When applying a formula, always begin the string with an equal sign (=) as you do when creating a formula in Microsoft Excel and use a comma (,) to delimit function parameters.

To calculate the results of formulas, the user may call the [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) method of the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class, which processes all formulas embedded in an Excel file. Or, the user may call the [**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) method of the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class, which processes all formulas embedded in a sheet. Or, the user may also call the [**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/) method of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class, which processes the formula of one Cell:

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Important to Know for Formulas**

{{% alert color="primary" %}}

The **GetFormula** property and **SetFormula(...)** methods of the [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class work differently from the **Calculate** methods of the [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/), and [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) classes. The **GetFormula** property and **SetFormula(...)** methods simply add the formula to a cell but do not calculate the result at runtime. To get the result of the formulas, please call the **Calculate** methods.

{{% /alert %}}

## **Direct Calculation of Formula**

Aspose.Cells has an embedded formula calculation engine. As well as calculating formulas imported from a designer file, Aspose.Cells can calculate formula results directly.

Sometimes, you need to calculate formula results directly without adding them into a worksheet. The values of the cells used in the formula already exist in a worksheet, and all you need is to find the result of those values based on some Microsoft Excel formula without adding the formula in a worksheet.

You can use Aspose.Cells' formula calculation engine APIs for [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) to [**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) the results of such formulas without adding them to the worksheet:

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

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

Above code produces the following output:
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **How to Calculate Formulas Repeatedly**

When there are lots of formulas in the workbook and the user needs to calculate them repeatedly with modifying only a small part of them, it may be helpful for performance to enable the formula calculation chain: [**FormulaSettings.EnableCalculationChain**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/enablecalculationchain/).

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Important to Know**

{{% alert color="primary" %}}

By default, the calculation chain is disabled. Because creating the chain also needs extra time, the first time of calculating formulas ([**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)) may consume more CPU processing time and memory when comparing with calculating formulas without a chain. If the user does not need to calculate formulas repeatedly, the default behavior (calculating formula directly without creating a calculation chain) should be the better way.

{{% /alert %}}

## **Advance Topics**
- [Add Cells to Microsoft Excel Formula Watch Window](/cells/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Calculating IFNA function using Aspose.Cells](/cells/cpp/calculating-ifna-function-using-aspose-cells/)
- [Calculation of Array Formula of Data Tables](/cells/cpp/calculation-of-array-formula-of-data-tables/)
- [Calculation of Excel 2016 MINIFS and MAXIFS functions](/cells/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Decrease the Calculation Time of Cell.Calculate method](/cells/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Direct calculation of custom function without writing it in a worksheet](/cells/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Returning a Range of Values using AbstractCalculationEngine](/cells/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Setting Formula Calculation Mode of Workbook](/cells/cpp/setting-formula-calculation-mode-of-workbook/)
- [Using FormulaText function in Aspose.Cells](/cells/cpp/using-formulatext-function-in-aspose-cells/)