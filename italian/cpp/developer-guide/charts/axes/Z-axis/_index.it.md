---
title: Asse Z con C++
linktitle: Asse Z
description: Impara come lavorare con l asse Z in Aspose.Cells for C++. La nostra guida ti aiuterà a capire come configurare e personalizzare l asse Z, inclusa la scala e le etichette, per migliorare i tuoi grafici.
keywords: Aspose.Cells for C++, asse Z, creazione di grafici, configurazione, personalizzazione, scala, etichette.
type: docs
weight: 210
url: /it/cpp/z-axis/
---

## **Possibili Scenari di Utilizzo**
Per alcuni grafici 3D come grafico a colonne 3D, grafico a cono 3D o grafico a piramide 3D, che hanno un asse della profondità (serie), noto anche come asse Z, è possibile modificarlo. Puoi specificare l'intervallo tra i segni di spunta, le etichette degli assi e altre operazioni.

## **Gestire gli assi primario e secondario come Microsoft Excel**
Vedi il seguente esempio di codice che crea un nuovo file Excel e inserisce i valori del grafico nel primo foglio di lavoro. Poi aggiungiamo un grafico e impostiamo il tipo di grafico su Colonna3D, quindi puoi vedere anche l'Asse Z chiamato anche Asse Profondità. 

![todo:image_alt_text](excel.png)

## **Codice di Esempio**
```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put values to cells for creating chart
    worksheet.GetCells().Get(u"A1").PutValue(u"A");
    worksheet.GetCells().Get(u"B1").PutValue(u"B");
    worksheet.GetCells().Get(u"C1").PutValue(u"C");
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(1);
    worksheet.GetCells().Get(u"B2").PutValue(2);
    worksheet.GetCells().Get(u"B3").PutValue(3);
    worksheet.GetCells().Get(u"C2").PutValue(2);
    worksheet.GetCells().Get(u"C3").PutValue(3);

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column3D, 9, 6, 25, 16);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Calculate the chart
    chart.Calculate();

    // Add SeriesCollection (chart data source) to the chart ranging from "A2" cell to "C3"
    chart.SetChartDataRange(u"A2:C3", true);

    // Hide the CategoryAxis axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Hide the ValueAxis axis
    chart.GetValueAxis().SetIsVisible(false);

    // Save the file
    workbook.Save(u"ZAxis.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```
