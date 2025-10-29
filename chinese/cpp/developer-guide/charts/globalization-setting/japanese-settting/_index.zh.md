---
title: 用C++将图表转换为图片以支持日本地区使用
linktitle: 设置日本地区
type: docs
weight: 10
url: /zh/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: 学习如何使用Aspose.Cells for C++设置图表的日本配置。我们的指南将演示如何配置图表以支持日文字符和格式，包括字体、大小、文本方向等。
keywords: Aspose.Cells for C++，制表，日本配置，字体，字体大小，文本方向，支持。
---

{{% alert color="primary" %}}

在本主题中，我们将向您展示如何为图表设置日本地区。

{{% /alert %}}

## **定义继承类**

第一步，你需要定义一个继承自[**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/)的类`ChartJapaneseSettings`。 
然后，通过重写相关函数，你可以用自己的语言设置图表元素的文本。
代码示例:
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

## **为图表配置日本设置**

在这一步，你将使用在前一步定义的`ChartJapaneseSettings`类。
代码示例:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

然后，您可以在输出图像中看到效果，图表中的元素将根据您的设置进行渲染。

## **结论**

在此示例中，如果不为图表设置日本地区，则以下图表元素可能以默认语言（如英文）呈现。
在上述操作后，我们可以获得一个具有日本区域的输出图表图片。

|**支持的元素**|**本示例中的值**|**英文环境中的默认值**|
| :- | :- | :- |
|轴标题名称|軸タイトル|Axis Title|
|轴单位名称|百,千...|Hundreds, Thousands...|
|图表标题名称|グラフ タイトル|Chart Title|
|图例增加名称|ぞうか|Increase|
|图例减少名称|削減|Decrease|
|图例总数名称|すべての|Total|
|其它名称|その他|Other|
|系列名称|シリーズ|Series|
{{< app/cells/assistant language="cpp" >}}
