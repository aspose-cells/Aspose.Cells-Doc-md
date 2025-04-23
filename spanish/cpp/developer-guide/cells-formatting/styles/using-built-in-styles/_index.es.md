---
title: Usando estilos integrados con C++
linktitle: Utilizando Estilos Incorporados
type: docs
weight: 80
url: /es/cpp/using-built-in-styles/
description: Código en C++ para usar estilos predefinidos de Excel con la API Aspose.Cells for C++
keywords: uso de estilos integrados de Excel en C++, aplicar estilos en el libro de trabajo de manera programática, aplicar estilos en el libro de trabajo de manera programática, aplicar estilos integrados en Excel con C++, aplicar estilos integrados en el libro de trabajo, código en C++ para aplicar estilos integrados en el libro de trabajo, código en C++ para aplicar estilos en un libro de Excel
---

{{% alert color="primary" %}}

Aspose.Cells ofrece una vasta colección de estilos reutilizables para formatear una celda en un documento de hoja de cálculo. Podemos utilizar estilos incorporados en nuestro libro de trabajo y también crear estilos personalizados.

{{% /alert %}}

## **Cómo utilizar Estilos Incorporados**

El método [**Workbook.CreateBuiltinStyle**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/createbuiltinstyle/) y la enumeración [**BuiltinStyleType**](https://reference.aspose.com/cells/cpp/aspose.cells/builtinstyletype/) hacen conveniente el uso de estilos incorporados. Aquí hay una lista de todos los posibles estilos incorporados:

- TWENTY_PERCENT_ACCENT_1
- TWENTY_PERCENT_ACCENT_2
- TWENTY_PERCENT_ACCENT_3
- TWENTY_PERCENT_ACCENT_4
- TWENTY_PERCENT_ACCENT_5
- VEINTE_PORCIENTO_ACENTO_6
- CUARENTA_PORCIENTO_ACENTO_1
- CUARENTA_PORCIENTO_ACENTO_2
- CUARENTA_PORCIENTO_ACENTO_3
- CUARENTA_PORCIENTO_ACENTO_4
- CUARENTA_PORCIENTO_ACENTO_5
- CUARENTA_PORCIENTO_ACENTO_6
- SESENTA_PORCIENTO_ACENTO_1
- SESENTA_PORCIENTO_ACENTO_2
- SESENTA_PORCIENTO_ACENTO_3
- SESENTA_PORCIENTO_ACENTO_4
- SESENTA_PORCIENTO_ACENTO_5
- SESENTA_PORCIENTO_ACENTO_6
- ACENTO_1
- ACENTO_2
- ACENTO_3
- ACENTO_4
- ACENTO_5
- ACENTO_6
- MAL
- CÁLCULO
- VERIFICAR_CELDA
- COMA
- COMA_1
- MONEDA
- MONEDA_1
- TEXTO_EXPLICATIVO
- BUENO
- ENCABEZADO_1
- ENCABEZADO_2
- ENCABEZADO_3
- ENCABEZADO_4
- HYPERLINK
- HIPERVÍNCULO_SEGUIDO
- ENTRADA
- CELDA_VINCULADA
- NEUTRAL
- NORMAL
- NOTA
- SALIDA
- PORCENTAJE
- TÍTULO
- TOTAL
- TEXTO DE ADVERTENCIA
- NIVEL DE FILA
- NIVEL DE COLUMNA

## Código en C++ para usar estilos integrados

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output file paths
    U16String output1Path = srcDir + u"Output.xlsx";
    U16String output2Path = srcDir + u"Output.out.ods";

    // Create a new workbook
    Workbook workbook;

    // Create a built-in style of type Title
    Style style = workbook.CreateBuiltinStyle(BuiltinStyleType::Title);

    // Get the first worksheet and its cells
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Access cell A1 and set its value and style
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Aspose");
    cell.SetStyle(style);

    // Auto-fit the first column and row
    worksheet.AutoFitColumn(0);
    worksheet.AutoFitRow(0);

    // Save the workbook to the first output path
    workbook.Save(output1Path);
    std::cout << "File saved " << output1Path.ToUtf8() << std::endl;

    // Save the workbook to the second output path
    workbook.Save(output2Path);
    std::cout << "File saved " << output2Path.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
