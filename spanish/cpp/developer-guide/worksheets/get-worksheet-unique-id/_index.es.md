---
title: Obtener ID único de la hoja de trabajo con C++
linktitle: Obtener ID único de la hoja de trabajo
type: docs
weight: 190
url: /es/cpp/get-worksheet-unique-id/
description: Este artículo muestra cómo obtener el ID único de la hoja de cálculo de Excel usando la biblioteca y API en C++ de manera programática.
keywords: ID único de la hoja de cálculo de Excel en C++, ID de la hoja en C++
---

## **Obtener ID único de la hoja de trabajo**

Aspose.Cells proporciona la capacidad de obtener el ID único de una hoja de cálculo usando el método [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/). El siguiente fragmento de código demuestra el uso del método [**GetUniqueId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getuniqueid/) para imprimir el ID único de una hoja de cálculo. El siguiente fragmento de código usa este [archivo de Excel de ejemplo](105480213.xlsx).

### Código Fuente

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    Workbook workbook(srcDir + u"Book1.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Print Unique Id
    std::cout << "Unique Id: " << worksheet.GetUniqueId().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
