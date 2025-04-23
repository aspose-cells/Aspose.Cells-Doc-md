---
title: Crea un grafico azioni Volume High Low Close (VHLC) con C++
linktitle: Crea Grafico Azionario Volume Alto Basso Chiusura (VHLC)
description: Impara come creare un grafico azioni volume high low close usando Aspose.Cells for C++. La nostra guida dimostrerà come tracciare i dati del mercato azionario, inclusi volume, massimo, minimo e chiusura, per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for C++, Grafico azioni Volume High Low Close, Dati di Mercato, Analisi, Visualizzazione.
type: docs
weight: 183
url: /it/cpp/create-volume-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il terzo grafico azionario che analizzeremo è il grafico Volume High Low Close. È importante ribadire che i dati devono essere nel giusto ordine. Se necessario, riorganizza la tabella dei dati prima di configurare il grafico. Questo grafico include una colonna per il volume subito dopo la prima colonna (categoria), e i grafici comprendono un grafico a colonne sull'asse principale che mostra questo volume, mentre i prezzi sono spostati sull'asse secondario.

![todo:image_alt_text](data.png)
## **Grafico Azionario Volume-Alto-Basso-Chiusura (VHLC)**

![todo:image_alt_text](sample.png)
## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Volume-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Volume-High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockVolumeHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Volume-High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);

    // Set category data 
    chart.GetNSeries().SetCategoryData(u"A2:A9");

    // Set Color for the first series (Volume) data 
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color{ 79, 129, 189 });

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

