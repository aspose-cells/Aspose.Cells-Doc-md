---
title: Gestione della Legenda dei Grafici di Excel con C++
linktitle: Legenda
description: Impara come utilizzare Aspose.Cells for C++ per sfruttare e personalizzare efficacemente le legende dei grafici in Microsoft Excel. La nostra guida completa spiega la funzionalità della legenda, come accederci e modificarla, oltre a come migliorare la visualizzazione e la comprensione dei dati con le legende.
keywords: Aspose.Cells for C++, Legende del Grafico, Microsoft Excel, Visualizzazione, Comprensione dei dati.
type: docs
weight: 50
url: /it/cpp/chart-legend/
---

## **Opzioni della Legenda**
Aspose.Cells permette anche di gestire la leggenda di un grafico in tempo reale. Con l'oggetto [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/), la legenda può essere spostata, aggiornata e formattata.

|![todo:image_alt_text](chart_legend.png)|

## **Impostazione della Legenda del Grafico**
È semplice gestire la legenda di un grafico con Aspose.Cells [Legend](https://reference.aspose.com/cells/cpp/aspose.cells.charts/legend/).

Il seguente frammento di codice mostra come gestire la leggenda:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Workbook object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(60);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B3"
    chart.GetNSeries().Add(u"A1:B3", true);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Move the legend to left
    chart.GetLegend().SetPosition(LegendPositionType::Left);

    // Set font color of the legend
    chart.GetLegend().GetFont().SetColor(Color::Blue());

    // Save the file
    workbook.Save(u"chart_legend.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Argomenti avanzati**
- [Impostare il riempimento dell'voce della legenda del grafico su nessuna utilizzando Aspose.Cells](/cells/it/cpp/set-text-of-chart-legend-entry-fill-to-none-using-aspose-cells/)
