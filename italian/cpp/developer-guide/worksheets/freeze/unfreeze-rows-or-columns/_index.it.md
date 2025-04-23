---
title: Rimuovere la congelazione di righe o colonne del foglio di lavoro Excel con C++
linktitle: Scongelare riquadri
type: docs
weight: 190
url: /it/cpp/unfreeze-rows-or-columns-of-excel-worksheet
description: In questo articolo, imparerai come sbloccare righe, colonne o pannelli dei fogli di lavoro Excel tramite la programmazione con l API Aspose.Cells for C++.
keywords: Sbloccare pannelli, sbloccare righe, sbloccare colonne, sbloccare finestra.
---

## **Introduzione**

In questo articolo, impareremo come sbloccare righe, colonne e pannelli nei fogli di lavoro Excel. Se i fogli di lavoro nei file Excel sono congelati, a volte vogliamo sbloccare il foglio o regolare le righe, le colonne o i pannelli congelati.

## **In Excel**

1. Clicca sulla scheda **Visualizza** > **Blocca riquadri** > **Sblocca riquadri**.

**![scongelare riquadri in Excel](Scongela-Riquadri.png)**

## **Sblocca righe, colonne o pannelli con Aspose.Cells for C++**
È semplice sbloccare pannelli con Aspose.Cells for C++. Usa il metodo [**Worksheet.UnFreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/unfreezepanes/) per sbloccare i pannelli.

1. Costruisci un oggetto `Workbook` per aprire il file congelato.
Sblocca i riquadri utilizzando il metodo `Worksheet.UnFreezePanes()`.
3. Salvare il file.

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    U16String inputFilePath(u"Frozen.xlsx");
    Workbook workbook(inputFilePath);

    // Unfreeze panes in the first worksheet
    workbook.GetWorksheets().Get(0).UnFreezePanes();

    // Save the modified workbook
    U16String outputFilePath(u"Unfrozen.xlsx");
    workbook.Save(outputFilePath);

    std::cout << "Panes unfrozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Allegato il [file Excel di origine di esempio](Frozen.xlsx).
