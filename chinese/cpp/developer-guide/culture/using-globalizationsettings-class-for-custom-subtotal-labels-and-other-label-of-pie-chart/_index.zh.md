---
title: 使用 GlobalizationSettings 类进行自定义子合计标签和饼图中的其他标签（C++）
linktitle: 使用 GlobalizationSettings 类
type: docs
weight: 70
url: /zh/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: 学习如何在 Aspose.Cells for C++ 中使用 GlobalizationSettings 类自定义子合计标签和修改饼图中的“其他”标签。
---

## **可能的使用场景**

Aspose.Cells API已公开[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)类，以处理用户希望在电子表格中使用自定义标签的情形。此外，[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)类也可用于修改饼图渲染时的**其他**标签。

## **GlobalizationSettings类简介**

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)类目前提供以下3个方法，可以通过自定义类来覆盖以获得所需的小计标签，或者渲染饼图的**其他**标签的自定义文本。

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/)：获取函数的总名称。
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/)：获取函数的总计名称。

### **自定义小计标签**

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)类可通过覆盖[**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/)和[**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/)方法来自定义小计标签，如下所示。

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

为了注入自定义标签，需要将[**WorkbookSettings.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/)属性分配给上面定义的**CustomSettings**类的实例，然后将小计添加到工作表。

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"output_out.xlsx";

    // Loads an existing spreadsheet containing some data
    Workbook book(inputFilePath);

    // Assigns the GlobalizationSettings property of the WorkbookSettings class to the class created in first step
    CustomSettings customSettings;
    book.GetSettings().SetGlobalizationSettings(&customSettings);

    // Accesses the 1st worksheet from the collection which contains data resides in the cell range A2:B9
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Adds Subtotal of type Average to the worksheet
    CellArea cellArea = CellArea::CreateCellArea(u"A2", u"B9");
    sheet.GetCells().Subtotal(cellArea, 0, ConsolidationFunction::Average, {1});

    // Calculates Formulas
    book.CalculateFormula();

    // Auto fits all columns
    sheet.AutoFitColumns();

    // Saves the workbook on disc
    book.Save(outputFilePath);

    std::cout << "Workbook processed and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/)类仅适用于添加新的小计。如果电子表格已包含小计，它们的标签将无法修改。

{{% /alert %}}

### **饼状图的其他标签的自定义文本**

```c++
#include "Aspose.Cells.h"
#include <locale>
#include <codecvt>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

// Defines a custom class inherited by ChartGlobalizationSettings class
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

以下片段加载包含饼图的现有电子表格，并在利用上面创建的**CustomSettings**类的同时将图表渲染为图像。

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
    globalSettings->SetChartSettings(new GlobalCustomSettings());
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
