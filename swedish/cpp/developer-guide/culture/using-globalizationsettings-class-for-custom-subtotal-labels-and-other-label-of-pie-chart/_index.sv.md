---
title: Använder GlobalizationSettings klass för anpassade subtotaletiketter och andra etiketter i Kördiagram med C++
linktitle: Använder GlobalizationSettings klass
type: docs
weight: 70
url: /sv/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Lär dig att använda GlobalizationSettings klassen i Aspose.Cells for C++ för att anpassa subtotaletiketter och ändra "Andra" etiketten i Kördiagram.
---

## **Möjliga användningsscenario**

Aspose.Cells API:er har exponerat [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen för att hantera scenarier där användaren vill använda anpassade etiketter för subtotals i en kalkylblad. Dessutom kan [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen också användas för att modifiera **Oavslutad**-etiketten för Pie-diagrammet medan kalkylbladet eller diagrammet renderas.

## **Introduktion till klassen GlobalizationSettings**

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen erbjuder för närvarande följande 3 metoder som kan åsidosättas i en anpassad klass för att få önskade etiketter för subtotaler eller för att rendera anpassad text för **Oavslutad**-etiketten på ett Pie-diagram.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/): Hämtar det totala namnet på funktionen.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/): Hämtar det totala namnet på den totala funktionen.

### **Anpassade etiketter för subtotaler**

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) klassen kan användas för att anpassa subtotal-etiketterna genom att åsidosätta [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/) metoderna som visas framåt.

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

För att infogna anpassade etiketter krävs det att [**WorkbookSettings.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) egenskapen tilldelas en instans av **CustomSettings** klassen som definieras ovan innan subtotalerna läggs till i kalkylbladet.

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

Klassen [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) fungerar endast för att lägga till nya delsummeringar. Om ett kalkylblad redan innehåller delsummeringar kan deras etiketter inte ändras.

{{% /alert %}}

### **Anpassad text för annan etikett för cirkeldiagram**

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

Följande avsnutt laddar ett befintligt kalkylblad som innehåller ett Pie-diagram och renderar diagrammet till en bild med hjälp av **CustomSettings**-klassen skapad ovan.

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
