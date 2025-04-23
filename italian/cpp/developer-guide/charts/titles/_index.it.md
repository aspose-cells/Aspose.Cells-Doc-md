---
title: Gestione dei Titoli dei Grafici di Excel con C++
linktitle: Titoli
description: Impara come usare Aspose.Cells for C++ per aggiungere e formattare titoli di grafici e assi in Microsoft Excel. La nostra guida dimostrerà come impostare diversi tipi di titoli, regolare il loro aspetto e modificare i titoli degli assi per una migliore rappresentazione dei dati e chiarezza.
keywords: Aspose.Cells for C++, Titoli del grafico, Titoli degli assi, Microsoft Excel, Rappresentazione dei dati, Aspetto.
type: docs
weight: 50
url: /it/cpp/chart-and-axis-titles/
---

{{% alert color="primary" %}}

Nei grafici di Excel, ci sono 2 tipi di titoli:
1. Titolo del Grafico 
1. Titoli degli Assi

{{% /alert %}}

## **Opzioni del Titolo**
Aspose.Cells permette anche di gestire i titoli dei grafici a runtime. Con l'oggetto [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/), puoi cambiare testo, carattere e formato di riempimento per i titoli.

|![todo:image_alt_text](chart_title.png)|

## **Impostare i Titoli dei Grafici o degli Assi**
Puoi usare Microsoft Excel per impostare i titoli di un grafico e dei suoi assi in un ambiente WYSIWYG. Aspose.Cells permette anche agli sviluppatori di impostare i titoli di un grafico e dei suoi assi a runtime. Tutti i grafici e i loro assi contengono una proprietà [Title](https://reference.aspose.com/cells/cpp/aspose.cells.charts/title/) che può essere usata per impostare i loro titoli, come mostrato nell'esempio sotto.

Il seguente frammento di codice mostra come impostare i titoli per grafici e assi.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

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

    // Setting the foreground color of the plot area
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::Blue());

    // Setting the foreground color of the chart area
    chart.GetChartArea().GetArea().SetForegroundColor(Color::Yellow());

    // Setting the foreground color of the 1st SeriesCollection area
    chart.GetNSeries().Get(0).GetArea().SetForegroundColor(Color::Red());

    // Setting the foreground color of the area of the 1st SeriesCollection point
    chart.GetNSeries().Get(0).GetPoints().Get(0).GetArea().SetForegroundColor(Color::Cyan());

    // Filling the area of the 2nd SeriesCollection with a gradient
    chart.GetNSeries().Get(1).GetArea().GetFillFormat().SetOneColorGradient(Color::Lime(), 1, GradientStyleType::Horizontal, 1);

    // Setting the title of a chart
    chart.GetTitle().SetText(u"Title");

    // Setting the font color of the chart title to blue
    chart.GetTitle().GetFont().SetColor(Color::Blue());

    // Setting the title of category axis of the chart
    chart.GetCategoryAxis().GetTitle().SetText(u"Category");

    // Setting the title of value axis of the chart
    chart.GetValueAxis().GetTitle().SetText(u"Value");

    // Saving the Excel file
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti avanzati**
- [Leggi il sottotitolo del grafico dal file ODS](/cells/it/cpp/read-chart-subtitle-from-ods-file/)
