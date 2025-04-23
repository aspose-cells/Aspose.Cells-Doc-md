---
title: Asse Primario e Secondario con C++
linktitle: Asse primario e secondario
description: Impara come comprendere e lavorare con assi primari e secondari in Aspose.Cells for C++. La nostra guida ti aiuterà a capire le differenze tra assi primari e secondari, e come configurarli e usarli efficacemente nei tuoi grafici.
keywords: Aspose.Cells for C++, assi primari, assi secondari, comprensione, differenze, configurazione, utilizzo.
type: docs
weight: 190
url: /it/cpp/primary-and-second-axis/
---

## **Possibili Scenari di Utilizzo**
Quando i numeri in un grafico variano ampiamente da serie di dati a serie di dati, o quando hai tipi di dati misti (prezzo e volume), rappresenta una o più serie di dati su un asse verticale (valore) secondario. La scala dell'asse verticale secondario mostra i valori per le serie di dati associate. Un asse secondario funziona bene in un grafico che mostra una combinazione di grafici a colonne e a linee.

## **Gestire gli assi primario e secondario come Microsoft Excel**
Vedi il seguente esempio di codice che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro. 
Quindi aggiungiamo un grafico e mostriamo l'asse secondario.

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

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put the sample values used in a chart
    worksheet.GetCells().Get(u"A1").PutValue(u"Region");
    worksheet.GetCells().Get(u"A2").PutValue(u"Peking");
    worksheet.GetCells().Get(u"A3").PutValue(u"New York");
    worksheet.GetCells().Get(u"A4").PutValue(u"Paris");
    worksheet.GetCells().Get(u"B1").PutValue(u"Sales Volume");
    worksheet.GetCells().Get(u"C1").PutValue(u"Growth Rate");
    worksheet.GetCells().Get(u"B2").PutValue(100);
    worksheet.GetCells().Get(u"B3").PutValue(80);
    worksheet.GetCells().Get(u"B4").PutValue(140);
    worksheet.GetCells().Get(u"C2").PutValue(0.7);
    worksheet.GetCells().Get(u"C3").PutValue(0.8);
    worksheet.GetCells().Get(u"C4").PutValue(1.0);

    // Create a Scatter chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::Scatter, 6, 6, 15, 11);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Add Series
    chart.GetNSeries().Add(u"B2:C4", true);

    // Set the category data
    chart.GetNSeries().SetCategoryData(u"=Sheet1!$A$2:$A$4");

    // Set the Second-Axis
    chart.GetNSeries().Get(1).SetPlotOnSecondAxis(true);

    // Show the Second-Axis
    chart.GetSecondValueAxis().SetIsVisible(true);

    // Set the second series ChartType to line
    chart.GetNSeries().Get(1).SetType(ChartType::Line);

    // Set the series name
    chart.GetNSeries().Get(0).SetName(u"Sales Volume");
    chart.GetNSeries().Get(1).SetName(u"Growth Rate");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Fill the PlotArea area with nothing
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the file
    workbook.Save(u"PrimaryandSecondaryAxis.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
