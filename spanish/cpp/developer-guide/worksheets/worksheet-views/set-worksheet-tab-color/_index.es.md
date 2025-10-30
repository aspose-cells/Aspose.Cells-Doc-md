---
title: Establecer color de pestaña de hoja de cálculo con C++
linktitle: Establecer el color de la pestaña de la hoja de cálculo
type: docs
weight: 120
url: /es/cpp/set-worksheet-tab-color/
description: Este artículo demuestra código de ejemplo que establece el color de la pestaña de la hoja de Excel programáticamente usando la API o Biblioteca en C++.
keywords: establecer color de pestaña de Excel en C++, código para establecer color de pestaña de Excel en C++
---

{{% alert color="primary" %}}

Aspose.Cells te permite cambiar el color de las pestañas individuales de las hojas de cálculo para hacerlas más destacadas. Por ejemplo, puedes hacer que Gastos sean rojos, Ventas verdes, Activos azules, etc.

{{% /alert %}}

## **Establecer el color de la pestaña de la hoja de cálculo con Microsoft Excel**
1. Haz clic derecho en una pestaña en la hoja de pestañas en la parte inferior de la hoja de cálculo actual.
1. Seleccione **Color de pestaña**.
1. Selecciona un color de la paleta.
1. Haz clic en **Aceptar**.

## **Configurar el color de la pestaña de la hoja de cálculo con Aspose.Cells**
El código de ejemplo a continuación muestra cómo configurar el color de la pestaña con Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
