---
title: Come creare un grafico dinamico con menu a discesa con C++
linktitle: Creare grafico dinamico con menu a discesa
description: Impara come creare un grafico dinamico che si aggiorna in base alla selezione di un menu a discesa usando Aspose.Cells for C++. La nostra guida passo passo dimostrerà come integrare un menu a discesa nel tuo grafico per una visualizzazione dati flessibile.
keywords: Aspose.Cells for C++, Grafico dinamico, Menu a discesa, Visualizzazione dati, Integrazione, Visualizzazione flessibile.
type: docs
weight: 76
url: /it/cpp/create-dynamic-chart-with-dropdownlist/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico con elenco a discesa in Excel è uno strumento potente che consente agli utenti di creare grafici interattivi che possono aggiornarsi dinamicamente in base ai dati selezionati. Questa funzione è particolarmente utile in situazioni in cui è necessario analizzare più set di dati o confrontare vari scenari.

Una comune applicazione di un grafico dinamico con elenco a discesa è nell'analisi finanziaria. Ad esempio, un'azienda potrebbe avere dati finanziari per diversi anni o reparti. Utilizzando un elenco a discesa, gli utenti possono selezionare il set di dati specifico che desiderano analizzare e il grafico si aggiornerà automaticamente per visualizzare le informazioni corrispondenti. Questo consente un facile confronto e identificazione di tendenze o pattern.

Un'altra applicazione è nelle vendite e nel marketing. Un'azienda potrebbe avere dati di vendita per diversi prodotti o regioni. Con un grafico dinamico con elenco a discesa, gli utenti possono scegliere un prodotto o una regione specifica dall'elenco a discesa e il grafico si aggiornerà dinamicamente per mostrare le performance di vendita per l'opzione selezionata. Ciò aiuta a identificare le aree o i prodotti più performanti e a prendere decisioni basate sui dati.

In sintesi, un grafico dinamico con elenco a discesa in Excel fornisce un modo flessibile e interattivo per visualizzare e analizzare i dati. È prezioso in situazioni in cui è necessario confrontare più set di dati o esplorare diversi scenari, rendendolo uno strumento versatile per l'analisi finanziaria, le vendite e il marketing e molte altre applicazioni.

## **Usa Aspose Cells per creare un grafico dinamico con menu a discesa**
Nei paragrafi successivi, ti mostreremo come creare un grafico dinamico con menu a discesa usando Aspose.Cells. Mostreremo il codice dell'esempio, così come il file Excel creato con questo codice.

## **Codice di Esempio**
Il seguente codice di esempio genererà il [File del grafico dinamico con elenco a discesa](DynamicChartWithDropdownlist.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A3").PutValue(u"Tea");
    sheet.GetCells().Get(u"A4").PutValue(u"Coffee");
    sheet.GetCells().Get(u"A5").PutValue(u"Sugar");

    // In this example, we will add 12 months of data
    sheet.GetCells().Get(u"B2").PutValue(u"Jan");
    sheet.GetCells().Get(u"C2").PutValue(u"Feb");
    sheet.GetCells().Get(u"D2").PutValue(u"Mar");
    sheet.GetCells().Get(u"E2").PutValue(u"Apr");
    sheet.GetCells().Get(u"F2").PutValue(u"May");
    sheet.GetCells().Get(u"G2").PutValue(u"Jun");
    sheet.GetCells().Get(u"H2").PutValue(u"Jul");
    sheet.GetCells().Get(u"I2").PutValue(u"Aug");
    sheet.GetCells().Get(u"J2").PutValue(u"Sep");
    sheet.GetCells().Get(u"K2").PutValue(u"Oct");
    sheet.GetCells().Get(u"L2").PutValue(u"Nov");
    sheet.GetCells().Get(u"M2").PutValue(u"Dec");

    int allMonths = 12;
    int iCount = 3;
    for (int i = 0; i < iCount; i++)
    {
        for (int j = 0; j < allMonths; j++)
        {
            int _row = i + 2;
            int _column = j + 1;
            sheet.GetCells().Get(_row, _column).PutValue(50 * (i % 2) + 20 * (j % 3) + 10 * (i / 3) + 10);
        }
    }

    // This is the Dropdownlist for Dynamic Data
    CellArea ca = CellArea::CreateCellArea(9, 0, 9, 0);
    int _index = sheet.GetValidations().Add(ca);
    Validation _va = sheet.GetValidations().Get(_index);
    _va.SetType(ValidationType::List);
    _va.SetInCellDropDown(true);
    _va.SetFormula1(u"=$B$2:$M$2");

    sheet.GetCells().Get(u"A9").PutValue(u"Current Month");
    sheet.GetCells().Get(u"A10").PutValue(u"Jan");

    Style _style = sheet.GetCells().Get(u"A10").GetStyle();
    _style.GetFont().SetIsBold(true);
    _style.SetPattern(BackgroundType::Solid);
    _style.SetForegroundColor(Color::Yellow());
    sheet.GetCells().Get(u"A10").SetStyle(_style);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtMonthData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtXLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=Sheet1!$A$3:$A$5");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Column, 8, 2, 20, 8);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"month", true);
    chart.GetNSeries().Get(0).SetName(u"=Sheet1!$A$10");
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtMonthData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtXLabels");

    // Save the workbook as an Excel file.
    workbook.Save(u"DynamicChartWithDropdownlist.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Note**
Nel file generato, il grafico conterà dinamicamente i dati per il mese selezionato. Questo viene fatto utilizzando la formula "OFFSET" nel codice di esempio:

```cpp
"=OFFSET(Sheet1!$A$3,0,MATCH($A$10, $B$2:$M$2, 0),3,1)"
```

Puoi provare a cambiare il valore della lista a discesa nella cella "Foglio1!$A$10", e vedrai il cambiamento dinamico del grafico. Abbiamo creato con successo un grafico dinamico con lista a discesa utilizzando Aspose.Cells.
