---
title: Gestisci i DataLabel dei grafici Excel con C++
linktitle: Etichette dei dati
type: docs
weight: 50
url: /it/cpp/insert-datalabels-to-chart/
description: Impara come gestire efficacemente le etichette dei dati nei grafici Excel usando Aspose.Cells for C++. La nostra guida completa copre vari compiti di gestione, inclusa l aggiunta, la rimozione e la modifica delle etichette per migliorare la leggibilità e l usabilità del grafico.
keywords: Aspose.Cells for C++, grafici Excel, etichette dei dati, gestione, leggibilità, usabilità, aggiunta, rimozione, modifica.
---

{{% alert color="primary" %}}

Le DataLabels sono una parte importante di un grafico. Possiamo facilmente conoscere il valore, la percentuale, ecc. di ogni serie.

{{% /alert %}}

## **Opzioni delle etichette dei dati**
Aspose.Cells consente anche di gestire le etichette dei dati del grafico in runtime con l'oggetto [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/). È semplice spostare, aggiornare e formattare le etichette dei dati del grafico.

|![todo:image_alt_text](chart_datalabels.png)|

## **Gestisci le etichette dei dati del grafico**
È semplice gestire le etichette dei dati del grafico con Aspose.Cells [DataLabels](https://reference.aspose.com/cells/cpp/aspose.cells.charts/datalabels/).

Il seguente snippet di codice dimostra come gestire le DataLabels:

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
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

    // Show value labels
    chart.GetNSeries().Get(0).GetDataLabels().SetShowValue(true);

    // Show series name labels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowSeriesName(true);

    // Move labels to center
    chart.GetNSeries().Get(1).GetDataLabels().SetPosition(LabelPositionType::Center);

    // Save the file
    workbook.Save(u"chart_datalabels.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Argomenti Avanzati**
- [Aggiunta di etichette personalizzate ai punti dati della serie del grafico](/cells/it/cpp/adding-custom-labels-to-data-points-in-the-series-of-the-chart/)
- [Disabilita il testo a capo per le etichette dei dati del grafico](/cells/it/cpp/disable-text-wrapping-for-data-labels-of-the-chart/)
- [Ridimensiona la forma dell'etichetta dati del grafico per adattarla al testo](/cells/it/cpp/resize-chart-s-data-label-shape-to-fit-text/)
- [Etichetta dati personalizzata in formato testo ricco del punto del grafico](/cells/it/cpp/rich-text-custom-data-label-of-chart-point/)
- [Imposta il tipo di forma delle etichette dati del grafico](/cells/it/cpp/set-the-shape-type-of-data-labels-of-chart/)
- [Mostra l'intervallo di celle come etichette dati](/cells/it/cpp/showing-cell-range-as-the-data-labels/)
