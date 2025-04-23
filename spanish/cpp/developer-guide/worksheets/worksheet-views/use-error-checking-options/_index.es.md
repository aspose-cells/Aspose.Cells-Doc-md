---
title: Utilizar opciones de comprobación de errores con C++
linktitle: Usar opciones de verificación de errores
type: docs
weight: 140
url: /es/cpp/use-error-checking-options/
description: En este artículo, encontrarás código de ejemplo que usará programáticamente las opciones de verificación de errores de las hojas de cálculo de Excel, por ejemplo, Números almacenados como Texto usando la API o Biblioteca en C++.
keywords: almacenando número como texto en Excel usando C++, verificación de errores en opciones de Excel en C++
---

{{% alert color="primary" %}}

Microsoft Excel permite a los usuarios definir opciones y reglas de verificación de errores. Los usuarios a menudo ven verificaciones de errores al crear fórmulas, un pequeño triángulo en la esquina superior derecha de una celda resalta cuando hay un problema con una celda. Excel proporciona información que ayuda a los usuarios a corregir problemas comunes.

{{% /alert %}}

## **Tipos de Errores**

Errores que significan que la fórmula no puede devolver un resultado, como dividir un número por cero, requieren atención inmediata y se muestra un valor de error en la celda. Al hacer clic en el triángulo verde se muestra un signo de exclamación, al hacer clic en esto se abre una lista de opciones.

El error puede resolverse utilizando las opciones, o ignorarse. Ignorar un error significa que ese error no aparecerá en futuras verificaciones de errores.

Aspose.Cells proporciona características de opción de verificación de errores. La clase [**ErrorCheckOption**](https://reference.aspose.com/cells/cpp/aspose.cells/errorcheckoption/) gestiona diferentes tipos de comprobaciones de errores, por ejemplo, números almacenados como texto, errores de cálculo de fórmulas y errores de validación. Utiliza la enumeración [**ErrorCheckType**](https://reference.aspose.com/cells/cpp/aspose.cells/errorchecktype/) para establecer la verificación de errores deseada.

## **Números Almacenados como Texto**

Ocasionalmente, los números pueden formatearse y almacenarse en celdas como texto. Esto puede causar problemas con cálculos o producir órdenes de clasificación confusos. Los números formateados como texto están alineados a la izquierda en lugar de a la derecha en la celda. Si una fórmula que debería realizar una operación matemática en celdas no devuelve un valor, verifica la alineación en las celdas a las que hace referencia la fórmula; algunas o todas esas celdas pueden ser números formateados como texto.

Puedes usar las opciones de verificación de errores para convertir rápidamente los números almacenados como texto en números reales. En Microsoft Excel 2003:

1. En el menú **Herramientas**, haz clic en **Opciones**.
1. Selecciona la pestaña de Verificación de Errores.
   La opción de **Número almacenado como texto** está marcada por defecto.
1. Desactívala.

El siguiente código de muestra muestra cómo deshabilitar la opción de verificación de errores de números almacenados como texto para una hoja de cálculo en el archivo XLS de plantilla utilizando las APIs de Aspose.Cells.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Create a workbook and open the template spreadsheet
    Workbook workbook(inputFilePath);

    // Get the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Instantiate the error checking options
    ErrorCheckOptionCollection opts = sheet.GetErrorCheckOptions();

    // Add a new error check option
    int index = opts.Add();
    ErrorCheckOption opt = opts.Get(index);

    // Disable the numbers stored as text option
    opt.SetErrorCheck(ErrorCheckType::NumberStoredAsText, false);

    // Set the range
    CellArea area = CellArea::CreateCellArea(0, 0, 1000, 50);
    opt.AddRange(area);

    // Path of output excel file
    U16String outputFilePath = outDir + u"out_test.out.xlsx";

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Error check options applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
