---
title: Imposta la fonte dei dati per il grafico con C++
linktitle: Origine dati
type: docs
weight: 10
url: /it/cpp/data-formatting-in-charts/
description: Impara sui vari tipi di fonti di dati supportate da Aspose.Cells for C++. La nostra guida ti illustrerà i diversi tipi di fonti di dati disponibili e ti mostrerà come connetterti e recuperare dati da esse per compilare i tuoi fogli di lavoro.
keywords: Aspose.Cells for C++, grafici, formattazione dati, etichette, colori, caratteri, aspetto, usabilità.
---

Nei nostri argomenti precedenti, abbiamo già fornito molti esempi per dimostrare come puoi impostare una fonte di dati per il tuo grafico. In questo argomento, forniremo ulteriori dettagli sui tipi di dati che possono essere impostati per un grafico.

## **Impostazione dei dati del grafico**

Ci sono due tipi di dati con cui lavorare mentre si lavora sui grafici utilizzando Aspose.Cells come segue:

- Dati del grafico.
- Dati di categoria.

### **Dati del grafico**

I dati del grafico sono i dati che utilizziamo come origine dati per costruire i nostri grafici. Possiamo aggiungere un intervallo delle celle (contenenti dati del grafico) chiamando il metodo [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/add/) dell'oggetto [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiating a Workbook object
    Workbook workbook;

    // Adding a new worksheet to the Excel object
    int sheetIndex = workbook.GetWorksheets().Add();

    // Obtaining the reference of the newly added worksheet by passing its sheet index
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Adding sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(50);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(300);
    worksheet.GetCells().Get(u"B1").PutValue(160);
    worksheet.GetCells().Get(u"B2").PutValue(32);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Adding sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Adding a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Accessing the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Adding SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Saving the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Dati di categoria**

I dati di categoria vengono utilizzati per l'etichettatura dei dati del grafico e possono essere aggiunti a [**SeriesCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/) utilizzando la sua proprietà [**GetCategoryData()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/seriescollection/getcategorydata/). Di seguito viene fornito un esempio completo per dimostrare l'uso dei dati del grafico e di categoria. Dopo l'esecuzione del codice di esempio sopra, verrà aggiunto un grafico a colonne al foglio di lavoro come mostrato di seguito.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add sample values to cells
    worksheet.GetCells().Get(u"A1").PutValue(10);
    worksheet.GetCells().Get(u"A2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(170);
    worksheet.GetCells().Get(u"A4").PutValue(200);
    worksheet.GetCells().Get(u"B1").PutValue(120);
    worksheet.GetCells().Get(u"B2").PutValue(320);
    worksheet.GetCells().Get(u"B3").PutValue(50);
    worksheet.GetCells().Get(u"B4").PutValue(40);

    // Add sample values to cells as category data
    worksheet.GetCells().Get(u"C1").PutValue(u"Q1");
    worksheet.GetCells().Get(u"C2").PutValue(u"Q2");
    worksheet.GetCells().Get(u"C3").PutValue(u"Y1");
    worksheet.GetCells().Get(u"C4").PutValue(u"Y2");

    // Add a chart to the worksheet
    int chartIndex = worksheet.GetCharts().Add(ChartType::Column, 5, 0, 15, 5);

    // Access the instance of the newly added chart
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Add SeriesCollection (chart data source) to the chart ranging from "A1" cell to "B4"
    chart.GetNSeries().Add(u"A1:B4", true);

    // Set the data source for the category data of SeriesCollection
    chart.GetNSeries().SetCategoryData(u"C1:C4");

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Chart added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Argomenti Avanzati**
- [Modifica dell'origine dei dati del grafico al foglio di lavoro di destinazione durante la copia delle righe o dell'intervallo](/cells/it/cpp/change-data-source-of-the-chart-to-destination-worksheet-while-copying-rows-or-range/)
- [Creazione di grafici dinamici](/cells/it/cpp/create-dynamic-charts/)
- [Modo semplice per l'impostazione del grafico utilizzando il metodo Chart.SetChartDataRange](/cells/it/cpp/easy-way-for-chart-setup-using-chart-setchartdatarange-method/)
- [Trova il tipo di valori X e Y dei punti nella serie del grafico](/cells/it/cpp/find-type-of-x-and-y-values-of-points-in-chart-series/)
