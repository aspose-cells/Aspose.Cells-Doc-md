---
title: Tre metodi per filtrare i dati del grafico con C++
linktitle: Tre metodi per filtrare i dati del grafico
description: Impara come filtrare i grafici in Excel usando API Aspose.Cells for C++. La nostra guida completa dimostrerà come applicare filtri ai grafici, personalizzare gli elementi del grafico e usare strumenti di analisi dei dati per migliori insights e decisioni informate.
keywords: Aspose.Cells for C++, Filtrare i grafici in Excel, Analisi dei dati, Decisioni, Visualizzazione.
type: docs
weight: 2210
url: /it/cpp/filtering-charts-in-excel/
---

{{% alert color="primary" %}}

## **1. Filtrare le serie per visualizzare un grafico**

### **Passaggi per filtrare le serie da un grafico in Excel**
In Excel, possiamo filtrare specifiche serie da un grafico, facendo sì che quelle serie filtrate non siano visualizzate nel grafico. Il grafico originale è mostrato in **Figura 1**. Tuttavia, quando filtriamo **Testseries2** e **Testseries4**, il grafico apparirà come mostrato in **Figura 2**.

 In Aspose.Cells, possiamo eseguire operazioni simili. Per un file [esempio](seriesFiltered.xlsx) come questo, se vogliamo filtrare **Testseries2** e **Testseries4**, possiamo eseguire il seguente codice. Inoltre, manterremo due liste: una ([GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/)) per memorizzare tutte le serie selezionate e un'altra ([GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/)) per memorizzare le serie filtrate.

<b>Nota</b> che nel codice, quando impostiamo **chart->GetNSeries()->Get(0)->SetIsFiltered(true);**, la prima serie in [GetNSeries()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getnseries/) verrà rimossa e posizionata nel posto appropriato all'interno di [GetFilteredNSeries](https://reference.aspose.com/cells/cpp/aspose.cells.charts/chart/getfilterednseries/). Successivamente, il precedente **NSeries[1]** diventerà il nuovo primo elemento della lista, e tutte le serie seguenti si sposteranno avanti di una posizione. Questo significa che se poi eseguiamo **chart->GetNSeries()->Get(1)->SetIsFiltered(true);**, rimuoviamo effettivamente la terza serie originale. Questo può causare confusione, quindi si consiglia di seguire l'operazione nel codice, che elimina le serie dall'ultimo al primo.

![todo:image_alt_text](Figure1.png)

![todo:image_alt_text](Figure2.png)

