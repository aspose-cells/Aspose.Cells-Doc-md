---
title: C++ ile Küreselleşme Ayarları Sınıfını kullanarak Pasta Grafiği Özelleştirme Etiketleri ve Diğer Etiketler
linktitle: Küreselleşme Ayarları Sınıfını Kullanma
type: docs
weight: 70
url: /tr/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Aspose.Cells for C++ kullanarak Subtotal etiketlerini özelleştirmek ve Pasta grafiklerinde "Diğer" etiketini değiştirmek için GlobalizationSettings sınıfını nasıl kullanacağınızı öğrenin.
---

## **Olası Kullanım Senaryoları**

Aspose.Cells API'leri, kullanıcının elektronik tabloda Özel Alt Toplam etiketleri kullanmak istediği senaryolarla başa çıkmak için [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfını açığa çıkarmıştır. Ayrıca, [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfı, çalışma sayfasını veya çizimi render ederken **Diğer** etiketi için özel metni değiştirmek için kullanılabilir.

## **GlobalizationSettings Sınıfı Tanıtımı**

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfı şu anda istenen toplam etiketleri almak için özelleştirilmiş bir sınıfta geçersiz kılınabilen aşağıdaki 3 yöntemi sunmaktadır veya bir Pasta grafiğinin **Diğer** etiketi için özel metni oluşturmak için.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/): Fonksiyonun toplam ismini alır.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/): Fonksiyonun genel toplam ismini alır.

### **Alt toplamlar için özel etiketler**

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfı, alt toplam etiketlerini özelleştirmek için önümüzdeki gibi [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/) ve [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/) yöntemlerini geçersiz kılma amacıyla kullanılabilir.

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

Özel etiketler enjekte etmek için, Alt toplamları çalışma sayfasına eklemek öncesinde yukarıda tanımlanan **CustomSettings** sınıfına bir örnek atamak gereklidir.

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

[**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) sınıfı yalnızca yeni Alt toplamları eklemek için çalışır. Bir elektronik tablo zaten Alt toplamlar içeriyorsa, etiketleri değiştirilemez.

{{% /alert %}}

### **Pasta Grafiği için Diğer Etiket için Özel Metin**

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

Aşağıdaki kesit, yukarıda oluşturulan **CustomSettings** sınıfını kullanarak bir Pasta grafiği içeren mevcut bir elektronik tabloyu yükler ve grafiği resim olarak oluşturur.

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
