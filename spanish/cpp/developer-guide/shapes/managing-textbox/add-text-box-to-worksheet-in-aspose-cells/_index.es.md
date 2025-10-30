---
title: Cómo agregar/insertar un cuadro de texto en la hoja de cálculo con C++
linktitle: Agregar cuadro de texto a la hoja de cálculo
type: docs
weight: 10
url: /es/cpp/add-text-box-to-worksheet-in-aspose-cells/
description: Cómo agregar/insertar un cuadro de texto en la hoja de cálculo en Aspose.Cells con C++.
keywords: Agregar/insertar cuadro de texto en la hoja de cálculo de Excel Aspose
---

## Agregar cuadro de texto a la hoja de cálculo en Excel

En el programa de Excel (versión 07 y superior), hay dos lugares donde puede insertar cuadros de texto. Uno en "insertar-formas", el otro en la parte derecha del menú superior de la opción "Insertar".

### Método Uno:

![1](1.png)

### Método Dos:

![2](2.png)

## Cómo Crear

Puedes crear cuadros de texto con texto horizontal o vertical.

- Seleccione la opción correspondiente (horizontal o vertical)
- Haz clic izquierdo en la página
- Mantén presionado el botón izquierdo y arrastra una distancia en la página
- Suelta el botón izquierdo

Ahora tienes un cuadro de texto.

## Agregar cuadro de texto a la hoja de cálculo en Aspose.Cells

Cuando necesite insertar en bloque TextBox en la hoja de cálculo, el método manual de inserción es claramente un desastre. Si esto le molesta, creo que este documento le ayudará. [Aspose.Cells](https://products.aspose.com/cells/) le proporciona una API para realizar inserciones masivas fácilmente en su código.

El siguiente código de ejemplo crea un cuadro de texto.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create an object of the Workbook class
    Workbook workbook;

    // Access first worksheet from the collection
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Add the TextBox to the worksheet
    sheet.GetTextBoxes().Add(6, 10, 100, 200);

    // Save the workbook with the text box
    workbook.Save(outDir + u"result.xlsx", SaveFormat::Xlsx);

    std::cout << "Text box added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Obtendrás un archivo similar a [archivo resultante](result.xlsx). En el archivo, verás lo siguiente:

![](52449.png)
{{< app/cells/assistant language="cpp" >}}
