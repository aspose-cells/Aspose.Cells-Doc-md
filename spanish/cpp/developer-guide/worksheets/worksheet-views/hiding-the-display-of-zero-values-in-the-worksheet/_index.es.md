---
title: ocultar la visualización de valores cero en la hoja de cálculo con C++
linktitle: Ocultar la visualización de los valores cero en la hoja de cálculo
type: docs
weight: 50
url: /es/cpp/hiding-the-display-of-zero-values-in-the-worksheet/
description: Este artículo te mostrará un código ejemplo que explica cómo ocultar programáticamente los valores cero en una hoja de cálculo Excel usando la biblioteca o API en C++.
keywords: ocultar valores cero en hoja de excel en C++
---

{{% alert color="primary" %}} 

A veces, es necesario ocultar los valores cero en una hoja de cálculo. Puede ser una preferencia personal o un estándar de formato.

{{% /alert %}} 

Para ocultar los valores cero en una hoja de cálculo en Microsoft Excel (por ejemplo, Microsoft Excel 2003):

1. Desde el menú **Herramientas**, seleccione **Opciones**, y luego seleccione la pestaña **Ver**.
1. Desmarque la opción **Valores de cero**.
1. Haz clic en **Aceptar**.

Consulte el siguiente código de ejemplo que demuestra cómo ocultar los ceros usando Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    //Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    //Path of input excel file
    U16String inputFilePath = srcDir + u"book1.xlsx";

    // Create a new Workbook object
    Workbook workbook(inputFilePath);

    // Get First worksheet of the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Hide the zero values in the sheet
    sheet.SetDisplayZeros(false);

    // Save the workbook
    workbook.Save(srcDir + u"outputfile.out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
