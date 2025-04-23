---
title: Rendere componenti aggiuntivi Office durante la conversione di Excel in PDF con C++
linktitle: Render Office Add Ins durante la conversione di Excel in PDF
type: docs
weight: 100
url: /it/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Impara come rendere componenti aggiuntivi Office durante la conversione di file Excel in PDF utilizzando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

In passato, Aspose.Cells non riusciva a rendere gli componenti aggiuntivi di Office quando un file Excel veniva salvato in formato PDF. Ora, Aspose.Cells lo rende correttamente. Non è necessario usare metodi o proprietà speciali per rendere gli componenti aggiuntivi di Office nel PDF risultante. Basta salvare il file Excel in formato PDF e questi verranno visualizzati correttamente.

## **Render Office Add-Ins durante la conversione di Excel in PDF**

Il seguente esempio di codice salva il [file Excel di esempio](60489769.xlsx) che contiene gli componenti aggiuntivi di Office. Si prega di vedere il [PDF in output generato con la versione precedente, cioè 17.11](60489770.pdf) e il [PDF in output generato con la versione più recente, cioè 17.12 e successive](60489771.pdf). Il PDF della versione precedente è vuoto, mentre quello della versione più recente mostra l'Add-In di Office.

## **Codice di Esempio**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
