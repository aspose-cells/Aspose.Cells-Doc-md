---
title: Convert Chart to Image for Japanese Region with C++
linktitle: Set Japanese Region
type: docs
weight: 10
url: /cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Learn how to use Aspose.Cells for C++ to set the Japanese configuration for the chart. Our guide will demonstrate how to configure charts to support Japanese characters and formatting, including fonts, size, text direction, and more.
keywords: Aspose.Cells for C++, Charts, Japanese configuration, font, font size, text direction, support.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

In this topic, we will show you how to set Japanese Region for a chart.

{{% /alert %}}

## **Defines an inheritance class**

First step, you need to define a class `ChartJapaneseSettings` that inherits from [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Then, by overriding the related functions, you can set the text of the chart elements in your own language.
Code example:
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

## **Config Japanese Setting For Chart**

In this step, you will use the class `ChartJapaneseSettings` you defined in the previous step.
Code example:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

Then you can see the effect in the output image, the elements in the chart will be rendered according to your settings.

## **Conclusion**

In this example, if you do not set Japanese Region for a chart, the following chart elements may be rendered in the default language, such as English.
After the above operation, we can get an output chart picture with Japanese Region.

|**Supported elements**|**Value in this example**|**default value in the English environment**|
| :- | :- | :- |
|Axis Title Name|軸タイトル|Axis Title|
|Axis Unit Name|百,千...|Hundreds, Thousands...|
|Chart Title Name|グラフ タイトル|Chart Title|
|Legend Increase Name|ぞうか|Increase|
|Legend Decrease Name|削減|Decrease|
|Legend Total Name|すべての|Total|
|Other Name|その他|Other|
|Series Name|シリーズ|Series|
{{< app/cells/assistant language="cpp" >}}
