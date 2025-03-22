---
title: Returning a Range of Values using AbstractCalculationEngine with C++
linktitle: Returning a Range of Values using AbstractCalculationEngine
description: This article introduces an abstract calculation engine that returns a range of values in Microsoft Excel using the Aspose.Cells library with C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to get a range of values and return the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, an abstract calculation engine that returns a series of values
type: docs
weight: 55
url: /cpp/returning-a-range-of-values-using-abstractcalculationengine/
---

{{% alert color="primary" %}}

Aspose.Cells provides [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) class which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

This article will explain how to return the range of values from [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

{{% /alert %}}

The following code demonstrates the use of the [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) class and returns the range of values via its method.

Create a class with a function `CalculateCustomFunction`. This class implements [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/).

```c++
#include "Aspose.Cells.h"
#include <vector>
#include <memory>

using namespace Aspose::Cells;

class CustomFunctionStaticValue : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        // Create a 2D vector to hold the static values
        std::vector<std::vector<Object>> calculatedValue = {
            { Object(DateTime(2015, 6, 12, 10, 6, 30)), Object(2) },
            { Object(3.0), Object(U16String(u"Test")) }
        };

        // Set the calculated value in the CalculationData object
        data.SetCalculatedValue(Object(calculatedValue));
    }
};
```

Now use the above function in your program.

```c++
c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomFunctionStaticValue : public ICustomFunction
{
public:
    virtual bool CalculateCustomFunction(const U16String& name, const System::SharedPtr<System::Collections::ArrayList>& paramsList, System::SharedPtr<System::Object>& result) override
    {
        if (name == u"MYFUNC")
        {
            result = System::MakeObject<double>(0.0);
            return true;
        }
        return false;
    }
};

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook workbook;
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    Cell cell = cells.Get(0, 0);
    cell.SetArrayFormula(u"=MYFUNC()", 2, 2);

    Style style = cell.GetStyle();
    style.SetNumber(14);
    cell.SetStyle(style);

    CalculationOptions calculationOptions;
    calculationOptions.SetCustomEngine(new CustomFunctionStaticValue());
    workbook.CalculateFormula(calculationOptions);

    workbook.GetSettings().GetFormulaSettings().SetCalculationMode(CalcModeType::Manual);
    workbook.Save(outDir + u"output_out.xlsx");
    workbook.Save(outDir + u"output_out.pdf");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```