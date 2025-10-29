---
title: Конвертация графика в изображение для японского региона с помощью C++
linktitle: Установить японский регион
type: docs
weight: 10
url: /ru/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Узнайте, как использовать Aspose.Cells for C++ для настройки японской конфигурации графика. Наш гид покажет, как настроить графики для поддержки японских символов и форматирования, включая шрифты, размер, направление текста и многое другое.
keywords: Aspose.Cells for C++, Графики, японская настройка, шрифт, размер шрифта, направление текста, поддержка.
---

{{% alert color="primary" %}}

В этой теме мы покажем вам, как установить японский регион для диаграммы.

{{% /alert %}}

## **Определяет класс наследования**

Первый шаг — нужно определить класс `ChartJapaneseSettings`, который наследует от [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Далее, переопределяя соответствующие функции, вы можете задавать текст элементов графика на вашем языке.
Пример кода:
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

## **Настройка японских настроек для диаграммы**

На этом шаге вы используете класс `ChartJapaneseSettings`, который определили на предыдущем шаге.
Пример кода:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

Затем вы можете увидеть эффект на выходном изображении, элементы на диаграмме будут отображаться в соответствии с вашими настройками.

## **Заключение**

В этом примере, если вы не установите японскую регион для диаграммы, следующие элементы диаграммы могут быть отображены на языке по умолчанию, таком как английский.
После вышеуказанных операций мы можем получить выходное изображение диаграммы с японским регионом.

|**Поддерживаемые элементы**|**Значение в этом примере**|**значение по умолчанию в английской среде**|
| :- | :- | :- |
|Название оси|軸タイトル|Название оси|
|Единица оси|百,千...|Сотни, тысячи...|
|Название диаграммы|グラフ タイトル|Название диаграммы|
|Название легенды увеличения|ぞうか|Увеличение|
|Название легенды уменьшения|削減|Уменьшение|
|Название общего легенды|すべての|Всего|
|Прочие название|その他|Другое|
|Название серии|シリーズ|Серии|
{{< app/cells/assistant language="cpp" >}}
