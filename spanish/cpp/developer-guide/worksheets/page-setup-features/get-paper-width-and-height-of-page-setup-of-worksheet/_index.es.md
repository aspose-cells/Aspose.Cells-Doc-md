---
title: Obtener Ancho y Alto del Papel en la Configuración de Página de la hoja de trabajo con C++
linktitle: Obtener Ancho y Alto del Papel en la Configuración de Página
type: docs
weight: 50
url: /es/cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Aprenda cómo obtener el Ancho y Alto del Papel en la Configuración de Página de la Hoja de Excel mediante código C++ de forma programática con la API Aspose.Cells for C++.
keywords: ancho de papel en configuración de página de excel c++, altura de papel en configuración de página de excel c++
---

## **Escenarios de uso posibles**

A veces, necesitas conocer el ancho y la altura del tamaño del papel tal como se ha establecido en la configuración de página de la hoja de trabajo. Utiliza los métodos [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) y [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/) para este propósito.

## **Obtener el ancho y alto del papel del diseño de página de la hoja de cálculo**

 El siguiente código de ejemplo explica el uso de los métodos [**GetPaperWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperwidth/) y [**GetPaperHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getpaperheight/). Primero cambia el tamaño del papel a *A2* y luego encuentra el ancho y la altura del papel, luego lo cambia a *A3*, *A4*, *Carta* y encuentra el ancho y la altura del papel respectivamente.

### **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Create an instance of Workbook class
    Workbook book;

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Set paper size to A2 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA2);
    cout << "PaperA2: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A3 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA3);
    cout << "PaperA3: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to A4 and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperA4);
    cout << "PaperA4: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    // Set paper size to Letter and print paper width and height in inches
    sheet.GetPageSetup().SetPaperSize(PaperSizeType::PaperLetter);
    cout << "PaperLetter: " << sheet.GetPageSetup().GetPaperWidth() << "x" << sheet.GetPageSetup().GetPaperHeight() << endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Salida de la consola**

Aquí está la salida en consola del código de muestra anterior.

{{< highlight java >}}

PaperA2: 16.54x23.39

PaperA3: 11.69x16.54

PaperA4: 8.27x11.69

PaperLetter: 8.5x11

{{< /highlight >}}
