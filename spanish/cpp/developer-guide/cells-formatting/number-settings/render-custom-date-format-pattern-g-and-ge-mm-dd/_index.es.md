---
title: Renderizar patrón de formato de fecha personalizado g y ge mm dd con C++
description: Aspose.Cells es una librería en C++ para trabajar con archivos de hojas de cálculo que soporta renderizar fechas usando patrones de formato de fecha personalizados g y ge . Este artículo describirá cómo renderizar estos patrones de formato de fecha personalizado usando la librería Aspose.Cells para que los usuarios puedan controlar cómo se muestran las fechas si así lo desean.
keywords: Aspose.Cells, librería C++, hoja de cálculo electrónica, formato de fecha personalizado, renderizado, patrón g , patrón ge , control de visualización
type: docs
weight: 160
url: /es/cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/
---

{{% alert color="primary" %}}

Ahora Aspose.Cells puede representar los patrones de formato de fecha personalizados como g, ge.mm.dd y similares. Consulte el archivo de Excel adjunto [5112361.xlsx] y el PDF convertido [5112360.pdf] por Aspose.Cells para su referencia.

{{% /alert %}}

El siguiente código de ejemplo convierte el [archivo de Excel fuente](5112361.xlsx) que contiene valores de fecha con patrones de formato personalizados como g y ge.mm.dd en un [PDF de salida](5112360.pdf).

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook from an existing Excel file
    U16String inputFilePath = srcDir + u"SourceFile.xlsx";
    Workbook workbook(inputFilePath);

    // Save the Excel file as PDF
    workbook.Save(outDir + u"CustomDateFormat_out.pdf");

    std::cout << "File saved successfully as PDF!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
