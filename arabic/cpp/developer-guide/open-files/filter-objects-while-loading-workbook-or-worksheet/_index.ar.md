---
title: تصفية الكائنات أثناء تحميل دفتر العمل أو ورقة العمل باستخدام C++
linktitle: تصفية الكائنات أثناء تحميل المصنف أو ورقة العمل
type: docs
weight: 330
url: /ar/cpp/filter-objects-while-loading-workbook-or-worksheet/
description: تعلم كيفية تصفية الكائنات مثل الرسوم البيانية والأشكال والتنسيق الشرطي أثناء تحميل دفاتر العمل أو أوراق العمل باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**
 يرجى استخدام خاصية [LoadOptions.GetLoadFilter()](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getloadfilter/) أثناء تصفية البيانات من دفتر العمل. ولكن إذا كنت تريد تصفية البيانات من أوراق عمل فردية، فستحتاج إلى تجاوز طريقة [LoadFilter.StartSheet](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/startsheet/). يرجى تقديم القيمة المناسبة من تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) أثناء إنشاء أو العمل مع [LoadFilter](https://reference.aspose.com/cells/cpp/aspose.cells/loadfilter/).

 يحتوي تعداد [LoadDataFilterOptions](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/) على القيم المحتملة التالية.

- الكل
- إعدادات الكتاب
- خلية فارغة
- خلية مع تخطيط
- بيانات الخلية
- خطأ الخلية
- رقم الخليّة
- سلسلة الخليّة
- قيمة الخلية
- Chart
- تنسيق شرطي
- التحقق من البيانات
- الأسماء المعرفة
- خصائص المستند
- صيغة
- الروابط الفائقة
- منطقة مدمجة
- الجدول المحوري
- الإعدادات
- الشكل
- بيانات الورقة
- إعدادات الورقة
- البنية
- النمط
- الجدول
- VBA
- خريطة Xml

## **تصفية الكائنات أثناء تحميل دفتر العمل**
يوضح الكود المصدري التالي كيفية تصفية الرسوم البيانية من دفتر العمل. يرجى التحقق من [ملف الإكسل العيني](5115258.xlsx) المستخدم في هذا الكود و [ملف PDF الناتج](5115257.pdf) الذي تم إنشاؤه بواسطته. كما يمكنك رؤية في ملف PDF الناتج، تم تصفية جميع الرسوم البيانية من دفتر العمل.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter charts from the workbook
    LoadOptions lOptions;
    lOptions.SetLoadFilter(new LoadFilter(LoadDataFilterOptions::All & ~LoadDataFilterOptions::Chart));

    // Load the workbook with the above filter
    U16String inputFilePath = srcDir + u"sampleFilterCharts.xlsx";
    Workbook workbook(inputFilePath, lOptions);

    // Save worksheet to a single PDF page
    PdfSaveOptions pOptions;
    pOptions.SetOnePagePerSheet(true);

    // Save the workbook in PDF format
    U16String outputFilePath = outDir + u"sampleFilterCharts.pdf";
    workbook.Save(outputFilePath, pOptions);

    std::cout << "Workbook saved successfully with filtered charts!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تصفية الكائنات أثناء تحميل ورقة العمل**
يقوم الكود المصدري التالي بتحميل [ملف الإكسل الأصلي](5115255.xlsx) ويقوم بتصفية البيانات التالية من ورقات العمل باستخدام تصفية مخصصة.

- يتم تصفية الرسوم البيانية من ورقة العمل التي تحمل اسم لا توجد فيها رسوم بيانية.
- يتم تصفية الأشكال من ورقة العمل التي تحمل اسم لا توجد فيها أشكال.
- يتم تصفية التنسيق الشرطي من ورقة العمل التي تحمل اسم لا توجد فيها تنسيق شرطي.

يقوم بتحميل ملف Excel المصدر (5115255.xlsx) بتصفية مخصصة، ثم يأخذ صور جميع ورقات العمل بشكل تتابع. إليك صور الإخراج للإشارة. كما يمكنك أن ترى، الصورة الأولى ليست تحتوي على رسوم بيانية، الصورة الثانية ليست تحتوي على أشكال، والصورة الثالثة ليست تحتوي على تنسيق شرطي.

- [NoCharts.png](5115254.png)
- [NoShapes.png](5115256.png)
- [NoConditionalFormatting.png](5115251.png)

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    void StartSheet(Worksheet& sheet) override
    {
        U16String sheetName = sheet.GetName();

        if (sheetName == u"NoCharts")
        {
            // Load everything and filter charts
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Chart)));
        }

        if (sheetName == u"NoShapes")
        {
            // Load everything and filter shapes
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::Drawing)));
        }

        if (sheetName == u"NoConditionalFormatting")
        {
            // Load everything and filter conditional formatting
            SetLoadDataFilterOptions(static_cast<LoadDataFilterOptions>(static_cast<int>(LoadDataFilterOptions::All) & ~static_cast<int>(LoadDataFilterOptions::ConditionalFormatting)));
        }
    }
};

// Add main function to serve as entry point
int main() {
    Aspose::Cells::Startup();
    Aspose::Cells::Cleanup();
    return 0;

}
```

هكذا تستخدم فئة CustomLoadFilter حسب أسماء ورقة العمل.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class CustomLoadFilter : public LoadFilter
{
public:
    CustomLoadFilter() : LoadFilter(LoadDataFilterOptions::All) {}
};

int main()
{
    Aspose::Cells::Startup();

    // Source directory
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Filter worksheets using CustomLoadFilter class
    LoadOptions loadOpts;
    CustomLoadFilter customLoadFilter;
    loadOpts.SetLoadFilter(&customLoadFilter);

    // Load the workbook with filter defined in CustomLoadFilter class
    Workbook workbook(srcDir + u"sampleCustomFilteringPerWorksheet.xlsx", loadOpts);

    // Take the image of all worksheets one by one
    WorksheetCollection sheets = workbook.GetWorksheets();
    for (int i = 0; i < sheets.GetCount(); i++)
    {
        // Access worksheet at index i
        Worksheet worksheet = sheets.Get(i);

        // Create an instance of ImageOrPrintOptions
        // Render entire worksheet to image
        ImageOrPrintOptions imageOpts;
        imageOpts.SetOnePagePerSheet(true);
        imageOpts.SetImageType(Aspose::Cells::Drawing::ImageType::Png);

        // Convert worksheet to image
        SheetRender render(worksheet, imageOpts);
        render.ToImage(0, outDir + u"outputCustomFilteringPerWorksheet_" + worksheet.GetName() + u".png");
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
