---
title: Using ICustomFunction Feature with C++
linktitle: Using ICustomFunction Feature
description: This article describes how to create a custom function in Microsoft Excel using the ICustomFunction feature in the Aspose.Cells library with C++. By loading an existing Excel file or creating a new Excel file, we can use the methods provided by Aspose.Cells to define and register custom functions and get the results. Finally, we save the modified Excel file to disk.
keywords: Aspose.Cells, Excel, ICustomFunction features, custom functions, how to calculate custom functions.
type: docs
weight: 30
url: /cpp/how-to-calculate-custom-fuctions/
---

{{% alert color="primary" %}} 

This article provides a detailed understanding of how to use the ICustomFunction feature to implement custom functions with Aspose.Cells APIs.

The ICustomFunction interface allows adding custom formula calculation functions to extend the Aspose.Cells' core calculation engine to meet certain requirements. This feature is useful to define custom (user-defined) functions in a template file or in code where the custom function can be implemented and evaluated using Aspose.Cells APIs like any other default Microsoft Excel function.

Please note, this interface has been replaced by [AbstractCalculationEngine](https://reference.aspose.com/cells/cpp/aspose.cells/abstractcalculationengine/) and will be removed in the future. Some technical articles/examples about the new API: [here](/cells/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/) and [here](/cells/cpp/returning-a-range-of-values-using-abstractcalculationengine/)

{{% /alert %}} 

## **Creating and Evaluating a User-defined Function**
This article demonstrates the implementation of the ICustomFunction interface to write a custom function and use it in the spreadsheet to get the results. We will define a custom function by name **MyFunc** which accepts 2 parameters with the following details.

- 1st parameter refers to a single cell
- 2nd parameter refers to a range of cells

The custom function will add all the values from the cell range specified as the 2nd parameter and divide the result by the value in the 1st parameter.

Here is how we have implemented the `CalculateCustomFunction` method.

```c++
#include <iostream>
#include <vector>
#include <memory>
#include <stdexcept>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class CustomFunction : public ICustomFunction
{
public:
    std::shared_ptr<Object> CalculateCustomFunction(const U16String& functionName, const std::vector<std::shared_ptr<Object>>& paramsList, const std::vector<std::shared_ptr<Object>>& contextObjects) override
    {
        double total = 0.0;
        try
        {
            // Get value of first parameter
            double firstParamB1 = std::stod(paramsList[0]->ToString());

            // Get value of second parameter
            auto secondParamC1C5 = std::dynamic_pointer_cast<std::vector<std::shared_ptr<Object>>>(paramsList[1]);

            // Get every item value of second parameter
            for (const auto& value : *secondParamC1C5)
            {
                total += std::stod(value->ToString());
            }

            total = total / firstParamB1;
        }
        catch (const std::exception&)
        {
            // Handle exceptions if necessary
        }

        // Return result of the function
        return std::make_shared<Object>(total);
    }
};
```

Here is how to use the newly defined function in a spreadsheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomFunction : public ICustomFunction
{
public:
    virtual Vector<Aspose::Cells::Object> CalculateCustomFunction(const U16String& functionName, const Vector<Vector<Aspose::Cells::Object>>& paramsList, const Vector<Aspose::Cells::Object>& contextData) override
    {
        // Implement your custom function logic here
        Vector<Aspose::Cells::Object> result;
        // Example implementation
        result.PushBack(42); // Return a sample value
        return result;
    }
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Obtain the reference of the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"B1").PutValue(5);
    worksheet.GetCells().Get(u"C1").PutValue(100);
    worksheet.GetCells().Get(u"C2").PutValue(150);
    worksheet.GetCells().Get(u"C3").PutValue(60);
    worksheet.GetCells().Get(u"C4").PutValue(32);
    worksheet.GetCells().Get(u"C5").PutValue(62);

    // Adding custom formula to Cell A1
    worksheet.GetCells().Get(u"A1").SetFormula(u"=MyFunc(B1,C1:C5)");

    // Calculating Formulas with custom function
    CustomFunction customFunction;
    workbook.CalculateFormula(false, &customFunction);

    // Assign resultant value to Cell A1
    worksheet.GetCells().Get(u"A1").PutValue(worksheet.GetCells().Get(u"A1").GetValue());

    // Save the file
    workbook.Save(outDir + u"UsingICustomFunction_out.xls");

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Overview**
The Aspose.Cells APIs just put the `ReferredArea` object into the `paramsList` when the corresponding parameter is a reference or its calculated result is a reference. If you need the reference itself, then you can use the `ReferredArea` directly. If you need to get the value of a single cell from the reference corresponding with the formula's position, you can use the `ReferredArea.GetValue(rowOffset, int colOffset)` method. If you need a cell values array for the whole area, then you can use the `ReferredArea.GetValues` method.

As the Aspose.Cells APIs give the `ReferredArea` in `paramsList`, the `ReferredAreaCollection` in `contextObjects` will not be needed anymore (in old versions, it was not able to give a one-to-one map to the parameters of the custom function always), therefore it has been removed from the `contextObjects`.

{{< highlight cpp >}}
public:
    virtual System::Object^ CalculateCustomFunction(System::String^ functionName, System::Collections::ArrayList^ paramsList, System::Collections::ArrayList^ contextObjects)
    {
        ...
        System::Object^ o = paramsList[i];
        if (dynamic_cast<ReferredArea^>(o) != nullptr) //fetch data from reference
        {
            ReferredArea^ ra = (ReferredArea^)o;
            if (ra->IsArea)
            {
                o = ra->GetValues();
            }
            else
            {
                o = ra->GetValue(0, 0);
            }
        }
        if (dynamic_cast<System::Array^>(o) != nullptr)
        {
            ...
        }
        else if...
        ...
    }
{{< /highlight >}}