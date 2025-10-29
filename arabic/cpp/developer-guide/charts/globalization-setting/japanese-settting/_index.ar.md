---
title: تحويل المخطط إلى صورة للمنطقة اليابانية باستخدام ++C
linktitle: تعيين منطقة يابانية
type: docs
weight: 10
url: /ar/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: تعلم كيفية استخدام Aspose.Cells for C++ لضبط إعدادات اللغة اليابانية للمخطط. سيُظهر دليلنا كيفية تكوين المخططات لدعم الأحرف والتنسيقات اليابانية، بما في ذلك الخطوط، الحجم، اتجاه النص، والمزيد.
keywords: Aspose.Cells for C++، المخططات، الإعدادات اليابانية، الخط، حجم الخط، اتجاه النص، الدعم.
---

{{% alert color="primary" %}}

في هذا الموضوع، سنوضح لك كيفية تعيين المنطقة اليابانية للرسم البياني.

{{% /alert %}}

## **تحديد فئة الإرث**

 الخطوة الأولى، تحتاج إلى تعريف فئة `ChartJapaneseSettings` التي ترث من [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
 ثم، من خلال تجاوز الدالات ذات الصلة، يمكنك ضبط نص عناصر المخطط بلغتك الخاصة.
مثال على الكود:
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class ChartJapaneseSetttings : public ChartGlobalizationSettings
{
public:
    ChartJapaneseSetttings() : ChartGlobalizationSettings() {}

    U16String GetAxisTitleName() override
    {
        return U16String(u"\u8EF8\u30BF\u30A4\u30C8\u30EB");
    }

    U16String GetAxisUnitName(DisplayUnitType type) override
    {
        switch (type)
        {
        case DisplayUnitType::None:
            return U16String(u"");
        case DisplayUnitType::Hundreds:
            return U16String(u"\u767E");
        case DisplayUnitType::Thousands:
            return U16String(u"\u5343");
        case DisplayUnitType::TenThousands:
            return U16String(u"\u4E07");
        case DisplayUnitType::HundredThousands:
            return U16String(u"\u0031\u0030\u4E07");
        case DisplayUnitType::Millions:
            return U16String(u"\u767E\u4E07");
        case DisplayUnitType::TenMillions:
            return U16String(u"\u5343\u4E07");
        case DisplayUnitType::HundredMillions:
            return U16String(u"\u5104");
        case DisplayUnitType::Billions:
            return U16String(u"\u0031\u0030\u5104");
        case DisplayUnitType::Trillions:
            return U16String(u"\u5146");
        default:
            return U16String(u"");
        }
    }

    U16String GetChartTitleName() override
    {
        return U16String(u"\u30B0\u30E9\u30D5\u0020\u30BF\u30A4\u30C8\u30EB");
    }

    U16String GetLegendDecreaseName() override
    {
        return U16String(u"\u524A\u6E1B");
    }

    U16String GetLegendIncreaseName() override
    {
        return U16String(u"\u305E\u3046\u304B");
    }

    U16String GetLegendTotalName() override
    {
        return U16String(u"\u3059\u3079\u3066\u306E");
    }

    U16String GetOtherName() override
    {
        return U16String(u"\u305D\u306E\u4ED6");
    }

    U16String GetSeriesName() override
    {
        return U16String(u"\u30B7\u30EA\u30FC\u30BA");
    }
};
```

## **تكوين إعدادات اللغة اليابانية للرسم البياني**

 في هذه الخطوة، ستستخدم الفئة `ChartJapaneseSettings` التي قمت بتعريفها في الخطوة السابقة.
مثال على الكود:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

ثم يمكنك رؤية التأثير في الصورة الناتجة، حيث سيتم تقديم عناصر الرسم البياني وفقًا لإعداداتك.

## **الاستنتاج**

في هذا المثال ، إذا لم تقم بتعيين المنطقة اليابانية للرسم البياني ، فقد يتم رسم عناصر الرسم البياني التالية باللغة الافتراضية ، مثل الإنجليزية.
بعد العملية أعلاه ، يمكننا الحصول على صورة رسم بياني مخرجات مع منطقة يابانية.

| ** العناصر المدعومة ** | ** القيمة في هذا المثال ** | ** القيمة الافتراضية في بيئة اللغة الإنجليزية ** |
| :- | :- | :- |
| اسم عنوان المحور | 軸タイトル | عنوان المحور |
| اسم وحدة المحور | 百,千... | مئات ، آلاف ... |
| اسم عنوان الرسم البياني | グラフ タイトル | عنوان الرسم البياني |
| اسم زيادة الوسيلة | ぞうか | زيادة |
| اسم نقصان الوسيلة | 削減 | نقص |
| اسم المجموع الأسطوري | すべての | مجموع |
| اسم آخر | その他 | آخر |
| اسم السلسلة | シリーズ | السلسلة |
{{< app/cells/assistant language="cpp" >}}
