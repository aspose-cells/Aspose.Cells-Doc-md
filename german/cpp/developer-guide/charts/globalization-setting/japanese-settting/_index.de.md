---
title: Diagramm in Bild für Japanische Region mit C++ konvertieren
linktitle: Japanische Region festlegen
type: docs
weight: 10
url: /de/cpp/convert-chart-to-image-for-japanese-region/
alias: [/cpp/set-japanese-configuration-for-chart/]
description: Erfahren Sie, wie Sie Aspose.Cells for C++ verwenden, um die japanische Konfiguration für das Diagramm einzustellen. Unser Leitfaden demonstriert, wie man Diagramme konfiguriert, um japanische Schriftzeichen und Formatierungen zu unterstützen, einschließlich Schriftarten, Größe, Textausrichtung und mehr.
keywords: Aspose.Cells for C++, Diagramme, Japanische Konfiguration, Schriftart, Schriftgröße, Textausrichtung, Unterstützung.
---

{{% alert color="primary" %}}

In diesem Thema zeigen wir Ihnen, wie Sie die japanische Region für ein Diagramm festlegen können.

{{% /alert %}}

## **Definiert eine Vererbungsklasse**

Erster Schritt, Sie müssen eine Klasse `ChartJapaneseSettings` definieren, die von [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) erbt. 
Anschließend können Sie durch Überschreiben der zugehörigen Funktionen den Text der Diagrammelemente in Ihrer eigenen Sprache einstellen.
Codebeispiel:
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

## **Japanische Einstellung für Diagramm konfigurieren**

In diesem Schritt verwenden Sie die Klasse `ChartJapaneseSettings`, die Sie im vorherigen Schritt definiert haben.
Codebeispiel:

```cpp
    Workbook wb("Japanese.xls");
    wb.GetSettings().GetGlobalizationSettings().SetChartSettings(new ChartJapaneseSettings());
    Chart chart0 = wb.GetWorksheets().Get(0).GetCharts().Get(0);
    chart0.ToImage("Output.png");
```

Dann können Sie den Effekt im Ausgabebild sehen, die Elemente im Diagramm werden gemäß Ihren Einstellungen gerendert.

## **Fazit**

In diesem Beispiel, wenn Sie für ein Diagramm keine japanische Region festlegen, können die folgenden Diagrammelemente in der Standardsprache gerendert werden, wie zum Beispiel Englisch.
Nach obiger Operation können wir ein Ausgabediagrammbild mit japanischer Region erhalten.

|**Unterstützte Elemente**|**Wert in diesem Beispiel**|**Standardwert in der englischen Umgebung**|
| :- | :- | :- |
|Achsentitelname|軸タイトル|Achsentitel|
|Achsenbezeichnung|百,千...|Hunderte, Tausende...|
|Diagramm-Titelname|グラフ タイトル|Diagrammtitel|
|Legende Anstiegsname|ぞうか|Erhöhen|
|Legende Abnahmename|削減|Abnehmen|
|Legende Gesamtname|すべての|Gesamt|
|Andere Bezeichnung|その他|Andere|
|Serienname|シリーズ|Serie|
{{< app/cells/assistant language="cpp" >}}
