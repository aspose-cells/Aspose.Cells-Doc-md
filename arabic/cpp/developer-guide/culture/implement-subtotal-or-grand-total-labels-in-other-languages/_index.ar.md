---
title: تنفيذ عناوين الإجماليات الفرعية أو الإجمالي في لغات أخرى باستخدام C++
linktitle: تنفيذ تسميات Subtotal أو Grand Total بلغات أخرى
type: docs
weight: 50
url: /ar/cpp/implement-subtotal-or-grand-total-labels-in-other-languages/
description: تعرف على كيفية تنفيذ عناوين الإجماليات الفرعية والإجمالي في لغات غير الإنجليزية باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

أحيانًا، تريد عرض عناوين الإجمالي الفرعي والإجمالي العام بلغات غير الإنجليزية مثل الصينية واليابانية والعربية والهندية، إلخ. يتيح لك Aspose.Cells القيام بذلك باستخدام فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) وخصيصة [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). يرجى مراجعة هذا المقال حول كيفية الاستفادة من فئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/):

- [استخدام فئة GlobalizationSettings لتحديد تسميات الإجمالي الفرعي المخصصة وتسمية أخرى لمخطط القطاع](/cells/ar/cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/)

## ** تنفيذ تسميات Subtotal أو Grand Total بلغات أخرى**

يتم تحميل الكود النموذجي التالي ملف Excel كمثال ويقوم بتنفيذ أسماء الإجمالي الفرعي والإجمالي العام باللغة الصينية. يرجى مراجعة ملف Excel الناتج ([ملف الإكسل الناتج](5115152.xlsx)) الذي تم إنشاؤه بواسطة هذا الكود للمرجعية الخاصة بك. أولاً نقوم بإنشاء فئة من [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/) ثم نستخدمها في كودنا.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings
{
public:
    U16String GetTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }

    U16String GetGrandTotalName(ConsolidationFunction functionType) override
    {
        return u"Chinese Grand Total - \u53EF\u80FD\u7684\u7528\u6CD5";
    }
};
```

الآن استخدم الفئة التي أنشأت أعلاه في الكود كما يلي:

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

class GlobalizationSettingsImp : public GlobalizationSettings {
public:
    virtual U16String GetTotalName(ConsolidationFunction functionType) override {
        return u"Custom Total";
    }

    virtual U16String GetGrandTotalName(ConsolidationFunction functionType) override {
        return u"Custom Grand Total";
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb(srcDir + u"sample.xlsx");

    GlobalizationSettingsImp gsi;
    wb.GetSettings().SetGlobalizationSettings(&gsi);

    Worksheet ws = wb.GetWorksheets().Get(0);

    CellArea ca = CellArea::CreateCellArea(u"A1", u"B10");
    ws.GetCells().Subtotal(ca, 0, ConsolidationFunction::Sum, {2, 3, 4});

    ws.GetCells().SetColumnWidth(0, 40);

    wb.Save(outDir + u"output_out.xlsx");

    std::cout << "Subtotal applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
