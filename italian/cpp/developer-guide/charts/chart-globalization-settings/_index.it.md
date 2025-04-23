---
title: Utilizzo della classe ChartGlobalizationSettings per impostare diverse lingue per il componente grafico con C++
linktitle: Utilizzo della classe ChartGlobalizationSettings
description: Impara come usare la classe ChartGlobalizationSettings in Aspose.Cells for C++ per impostare lingue diverse per i componenti del grafico. La nostra guida ti aiuterà a capire come localizzare gli elementi del grafico, le etichette e le legende in diverse lingue, permettendoti di presentare i dati in modo culturalmente appropriato.
keywords: Aspose.Cells for C++, grafici, globalizzazione del grafico, lingue, localizzazione, ChartGlobalizationSettings, elementi, etichette, legende.
type: docs
weight: 2200
url: /it/cpp/using-chartglobalizationsettings-class-to-set-different-language-for-chart-component/
---

## **Possibili Scenari di Utilizzo**

Le API di Aspose.Cells hanno esposto la classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) per gestire gli scenari in cui l'utente desidera impostare un componente del grafico in una lingua diversa, etichette personalizzate per i subtotali in un foglio di calcolo. 

## **Introduzione alla classe ChartGlobalizationSettings**

La classe [**ChartGlobalizationSettings**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/) attualmente offre i seguenti 8 metodi che possono essere sovrascritti in una classe personalizzata per tradurre come il nome di AxisTitle, AxisUnit, ChartTitle e così via in lingue diverse.

1. [**GetAxisTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxistitlename/): Ottiene il nome del Titolo per l'Asse.
1. [**GetAxisUnitName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getaxisunitname/): Ottiene il Nome dell'Unità di Asse.
1. [**GetChartTitleName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getcharttitlename/): Ottiene il nome del Titolo del Grafico.
1. [**GetLegendDecreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegenddecreasename/): Ottiene il nome di Diminuzione per la Leggenda.
1. [**GetLegendIncreaseName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendincreasename/): Ottiene il nome di aumento per la Leggenda.
1. [**GetLegendTotalName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getlegendtotalname/): Ottiene il nome di Totale per la Leggenda.
1. [**GetOtherName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getothername/): Ottiene il nome delle etichette "Altro" per il Grafico.
1. [**GetSeriesName**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chartglobalizationsettings/getseriesname/): Ottiene il nome di Serie nel Grafico.

### **Traduzione personalizzata**
Qui, creeremo un grafico a barre basato sui seguenti dati. I nomi dei componenti del grafico verranno visualizzati in inglese nel grafico. Useremo un esempio in lingua turca per mostrare come visualizzare il Titolo del Grafico, i nomi di Aumento/Diminuzione della Leggenda, il nome Totale e il Titolo dell'Asse in turco.

![todo:image_alt_text](sample.png)

## **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](waterfall.xlsx).

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

## Output generato dal codice di esempio

Questo è l'output console del codice di esempio precedente.

{{< highlight java >}}

Workbook chart title: Grafik Başlığı

Workbook chart legend: Artış

Workbook chart legend: Düşüş

Workbook chart legend: Toplam

Workbook category axis tile: Eksen Başlığı

{{< /highlight >}}
