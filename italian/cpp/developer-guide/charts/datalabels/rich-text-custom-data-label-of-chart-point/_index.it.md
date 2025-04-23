---
title: Etichetta dati personalizzata Ricca di Testo del Punto del Grafico con C++
description: Scopri come aggiungere etichette dati personalizzate di testo ricco ai punti del grafico in Aspose.Cells for C++. La nostra guida ti mostrerà come formattare le etichette con font, colori e opzioni di allineamento diversi per migliorare l aspetto e la leggibilità dei tuoi grafici.
keywords: Aspose.Cells for C++, tracciamento, testo ricco, etichette dati personalizzate, font, colori, allineamento, aspetto, leggibilità.
type: docs
weight: 10
url: /it/cpp/rich-text-custom-data-label-of-chart-point/
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells per creare etichette dati personalizzate ricche per il punto del grafico. Aspose.Cells fornisce il metodo [DataLabels.Characters()](https://reference.aspose.com/cells/cpp/aspose.cells.charts/charttextframe/characters/) per restituire l'oggetto [FontSetting](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/) che può essere usato per impostare le proprietà del font del testo come il colore, il grassetto, ecc.

{{% /alert %}}

## Etichetta dati personalizzata di testo ricco del punto del grafico

Il seguente codice accede al primo punto del grafico della prima serie, imposta il suo testo e poi imposta il font dei primi 10 caratteri impostando il colore su rosso e il grassetto su **true**.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create a workbook from source Excel file
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access the first chart inside the sheet
    Chart chart = worksheet.GetCharts().Get(0);

    // Access the data label of first series first point
    DataLabels dlbls = chart.GetNSeries().Get(0).GetPoints().Get(0).GetDataLabels();

    // Set data label text
    dlbls.SetText(u"Rich Text Label");

    // Set the font setting of the first 10 characters
    FontSetting fntSetting = dlbls.Characters(0, 10);
    fntSetting.GetFont().SetColor(Color::Red());
    fntSetting.GetFont().SetIsBold(true);

    // Save the workbook
    workbook.Save(srcDir + u"output_out.xlsx");

    Aspose::Cells::Cleanup();
}
```
