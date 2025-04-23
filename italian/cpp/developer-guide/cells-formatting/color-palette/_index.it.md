---
title: Come usare la tavolozza dei colori con C++
linktitle: Come Usare la Palette di Colori
type: docs
weight: 80
url: /it/cpp/excel-color-palette/
description: Codice C++ per aggiungere colori personalizzati alla tavolozza e usare la tavolozza di Excel con l API Aspose.Cells for C++.
keywords: aggiungi colori personalizzati alla palette, palette di colori excel programmaticamente in c++, come usare programmaticamente la palette dei colori nel workbook, come usare la palette dei colori in excel con c++
---

## **Colori e Palette**

Una palette è il numero di colori disponibili per creare un'immagine. L'uso di una palette standardizzata in una presentazione consente all'utente di creare un aspetto costante. Ogni file di Microsoft Excel (97-2003) ha una palette di 56 colori che possono essere applicati a celle, caratteri, linee guida, oggetti grafici, riempimenti e linee in un grafico.

Con Aspose.Cells è possibile utilizzare non solo i colori esistenti nella palette ma anche colori personalizzati. Prima di utilizzare un colore personalizzato, aggiungilo prima alla palette.

Questo argomento tratta come aggiungere colori personalizzati alla palette.

## **Aggiungi Colori Personalizzati alla Palette**

Aspose.Cells supporta la palette a 56 colori di Microsoft Excel. Per utilizzare un colore personalizzato non definito nella palette, aggiungi il colore alla palette.

Aspose.Cells fornisce una classe, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), che rappresenta un file di Microsoft Excel. La classe [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) fornisce un metodo [**ChangePalette**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/changepalette/) che richiede i seguenti parametri per aggiungere un colore personalizzato alla modifica della palette:

- Colore personalizzato, il colore personalizzato da aggiungere.
- Indice, l'indice del colore nella palette che il colore personalizzato sostituirà. Dovrebbe essere compreso tra 0 e 55.

Nell'esempio seguente viene aggiunto un colore personalizzato (Orchidea) alla palette prima di applicarlo a un carattere.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Check if Orchid color is in the palette
    std::cout << "Is Orchid in palette? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add Orchid color to the palette at index 55
    workbook.ChangePalette(Color::Orchid(), 55);

    // Verify if Orchid is now in the palette
    std::cout << "Is Orchid in palette now? " << workbook.IsColorInPalette(Color::Orchid()) << std::endl;

    // Add a new worksheet
    int i = workbook.GetWorksheets().Add();

    // Get the reference to the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(i);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set value in cell A1
    cell.PutValue(u"Hello Aspose!");

    // Create a new style
    Style styleObject = workbook.CreateStyle();

    // Set the custom color (Orchid) to the font
    styleObject.GetFont().SetColor(workbook.GetColors()[55]);

    // Apply the style to the cell
    cell.SetStyle(styleObject);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

La palette contiene solo 56 colori. Quando si aggiunge un colore personalizzato alla palette, la palette cambia e qualsiasi elemento nel file formattato con il colore precedente viene modificato. Quindi, quando si modifica la palette, si prega di fare molta attenzione. Inoltre, questa è una limitazione solo nel formato file XLS (Excel 97 - 2003) in quanto non vi è alcuna limitazione per i formati file XLSX o altri formati di file avanzati di MS Excel (2007/2010 o 2013).

{{% /alert %}}
