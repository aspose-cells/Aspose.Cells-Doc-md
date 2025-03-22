---
title: Precedents and Dependents with C++
linktitle: Precedents and Dependents
type: docs
weight: 230
url: /cpp/precedents-and-dependents/
description: Learn how to trace precedent and dependent cells in Excel files using Aspose.Cells with C++.
---

{{% alert color="primary" %}} 

Complex financial worksheets, especially ones developed in collaboration, can hide the most embarrassing errors. Checking formulas for accuracy and finding the source of an error can be difficult when the formula uses precedent cells and dependent cells.

{{% /alert %}} 

## **Introduction**
- **Precedent cells** are cells that are referred to by a formula in another cell. For example, if cell D10 contains the formula `=B5`, cell B5 is a precedent to cell D10.
- **Dependent cells** contain formulas that refer to other cells. For example, if cell D10 contains the formula `=B5`, cell D10 is dependent on cell B5.

To make the spreadsheet easy to read, you might want to clearly show which cells on a spreadsheet are used in a formula. Similarly, you may want to extract the dependent cells of other cells.

Aspose.Cells allows you to trace cells and find out which are linked.

## **Tracing Precedent and Dependent Cells: Microsoft Excel**
Formulas may change based on modifications made by a client. For example, if cell C1 is dependent on C3 and C4 containing a formula, and C1 is changed (so the formula is overridden), C3 and C4, or other cells, need to change to balance the spreadsheet based on business rules.

Similarly, suppose C1 contains the formula `=(B1*22)/(M2*N32)`. You might want to find the cells that C1 depends on, that is the precedent cells B1, M2, and N32.

You might need to trace the dependency of a particular cell to other cells. If business rules are embedded in formulas, we would like to find out the dependency and execute some rules based on it. Similarly, if the value of a particular cell is modified, which cells in the worksheet are impacted by that change?

Microsoft Excel allows users to trace precedents and dependents.

1. On the **View Toolbar**, select **Formula Auditing**. The Formula Auditing dialog will be displayed.
1. Trace Precedents:
   1. Select the cell that contains the formula for which you want to find precedent cells.
   1. To display a tracer arrow to each cell that directly provides data to the active cell, click **Trace Precedents** on the **Formula Auditing** toolbar.
1. Trace formulas that reference a particular cell (dependents):
   1. Select the cell for which you want to identify the dependent cells.
   1. To display a tracer arrow to each cell that is dependent on the active cell, click **Trace Dependents** on the **Formula Auditing** toolbar.

## **Tracing Precedent and Dependent Cells: Aspose.Cells**
### **Tracing Precedents**
Aspose.Cells makes it easy to get precedent cells. Not only can it retrieve cells that provide data to simple formula precedents but also find cells that provide data to complex formula precedents with named ranges.

