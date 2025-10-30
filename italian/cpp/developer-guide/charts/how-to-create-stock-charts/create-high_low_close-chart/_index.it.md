--- 
title: Crea un Grafico Azione Altro Chiusura (HLC) Stock con C++ 
linktitle: Crea un grafico di scorta High Low Close (HLC) 
description: Impara come creare un grafico azioni alta bassa chiusura usando Aspose.Cells for C++. La nostra guida passo passo dimostrerà come tracciare i dati del mercato azionario, inclusi i prezzi massimo, minimo e di chiusura, per una migliore analisi e visualizzazione. 
keywords: Aspose.Cells for C++, Grafico Azioni Alta Bassa Chiusura, Dati di Mercato, Analisi, Visualizzazione. 
type: docs 
weight: 181 
url: /it/cpp/create-high-low-close-stock-chart/ 
--- 

## **Possibili Scenari di Utilizzo** 
Il grafico di stock High-Low-Close (HLC) utilizza quattro colonne di dati. La prima colonna è una categoria, di solito una data ma anche i nomi delle azioni possono essere utilizzati. Le successive tre colonne in ordine sono per i prezzi alti, bassi e di chiusura. L'intervallo di prezzo per ogni categoria è indicato da una linea verticale da basso a alto, e il prezzo di chiusura è mostrato utilizzando un segno di spunta che si estende verso destra di questa linea. 

![todo:image_alt_text](sample.png) 
## **Miglioramenti della visibilità nel grafico** 
A volte, per rendere il grafico più intuitivo, possiamo modificare l'aspetto del marcatore (chiusura), o farlo visualizzare sull'asse secondario. 

![todo:image_alt_text](sample2.png) 
## **Codice di Esempio** 
Il codice di esempio seguente carica il [file Excel di esempio](High-Low-Close.xlsx) e genera il [file Excel di output](out.xlsx).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook
    Workbook workbook(u"High-Low-Close.xlsx");

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Create High-Low-Close-Stock Chart
    int pieIdx = worksheet.GetCharts().Add(ChartType::StockHighLowClose, 5, 6, 20, 12);

    // Retrieve the Chart object
    Chart chart = worksheet.GetCharts().Get(pieIdx);

    // Set the legend can be showed
    chart.SetShowLegend(true);

    // Set the chart title name 
    chart.GetTitle().SetText(u"High-Low-Close Stock");

    // Set the Legend at the bottom of the chart area
    chart.GetLegend().SetPosition(LegendPositionType::Bottom);

    // Set data range
    chart.SetChartDataRange(u"A1:D9", true);

    // Set category data 
    chart.GetNSeries().GetCategoryData() = u"A2:A9";

    // Set the marker with the built-in data 
    chart.GetNSeries().Get(2).GetMarker().SetMarkerStyle(ChartMarkerType::Dash);
    chart.GetNSeries().Get(2).GetMarker().SetMarkerSize(20);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetFormatting(FormattingType::Custom);
    chart.GetNSeries().Get(2).GetMarker().GetArea().SetForegroundColor(Color::Maroon());

    // Fill the PlotArea area with nothing 
    chart.GetPlotArea().GetArea().GetFillFormat().SetFillType(FillType::None);

    // Save the Excel file
    workbook.Save(u"out.xlsx");

    std::cout << "Chart created and Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
``` 
{{< app/cells/assistant language="cpp" >}}
