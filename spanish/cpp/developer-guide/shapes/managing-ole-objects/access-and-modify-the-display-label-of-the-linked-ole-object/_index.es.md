---
title: Acceder y modificar la etiqueta de visualización del objeto Ole vinculado con C++
linktitle: Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado
type: docs
weight: 100
url: /es/cpp/access-and-modify-the-display-label-of-the-linked-ole-object/
description: Aprenda cómo acceder y modificar la etiqueta de visualización de los objetos Ole vinculados en archivos de Excel usando Aspose.Cells for C++.
---

## **Escenarios de uso posibles**

Microsoft Excel le permite cambiar la etiqueta de visualización del objeto Ole como se muestra en la siguiente captura de pantalla. También puede acceder o modificar la etiqueta de visualización del objeto Ole usando las API de Aspose.Cells con los métodos [**GetLabel()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getlabel/) y [**SetLabel(const U16String\& value)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/setlabel/).

![todo:image_alt_text](access-and-modify-the-display-label-of-the-linked-ole-object_1.png)

## **Acceder y Modificar la Etiqueta de Visualización del Objeto Ole Vinculado**

Consulte el siguiente código de ejemplo, carga el [archivo de Excel de ejemplo](64716810.xlsx) que contiene el Objeto Ole. El código accede al Objeto Ole y cambia su Etiqueta de Muestra de APIs de Muestra a APIs de Aspose. Consulte la salida de consola que se muestra a continuación que muestra el efecto del código de ejemplo en el archivo de Excel de ejemplo como referencia.

## **Código de muestra**

```cpp
#include <iostream>
#include <memory>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Load the sample Excel file
    U16String inputFilePath = u"sampleAccessAndModifyLabelOfOleObject.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    OleObject oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object
    std::cout << "Ole Object Label - Before: " << oleObject.GetLabel().ToUtf8() << std::endl;

    // Modify the Label of the Ole Object
    oleObject.SetLabel(u"Aspose APIs");

    // Save workbook to memory stream
    auto ms = wb.SaveToStream();

    // Set the workbook reference to null
    wb = Workbook();

    // Load workbook from memory stream
    wb = Workbook(ms);

    // Access first worksheet
    ws = wb.GetWorksheets().Get(0);

    // Access first Ole Object
    oleObject = ws.GetOleObjects().Get(0);

    // Display the Label of the Ole Object that has been modified earlier
    std::cout << "Ole Object Label - After: " << oleObject.GetLabel().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Salida de la consola**

{{< highlight java >}}

Ole Object Label - Before: Sample APIs

Ole Object Label - After: Aspose APIs

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
