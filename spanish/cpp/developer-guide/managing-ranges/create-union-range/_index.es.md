---
title: Crear rango de unión con C++
linktitle: Crear rango de unión
type: docs
weight: 360
url: /es/cpp/create-union-range/
description: Crear rango de unión en archivos de Excel usando Aspose.Cells con C++.
---

## **Crear rango de unión**
Aspose.Cells proporciona la capacidad de crear un rango de unión usando el método [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). El método [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/) acepta dos parámetros, la dirección para crear el rango de unión y el índice de la hoja de trabajo. El método devuelve un objeto [UnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/unionrange/).

El siguiente fragmento de código demuestra cómo crear un rango de unión usando el método [CreateUnionRange](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/createunionrange/). El archivo de salida generado por el código está adjunto para referencia.

- [Archivo de salida](106364952.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Create union range
    UnionRange unionRange = workbook.GetWorksheets().CreateUnionRange(u"sheet1!A1:A10,sheet1!C1:C10", 0);

    // Put value "ABCD" in the range
    unionRange.SetValue(u"ABCD");

    // Save the output workbook
    workbook.Save(u"CreateUnionRange_out.xlsx");

    std::cout << "Union range created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
