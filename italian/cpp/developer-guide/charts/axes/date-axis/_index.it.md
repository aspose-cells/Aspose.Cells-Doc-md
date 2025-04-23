---
title: Asse delle Date con C++
linktitle: Asse data
description: Impara come gestire l asse delle date in Aspose.Cells for C++. La nostra guida ti aiuterà a capire come lavorare con vari formati di data, scale temporali e frequenze delle etichette dei tick.
keywords: Aspose.Cells for C++, asse delle date, gestire, formati di data, scale temporali, frequenze delle etichette dei tick.
type: docs
weight: 200
url: /it/cpp/date-axis/
---

## **Possibili Scenari di Utilizzo**
Quando crei un grafico dai dati del foglio di lavoro che utilizzano date, e le date sono rappresentate lungo l'asse orizzontale (categoria) nel grafico, Aspose.Cells cambia automaticamente l'asse delle categorie in un asse delle date (scala temporale).
Un asse data visualizza le date in ordine cronologico a intervalli o unità di base specifici, come il numero di giorni, mesi o anni, anche se le date sul foglio di lavoro non sono in ordine sequenziale o nelle stesse unità di base.
Per impostazione predefinita, Aspose.Cells determina le unità di base per l'asse delle date in base alla differenza più piccola tra due date nei dati del foglio di lavoro. Ad esempio, se hai dati sui prezzi delle azioni e la differenza più piccola tra le date è di sette giorni, Aspose.Cells imposta l'unità di base ai giorni, ma puoi cambiare l'unità di base in mesi o anni se vuoi vedere le prestazioni delle azioni su un periodo più lungo.

## **Gestire l'Asse Data come Microsoft Excel**
Vedi il seguente esempio di codice che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro. 
Poi aggiungiamo un grafico e impostiamo il tipo del [**Axis**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/) 
a [**TimeScale**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/categorytype/) e quindi impostiamo le unità di base su Giorni.

![todo:image_alt_text](excel.png)

## **Codice di Esempio**
```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add the sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(u"Date");

    // 14 means datetime format
    Style style = worksheet.GetCells().GetStyle();
    style.SetNumber(14);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A2").SetStyle(style);
    worksheet.GetCells().Get(u"A2").PutValue(Date{2022, 6, 26, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A3").SetStyle(style);
    worksheet.GetCells().Get(u"A3").PutValue(Date{2022, 5, 22, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"A4").SetStyle(style);
    worksheet.GetCells().Get(u"A4").PutValue(Date{2022, 8, 3, 0, 0, 0, 0});

    worksheet.GetCells().Get(u"B1").PutValue(u"Price");
    worksheet.GetCells().Get(u"B2").PutValue(40);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(60);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 9, 6, 21, 13);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Set the Axis type to Date time
    chart.GetCategoryAxis().SetCategoryType(CategoryType::TimeScale);

    // Set the base unit for CategoryAxis to days
    chart.GetCategoryAxis().SetBaseUnitScale(TimeUnit::Days);

    // Set the direction for the axis text to be vertical
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Vertical);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set max value of Y axis
    chart.GetValueAxis().SetMaxValue(70);

    // Set major unit
    chart.GetValueAxis().SetMajorUnit(10);

    // Save the file
    workbook.Save(u"DateAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
