---
title: Gestisci gli assi dei grafici Excel con C++
description: Impara come configurare gli assi dei grafici in Aspose.Cells for C++. La nostra guida ti mostrerà come regolare gli assi primari e secondari, impostare i loro intervalli e modificare le loro proprietà per migliorare i tuoi grafici.
keywords: Aspose.Cells for C++, assi del grafico, configurazione, assi primari, assi secondari, intervallo, proprietà.
linktitle: Assi
type: docs
weight: 50
url: /it/cpp/chart-axes/
---

{{% alert color="primary" %}}

Nei grafici Excel, ci sono 3 tipi di assi:
1. Asse Orizzontale (Categoria): Asse X
1. Asse Verticale (Valore): Asse Y
1. Asse di Profondità (Serie): Asse Z

{{% /alert %}}

## **Opzioni dell'asse**
Aspose.Cells consente anche di gestire gli assi del grafico in fase di esecuzione. Con l’oggetto [Axis](https://reference.aspose.com/cells/cpp/aspose.cells.charts/axis/), puoi modificare tutte le opzioni dell’Asse come fatto in Excel.

|![todo:image_alt_text](chart_axes.png)|

## **Gestisci gli assi X e Y**

Nei grafici di Excel, gli assi orizzontali e verticali sono i due assi più popolari da usare.

Il seguente esempio di codice dimostra come impostare le opzioni degli assi X e Y.

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
    worksheet.GetCells().Get(u"A1").PutValue(u"Series1");
    worksheet.GetCells().Get(u"A2").PutValue(50);
    worksheet.GetCells().Get(u"A3").PutValue(100);
    worksheet.GetCells().Get(u"A4").PutValue(150);
    worksheet.GetCells().Get(u"B1").PutValue(u"Series2");
    worksheet.GetCells().Get(u"B2").PutValue(60);
    worksheet.GetCells().Get(u"B3").PutValue(32);
    worksheet.GetCells().Get(u"B4").PutValue(50);

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.SetChartDataRange(u"A1:B4", true);

    // Hiding X axis
    chart.GetCategoryAxis().SetIsVisible(false);

    // Setting max value of Y axis
    chart.GetValueAxis().SetMaxValue(200);

    // Setting major unit
    chart.GetValueAxis().SetMajorUnit(50);

    // Save the file
    workbook.Save(u"chart_axes.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Argomenti Avanzati**
- [Cambia la direzione delle etichette di graduazione](/cells/it/cpp/change-tick-label-direction/)
- [Determina quali assi esistono nel grafico.](/cells/it/cpp/determine-which-axis-exists-in-the-chart/)
- [Gestire le unità automatiche dell'asse del grafico come Microsoft Excel](/cells/it/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/)
- [Leggere le etichette dell'asse dopo il calcolo del grafico](/cells/it/cpp/read-axis-labels-after-calculating-the-chart/)
- [Come impostare l'asse delle categorie nel grafico Excel](/cells/it/cpp/how-to-set-category-axis/)
