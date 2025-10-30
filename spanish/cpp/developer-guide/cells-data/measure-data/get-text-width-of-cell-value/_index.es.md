---
title: Obtener el Ancho del Texto del Valor de la Celda con C++
linktitle: Obtener Ancho de Texto del Valor de la Celda
type: docs
weight: 50
url: /es/cpp/get-text-width-of-cell-value/
description: Aprende cómo obtener el ancho del texto del valor de la celda a través de la API Aspose.Cells for C++.
keywords: Obtener el ancho del texto del valor de la celda, obtener el ancho del texto del valor de la celda
---

## **Obtener Ancho de Texto del Valor de la Celda**

A veces, los desarrolladores pueden necesitar calcular el ancho del valor de la celda para organizar datos en algún diseño. Aspose.Cells proporciona el método [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) que permite a los desarrolladores obtener el ancho del texto del valor de la celda. El siguiente código de ejemplo ilustra cómo usar [**CellsHelper::GetTextWidth**](https://reference.aspose.com/cells/cpp/aspose.cells/cellshelper/gettextwidth/) para acceder al ancho del texto del valor de la celda.

El archivo de origen usado en el siguiente fragmento de código está adjunto para su referencia.

[Archivo fuente](96928090.xlsx)

## Código de Muestra

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Directory path for source files
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook from the specified Excel file
    Workbook workbook(sourceDir + u"GetTextWidthSample.xlsx");

    // Calculate the text width for the string value of cell A1
    double textWidth = CellsHelper::GetTextWidth(workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").GetStringValue(), workbook.GetDefaultStyle().GetFont(), 1);

    // Output the text width
    std::wcout << u"Text width: " << textWidth << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
