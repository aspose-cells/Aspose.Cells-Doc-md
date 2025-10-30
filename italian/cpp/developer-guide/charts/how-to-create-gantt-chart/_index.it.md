---
title: Come creare un diagramma di Gantt con C++
linktitle: Come creare un diagramma di Gantt
type: docs
weight: 72
url: /it/cpp/how-to-create-gantt-chart/
description: Impara come creare un diagramma di Gantt con API Aspose.Cells for C++.
keywords: C++ crea un diagramma di Gantt, aggiungi un diagramma di Gantt, inserisci un diagramma di Gantt
---

## **Che cos'è un diagramma di Gantt**

Un diagramma di Gantt è un tipo di diagramma a barre che illustra un programma di progetto. Mostra le date di inizio e fine delle varie componenti di un progetto. Ogni attività è rappresentata da una barra, con la sua lunghezza corrispondente alla durata. I diagrammi di Gantt indicano anche le dipendenze tra le attività, permettendo ai project manager di visualizzare la sequenza in cui le attività devono essere completate. Sono ampiamente usati nella gestione di progetti per pianificare, programmare e monitorare efficacemente i progetti.

## **Come creare un diagramma di Gantt in Excel**

Puoi creare un diagramma di Gantt in Excel seguendo questi passaggi:
1. Aggiungi alcuni dati per il diagramma di Gantt. 
<br>
<img src="00.png" width=50% />
1. Seleziona i dati e vai su Inserisci --> Grafici --> Inserisci grafico a colonne o barre --> Grafico a barre impilate. Nel nostro esempio, sono B1:B7, quindi inserisci un grafico **Barra impilata**.
<br>
<img src="1.png" width=50% />

1. Seleziona il grafico, **Seleziona dati** -> **Aggiungi**, imposta il **Nome serie** e i **Valori serie** come segue.
<br>
<img src="2.png" width=50% />

1. Seleziona il grafico, modifica le **Etichette dell'asse orizzontale (Categoria)**.
<br>
<img src="3.png" width=50% />

1. **Formatta l'asse** Y, seleziona **Categorie in ordine inverso**.
1. Seleziona la **Serie Blu** e imposta **Riempi -> Nessun riempimento**.
1. **Formatta l'asse** l'asse X, imposta i valori **Minimo e Massimo** (01/05/2019:43470, 30/01/2019:43494).
<br>
<img src="4.png" width=50% />

1. **Aggiungi etichette dati** al grafico, ora otterrai un diagramma di Gantt.
<br>
<img src="0.png" width=50% />


## **Come aggiungere un diagramma di Gantt in Aspose.Cells**
Vedi il seguente esempio di codice. Carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati esempio. Poi crea il grafico a barre impilate in base ai dati iniziali e imposta le proprietà pertinenti. Infine, salva il workbook in formato [output XLSX](result.xlsx). Lo screenshot seguente mostra il diagramma di Gantt creato da Aspose.Cells nel file Excel di output.
<br>
<img src="5.png" width=60% />

### **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create BarStacked Chart
    int32_t chartIndex = worksheet.GetCharts().Add(ChartType::BarStacked, 5, 6, 20, 15);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(chartIndex);

    // Set the chart title name
    chart.GetTitle().SetText(u"Gantt Chart");

    // Set the chart title visibility
    chart.GetTitle().SetIsVisible(true);

    // Set data range
    chart.SetChartDataRange(u"B1:B6", true);

    // Add series data range
    chart.GetNSeries().Add(u"C2:C6", true);

    // No fill for one series
    chart.GetNSeries().Get(0).GetArea().GetFillFormat().SetFillType(FillType::None);

    // Set the Horizontal(Category) Axis
    chart.GetNSeries().SetCategoryData(u"A2:A6");

    // Reverse the Horizontal(Category) Axis
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set the value axis's MinValue and MaxValue
    chart.GetValueAxis().SetMinValue(worksheet.GetCells().Get(u"B2").GetValue());
    chart.GetValueAxis().SetMaxValue(worksheet.GetCells().Get(u"D6").GetValue());

    // Set the PlotArea with no fill
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Show the DataLabels
    chart.GetNSeries().Get(1).GetDataLabels().SetShowValue(true);

    // Disable the Legend
    chart.SetShowLegend(false);

    // Save the result
    workbook.Save(u"result.xlsx");

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
