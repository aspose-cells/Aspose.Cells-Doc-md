---
title: Especifique cómo cruzar la cadena en el PDF de salida y en la imagen con C++
linktitle: Especificar cómo cruzar cadenas en PDF de salida e imagen
type: docs
weight: 120
url: /es/cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Aprenda cómo controlar el desbordamiento de texto en salidas PDF y de imagen usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Cuando una celda contiene texto o cadena más grande que el ancho de la celda, la cadena desborda si la siguiente celda en la siguiente columna está nula o vacía. Cuando guarda su archivo de Excel en formato PDF o Imagen, puede controlar este desbordamiento especificando el tipo de cruce usando la enumeración [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). Tiene los siguientes valores:

- **TextCrossType.Default**: Mostrar texto como MS Excel, que depende de la siguiente celda. Si la siguiente celda es nula, la cadena se cruzará o será truncada.

- **TextCrossType.CrossKeep**: Mostrar la cadena como MS Excel exportando a PDF/Imagen.

- **TextCrossType.CrossOverride**: Mostrar todo el texto cruzando otras celdas y sobrescribir el texto de las celdas cruzadas.

- **TextCrossType.StrictInCell**: Solo muestra la cadena dentro del ancho de la celda.

## **Especifica cómo cruzar la cadena en el PDF/Imagen de salida utilizando TextCrossType**

El siguiente código de ejemplo carga el archivo de Excel de muestra y lo guarda en formato PDF/Imagen especificando diferentes [**TextCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/textcrosstype/). El archivo de Excel de muestra y los archivos de salida se pueden descargar desde los siguientes enlaces:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Código de Ejemplo

```c++
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Rendering;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load template Excel file
    Workbook wb(srcDir + u"sampleCrosssType.xlsx");

    // Initialize PDF save options
    PdfSaveOptions pdfSaveOptions;
    pdfSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Save PDF file
    wb.Save(outDir + u"outputCrosssType.pdf", pdfSaveOptions);

    // Initialize image or print options
    ImageOrPrintOptions imageSaveOptions;
    imageSaveOptions.SetTextCrossType(TextCrossType::StrictInCell);

    // Initialize sheet renderer object
    SheetRender sheetRenderer(wb.GetWorksheets().Get(0), imageSaveOptions);

    // Save PNG image
    sheetRenderer.ToImage(0, outDir + u"outputCrosssType.png");

    Aspose::Cells::Cleanup();
}
```
