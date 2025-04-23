---
title: Dibuja la Línea de Tiempo al renderizar Excel a PDF con C++
linktitle: Dibujar línea de tiempo al renderizar Excel a PDF
type: docs
weight: 60
url: /es/cpp/draw-timeline-while-rendering-excel-to-pdf/
description: Gestiona cronogramas de archivos de Excel con Aspose.Cells con C++.
keywords: Renderización de línea de tiempo a PDF sin Office 2013, Office 2016, Office 2019 y Office 365
---

## **Dibuje una línea de tiempo mientras renderiza Excel a PDF**
Si tienes un archivo de Excel con una línea de tiempo aplicada y quieres exportar el Excel a PDF con la configuración de línea de tiempo, Aspose.Cells ahora admite esto por defecto. Solo exporta el archivo de Excel con línea de tiempo a PDF y el PDF generado mostrará la línea de tiempo aplicada.

El siguiente código de muestra carga el [archivo Excel de muestra](input.xlsx) que contiene una línea de tiempo existente. Luego guarda el libro de trabajo como [archivo PDF de salida](out.pdf). La siguiente captura de pantalla compara el archivo Excel fuente y el archivo PDF generado.

<img src="out.png" width="60%">

## **Código de muestra**
```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file
    U16String inputFilePath(u"input.xlsx");
    std::unique_ptr<Workbook> wb = std::make_unique<Workbook>(inputFilePath);

    // Save file to pdf
    U16String outputFilePath(u"out.pdf");
    wb->Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "Workbook saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <aspose.cells.h>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();
    // Load the sample Excel file
    Workbook workbook(u"input.xlsx");

    // Save the workbook as a PDF file
    workbook.Save(u"output.pdf", SaveFormat::Pdf);
    Aspose::Cells::Cleanup();
    return 0;

}
```

