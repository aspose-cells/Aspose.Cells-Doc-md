---
title: تنفيذ الأخطاء والقيم المنطقية باللغة الروسية أو أي لغة أخرى باستخدام C++
linktitle: تنفيذ الأخطاء والقيم المنطقية
type: docs
weight: 40
url: /ar/cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: تعلم كيفية تنفيذ الأخطاء والقيم المنطقية باللغة الروسية أو أي لغة أخرى باستخدام Aspose.Cells مع C++.
---

## **سيناريوهات الاستخدام المحتملة**

إذا كنت تستخدم Microsoft Excel باللغة الروسية أو في إعدادات لغة أو منطقة أخرى، فسيعرض أخطاء وقيم بوليانية وفقًا لتلك الإعدادات أو اللغة. يمكنك تحقيق سلوك مشابه باستخدام Aspose.Cells عبر خاصية [**Workbook.GetGlobalizationSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getglobalizationsettings/). سيتعين عليك تجاوز الطرق التالية لفئة [**GlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/).

- [**GlobalizationSettings.GetErrorValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/geterrorvaluestring/)
- [**GlobalizationSettings.GetBooleanValueString()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getbooleanvaluestring/)

## **تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى**

الشيفرة النموذجية التالية توضح كيفية تنفيذ الأخطاء والقيمة البوليانية باللغة الروسية أو أي لغة أخرى. يرجى التحقق من [ملف الإكسل النموذجي](73990159.xlsx) المستخدم في هذا الشيفرة و [PDF الناتج](73990160.pdf) الخاص به. تُظهر اللقطة الفوتوغرافية الفرق بين ملف الإكسل النموذجي والملف الناتج بصيغة PDF للرجوع إليها.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class RussianGlobalization : public GlobalizationSettings
{
public:
    virtual U16String GetErrorValueString(const U16String& err) override
    {
        if (err == u"#NAME?")
        {
            return u"#RussianName-имя?";
        }
        return u"RussianError-ошибка";
    }

    virtual U16String GetBooleanValueString(bool bv) override
    {
        return bv ? u"RussianTrue-правда" : u"RussianFalse-ложный";
    }
};

class ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage
{
public:
    static void Run()
    {
        Aspose::Cells::Startup();

        Workbook wb(u"sampleRussianGlobalization.xlsx");

        auto russianGlobalization = std::make_shared<RussianGlobalization>();
        wb.GetSettings().SetGlobalizationSettings(russianGlobalization.get());

        wb.CalculateFormula();

        wb.Save(u"outputRussianGlobalization.pdf");

        Aspose::Cells::Cleanup();
    }
};

int main()
{
    ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage::Run();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
