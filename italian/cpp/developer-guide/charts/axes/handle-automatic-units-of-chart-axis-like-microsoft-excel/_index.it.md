---
title: Gestire le unità automatiche dell asse del grafico come Microsoft Excel con C++
linktitle: Gestire le unità automatiche dell asse del grafico
description: Impara come gestire le unità automatiche sugli assi del grafico in Aspose.Cells for C++, simile a Microsoft Excel. La nostra guida ti mostrerà come configurare e personalizzare le unità automatiche su un asse del grafico, inclusa la visualizzazione in notazione scientifica e la regolazione della scala.
keywords: Aspose.Cells for C++, assi del grafico, unità automatiche, Microsoft Excel, configurazione, personalizzazione, notazione scientifica, scala.
type: docs
weight: 120
url: /it/cpp/handle-automatic-units-of-chart-axis-like-microsoft-excel/
---

## **Possibili Scenari di Utilizzo**
Le prime versioni di Aspose.Cells non potevano gestire correttamente le unità automatiche dell'asse del grafico quando il grafico veniva reso in immagine o PDF. Ora, Aspose.Cells supporta la gestione delle unità automatiche dell'asse del grafico. Non c'è alcuna modifica del codice. Basta convertire il tuo grafico in immagine o PDF e renderà l'asse del grafico esattamente come lo renderà Microsoft Excel.

## **Gestire le unità automatiche dell'asse del grafico come Microsoft Excel**
Il seguente codice di esempio carica il [file Excel di esempio](61767755.xlsx) e genera il [grafico PDF di output](61767752.pdf). La schermata mostra le unità automatiche dell'asse del grafico in rettangoli rossi e confronta anche il grafico del file Excel di esempio con il grafico PDF di output. Entrambi sono esattamente simili.

![todo:image_alt_text](handle-automatic-units-of-chart-axis-like-microsoft-excel_1.png)

## **Codice di Esempio**
```c++
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

    // Load the sample Excel file
    U16String inputFilePath = srcDir + u"sampleHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = wb.GetWorksheets();
    Worksheet ws = worksheets.Get(0);

    // Access first chart
    ChartCollection charts = ws.GetCharts();
    Chart ch = charts.Get(0);

    // Render chart to PDF
    U16String outputFilePath = outDir + u"outputHandleAutomaticUnitsOfChartAxisLikeMicrosoftExcel.pdf";
    ch.ToPdf(outputFilePath);

    std::cout << "Chart rendered to PDF successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
