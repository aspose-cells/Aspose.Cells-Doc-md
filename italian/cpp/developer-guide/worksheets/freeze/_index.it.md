---
title: Blocca pannelli del Foglio di Lavoro di Excel con C++
linktitle: Blocca riquadri
type: docs
weight: 190
url: /it/cpp/how-to-freeze-panes-of-excel-worksheet
description: In questo articolo, imparerai come bloccare i pannelli dei Fogli di Excel programmaticamente utilizzando la libreria C++ con l API Aspose.Cells.
keywords: Blocca pannelli, Blocca finestra.
---

## **Introduzione**

In questo articolo, impareremo Come Bloccare i Pannelli. Quando hai una grande quantità di dati sotto un'intestazione comune, non riesci a vedere l'intestazione quando scorri verso il basso il foglio. E ogni record contiene molti dati. Puoi bloccare i pannelli in modo da poter vedere quella parte bloccata anche quando il resto dei dati viene scrollato. Puoi facilmente vedere gli intestazioni nelle righe superiori o nelle prime colonne. Bloccare e sbloccare i pannelli cambia solo la visualizzazione dei dati senza modificare i dati stessi.

## **In Excel**

**![Blocca riquadri in Excel](Freeze-panes.png)**

1. Se vuoi bloccare i pannelli, blocca righe e colonne, allora prima seleziona una cella (come B2).
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Blocca riquadri.
4. Se scorri verso il basso o a destra, la prima riga e colonna sono bloccate.

**![Pannelli bloccati](Frozen-Panes.png)**

Come puoi vedere, la prima riga e la colonna A sono Bloccate, la seconda riga è 32, e la seconda colonna visibile è D.

Bloccare i pannelli ti permette di visualizzare grandi quantità di dati senza dover tenere traccia delle etichette di riga o colonna.

## **Blocca Panes con Aspose.Cells for C++**
È semplice bloccare i pannelli con Aspose.Cells for C++. Si prega di utilizzare il metodo [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) per bloccare i pannelli alla cella selezionata.
1. Costruisci un Workbook per aprire il file o crea un file vuoto.
2. Blocca i pannelli con il metodo Worksheet.FreezePanes().
3. Salvare il file.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Freeze.xlsx");
    Workbook workbook(inputFilePath);

    // Freeze panes at the cell B2
    WorksheetCollection sheets = workbook.GetWorksheets();
    sheets.Get(0).FreezePanes(u"B2", 1, 1);

    // Save the file
    U16String outputFilePath(u"frozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

File Excel di esempio allegato (Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
