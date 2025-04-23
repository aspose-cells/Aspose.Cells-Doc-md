---
title: Impostare formula condivisa con C++
linktitle: Impostazione Formula Condivisa
type: docs
weight: 10
url: /it/cpp/setting-shared-formula/
description: Impara come impostare formule condivise nei fogli di lavoro di Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Se desideri aggiungere una funzione in un foglio di lavoro che esegua calcoli, questo articolo spiega come ottenere questo risultato utilizzando Aspose.Cells.

{{% /alert %}}

## Impostazione Formula Condivisa utilizzando Aspose.Cells

Supponiamo di avere un foglio di lavoro pieno di dati nel formato che assomiglia al seguente foglio di lavoro di esempio.

|**File di input con una colonna di dati**|
| :- |
|![todo:image_alt_text](setting-shared-formula_1.png)|

Desideri aggiungere una funzione in B2 che calcolerà l'IVA per la prima riga di dati. L'IVA è del **9%**. La formula che calcola l'IVA è: **"=A2*0.09"**. Questo articolo spiega come applicare questa formula con Aspose.Cells.

Aspose.Cells consente di specificare una formula utilizzando la proprietà [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/). Ci sono due opzioni per aggiungere formule alle altre celle (B3, B4, B5, e così via) nella colonna.

Puoi ripetere ciò che hai fatto per la prima cella, impostando effettivamente la formula per ogni cella, aggiornando di conseguenza il riferimento della cella (A3*0.09, A4*0.09, A5*0.09, ecc.). Questo richiede di aggiornare i riferimenti di cella per ogni riga. Richiede anche che Aspose.Cells analizzi ogni formula singolarmente, il che può essere lento per fogli di calcolo grandi e formule complesse. Aggiunge inoltre righe di codice extra, anche se i cicli possono ridurle in parte.

Un altro approccio è utilizzare una **formula condivisa**. Con una formula condivisa, le formule vengono aggiornate automaticamente per i riferimenti alle celle in ogni riga in modo che l'imposta venga calcolata correttamente. Il metodo [**SetSharedFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setsharedformula/) è più efficiente del primo metodo.

L'esempio seguente mostra come utilizzarla.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"source.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Output_out.xlsx";

    // Instantiate a Workbook from existing file
    Workbook workbook(inputFilePath);

    // Get the cells collection in the first worksheet
    Cells cells = workbook.GetWorksheets().Get(0).GetCells();

    // Apply the shared formula in the range i.e.., B2:B14
    cells.Get(u"B2").SetSharedFormula(u"=A2*0.09", 13, 1);

    // Save the excel file
    workbook.Save(outputFilePath, SaveFormat::Xlsx);

    std::cout << "Shared formula applied and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
