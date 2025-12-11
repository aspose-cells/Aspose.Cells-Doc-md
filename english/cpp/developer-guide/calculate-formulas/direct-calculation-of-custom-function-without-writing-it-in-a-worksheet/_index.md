---
title: Direct Calculation of Custom Function without Writing it in a Worksheet with C++
linktitle: Direct Calculation of Custom Function
description: This article introduces how to use Aspose.Cells library to directly calculate custom functions in Microsoft Excel without writing the function in a worksheet. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to calculate the custom function and get the result. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, custom functions, direct calculations, no need to write, worksheets
type: docs
weight: 90
url: /cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Direct Calculation of Custom Function without Writing it in a Worksheet**

This topic explains how you can directly calculate your custom functions without first writing them in a worksheet. Please use the [**Worksheet::CalculateFormula(System::String formula, CalculationOptions opts)**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) method for this purpose.

Please see the following sample code that illustrates the usage of this method. We have used a custom function named `MyCompany::CustomFunction()` and we calculate its value as **“Aspose.Cells.”** ourselves; this value is then automatically concatenated with the value of cell A1, which is **“Welcome to ”**, by the calculation engine. The final calculated value is **“Welcome to Aspose.Cells.”** As you can see in the code, we have not written our custom function anywhere in a worksheet, and it is calculated directly by our own custom logic.

### **Programming Sample**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class ICustomEngine : public AbstractCalculationEngine
{
public:
    void Calculate(CalculationData& data) override
    {
        // Check the formula name and calculate it yourself
        if (data.GetFunctionName() == u"MyCompany.CustomFunction")
        {
            // This is our calculated value
            data.SetCalculatedValue(Aspose::Cells::Object(u"Aspose.Cells."));
        }
    }
};

class ImplementDirectCalculationOfCustomFunction
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        // Create a workbook
        Workbook wb;

        // Access first worksheet
        Worksheet ws = wb.GetWorksheets().Get(0);

        // Add some text in cell A1
        ws.GetCells().Get(u"A1").PutValue(u"Welcome to ");

        // Create calculation options with custom engine
        CalculationOptions opts;
        opts.SetCustomEngine(new ICustomEngine());

        // This line shows how you can call your own custom function without
        // needing to write it in any worksheet cell
        // After the execution of this line, it will return
        // Welcome to Aspose.Cells.
        Aspose::Cells::Object ret = ws.CalculateFormula(u"=A1 & MyCompany.CustomFunction()", opts);

        // Print the calculated value to the console
        std::cout << "Calculated Value: " << ret.ToString().ToUtf8() << std::endl;

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementDirectCalculationOfCustomFunction::Run();
    return 0;
}
```

### **Console Output**

Below is the console output of the above sample code.

{{< highlight cpp >}}

Calculated Value: Welcome to Aspose.Cells.

{{< /highlight >}}

### **Related Article**

{{% alert color="primary" %}}

[Implement Custom Calculation Engine to extend the Default Calculation Engine of Aspose.Cells](/cells/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="cpp" >}}
