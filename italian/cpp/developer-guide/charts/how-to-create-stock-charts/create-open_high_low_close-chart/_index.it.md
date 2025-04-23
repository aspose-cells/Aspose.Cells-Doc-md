---
title: Crea un grafico azioni Open High Low Close (OHLC) con C++
description: Impara come creare un grafico azioni open high low close usando Aspose.Cells for C++. La nostra guida dimostrerà come tracciare i dati del mercato azionario, inclusi i prezzi di apertura, massimo, minimo e chiusura, per una migliore analisi e visualizzazione.
keywords: Aspose.Cells for C++, Grafico azioni Open High Low Close, Dati di Mercato, Analisi, Visualizzazione.
type: docs
weight: 182
url: /it/cpp/create-open-high-low-close-stock-chart/
---

## **Possibili Scenari di Utilizzo**
Il grafico Open-High-Low-Close (OHLC) utilizza cinque colonne di dati, in ordine: categoria, apertura, alta, bassa e chiusura. L'intervallo di prezzi in ogni categoria è nuovamente indicato da una linea verticale, mentre l'intervallo tra apertura e chiusura è dato da una barra galleggiante più ampia; se il prezzo aumenta nella categoria (chiusura è superiore all'apertura), la barra è riempita con un colore, mentre se il prezzo diminuisce, la barra è riempita con un altro. Questo tipo di grafico è spesso chiamato grafico a candela.

![todo:image_alt_text](data.png)

![todo:image_alt_text](sample.png)

## **Miglioramenti della visibilità nel grafico**
Spesso usiamo colori anziché bianco e nero per indicare prezzi in aumento e diminuzione. Nel primo set di candlestick sottostante, il rosso mostra prezzi in aumento e il verde in diminuzione.

![todo:image_alt_text](sample2.png)

## **Codice di Esempio**
Il codice di esempio seguente carica il [file Excel di esempio](Open-High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"Open-High-Low-Close.xlsx");
    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Create High-Low-Close-Stock Chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::StockOpenHighLowClose, 5, 6, 20, 12);
    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);
    // Set the legend can be showed
    chart.SetShowLegend(true);
    // Set the chart title name
    chart.GetTitle().SetText(u"Open-High-Low-Close Stock");
    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);
    // Set data range
    chart.SetChartDataRange(u"A1:E9", true);
    // Set category data
    chart.GetNSeries().GetCategoryData() = u"A2:A9";
    // Set the DownBars and UpBars with different color
    chart.GetNSeries().Get(0).GetDownBars().GetArea().SetForegroundColor(Color::Green());
    chart.GetNSeries().Get(0).GetUpBars().GetArea().SetForegroundColor(Color::Red());
    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);
    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
