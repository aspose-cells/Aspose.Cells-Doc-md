---
title: Obtener conjuntos de iconos, barras de datos o escalas de color utilizados en el formato condicional con C++
linktitle: Obtener conjuntos de iconos, barras de datos o escalas de color
description: Aspose.Cells for C++ es una biblioteca para trabajar con archivos de hojas de cálculo. Soporta el uso de conjuntos de iconos, barras de datos y objetos de escala de color en el formato condicional para mostrar datos de hojas de cálculo. Este artículo describe cómo usar la biblioteca Aspose.Cells para recuperar datos de estos objetos.
keywords: Aspose.Cells, Formato condicional, Conjunto de iconos, Barra de datos, Escala de colores, Hoja de cálculo
type: docs
weight: 10
url: /es/cpp/get-icon-sets-data-bars-or-color-scales-objects-used-in-conditional-formatting/
---

{{% alert color="primary" %}} 

A veces, necesitas recuperar conjuntos de iconos utilizados en el formateo condicional de una celda o un rango de celdas y quieres crear un archivo de imagen basado en ello. Podrías requerir leer las barras de datos o escalas de color usadas en el formateo condicional. Aspose.Cells for C++ soporta esta función.

{{% /alert %}} 

El siguiente ejemplo muestra cómo leer conjuntos de íconos utilizados en formato condicional. Con la API sencilla de Aspose.Cells, los datos de la imagen del conjunto de íconos se guardan como una imagen.

```cpp
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Get the A1 cell
    Cell cell = sheet.GetCells().Get(u"A1");

    // Get the conditional formatting result object
    ConditionalFormattingResult cfr = cell.GetConditionalFormattingResult();

    // Get the icon set
    ConditionalFormattingIcon icon = cfr.GetConditionalFormattingIcon();

    // Get the image data from the icon
    Vector<uint8_t> imageData = icon.GetImageData();

    // Create the image file based on the icon's image data
    ofstream outputFile((outDir + u"imgIcon.out.jpg").ToUtf8(), ios::binary);
    outputFile.write(reinterpret_cast<const char*>(imageData.GetData()), imageData.GetLength());
    outputFile.close();

    std::cout << "Icon image saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
