---
title: Actualizar automáticamente el objeto OLE mediante Microsoft Excel con C++
linktitle: Actualizar automáticamente el objeto OLE
type: docs
weight: 270
url: /es/cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Aprende cómo actualizar automáticamente los objetos OLE en Microsoft Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la propiedad [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getautoload/) para actualizar el objeto OLE cuando se abre el archivo de Excel en Microsoft Excel. Debido a esta propiedad, el objeto OLE mostrará la imagen OLE correcta generada por Microsoft Excel.

{{% /alert %}}

El siguiente código de ejemplo carga el [archivo de Excel de ejemplo](5115231.xlsx) que tiene una imagen OLE no real. El objeto OLE es en realidad un documento de Microsoft Word, pero el archivo de Excel de muestra muestra la imagen del animal en lugar de la imagen de Microsoft Word. Sin embargo, si abres el [archivo de Excel de salida](5115225.xlsx), verás que Microsoft Excel muestra la imagen OLE correcta.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Create workbook object from your sample excel file
    Workbook wb(srcDir + u"sample.xlsx");

    // Access first worksheet
    Worksheet sheet = wb.GetWorksheets().Get(0);

    // Set auto load property of first ole object to true
    sheet.GetOleObjects().Get(0).SetAutoLoad(true);

    // Save the workbook in xlsx format
    wb.Save(srcDir + u"RefreshOLEObjects_out.xlsx", SaveFormat::Xlsx);

    std::cout << "OLE object refreshed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
