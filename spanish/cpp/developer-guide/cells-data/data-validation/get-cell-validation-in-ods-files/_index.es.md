---
title: Obtener validación de celdas en archivos ODS con C++
linktitle: Obtener validación de celda en archivos ODS
type: docs
weight: 180
url: /es/cpp/get-cell-validation-in-ods-files/
description: Aprende cómo obtener la validación de celdas en archivos ODS usando Aspose.Cells for C++.
keywords: Obtener Validación de Celda, Obtener Validación de Celda 
---

## **Obtener validación de celda en archivos ODS**

Con Aspose.Cells for C++, puedes obtener la validación aplicada a una celda en archivos ODS. La API proporciona el método [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) de la clase [**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/).

El siguiente ejemplo de código demuestra cómo usar el método [**GetValidation**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getvalidation/) cargando el archivo [source ODS](101089354.ods) y leyendo la validación de la celda A9.

### **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load source Excel file
    U16String inputFilePath = srcDir + u"SampleBook1.ods";
    Workbook workbook(inputFilePath);

    // Access first worksheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);

    // Access cell A9
    Cells cells = worksheet.GetCells();
    Cell cell = cells.Get(U16String(u"A9"));

    // Check validation existence
    Validation validation = cell.GetValidation();
    if (validation.IsNull() == false)
    {
        std::cout << "Validation type: " << static_cast<int>(validation.GetType()) << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
