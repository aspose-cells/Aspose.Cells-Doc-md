---
title: Calcolo della funzione IFNA usando Aspose.Cells con C++
linktitle: Calcolo della funzione IFNA
description: Come calcolare le funzioni IFNA usando la libreria Aspose.Cells con C++. Caricando un file Excel esistente o creando un nuovo file Excel, possiamo usare i metodi forniti da Aspose.Cells per calcolare la funzione IFNA e ottenere il risultato. Infine, salviamo il file Excel modificato su disco.
keywords: Aspose.Cells, Excel, funzioni IFNA, calcoli, C++
type: docs
weight: 40
url: /it/cpp/calculating-ifna-function-using-aspose-cells/
---

{{% alert color="primary" %}} 

Aspose.Cells supporta il calcolo della funzione Excel IFNA. La funzione IFNA restituisce il valore specificato se la formula restituisce il valore di errore #N/A; altrimenti restituisce il risultato della formula.

{{% /alert %}} 

## **Calcolare la funzione IFNA utilizzando Aspose.Cells**
Il seguente codice di esempio illustra il calcolo della funzione IFNA tramite Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create new workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Add data for VLOOKUP
    worksheet.GetCells().Get(u"A1").PutValue(u"Apple");
    worksheet.GetCells().Get(u"A2").PutValue(u"Orange");
    worksheet.GetCells().Get(u"A3").PutValue(u"Banana");

    // Access cell A5 and A6
    Cell cellA5 = worksheet.GetCells().Get(u"A5");
    Cell cellA6 = worksheet.GetCells().Get(u"A6");

    // Assign IFNA formula to A5 and A6
    cellA5.SetFormula(u"=IFNA(VLOOKUP(\"Pear\",$A$1:$A$3,1,0),\"Not found\")");
    cellA6.SetFormula(u"=IFNA(VLOOKUP(\"Orange\",$A$1:$A$3,1,0),\"Not found\")");

    // Calculate the formula of workbook
    workbook.CalculateFormula();

    // Print the values of A5 and A6
    std::cout << cellA5.GetStringValue().ToUtf8() << std::endl;
    std::cout << cellA6.GetStringValue().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Output della console**
Ecco l'output della console del codice di esempio sopra.

{{< highlight java >}}

Not found

Orange

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
