---
title: استخدام فئة إعدادات التدويل لتخصيص عناوين الإجمالي الفرعي والعنصر "غير ذلك" في مخططات الفطيرة باستخدام C++
linktitle: استخدام فئة إعدادات التدويل
type: docs
weight: 70
url: /ar/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: تعلّم كيفية استخدام فئة إعدادات التدويل في Aspose.Cells for C++ لتخصيص عناوين الإجمالي الفرعي وتعديل عنوان "غير ذلك" في مخططات الفطيرة.
---

## **سيناريوهات الاستخدام المحتملة**

وقد طرحت واجهة برمجة تطبيقات Aspose.Cells الفئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) للتعامل مع السيناريوهات التي يرغب المستخدم في استخدام علامات مخصصة للمجاميع الجزئية في جدول بيانات. علاوة على ذلك، يمكن أيضًا استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) لتعديل العلامة **أخرى** لمخطط البيت أثناء استخراج الورقة العمل أو المخطط.

## **مقدمة في فئة GlobalizationSettings**

تقدم فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) حاليًا 3 طرق يمكن تجاوزها في فئة مخصصة للحصول على علامات مرجعية مرغوبة للمجاميع الجزئية أو لتصدير نص مخصص لعلامة **أخرى** لمخطط البيت.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/): يحصل على الاسم الكامل للوظيفة.
1. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/): يستلم اسم المجموع الكلي للوظيفة.

### **علامات مخصصة للمجاميع الجزئية**

يمكن استخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) لتخصيص علامات المجموع الجزئي عن طريق تجاوز الطرق [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/gettotalname/) و [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getgrandtotalname/) كما يظهر فيما يلي.

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

من أجل حقن علامات مخصصة، يجب تعيين خاصية [**WorkbookSettings.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/) إلى مثيل من فئة **CustomSettings** المعرفة أعلاه قبل إضافة المجاميع الجزئية إلى ورقة العمل.

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

تعمل فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) فقط لإضافة مجاميع جديدة. إذا كان جدول بيانات يحتوي بالفعل على مجاميع جزئية، فلا يمكن تعديل علاماتها.

{{% /alert %}}

### **نص مخصص لعلامة "أخرى" لمخطط البيت**

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

المقتطف التالي يحمل جدول بيانات موجود يحتوي على مخطط بيت ويعرض المخطط إلى صورة مستخدمًا فئة **CustomSettings** التي تم إنشاؤها أعلاه.

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
