---
title: Come creare un grafico Sunburst con C++
description: Impara come creare un grafico a sunburst in Aspose.Cells for C++, un grafico che presenta i dati in un cerchio. La nostra guida ti aiuterà a impostare varie proprietà e formattazioni del grafico, incluse etichette dati, legende, colori e altro.
keywords: Aspose.Cells for C++, grafico a sunburst, crea, imposta proprietà, etichette dati, leggenda, formato, colore, cerchio, rendering dei dati.
type: docs
weight: 162
url: /it/cpp/creating-sunburst-chart/
---

## **Possibili Scenari di Utilizzo**
I grafici Treemap sono utili per confrontare le proporzioni all'interno della gerarchia, tuttavia i grafici Treemap non sono ideali per mostrare i livelli gerarchici tra le categorie più grandi e ogni punto dati. Un grafico a sunburst è molto più efficace per questa visualizzazione. Il grafico a sunburst è ideale per mostrare dati gerarchici. Ogni livello della gerarchia è rappresentato da un anello o cerchio, con il cerchio più interno come la cima della gerarchia. Un grafico a sunburst senza dati gerarchici (un livello di categorie) assomiglia a un grafico a ciambella. Tuttavia, un grafico a sunburst con più livelli di categorie mostra come gli anelli esterni si relazionano con quelli interni. Il grafico a sunburst è più efficace nel mostrare come un anello si suddivide nelle sue parti contribuendo, mentre un altro tipo di grafico gerarchico, il grafico Treemap, è ideale per confrontare le dimensioni relative.

![todo:image_alt_text](sample.png)
## **Grafico sunburst**
Dopo aver eseguito il codice qui sotto, vedrai il grafico Sunburst come mostrato di seguito.

![todo:image_alt_text](result.png)
## **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](sunburst.xlsx) e genera il [file Excel di output](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sunburst.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add a Treemap chart
    int32_t pieIdx = worksheet.GetCharts().Add(ChartType::Sunburst, 5, 6, 25, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"Sunburst Chart");

    // Add series data range
    chart.GetNSeries().Add(u"D2:D16", true);

    // Set category data (A2:A16 is incorrect, as hierarchical category)
    chart.GetNSeries().SetCategoryData(u"A2:C16");

    // Show the DataLabels with category names
    chart.GetNSeries().Get(0).GetDataLabels().SetShowCategoryName(true);

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
