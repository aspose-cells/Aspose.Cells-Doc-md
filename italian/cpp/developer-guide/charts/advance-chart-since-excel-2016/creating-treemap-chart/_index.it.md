---
title: Come creare un grafico TreeMap con C++
description: Impara come creare un grafico Treemap in Aspose.Cells for C++. La nostra guida ti aiuterà a capire le varie proprietà e opzioni di formattazione disponibili per i grafici Treemap, incluse colori, etichette e rappresentazione dei dati.
keywords: Aspose.Cells for C++, grafico Treemap, crea, proprietà, formattazione, colori, etichette, rappresentazione dei dati, grafico circolare, grafico gerarchico.
type: docs
weight: 161
url: /it/cpp/creating-treemap-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico a mappa a riquadri fornisce una visualizzazione gerarchica dei tuoi dati e rende facile individuare modelli, ad esempio quali articoli sono i più venduti in un negozio. I rami dell'albero sono rappresentati da rettangoli e ogni sotto-ramo è mostrato come un rettangolo più piccolo. Il grafico a mappa a riquadri visualizza le categorie per colore e prossimità e può facilmente mostrare molti dati che sarebbero difficili da visualizzare con altri tipi di grafico.

![todo:image_alt_text](sample.png)
## **Grafico TreeMap**
Dopo aver eseguito il codice qui sotto, vedrai il grafico TreeMap come mostrato di seguito.

![todo:image_alt_text](result.png)
## **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](treemap.xlsx) e genera il [file Excel di output](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"treemap.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Treemap, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"TreeMap Chart");

    // Add series data range (D2:F13, actually)
    chart.GetNSeries().Add(u"D2:F13", true);

    // Set category data (A2:C13 is incorrect)
    chart.GetNSeries().SetCategoryData(u"A2:C13");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```
