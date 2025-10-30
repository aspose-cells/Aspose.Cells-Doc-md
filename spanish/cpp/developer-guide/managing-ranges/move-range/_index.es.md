---
title: Mover rango de celdas en una hoja de trabajo con C++
linktitle: Mover rango de celdas en una hoja de cálculo
type: docs
weight: 370
url: /es/cpp/move-range-of-cells-in-a-worksheet/
description: Aprende cómo mover un rango de celdas en una hoja de trabajo usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Este artículo muestra cómo mover un rango de celdas en una hoja de cálculo.

{{% /alert %}}

## **Mover rango de celdas en una hoja de cálculo**
El código de ejemplo utiliza un archivo de plantilla para demostrar la tarea.

**El archivo de entrada**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_1.png)

Por favor, vea el siguiente archivo generado con el rango A1:B5 movido a C1:D5.

**El archivo de salida**

![todo:image_alt_text](move-range-of-cells-in-a-worksheet_2.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate the workbook object. Open the Excel file
    U16String inputFilePath = u"book1.xlsx";
    Workbook workbook(inputFilePath);

    // Access the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Create a range from A1 to B5
    Range range = cells.CreateRange(u"A1", u"B5");

    // Move the range to the right by 2 columns
    range.MoveTo(0, 2);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
