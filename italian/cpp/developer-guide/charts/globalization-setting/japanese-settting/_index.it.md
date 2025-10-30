---
title: Convertire il grafico in immagine per regione giapponese con C++
linktitle: Imposta Regione Giapponese
type: docs
weight: 10
url: /it/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Impara come usare Aspose.Cells for C++ per impostare la configurazione giapponese del grafico. La nostra guida dimostrerà come configurare i grafici per supportare i caratteri e la formattazione giapponese, inclusi font, dimensioni, direzione del testo e altro.
keywords: Aspose.Cells for C++, Grafici, Configurazione giapponese, font, dimensione font, direzione del testo, supporto.
---

{{% alert color="primary" %}}

In questo argomento, ti mostreremo come impostare la Regione Giapponese per un grafico.

{{% /alert %}}

## **Definisce una classe di ereditarietà**

Prima fase, devi definire una classe `ChartJapaneseSettings` che eredita da [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/). 
Quindi, sovrascrivendo le funzioni correlate, puoi impostare il testo degli elementi del grafico nella tua lingua.
Esempio di codice:
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

## **Configura Impostazione Giapponese per Grafico**

In questa fase, utilizzerai la classe `ChartJapaneseSettings` che hai definito nel passo precedente.
Esempio di codice:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

Poi puoi vedere l'effetto nell'immagine di output, gli elementi nel grafico saranno resi in base alle tue impostazioni.

## **Conclusioni**

In questo esempio, se non si imposta la Regione Giapponese per un grafico, gli elementi del grafico seguenti potrebbero essere resi nella lingua predefinita, come l'inglese.
Dopo l'operazione sopra, possiamo ottenere un'immagine del grafico di output con la Regione Giapponese.

|**Elementi supportati**|**Valore in questo esempio**|**valore predefinito nell'ambiente inglese**|
| :- | :- | :- |
|Nome del titolo dell'asse|軸タイトル|Titolo dell'asse|
|Nome dell'unità dell'asse|百,千...|Centinaia, Migliaia...|
|Nome del titolo del grafico|グラフ タイトル|Titolo del grafico|
|Nome incremento legenda|ぞうか|Aumento|
|Nome decremento legenda|削減|Decremento|
|Nome totale legenda|すべての|Totale|
|Altro nome|その他|Altro|
|Nome serie|シリーズ|Serie|
{{< app/cells/assistant language="cpp" >}}
