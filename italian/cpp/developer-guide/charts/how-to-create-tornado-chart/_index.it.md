---
title: Come creare un grafico a tornado con C++
linktitle: Crea Grafico a Tornado
type: docs
weight: 73
url: /it/cpp/create-tornado-chart/
description: Impara come creare un grafico a tornado con API Aspose.Cells for C++.
keywords: C++ crea un grafico a tornado, aggiungi un grafico a tornado, inserisci un grafico a tornado
---

## **Introduzione**
Un grafico a tornado, noto anche come diagramma a tornado o grafico a tornado, è un tipo di visualizzazione dei dati che viene spesso utilizzato per l'analisi di sensibilità in Excel. Ti aiuta a capire l'impatto delle variabili in cambiamento su un particolare risultato o esito.

## **Come creare un grafico a tornado in Excel**
Puoi creare un grafico a tornado in Excel seguendo questi passaggi:
1. Seleziona i dati e vai su Inserisci --> Grafici --> Inserisci grafico a colonne o a barre --> Grafico a barre sovrapposte. Clicca su di esso.
<br>
<img src="1.png" width=70% />
2. Cambia l'asse Y: Fai clic con il pulsante destro sull'asse y. Fai clic su formatta asse. Nelle etichette, fai clic sul menu a discesa della posizione dell'etichetta e seleziona l'elemento Basso.
<br>
<img src="2.png" width=70% />
3. Seleziona una qualsiasi barra e vai al formato. Imposta una larghezza di intervallo appropriata.
<br>
<img src="3.png" width=70% />
4. Rimuoviamo il segno meno (-) dal grafico a tornado. Seleziona l'asse x. Vai al formato. Nelle opzioni asse, fai clic sul numero. Nella categoria, seleziona personalizzato. Nel codice di formato scrivi ###0,###0. Clicca su aggiungi.
<br>
<img src="4.png" width=70% />
5. Clicca sull'asse y e vai alle opzioni dell'asse. Nelle opzioni dell'asse, seleziona le **Categorie in ordine inverso**.
<br>
<img src="5.png" width=70% />

## **Come aggiungere un grafico a tornado in Aspose.Cells**
Si prega di consultare il seguente codice di esempio. Carica il [file Excel di esempio](sample.xlsx) che contiene alcuni dati di esempio. Successivamente, crea il grafico a barre sovrapposte basato sui dati iniziali e imposta le proprietà rilevanti. Infine, salva il lavoro in formato XLSX di output. La seguente schermata mostra il grafico a tornado creato da Aspose.Cells nel file Excel di output.
<br>
<img src="6.png" width=70% />

### **Codice di Esempio**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Get the chart collection from the worksheet
    ChartCollection charts = sheet.GetCharts();

    // Add a bar chart
    int index = charts.Add(ChartType::BarStacked, 8, 1, 24, 8);
    Chart chart = charts.Get(index);

    // Set data for the bar chart
    chart.SetChartDataRange(u"A1:C7", true);

    // Set properties for the bar chart
    chart.GetTitle().SetText(u"Tornado chart");
    chart.SetStyle(2);
    chart.GetPlotArea().GetArea().SetForegroundColor(Color::White());
    chart.GetPlotArea().GetBorder().SetColor(Color::White());
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set properties for the category axis
    chart.GetCategoryAxis().SetTickLabelPosition(TickLabelPositionType::Low);
    chart.GetCategoryAxis().SetIsPlotOrderReversed(true);

    // Set gap width
    chart.SetGapWidth(10);

    // Set properties for the value axis
    Axis valueAxis = chart.GetValueAxis();
    valueAxis.GetTickLabels().SetNumberFormat(u"#,##0;#,##0");

    // Save the workbook
    wb.Save(outputFilePath);

    std::cout << "Chart created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
