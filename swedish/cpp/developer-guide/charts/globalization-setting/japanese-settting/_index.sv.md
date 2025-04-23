---
title: Konvertera diagram till bild för japansk region med C++
linktitle: Ställ in japansk region
type: docs
weight: 10
url: /sv/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Lär dig hur du använder Aspose.Cells for C++ för att ställa in den japanska konfigurationen för diagram. Vår guide visar hur man konfigurerar diagram för att stödja japanska tecken och formateringar, inklusive teckensnitt, storlek, texts riktning och mer.
keywords: Aspose.Cells for C++, diagram, japansk konfiguration, teckensnitt, teckenstorlek, textriktning, stöd.
---

{{% alert color="primary" %}}

I det här ämnet kommer vi att visa dig hur du ställer in japansk region för ett diagram.

{{% /alert %}}

## **Definierar en arvs klass**

 Första steget, du måste definiera en klass `ChartJapaneseSettings` som ärver från [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
 Sedan, genom att överskrida relaterade funktioner, kan du ställa in texten på diagrammets element på ditt eget språk.
Kodexempel:
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

## **Konfigurera japanska inställningar för diagram**

I detta steg, kommer du att använda klassen `ChartJapaneseSettings` som du definierade i föregående steg.
Kodexempel:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

Sedan kan du se effekten i utdata bilden, elementen i diagrammet kommer att renderas enligt dina inställningar.

## **Slutsats**

I det här exemplet, om du inte anger japansk region för ett diagram, kan följande diagramelement renderas på standardspråket, såsom engelska.
Efter ovanstående operation kan vi få en utdata-diagrambild med japansk region.

|**Stödda element**|**Värde i detta exempel**|**Standardvärde i den engelska miljön**|
| :- | :- | :- |
|axeltitelnamn|軸タイトル|Axeltitel|
|axelenhetsnamn|百,千...|Hundratals, Tusentals...|
|diagramtitelnamn|グラフ タイトル|Diagramtitel|
|legend öka namn|ぞうか|Ökning|
|legend minskning namn|削減|Minskning|
|legend totalt namn|すべての|Totalt|
|annat namn|その他|Övrigt|
|Serienamn|シリーズ|Serie|
