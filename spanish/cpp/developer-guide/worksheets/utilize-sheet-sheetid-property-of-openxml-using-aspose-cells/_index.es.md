---
title: Utilice la propiedad Sheet.SheetId de OpenXml con C++
linktitle: Utilice la propiedad Sheet.SheetId de OpenXml
type: docs
weight: 200
url: /es/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Este artículo muestra cómo utilizar la propiedad Sheet.SheetId de OpenXml mediante la API o Biblioteca de manipulación de Excel en C++ de forma programática.
keywords: propiedad de id de hoja de OpenXml en C++, hoja de trabajo de Excel en C++
---

## **Escenarios de uso posibles**

La propiedad *Sheet.SheetId* se encuentra dentro del espacio de nombres *DocumentFormat.OpenXml.Spreadsheet* y forma parte de OpenXml. Puede ver esta propiedad y su valor dentro de *workbook.xml* como se muestra en la captura de pantalla siguiente. Aspose.Cells proporciona la propiedad equivalente como [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/).

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Utilizar la propiedad SheetId de OpenXml usando Aspose.Cells**

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](51740716.xlsx), lee su Id de hoja o pestaña, luego le asigna un nuevo Id de pestaña y lo guarda como [archivo de Excel de salida](51740717.xlsx). También consulte la salida de consola del código que se muestra a continuación como referencia.

## **Código de muestra**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Salida de la consola**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
