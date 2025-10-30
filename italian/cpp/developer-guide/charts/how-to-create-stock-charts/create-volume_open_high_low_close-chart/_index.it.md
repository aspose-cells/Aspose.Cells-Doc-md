---
title: Crea un grafico azioni Volume Apertura Alte Basse Chiusura (VOHLC) con C++
description: Impara come creare un grafico azioni volume apertura alte basse chiusura usando Aspose.Cells for C++. La nostra guida dimostrerà come tracciare i dati del mercato azionario, inclusi volume, apertura, massimo, minimo e chiusura, per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for C++, Grafico azioni Volume Apertura Alte Basse Chiusura, Dati di Mercato, Analisi, Visualizzazione.
type: docs
weight: 184
url: /it/cpp/create-volume-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il quarto grafico azionario che esamineremo è il grafico Volume Open High Low Close. Ancora una volta, è importante ripetere che i dati devono essere nell'ordine corretto. Se è necessario riorganizzare la tabella dei dati, fattelo prima di impostare il grafico. Questo grafico include una colonna per il volume immediatamente dopo la prima colonna (categoria), e i grafici includono un grafico a colonne sull'asse principale che mostra questo volume, mentre i prezzi sono spostati sull'asse secondario.

![todo:image_alt_text](data.png)

## **Grafico Azionario Volume-Apri-Alto-Basso-Chiusura (VHLC)**

![todo:image_alt_text](sample.png)

## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Volume-Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-Open-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeOpenHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend to be shown
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-Open-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:F9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{0xff, 79, 129, 189});

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
