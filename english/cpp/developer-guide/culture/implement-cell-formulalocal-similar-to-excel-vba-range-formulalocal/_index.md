---
title: Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal with C++
linktitle: Implement Cell.FormulaLocal
type: docs
weight: 30
url: /cpp/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/
description: Learn how to implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Microsoft Excel Formulas may have different names in different locales or regions or languages. For example, **SUM** function is called **SUMME** in German. Aspose.Cells cannot work with non-English function names. In Microsoft Excel VBA, there is **Range.FormulaLocal** property that returns the name of the function as per its language or region. Aspose.Cells also provides [**Cell.FormulaLocal**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformulalocal/) property for this purpose. However, this property will only work when you will implement [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) method.

## **Implement Cell.FormulaLocal similar to Excel VBA Range.FormulaLocal**

The following sample code explains how to implement [**GlobalizationSettings.GetLocalFunctionName(string standardName)**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getlocalfunctionname/) method. The method returns the local name of the standard function. If the standard function name is **SUM**, it returns **UserFormulaLocal_SUM**. You can change the code as per your needs and return the correct local function names e.g. **SUM** is **SUMME** in German and **TEXT** is **ТЕКСТ** in Russian. Please also see the console output of the sample code given below for a reference.

## **Sample Code**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

// Implement GlobalizationSettings class
class GS : public GlobalizationSettings
{
public:
    virtual U16String GetLocalFunctionName(const U16String& standardName) override
    {
        // Change the SUM function name as per your needs.
        if (standardName == u"SUM")
        {
            return u"UserFormulaLocal_SUM";
        }

        // Change the AVERAGE function name as per your needs.
        if (standardName == u"AVERAGE")
        {
            return u"UserFormulaLocal_AVERAGE";
        }

        return u"";
    }
};

void Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal()
{
    // Create workbook
    Workbook wb;

    // Assign GlobalizationSettings implementation class
    wb.GetSettings().SetGlobalizationSettings(new GS());

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access some cell
    Cell cell = ws.GetCells().Get(u"C4");

    // Assign SUM formula and print its FormulaLocal
    cell.SetFormula(u"SUM(A1:A2)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;

    // Assign AVERAGE formula and print its FormulaLocal
    cell.SetFormula(u"=AVERAGE(B1:B2, B5)");
    std::cout << "Formula Local: " << cell.GetFormulaLocal().ToUtf8() << std::endl;
}

int main()
{
    Aspose::Cells::Startup();
    Implement_Cell_FormulaLocal_SimilarTo_Range_FormulaLocal();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Console Output**

{{< highlight java >}}

Formula Local: =UserFormulaLocal_SUM(A1:A2)

Formula Local: =UserFormulaLocal_AVERAGE(B1:B2,B5)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
