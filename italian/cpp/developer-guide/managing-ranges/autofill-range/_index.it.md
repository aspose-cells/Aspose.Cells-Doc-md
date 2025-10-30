---
title: AutoFill del Range di un file Excel con C++
linktitle: Intervallo di riempimento automatico
type: docs
weight: 105
url: /it/cpp/autofill-ranges/
description: Impara come eseguire un operazione di riempimento automatico in un intervallo specificato di un file Excel usando Aspose.Cells con C++.
---

## **Esegui un riempimento automatico nell'intervallo specificato in Excel**

In Excel, seleziona un intervallo, sposta il mouse nell'angolo in basso a destra e trascina il "+" per riempire automaticamente i dati.

## **Auto Fill Ranges con Aspose.Cells**

Il seguente esempio mostra come eseguire un'operazione di AutoFill su un intervallo. Ecco il file di esempio che può essere scaricato per testare questa funzione:

[range_autofill.xlsx](range_autofill.xlsx)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook
    Workbook workbook(u"range_autofill.xlsx");

    // Get Cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create Range
    Range src = cells.CreateRange(u"C3:C4");
    Range dest = cells.CreateRange(u"C5:C10");

    // AutoFill
    src.AutoFill(dest, AutoFillType::Series);

    // Save the Workbook
    workbook.Save(u"range_autofill_result.xlsx");

    std::cout << "Range auto-filled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
