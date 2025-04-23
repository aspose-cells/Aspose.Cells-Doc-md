---
title: Rilascia risorse non gestite del libro di lavoro con C++
linktitle: Rilascia le risorse non gestite del libro di lavoro
type: docs
weight: 310
url: /it/cpp/release-unmanaged-resources-of-the-workbook/
description: Impara come rilasciare le risorse non gestite del libro di lavoro usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce il metodo [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) per rilasciare le risorse non gestite dell'oggetto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). Il modello di smaltimento viene utilizzato solo per gli oggetti che accedono a risorse non gestite, come gestori di file e di pipe, gestori di registro, gestori di attesa o puntatori a blocchi di memoria non gestita. Questo perché il garbage collector è molto efficiente nel recuperare gli oggetti gestiti inutilizzati, ma non è in grado di recuperare gli oggetti non gestiti.

{{% /alert %}}

 L'oggetto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) ora implementa l'interfaccia *IDisposable* che ha un singolo metodo [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/). Puoi chiamare direttamente il metodo [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) oppure usare l'istruzione *Using* per chiamare automaticamente questo metodo.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook object
    Workbook wb1;

    // Call Dispose method
    wb1.Dispose();

    // Call Dispose method via RAII (Resource Acquisition Is Initialization)
    {
        Workbook wb2;
        // Any other code goes here
    } // wb2 is automatically disposed when it goes out of scope

    Aspose::Cells::Cleanup();
}
```
