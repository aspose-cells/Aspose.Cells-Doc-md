---
title: Imposta il colore della scheda del foglio con C++
linktitle: Impostare il Colore della Scheda del Foglio di Lavoro
type: docs
weight: 120
url: /it/cpp/set-worksheet-tab-color/
description: Questo articolo dimostra un esempio di codice che imposta il colore della scheda del foglio Excel programmaticamente utilizzando l API o la libreria C++.
keywords: imposta il colore della scheda Excel c++, codice per impostare il colore della scheda Excel c++
---

{{% alert color="primary" %}}

Aspose.Cells consente di cambiare il colore delle singole schede del foglio di lavoro per renderle evidenti rispetto alle altre. Ad esempio, è possibile rendere Rosso le Spese, Verde le Vendite, Blu i Beni, ecc.

{{% /alert %}}

## **Impostare il Colore della Scheda del Foglio di Lavoro con Microsoft Excel**
1. Fare clic con il pulsante destro del mouse su una scheda nell'insieme di schede nella parte inferiore della scheda corrente.
1. Seleziona **Colore scheda**.
1. Seleziona un colore dalla tavolozza.
1. Fai clic su **OK**.

## **Impostazione colore scheda foglio di calcolo con Aspose.Cells**
Il codice di esempio di seguito mostra come impostare il colore della scheda con Aspose.Cells.

```cpp
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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