In the example below, a template Excel file, `Book1.xls`, is used. The spreadsheet has data and formulas on the first Worksheet.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class' [GetPrecedents](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getprecedents/) method used to trace a cell's precedents. It returns a [ReferredAreaCollection](https://reference.aspose.com/cells/cpp/aspose.cells/referredareacollection/). As you can see above, in `Book1.xls`, cell B7 contains a formula `=SUM(A1:A3)`. So cells A1:A3 are the precedent cells to cell B7. The following example demonstrates the tracing precedents feature using the template file `Book1.xls`.

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
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Get cells from the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Get cell at B4
    Cell cell = cells.Get(u"B4");

    // Get precedents of the cell
    ReferredAreaCollection ret = cell.GetPrecedents();

    // Get the first referred area
    ReferredArea area = ret.Get(0);

    // Print sheet name and cell range
    std::cout << area.GetSheetName().ToUtf8() << std::endl;
    std::cout << CellsHelper::CellIndexToName(area.GetStartRow(), area.GetStartColumn()).ToUtf8() << std::endl;
    std::cout << CellsHelper::CellIndexToName(area.GetEndRow(), area.GetEndColumn()).ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Tracing Dependents**
Aspose.Cells lets you get dependent cells in spreadsheets. Aspose.Cells not only can retrieve cells that provide data regarding a simple formula but also find cells that provide data to a complex formula dependents with named ranges.

Aspose.Cells provides the [Cell](https://reference.aspose.com/cells/cpp/aspose.cells/cell/) class' [GetDependents](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdependents/) method used to trace a cell's dependents. For example, in `Book1.xlsx` there are formulas: `=A1+20` and `=A1+30` in the B2 and C2 cells respectively. The following example demonstrates how to trace the dependents for the A1 cell using the template file `Book1.xlsx`.

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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cells collection
    Cells cells = worksheet.GetCells();

    // Get specific cell
    Cell cell = cells.Get(u"B2");

    // Get dependent cells
    Vector<Cell> dependents = cell.GetDependents(true);

    // Print names of dependent cells
    for (const Cell& dependent : dependents)
    {
        std::cout << dependent.GetName().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Tracing Precedent and Dependent Cells According to Calculation Chain**
The above APIs for tracing precedents and dependents are based on the formula expression itself. They simply provide a convenient way for users to trace interdependencies for a few formulas. If there are a large number of formulas in the workbook and the user needs to trace precedents and dependents for every cell, they will give poor performance. For such situations, users should consider using [GetPrecedentsInCalculation](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getprecedentsincalculation/) and [GetDependentsInCalculation](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getdependentsincalculation/) methods. These two methods trace dependencies according to the calculation chain. So, to use them, first, you need to enable the calculation chain by [Workbook.Settings.FormulaSettings.EnableCalculationChain](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/enablecalculationchain/). Then you should perform a full calculation for the Workbook by [Workbook.CalculateFormula()](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/). After that, you can trace precedents or dependents for all those cells you need.

For some formulas, the resultant precedents may be different for `GetPrecedents` and `GetPrecedentsInCalculation`, and the resultant dependents may be different for `GetDependents` and `GetDependentsInCalculation`. For example, if cell A1's formula is `=IF(TRUE,B2,C3)`, `GetPrecedents` will provide B2 and C3 as A1's precedent. Accordingly, B2 and C3 both have the dependent A1 when checking by `GetDependents`. However, for the calculation of this formula, it is obvious that only B2 can affect the calculated result. So `GetPrecedentsInCalculation` will not provide C3 for A1, and `GetDependentsInCalculation` will not provide A1 for C3. Sometimes users may just have the requirement of tracing those interdependencies that actually affect the calculated result of formulas based on the current data of the Workbook, then they also need to use `GetDependentsInCalculation`/`GetPrecedentsInCalculation` instead of `GetDependents`/`GetPrecedents`.

The following example demonstrates how to trace the precedents and dependents according to the calculation chain for cells:

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").SetFormula(u"=B1+SUM(B1:B10)+[Book1.xls]Sheet1!B2");
    cells.Get(u"A2").SetFormula(u"=IF(TRUE,B2,B1)");

    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);
    workbook.CalculateFormula();

    std::cout << "B1's calculation dependents:" << std::endl;
    auto enB1 = cells.Get(u"B1").GetDependentsInCalculation(false);
    while (enB1.MoveNext())
    {
        Cell c = enB1.GetCurrent();
        std::cout << c.GetName().ToUtf8() << std::endl;
    }

    std::cout << "B2's calculation dependents:" << std::endl;
    auto enB2 = cells.Get(u"B2").GetDependentsInCalculation(false);
    while (enB2.MoveNext())
    {
        Cell c = enB2.GetCurrent();
        std::cout << c.GetName().ToUtf8() << std::endl;
    }

    std::cout << "A1's calculation precedents:" << std::endl;
    auto enA1 = cells.Get(u"A1").GetPrecedentsInCalculation();
    while (enA1.MoveNext())
    {
        ReferredArea r = enA1.GetCurrent();
        std::cout << r.ToString().ToUtf8() << std::endl;
    }

    std::cout << "A2's calculation precedents:" << std::endl;
    auto enA2 = cells.Get(u"A2").GetPrecedentsInCalculation();
    while (enA2.MoveNext())
    {
        ReferredArea r = enA2.GetCurrent();
        std::cout << r.ToString().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```