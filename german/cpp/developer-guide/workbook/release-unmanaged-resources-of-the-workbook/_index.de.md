---
title: Freigabe unmanaged Ressourcen der Arbeitsmappe mit C++
linktitle: Freigeben unbeaufsichtigter Ressourcen der Arbeitsmappe
type: docs
weight: 310
url: /de/cpp/release-unmanaged-resources-of-the-workbook/
description: Erfahren Sie, wie Sie unmanaged Ressourcen der Arbeitsmappe mit Aspose.Cells und C++ freigeben.
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Methode [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) zur Freigabe der nicht verwalteten Ressourcen des Objekts [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) an. Das Freigabemuster wird nur für Objekte verwendet, die auf nicht verwaltete Ressourcen zugreifen, wie Datei- und Pipe-Handles, Registrierungshandles, Wartehandles oder Zeiger auf Blöcke nicht verwalteten Speichers. Dies liegt daran, dass der Garbage-Collector sehr effizient beim Freigeben nicht verwendeter verwalteter Objekte ist, aber nicht verwaltete Objekte nicht freigeben kann.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) Objekt implementiert jetzt die *IDisposable* Schnittstelle, die eine einzelne Methode [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) hat. Sie können entweder direkt die [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) Methode aufrufen oder die *Using* Anweisung verwenden, um diese Methode automatisch aufzurufen.

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
{{< app/cells/assistant language="cpp" >}}
