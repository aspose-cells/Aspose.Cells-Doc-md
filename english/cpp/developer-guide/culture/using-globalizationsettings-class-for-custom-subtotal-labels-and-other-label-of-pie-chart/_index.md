---
title: Using GlobalizationSettings Class for Custom Subtotal Labels and the “Other” Label of a Pie Chart with C++
linktitle: Using GlobalizationSettings Class
type: docs
weight: 70
url: /cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Learn how to use the GlobalizationSettings class in Aspose.Cells for C++ to customize subtotal labels and modify the “Other” label in pie charts.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Aspose.Cells APIs have exposed the [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) class in order to deal with scenarios where the user wishes to use custom labels for subtotals in a spreadsheet. Moreover, the [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) class can also be used to modify the **Other** label for a pie chart while rendering a worksheet or chart.

## **Introduction to GlobalizationSettings Class**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) class currently offers the following three methods, which can be overridden in a custom class to obtain desired labels for the subtotals or to render custom text for the **Other** label of a pie chart.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/): Gets the total name.
2. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/): Gets the grand total name.

### **Custom Labels for Subtotals**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) class can be used to customize subtotal labels by overriding the [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/) methods, as demonstrated below.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomSettings : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        switch (functionType)
        {
            case ConsolidationFunction::Average:
                return u"AVG";
            default:
                return GlobalizationSettings::GetTotalName(functionType);
        }
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        switch (functionType)
        {
            case ConsolidationFunction::Average:
                return u"GRD AVG";
            default:
                return GlobalizationSettings::GetGrandTotalName(functionType);
        }
    }
};
```

In order to inject custom labels, you must assign the `WorkbookSettings.GetGlobalizationSettings()` property to an instance of the **CustomSettings** class defined above before adding the subtotals to the worksheet.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomSettings : public GlobalizationSettings
{
public:
    CustomSettings() {}
    ~CustomSettings() {}

    // Override necessary methods from GlobalizationSettings
    // Example: Override GetTotalName if needed
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        // Custom implementation if needed
        return GlobalizationSettings::GetTotalName(functionType);
    }
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Loads an existing spreadsheet containing some data
    Workbook book(inputFilePath);

    // Assigns the GlobalizationSettings property of the WorkbookSettings class to the class created in the first step
    CustomSettings customSettings;
    book.GetSettings().SetGlobalizationSettings(&customSettings);

    // Accesses the first worksheet from the collection, which contains data residing in the cell range A2:B9
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Adds a subtotal of type Average to the worksheet
    CellArea cellArea = CellArea::CreateCellArea(u"A2", u"B9");
    sheet.GetCells().Subtotal(cellArea, 0, ConsolidationFunction::Average, {1});

    // Calculates formulas
    book.CalculateFormula();

    // Auto-fits all columns
    sheet.AutoFitColumns();

    // Saves the workbook on disk
    book.Save(outputFilePath);

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

The [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) class only works for adding new subtotals. If a spreadsheet already contains subtotals, their labels cannot be modified.

{{% /alert %}}

### **Custom Text for the “Other” Label of a Pie Chart**

```c++
#include "Aspose.Cells.h"
#include <locale>
#include <codecvt>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

// Defines a custom class that inherits from ChartGlobalizationSettings
class GlobalCustomSettings : public ChartGlobalizationSettings
{
public:
    // Overrides the GetOtherName method
    virtual U16String GetOtherName() override
    {
        // Gets the culture identifier for the current system
        std::locale loc("");
        std::wstring_convert<std::codecvt_utf8<wchar_t>> conv;
        std::string locName = loc.name();
        std::wstring wlocName = conv.from_bytes(locName);

        if (wlocName.find(L"en_US") != std::wstring::npos)
        {
            return U16String(u"Other");
        }
        else if (wlocName.find(L"fr_FR") != std::wstring::npos)
        {
            return U16String(u"Autre");
        }
        else if (wlocName.find(L"de_DE") != std::wstring::npos)
        {
            return U16String(u"Andere");
        }
        else
        {
            return ChartGlobalizationSettings::GetOtherName();
        }
    }
};
```

The following snippet loads an existing spreadsheet containing a pie chart and renders the chart to an image while utilizing the **GlobalCustomSettings** class created above.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalCustomSettings : public Aspose::Cells::Charts::ChartGlobalizationSettings
{
    // Implement custom settings if needed
};

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook book(srcDir + u"sample.xlsx");

    auto settings = book.GetSettings();
    GlobalizationSettings* globalSettings = new GlobalizationSettings();
    globalSettings.SetChartSettings(new GlobalCustomSettings());
    settings.SetGlobalizationSettings(globalSettings);

    Worksheet sheet = book.GetWorksheets().Get(0);
    Chart chart = sheet.GetCharts().Get(0);
    chart.Calculate();

    ImageOrPrintOptions options;
    chart.ToImage(srcDir + u"output_out.png", options);

    std::cout << "Chart rendered successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
