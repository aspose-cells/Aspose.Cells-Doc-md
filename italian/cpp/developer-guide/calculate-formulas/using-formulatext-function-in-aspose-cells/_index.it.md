---
title: Utilizzo della funzione FormulaText in Aspose.Cells con C++
linktitle: Uso della funzione FormulaText
description: Questo articolo presenta come utilizzare la funzione FormulaText nella libreria Aspose.Cells per elaborare formule in Microsoft Excel. Caricando un file Excel esistente o creandone uno nuovo, possiamo utilizzare il metodo fornito da Aspose.Cells per ottenere e impostare il testo della formula della cella e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, funzioni FormulaText
type: docs
weight: 60
url: /it/cpp/using-formulatext-function-in-aspose-cells/
---

{{% alert color="primary" %}} 

FormulaText è una funzione di Excel 2013 e versioni successive. Non è supportata dalle versioni precedenti come Excel 2010 o 2007, ecc. Come suggerisce il suo nome, stampa il testo della formula presente in una determinata cella. Questo articolo mostrerà come utilizzare questa funzione utilizzando Aspose.Cells.

{{% /alert %}} 

Il seguente codice di esempio mostra l'uso di FormulaText con Aspose.Cells. Il codice scrive prima una formula nella cella A1 e poi stampa il testo della formula utilizzando FormulaText nella cella A2.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some formula in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.SetFormula(u"=Sum(B1:B10)");

    // Get the text of the formula in cell A2 using FORMULATEXT function
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.SetFormula(u"=FormulaText(A1)");

    // Calculate the workbook
    workbook.CalculateFormula();

    // Print the results of A2, It will now print the text of the formula inside cell A1
    std::cout << cellA2.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Output della console**
Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

 =SUM(B1:B10)

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
