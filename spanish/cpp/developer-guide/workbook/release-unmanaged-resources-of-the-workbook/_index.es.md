---
title: Liberar recursos no administrados del libro con C++
linktitle: Liberar recursos no administrados del libro
type: docs
weight: 310
url: /es/cpp/release-unmanaged-resources-of-the-workbook/
description: Aprende cómo liberar recursos no administrados del libro usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona el método [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) para liberar los recursos no administrados del objeto [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/). El patrón de eliminación se utiliza solo para objetos que acceden a recursos no administrados, como manejadores de archivos y tuberías, manejadores de registro, manejadores de espera o punteros a bloques de memoria no administrada. Esto se debe a que el recolector de basura es muy eficiente al reclamar objetos administrados no utilizados, pero no puede reclamar objetos no administrados.

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) objeto ahora implementa la interfaz *IDisposable* que tiene un método único [**Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/). Puedes llamar directamente al método [**Workbook.Dispose()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/dispose/) o puedes usar la instrucción *Using* para llamar a este método automáticamente.

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
