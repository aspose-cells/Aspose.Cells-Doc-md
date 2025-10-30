---
title: Come creare un grafico a scorrimento dinamico con C++
linktitle: Creare grafico a scorrimento dinamico
description: Impara come creare un grafico dinamico a scorrimento usando Aspose.Cells for C++. La nostra guida passo passo dimostrerà come implementare transizioni di dati fluide e scorrimento automatico nel tuo grafico per una visualizzazione continua e aggiornata.
keywords: Aspose.Cells for C++, Grafico a Scorrimento Dinamico, Transizioni di Dati, Scorrimento Fluido, Visualizzazione Continua, Aggiornamento della Visualizzazione.
type: docs
weight: 75
url: /it/cpp/create-dynamic-scrolling-chart/
---

## **Possibili Scenari di Utilizzo**
Un grafico dinamico a scorrimento è un tipo di rappresentazione grafica utilizzato per visualizzare dati che cambiano nel tempo. È progettato per fornire una visualizzazione in tempo reale dei dati, consentendo agli utenti di monitorare aggiornamenti e tendenze continui. Il grafico si aggiorna continuamente man mano che vengono aggiunti nuovi dati e scorre automaticamente per mostrare le informazioni più recenti.

I grafici dinamici a scorrimento sono comunemente utilizzati in vari settori, come finanza, analisi del mercato azionario, tracciamento del meteo e analisi dei social media. Consentono agli utenti di visualizzare e analizzare pattern di dati e prendere decisioni informate basate su informazioni in tempo reale.

Questi grafici sono tipicamente interattivi, consentendo all'utente di ingrandire o ridurre, scorrere attraverso dati storici e regolare gli intervalli temporali. Spesso supportano più serie di dati, fornendo una visione completa di diverse metriche e le loro correlazioni.

In generale, i grafici di scorrimento dinamici sono strumenti preziosi per monitorare e analizzare i dati a serie temporali, facilitando la presa delle decisioni in tempo reale e potenziando le capacità di visualizzazione dei dati.

## **Usa Aspose Cells per Creare un Grafico a Scorrimento Dinamico**
Nei paragrafi successivi, ti mostreremo come creare un Grafico a Scorrimento Dinamico usando Aspose.Cells. Ti mostreremo il codice dell'esempio e il file Excel creato con questo codice.

## **Codice di Esempio**
Il codice di esempio seguente genererà il [File del grafico di scorrimento dinamico](DynamicScrollingChart.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    U16String localPath(u"");

    Workbook workbook;
    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);

    sheet.GetCells().Get(u"A1").PutValue(u"Day");
    sheet.GetCells().Get(u"B1").PutValue(u"Sales");

    int allDays = 30;
    int showDays = 10;
    int currentDay = 1;

    Cells cells = sheet.GetCells();
    for (int i = 0; i < allDays; i++)
    {
        int row = i + 1;
        cells.Get(row, 0).PutValue(i + 1);
        cells.Get(row, 1).PutValue(50 * (i % 2) + 20 * (i % 3) + 10 * (i / 3));
    }

    sheet.GetCells().Get(u"G19").PutValue(u"Start Day");
    sheet.GetCells().Get(u"G20").PutValue(currentDay);
    sheet.GetCells().Get(u"H19").PutValue(u"Show Days");
    sheet.GetCells().Get(u"H20").PutValue(showDays);

    int index = sheets.GetNames().Add(u"Sheet1!ChtScrollData");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    index = sheets.GetNames().Add(u"Sheet1!ChtScrollLabels");
    sheets.GetNames().Get(index).SetRefersTo(u"=OFFSET(Sheet1!$A$2,Sheet1!$G$20,0,Sheet1!$H$20,1)");

    ScrollBar bar = sheet.GetShapes().AddScrollBar(2, 0, 3, 0, 200, 30);
    bar.SetMin(0);
    bar.SetMax(allDays - showDays);
    bar.SetCurrentValue(currentDay);
    bar.SetLinkedCell(u"$G$20");

    int chartIndex = sheet.GetCharts().Add(ChartType::Line, 2, 4, 15, 10);
    Chart chart = sheet.GetCharts().Get(chartIndex);
    chart.GetNSeries().Add(u"Sales", true);
    chart.GetNSeries().Get(0).SetValues(u"Sheet1!ChtScrollData");
    chart.GetNSeries().Get(0).SetXValues(u"Sheet1!ChtScrollLabels");

    workbook.Save(localPath + u"DynamicScrollingChart.xlsx");

    Aspose::Cells::Cleanup();
}
```

## **Note**
Nel file generato, è possibile operare sulla barra di scorrimento, mentre il grafico conta dinamicamente gli ultimi 10 set di dati. Ciò viene fatto utilizzando la formula "OFFSET" nel codice di esempio:

```
"=OFFSET(Sheet1!$B$2,Sheet1!$G$20,0,Sheet1!$H$20,1)"
```

È possibile provare a modificare il numero "10" in "15" nella cella "Foglio1!$H$20", e il grafico dinamico conterà gli ultimi 15 set di dati. Ora abbiamo creato con successo un grafico di scorrimento dinamico utilizzando Aspose.Cells.
{{< app/cells/assistant language="cpp" >}}
