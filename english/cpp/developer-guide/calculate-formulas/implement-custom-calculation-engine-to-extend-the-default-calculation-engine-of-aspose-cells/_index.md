---
title: Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells with C++
linktitle: Implement Custom Calculation Engine
description: This article describes how to extend the default calculation engine by implementing a custom calculation engine using the Aspose.Cells library with C++. By loading an existing Excel file or creating a new one, we can use the methods provided by Aspose.Cells to implement a custom calculation engine and get the results. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, Custom Calculation Engine, extends the default calculation engine, C++
type: docs
weight: 80
url: /cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/
---

## **Implement Custom Calculation Engine**

Aspose.Cells has a powerful calculation engine that can calculate almost all of the Microsoft Excel formulas. Despite this, it also allows you to extend the default calculation engine which provides you greater power and flexibility.

The following property and classes are used in implementing this feature.

- [**CalculationOptions.GetCustomEngine()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getcustomengine/)
- [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/)
- [**CalculationData**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationdata/)

The following code implements the Custom Calculation Engine. It implements the interface [**AbstractCalculationEngine**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) which has a [**Calculate(CalculationData data)**](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/calculate/) method. This method is called against all of your formulas. Inside this method, we capture the **TODAY** function and add one day to the system date. So if the current date is 27/07/2023, then the custom engine will calculate TODAY() as 28/07/2023.

### **Programming Sample**

```c++
#include <iostream>
#include <cwctype>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        U16String funcName = data.GetFunctionName();
        std::u16string upperName;
        for (int i = 0; i < funcName.GetLength(); ++i)
        {
            upperName.push_back(std::towupper(funcName[i]));
        }
        if (upperName == u"TODAY")
        {
            Date today;
            double todayValue = CellsHelper::GetDoubleFromDateTime(today, false);
            data.SetCalculatedValue(todayValue + 1.0);
        }
    }

    bool GetProcessBuiltInFunctions() override { return true; }
};

class ImplementCustomCalculationEngine
{
public:
    static void Run()
    {
        Workbook workbook;
        Worksheet sheet = workbook.GetWorksheets().Get(0);
        Cell a1 = sheet.GetCells().Get(u"A1");
        Style style = a1.GetStyle();
        style.SetNumber(14);
        a1.SetStyle(style);
        a1.SetFormula(u"=TODAY()");
        workbook.CalculateFormula();
        std::cout << "The value of A1 with default calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        CustomEngine engine;
        CalculationOptions opts;
        opts.SetCustomEngine(&engine);
        workbook.CalculateFormula(opts);
        std::cout << "The value of A1 with custom calculation engine: " << a1.GetStringValue().ToUtf8() << std::endl;
        std::cout << "Press any key to continue..." << std::endl;
        std::cin.get();
    }
};

int main()
{
    Aspose::Cells::Startup();
    ImplementCustomCalculationEngine::Run();
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Result**

Please check the console output of the above sample code, the value(date time) of A1 with custom engine should be one day later than the result without custom engine.

### **Related Article**

{{% alert color="primary" %}}

[Direct calculation of custom function without writing it in a worksheet](/cells/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)

{{% /alert %}}