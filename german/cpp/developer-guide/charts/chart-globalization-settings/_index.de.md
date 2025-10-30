---
title: Verwendung der ChartGlobalizationSettings Klasse zur Einstellung verschiedener Sprachen für Diagrammelemente mit C++
linktitle: Verwendung der ChartGlobalizationSettings Klasse
description: Lernen Sie, wie man die ChartGlobalizationSettings Klasse in Aspose.Cells for C++ nutzt, um verschiedene Sprachen für Diagrammkomponenten einzustellen. Unser Leitfaden hilft Ihnen zu verstehen, wie man Diagrammelemente, Beschriftungen und Legenden in verschiedene Sprachen lokalisiert, sodass Sie Ihre Daten kulturell angemessen präsentieren können.
keywords: Aspose.Cells for C++, Diagramm, Chart Globalisierung, Sprachen, Lokalisierung, ChartGlobalizationSettings, Elemente, Beschriftungen, Legenden
type: docs
weight: 2200
url: /de/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Mögliche Verwendungsszenarien**

Aspose.Cells-APIs haben die Klasse [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) freigelegt, um mit Szenarien umzugehen, in denen der Benutzer die Diagrammkomponente auf eine andere Sprache einstellen möchte. Benutzerdefinierte Beschriftungen für Zwischensummen in einer Tabelle. 

## **Einführung in die ChartGlobalizationSettings-Klasse**

Die [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) Klasse bietet derzeit die folgenden 8 Methoden, die in einer benutzerdefinierten Klasse überschrieben werden können, um solche Übersetzungen wie AxisTitle Name, AxisUnit Name, ChartTitle Name und so weiter in eine andere Sprache vorzunehmen.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Gibt den Titel für die Achse zurück.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Gibt den Namen der Achseneinheit zurück.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Gibt den Titel des Diagramms zurück.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Gibt den Namen der Abnahme für die Legende zurück.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Gibt den Namen des Anstiegs für die Legende zurück.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Gibt den Namen des Gesamtwerts für die Legende zurück.
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/): Gibt den Namen der "Andere"-Beschriftungen für das Diagramm zurück.
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Gibt den Namen der Serie im Diagramm zurück.

### **Benutzerdefinierte Sprachübersetzung**
Hier erstellen wir ein Wasserfalldiagramm basierend auf den folgenden Daten. Die Namen der Diagrammkomponenten werden im Diagramm auf Englisch angezeigt. Wir verwenden ein Beispiel für die türkische Sprache, um zu zeigen, wie der Diagrammtitel, die Legenden-Abnahme/Zunahme-Namen, der Gesamtwert und der Achsentitel auf Türkisch angezeigt werden.

![todo:image_alt_text](sample.png)

## **Beispielcode**
Der folgende Beispielcode lädt die [Beispieldatei Excel](waterfall.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

class TurkeyChartGlobalizationSettings : public ChartGlobalizationSettings
{
public:
    TurkeyChartGlobalizationSettings() : ChartGlobalizationSettings() {}

    U16String GetChartTitleName() override
    {
        return u"Grafik Başlığı"; // Chart Title
    }

    U16String GetLegendIncreaseName() override
    {
        return u"Artış"; // Increase
    }

    U16String GetLegendDecreaseName() override
    {
        return u"Düşüş"; // Decrease
    }

    U16String GetLegendTotalName() override
    {
        return u"Toplam"; // Total
    }

    U16String GetAxisTitleName() override
    {
        return u"Eksen Başlığı"; // Axis Title
    }
};

void ChartGlobalizationSettingsTest()
{
    // Create an instance of existing Workbook
    U16String pathName = u"input.xlsx";
    Workbook workbook(pathName);

    // Set custom chartGlobalizationSettings, here is TurkeyChartGlobalizationSettings
    TurkeyChartGlobalizationSettings* globalizationSettings = new TurkeyChartGlobalizationSettings();
    workbook.GetSettings().GetGlobalizationSettings()->SetChartSettings(globalizationSettings);

    // Get the worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from source worksheet
    ChartCollection chartCollection = worksheet.GetCharts();
    Chart chart = chartCollection.Get(0);

    // Chart Calculate
    chart.Calculate();

    // Get the chart title
    Title title = chart.GetTitle();

    // Output the name of the Chart title
    std::cout << "\nWorkbook chart title: " << title.GetText().ToUtf8() << std::endl;

    // Get the legend labels
    Vector<U16String> legendEntriesLabels = chart.GetLegend().GetLegendLabels();

    // Output the name of the Legend
    for (int i = 0; i < legendEntriesLabels.GetLength(); i++)
    {
        std::cout << "\nWorkbook chart legend: " << legendEntriesLabels[i].ToUtf8() << std::endl;
    }

    // Output the name of the Axis title
    Title categoryAxisTitle = chart.GetCategoryAxis().GetTitle();
    std::cout << "\nWorkbook category axis title: " << categoryAxisTitle.GetText().ToUtf8() << std::endl;

    delete globalizationSettings;
}

int main()
{
    Aspose::Cells::Startup();
    ChartGlobalizationSettingsTest();
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Ausgabe, die vom Beispielcode generiert wurde

Dies ist die Konsolenausgabe des obigen Beispiels.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
