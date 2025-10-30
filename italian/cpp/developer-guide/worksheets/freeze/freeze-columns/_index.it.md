---
title: Blocca le prime colonne del foglio Excel con C++
linktitle: Congelare le colonne
type: docs
weight: 190
url: /it/cpp/how-to-freeze-columns-of-excel-worksheet
description: In questo articolo, imparerai come bloccare le colonne a sinistra dei fogli Excel programmaticamente utilizzando la libreria C++ con l API di Aspose.Cells.
keywords: Blocca le colonne a sinistra, Blocca le prime colonne, Blocca le colonne
---

## **Introduzione**

In questo articolo, impareremo come bloccare le colonne a sinistra. Quando hai una grande quantità di dati in una riga, non puoi vedere le colonne a sinistra quando scorri orizzontalmente il foglio di lavoro. Puoi bloccare e fissare le prime colonne in modo da poterle vedere anche quando il resto dei dati viene scorretti. Puoi facilmente vedere le intestazioni nelle colonne di sinistra.

## **Congela le colonne In Excel**

**![Congelare la/e colonna/e di sinistra in Excel](freeze-columns.png)**

1. Se vuoi bloccare le colonne a sinistra, seleziona prima la colonna sotto la colonna che deve essere bloccata.
2. Fare clic su Visualizza > Blocca riquadri.
3. Dal menu a discesa, clicca su Blocca prima colonna.
4. Se scorri verso il basso, la prima colonna rimane sempre visibile a sinistra.

**![Colonna bloccata](frozen-columns.png)**

Come puoi vedere, la prima colonna è bloccata, rimane sempre ancorata in alto alla vista quando scorri orizzontalmente.

Il blocco delle colonne ti permette di visualizzare i tuoi dati lunghi senza perdere di vista la prima colonna.

## **Blocca colonne con Aspose.Cells for C++**
È semplice bloccare le prime colonne con Aspose.Cells for C++. 
Usa il metodo [**Worksheet.FreezePanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/freezepanes/) per bloccare le colonne alla colonna selezionata.
1. Costruire un libro di lavoro per aprire il file o creare un file vuoto.
2. Blocca la prima colonna con il metodo Worksheet.FreezePanes().
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

    // Freezing panes at the second column
    workbook.GetWorksheets().Get(0).FreezePanes(u"B1", 0, 1);

    // Saving the file
    workbook.Save(u"frozen.xlsx");

    std::cout << "Panes frozen successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

File Excel di esempio allegato (Freeze.xlsx).
{{< app/cells/assistant language="cpp" >}}
