---
title: Extraer datos del tema del archivo de Excel con C++
linktitle: Extraer datos de tema de archivo de Excel
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo. Soporta la extracción de datos de tema de archivos de Excel, permitiendo a los usuarios obtener la información de estilo y formato de los documentos. Este artículo introducirá cómo extraer datos de tema de archivos de Excel usando Aspose.Cells.
keywords: Aspose.Cells, Archivo de Excel, Datos de tema, Estilo, Formato
type: docs
weight: 120
url: /es/cpp/extract-theme-data-from-excel-file/
---

{{% alert color="primary" %}}

Aspose.Cells permite a los usuarios extraer datos relacionados con temas de un archivo de Excel. Por ejemplo, puedes extraer el nombre del tema aplicado al libro y el color del tema aplicado a una celda o a los bordes de la celda, etc.

Puedes aplicar un tema a tu libro usando Microsoft Excel a través del comando Diseño de página > Temas.

{{% /alert %}}

## Código C++ para extraer datos de tema de un archivo de Excel

El siguiente ejemplo de código extrae el nombre del tema aplicado al libro fuente y luego extrae el color del tema aplicado a la celda A1 y el color del tema aplicado al borde inferior de la celda.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object
    Workbook workbook(srcDir + u"source.xlsx");

    // Extract theme name applied to this workbook
    std::cout << "Theme: " << workbook.GetTheme().ToUtf8() << std::endl;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Get the style object
    Style style = cell.GetStyle();

    // Check if theme has foreground color defined
    if (style.GetForegroundThemeColor().IsNull())
    {
        std::cout << "Theme has not foreground color defined." << std::endl;
    }
    else
    {
        // Extract theme color applied to this cell
        std::cout << "Foreground Theme Color Type: " << static_cast<int>(style.GetForegroundThemeColor().GetColorType()) << std::endl;
    }

    // Extract theme color applied to the bottom border of the cell
    Border bot = style.GetBorders().Get(BorderType::BottomBorder);
    if (bot.GetThemeColor().IsNull())
    {
        std::cout << "Theme has not Border color defined." << std::endl;
    }
    else
    {
        std::cout << "Border Theme Color Type: " << static_cast<int>(bot.GetThemeColor().GetColorType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
