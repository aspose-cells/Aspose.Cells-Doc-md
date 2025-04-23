---
title: Copiar configuraciones de la configuración de página desde la hoja de origen a la hoja de destino con C++
linktitle: Copiar configuraciones de la configuración de página
type: docs
weight: 80
url: /es/cpp/copy-page-setup-settings-from-source-worksheet-into-destination-worksheet/
description: Este artículo explica cómo usar la API o código de ejemplo de la biblioteca en C++ para copiar configuraciones de la configuración de página desde la hoja de origen a la hoja de destino programáticamente.
keywords: copiar configuraciones de la configuración de página en C++, copiar configuraciones de la página en la hoja objetivo en C++
---

## **Escenarios de uso posibles**

Cuando agregas una nueva hoja a un libro de trabajo, contiene las configuraciones de la *Configuración de Página* predeterminadas. Puede haber momentos en los que necesites transferir las configuraciones ([**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/)) de una hoja de cálculo a otra. Este documento explica cómo copiar las configuraciones de la Configuración de Página de una hoja a otra utilizando las APIs de Aspose.Cells.

## **Copiar Configuraciones de Configuración de Página de la Hoja de Cálculo de Origen en la Hoja de Cálculo de Destino**

El siguiente código de ejemplo ilustra cómo copiar las *Configuraciones de Configuración de Página* de una hoja a otra utilizando el método [**PageSetup.Copy()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/copy/). Por favor, consulta el siguiente código de ejemplo y su salida en consola para una referencia.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    Workbook wb;

    wb.GetWorksheets().Add(u"TestSheet1");
    wb.GetWorksheets().Add(u"TestSheet2");

    Worksheet TestSheet1 = wb.GetWorksheets().Get(u"TestSheet1");
    Worksheet TestSheet2 = wb.GetWorksheets().Get(u"TestSheet2");

    TestSheet1.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3ExtraTransverse);

    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "Before Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    CopyOptions copyOptions;
    TestSheet2.GetPageSetup().Copy(TestSheet1.GetPageSetup(), copyOptions);

    std::cout << "After Paper Size: " << static_cast<int>(TestSheet1.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << "After Paper Size: " << static_cast<int>(TestSheet2.GetPageSetup().GetPaperSize()) << std::endl;
    std::cout << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**

{{< highlight java >}}

Before Paper Size: PaperA3ExtraTransverse

Before Paper Size: PaperLetter

After Paper Size: PaperA3ExtraTransverse

After Paper Size: PaperA3ExtraTransverse

{{< /highlight >}}
