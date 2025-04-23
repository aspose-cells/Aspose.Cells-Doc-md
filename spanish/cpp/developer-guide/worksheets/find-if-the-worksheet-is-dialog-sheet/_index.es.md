---
title: Encontrar si la hoja de trabajo es una hoja de diálogo con C++
linktitle: Encontrar si la hoja de cálculo es una hoja de diálogo
type: docs
weight: 90
url: /es/cpp/find-if-the-worksheet-is-dialog-sheet/
description: La hoja de diálogo es un formato antiguo de hoja. Este artículo proporciona instrucciones y código de ejemplo para determinar automáticamente si una hoja de trabajo de Excel es una hoja de diálogo usando la API de C++.
keywords: Encontrar tipo de diálogo de hoja de Excel en C++, diálogo de hoja en C++
---

## **Escenarios de uso posibles**

La hoja de diálogo es un formato antiguo de hoja que contiene un cuadro de diálogo. Tal hoja podría ser insertada por una versión anterior de Microsoft Excel, por ejemplo, 2003, como se muestra en esta captura de pantalla. También se puede insertar con VBA en versiones más nuevas, por ejemplo, Microsoft Excel 2016.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Puedes determinar si la hoja es una hoja de diálogo u otro tipo de hoja con la propiedad [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) proporcionada por Aspose.Cells. Si devuelve el valor de enumeración [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/), entonces estás tratando con una hoja de diálogo.

## **Buscar si la hoja de trabajo es una hoja de diálogo**

El siguiente código de ejemplo carga el [archivo de Excel de muestra](64716820.xlsx) que contiene una hoja de diálogo. Verifica la propiedad [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) en comparación con [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) y luego imprime el mensaje. Por favor, consulta la salida de consola del código de ejemplo a continuación para más ayuda.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Salida de la consola**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
