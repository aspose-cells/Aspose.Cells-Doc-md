---
title: Determinar si el tamaño del papel de la hoja de cálculo es automático con C++
linktitle: Determinar si el Tamaño de Papel de la Hoja de Cálculo es Automático
type: docs
weight: 90
url: /es/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Este artículo explica cómo usar la API o código de muestra de la biblioteca C++ para determinar si el tamaño de papel de la hoja de trabajo es automático.
keywords: determinar si el tamaño del papel de la hoja de trabajo es automático c++
---

## **Escenarios de uso posibles**

 La mayoría de las veces, el tamaño del papel de la hoja de trabajo es automático. Cuando es automático, a menudo se establece como *Carta*. Algunas veces, el usuario configura el tamaño del papel según sus requisitos. En este caso, el tamaño del papel no es automático. Puedes verificar si el tamaño del papel de la hoja de trabajo es automático o no usando la propiedad [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) de la clase **Worksheet**.

## **Determinar si el tamaño de papel de la hoja de cálculo es automático**

El código de muestra proporcionado a continuación carga los dos siguientes archivos de Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

 y encuentra si el tamaño del papel de su primera hoja de trabajo es automático o no. En Microsoft Excel, puedes verificar si el tamaño del papel es automático o no a través de la ventana Configuración de Página como muestra esta captura de pantalla.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**

Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con los archivos de Excel de muestra proporcionados.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
