---
title: Blocca le righe superiori del foglio Excel con C++
linktitle: Congelare righe
type: docs
weight: 190
url: /it/cpp/how-to-freeze-rows-of-excel-worksheet
description: In questo articolo, imparerai come bloccare le righe superiori dei fogli Excel programmaticamente usando la libreria C++ con l API di Aspose.Cells.
keywords: Congela le righe superiori, Congela la prima riga.
---

## **Introduzione**

In questo articolo, impareremo come bloccare le righe superiori. Quando hai una grande quantità di dati sotto una intestazione comune, non puoi vedere l'intestazione quando scorri verso il basso nel foglio di lavoro. Puoi bloccare le righe superiori in modo che quelle rimangano visibili anche quando il resto dei dati viene scrolled. Puoi facilmente vedere le intestazioni nelle righe superiori.

## **Congelare le righe in Excel**

**![Congelare la/e riga/e superiore/i in Excel](Freeze-Rows.png)**

1. Se vuoi bloccare le righe superiori, seleziona prima la riga sotto la riga che deve essere bloccata.
2. Fare clic su Visualizza > Blocca riquadri.
3. Nel menu a discesa, fare clic su Congela riga superiore.
4. Se scorri verso il basso, la prima riga rimane sempre visibile in alto.

**![Riga congelata](Frozen-Row.png)**

Come puoi vedere, la prima riga è congelata, e la prima riga rimane sempre in cima alla visualizzazione quando scorri verso il basso.

Congelare le righe ti permette di visualizzare i tuoi grandi dati senza perdere di vista l'etichetta della riga.

## **Congela le righe con Aspose.Cells for C++**
È semplice congelare riga(i) con Aspose.Cells for C++. 
Usa il metodo [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) per congelare riga(i) alla riga selezionata.
1. Costruisci un Workbook per aprire il file o crea un file vuoto.
2. Congela la prima riga con il metodo Worksheet.FreezePanes().
3. Salvare il file.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook
    Workbook workbook(u"Freeze.xlsx");

    // Freezing panes at the cell B2
    workbook.GetWorksheets().Get(0).FreezePanes(u"A2", 1, 0);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

File Excel di esempio allegato(../Freeze.xlsx).
