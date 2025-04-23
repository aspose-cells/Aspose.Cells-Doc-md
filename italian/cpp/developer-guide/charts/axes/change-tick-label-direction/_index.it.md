---
title: Cambia la direzione delle etichette degli scatti con C++
linktitle: Cambiare la direzione delle etichette degli intervalli
description: Impara come cambiare la direzione delle etichette dei tick in Aspose.Cells for C++. La nostra guida ti aiuterà a capire come regolare l orientamento delle etichette dei tick sugli assi, inclusi orientamenti orizzontale, verticale e inclinato.
keywords: Aspose.Cells for C++, etichette dei tick, direzione, orientamento, assi, orizzontale, verticale, inclinato.
type: docs
weight: 170
url: /it/cpp/change-tick-label-direction/
---

## **Cambia la direzione delle etichette di graduazione**

Aspose.Cells ti permette di cambiare la direzione delle etichette dei tick dell'asse utilizzando la proprietà [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/). La proprietà [**TickLabels.GetDirectionType()**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/ticklabels/getdirectiontype/) accetta il valore dell'enumerazione [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype). L'enumerazione [**ChartTextDirectionType**](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextdirectiontype) include i seguenti membri:

- Orizzontale
- Verticale
- Ruota90
- Ruota270
- Impilato

L'immagine seguente confronta i file di origine e di output:

### **Immagine del file sorgente**

![todo:image_alt_text](change-tick-label-direction_1.jpg)

### **Immagine del file di output**

![todo:image_alt_text](change-tick-label-direction_2.jpg)

Il seguente frammento di codice cambia la direzione dell'etichetta dell'asse da Rotate90 a Orizzontale.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory source and output paths
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook and load the sample Excel file
    Workbook workbook(sourceDir + u"SampleChangeTickLabelDirection.xlsx");

    // Obtain the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Load the chart from the source worksheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Set the category axis tick labels direction to Horizontal
    chart.GetCategoryAxis().GetTickLabels().SetDirectionType(ChartTextDirectionType::Horizontal);

    // Output the modified workbook to a new file
    workbook.Save(outDir + u"outputChangeChartDataLableDirection.xlsx");

    std::cout << "Chart tick label direction changed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

I file sorgente e di output possono essere scaricati dai seguenti link.

[File sorgente](105480221.xlsx)

[File di output](105480223.xlsx)
