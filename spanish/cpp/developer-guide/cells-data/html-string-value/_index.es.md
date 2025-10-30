---
title: Añadir Texto Enriquecido HTML dentro de la Celda con C++
linktitle: Valor de cadena HTML
type: docs
weight: 50
url: /es/cpp/adding-html-rich-text-inside-the-cell/
description: Aprende cómo agregar texto enriquecido HTML en la celda a través de la API Aspose.Cells for C++.
keywords: Agregar texto enriquecido HTML dentro de la celda, Definir texto enriquecido HTML dentro de la celda, Agregar texto enriquecido HTML en la celda
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de HTML orientado a Microsoft Excel a formato XLS/XLSX. Esto significa que el HTML generado por Microsoft Excel se puede convertir de nuevo al formato XLS/XLSX utilizando Aspose.Cells.

De manera similar, si hay HTML simple, Aspose.Cells puede convertirlo en HTML Rich Text. Aspose.Cells proporciona el método [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/) que puede tomar tal HTML simple y convertirlo en texto de celda formateado.

{{% /alert %}}

El siguiente ejemplo de código le muestra cómo agregar texto enriquecido HTML dentro de la celda. Por favor vea la captura de pantalla del archivo de Excel de salida.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Artículos relacionados

- [Mostrar Viñetas al Establecer el Valor de la Celda usando HTML](/cells/es/cpp/display-bullets-by-setting-cell-value-using/)
- [Obtener cadena HTML5 de la Celda](/cells/es/cpp/get-html5-string-from-cell/)
{{< app/cells/assistant language="cpp" >}}
