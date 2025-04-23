---
title: Renderizar complementos de Office al convertir Excel a PDF con C++
linktitle: Renderizar complementos de Office al convertir Excel a PDF
type: docs
weight: 100
url: /es/cpp/render-office-add-ins-while-converting-excel-to-pdf/
description: Aprende cómo renderizar complementos de Office al convertir archivos de Excel a PDF usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Anteriormente, Aspose.Cells no podía renderizar complementos de Office cuando un archivo de Excel se guardaba en formato PDF. Ahora, Aspose.Cells lo renderiza correctamente. No necesitas usar ningún método o propiedad especial para renderizar complementos de Office en el PDF de salida. Simplemente guarda tu archivo de Excel en formato PDF y se renderizarán los complementos de Office.

## **Renderizar complementos de Office al convertir Excel a PDF**

El siguiente código de ejemplo guarda el [archivo de Excel de muestra](60489769.xlsx), que contiene los complementos de Office. Por favor, mira el [PDF de salida generado con la versión anterior, es decir, 17.11](60489770.pdf) y el [PDF de salida generado con la versión más reciente, es decir, 17.12 y posteriores](60489771.pdf). La salida de la versión anterior es en blanco, pero la versión más reciente muestra los complementos de Office.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file containing Office Add-Ins
    U16String inputFilePath = u"sampleRenderOfficeAdd-Ins.xlsx";
    Workbook wb(inputFilePath);

    // Save it to Pdf format with version appended to the output filename
    U16String outputFilePath = u"output-" + CellsHelper::GetVersion() + u".pdf";
    wb.Save(outputFilePath, SaveFormat::Pdf);

    std::cout << "File saved successfully: " << outputFilePath.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