### **Codice di Esempio**
Il seguente codice di esempio carica il [file Excel di esempio](seriesFiltered.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of existing Workbook
    Workbook workbook(u"seriesFiltered.xlsx");

    // Get filtered series list
    SeriesCollection nSeriesFiltered = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetFilteredNSeries();

    // Get selected series list
    SeriesCollection nSeries = workbook.GetWorksheets().Get(0).GetCharts().Get(u"Chart 1").GetNSeries();

    // Should be 0
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 6
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Process from the end to the beginning
    nSeries.Get(1).SetIsFiltered(true);
    nSeries.Get(0).SetIsFiltered(true);

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    // Save the workbook
    workbook.Save(u"seriesFiltered-out.xlsx");

    // Reload the workbook
    workbook = Workbook(u"seriesFiltered-out.xlsx");

    // Should be 2
    std::cout << "Filtered Series count: " << nSeriesFiltered.GetCount() << std::endl;

    // Should be 4
    std::cout << "Visible Series count: " << nSeries.GetCount() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **2. Filtrare i dati e far cambiare il grafico**

Filtrare i propri dati è un ottimo modo per gestire i filtri del grafico con molti dati. Quando filtri i dati, il grafico cambierà. Un problema che dovremo affrontare è assicurarsi che il grafico rimanga visibile a schermo. Quando si applicano filtri, vengono nastrate righe e occasionalmente il grafico sarà in quelle righe nascoste.

![todo:image_alt_text](Figure3.png)

### **Passaggi per utilizzare i filtri dei dati per modificare il grafico in Excel**

1. Fare clic all'interno del proprio intervallo di dati.
2. Fare clic sulla scheda **Dati**, e attivare i filtri cliccando su Filtri. La riga di intestazione avrà frecce a discesa.
3. Creare un grafico andando alla scheda **Inserisci** e selezionando un grafico a colonne.
4. Ora filtra i tuoi dati utilizzando le frecce a discesa nei dati. Non utilizzare i filtri del grafico.

### **Codice di Esempio**
Il seguente esempio di codice mostra la stessa funzione usando Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;

int main() {
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook;

    // Get the First sheet.
    Worksheet sheet = workbook.GetWorksheets().Get(u"Sheet1");

    // Add data into details cells.
    sheet.GetCells().Get(0, 0).PutValue(u"Fruits Name");
    sheet.GetCells().Get(0, 1).PutValue(u"Fruits Price");
    sheet.GetCells().Get(1, 0).PutValue(u"Apples");
    sheet.GetCells().Get(2, 0).PutValue(u"Bananas");
    sheet.GetCells().Get(3, 0).PutValue(u"Grapes");
    sheet.GetCells().Get(4, 0).PutValue(u"Oranges");
    sheet.GetCells().Get(1, 1).PutValue(5);
    sheet.GetCells().Get(2, 1).PutValue(2);
    sheet.GetCells().Get(3, 1).PutValue(1);
    sheet.GetCells().Get(4, 1).PutValue(4);

    // Add a chart to the worksheet
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);

    // Access the instance of the newly added chart
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B5", true);

    // Set AutoFilter range
    sheet.GetAutoFilter().SetRange(u"A1:B5");

    // Add filters for a filter column.
    sheet.GetAutoFilter().AddFilter(0, u"Bananas");
    sheet.GetAutoFilter().AddFilter(0, u"Oranges");

    // Apply the filters
    sheet.GetAutoFilter().Refresh();

    // Save the chart as an image
    chart.ToImage(u"Autofilter.png");

    // Save the workbook
    workbook.Save(u"Autofilter.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **3. Filtra i dati utilizzando una Tabella e fai cambiare il grafico**

Utilizzare una Tabella è simile al Metodo 2, utilizzando un intervallo, ma hai vantaggi con le tabelle rispetto agli intervalli. Quando cambia il tuo intervallo in una Tabella e aggiungi dati, il grafico si aggiorna automaticamente. Con un intervallo, dovrai modificare la fonte dati.

### **Formatta come tabella in Excel**

Fare clic all'interno dei dati e utilizzare **CTRL + T** oppure utilizzare la scheda Home, **Formatta come Tabella**

![todo:image_alt_text](Figure4.png)

### **Codice di Esempio**
Il seguente esempio di codice carica il [file di esempio Excel](TableFilters.xlsx) e mostra la stessa funzionalità usando Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Charts;
using namespace Aspose::Cells::Tables;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook
    Workbook workbook(u"TableFilters.xlsx");

    // Access first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Access the instance of the newly added chart
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 7, 7, 15, 15);
    Chart chart = sheet.GetCharts().Get(chartIndex);

    // Set data range
    chart.SetChartDataRange(u"A1:B7", true);

    // Convert the chart to image
    chart.ToImage(u"TableFilters.before.png");

    // Add a new List Object to the worksheet
    ListObject listObject = sheet.GetListObjects().Get(sheet.GetListObjects().Add(u"A1", u"B7", true));

    // Add default style to the table
    listObject.SetTableStyleType(TableStyleType::TableStyleMedium10);

    // Show Total
    listObject.SetShowTotals(false);

    // Add filters for a filter column
    listObject.GetAutoFilter().AddFilter(0, u"James");

    // Apply the filters
    listObject.GetAutoFilter().Refresh();

    // After adding new value the chart will change
    listObject.PutCellValue(7, 0, Object(u"Me"));
    listObject.PutCellValue(7, 1, Object(1000));

    // Check the changed images
    chart.ToImage(u"TableFilters.after.png");

    // Saving the Excel file
    workbook.Save(u"TableFilter.out.xlsx");

    Aspose::Cells::Cleanup();
}
```
