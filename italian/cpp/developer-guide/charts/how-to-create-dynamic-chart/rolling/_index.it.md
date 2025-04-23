---
title: Come creare un grafico rotante dinamico con C++
linktitle: Come creare un grafico dinamico a scorrimento
description: Impara come creare un grafico rotante dinamico usando Aspose.Cells for C++. La nostra guida dimostrerà come implementare transizioni di dati fluide e medie mobili nel tuo grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells for C++, Grafico rotante dinamico, Transizioni di dati, Medie mobili fluide, Visualizzazione continua, Aggiornamento della visualizzazione.
type: docs
weight: 74
url: /it/cpp/create-dynamic-rolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento si riferisce a una rappresentazione grafica che visualizza costantemente punti dati in continuo spostamento e aggiornamento nel tempo. È un tipo di grafico che si aggiorna continuamente, mostrando una finestra mobile dei punti dati più recenti mentre scarta i punti dati più vecchi man mano che ne arrivano di nuovi.

I grafici dinamici a scorrimento sono comunemente utilizzati per visualizzare tendenze e pattern in dati in tempo reale o in streaming. Sono particolarmente utili in scenari in cui gli aspetti temporali e i cambiamenti nel tempo sono fondamentali, come l'analisi di mercato azionario, il monitoraggio meteorologico o il tracciamento delle performance in tempo reale.

Questi grafici di solito impiegano meccanismi di animazione o autoscrolling per assicurare che le informazioni più aggiornate siano sempre presentate. La lunghezza della finestra mobile può essere personalizzata per mostrare un periodo temporale specifico, come l'ultima ora, giorno o settimana.

In sintesi, un grafico dinamico a scorrimento è una rappresentazione grafica continuamente aggiornata che visualizza gli ultimi punti dati mentre scarta quelli più vecchi, consentendo agli utenti di osservare tendenze e pattern in tempo reale.

## **Usa Aspose Cells per creare un grafico dinamico a scorrimento**
Nei paragrafi successivi, ti mostreremo come creare un grafico dinamico a scorrimento utilizzando Aspose.Cells. Ti mostreremo il codice dell'esempio, nonché il file Excel creato con questo codice.

## **Codice di Esempio**
Il seguente codice di esempio genererà il [File del Grafico Dinamico a Scorrimento](DynamicRollingChart.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Your local test path
    U16String LocalPath = u"";

    // Create a new workbook and access the first worksheet.
    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    // Populate the data for the chart. Add values to cells and set series names.
    sheet.GetCells().Get(u"A1").PutValue(u"Month");
    sheet.GetCells().Get(u"A2").PutValue(1);
    sheet.GetCells().Get(u"A3").PutValue(2);
    sheet.GetCells().Get(u"A4").PutValue(3);
    sheet.GetCells().Get(u"A5").PutValue(4);
    sheet.GetCells().Get(u"A6").PutValue(5);
    sheet.GetCells().Get(u"A7").PutValue(6);
    sheet.GetCells().Get(u"A8").PutValue(7);

    sheet.GetCells().Get(u"B1").PutValue(u"Sales");
    sheet.GetCells().Get(u"B2").PutValue(50);
    sheet.GetCells().Get(u"B3").PutValue(45);
    sheet.GetCells().Get(u"B4").PutValue(55);
    sheet.GetCells().Get(u"B5").PutValue(60);
    sheet.GetCells().Get(u"B6").PutValue(55);
    sheet.GetCells().Get(u"B7").PutValue(65);
    sheet.GetCells().Get(u"B8").PutValue(70);

    // Set the dynamic range for the chart's data source.
    int index = sheets.GetNames().Add(u"Sheet1!ChtData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$1,COUNT(Sheet1!$B:$B),0,-5,1)");

    // Set the dynamic range for the chart's data labels.
    index = sheets.GetNames().Add(u"Sheet1!ChtLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)");

    // Create a chart object and set its data source.
    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 10, 3, 25, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtLabels");

    // Save the workbook as an Excel file.
    workbook.Save(LocalPath + u"DynamicRollingChart.xlsx");

    std::cout << "Dynamic rolling chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Note**
Nel file generato, puoi continuare ad aggiungere dati nelle colonne A e B, mentre il grafico conta dinamicamente gli ultimi 5 set di dati. Ciò viene fatto utilizzando la formula "SCARTO" nel codice di esempio:

```
"=OFFSET(Sheet1!$A$1,COUNT(Sheet1!$A:$A),0,-5,1)"
```

Puoi provare a cambiare il numero "-5" in "-10" nella formula, e il grafico dinamico conterà gli ultimi 10 set di dati. Ora abbiamo creato con successo un grafico dinamico a scorrimento utilizzando Aspose.Cells.
