---
title: Verificar formato de número personalizado al establecer la propiedad Style.Custom con C++
description: Aspose.Cells es una biblioteca C++ para trabajar con archivos de hojas de cálculo, que soporta verificar formatos de número personalizados al aplicar estilos. Este artículo mostrará cómo usar la biblioteca Aspose.Cells para verificar formatos de número personalizados y asegurar que el estilo sea correcto.
keywords: Aspose.Cells, bibliotecas C++, hojas de cálculo, estilos, formato de número personalizado, verificación, validación
type: docs
weight: 170
url: /es/cpp/check-custom-number-format-when-setting-style-custom-property/
---

## **Escenarios de uso posibles**

Si asignas un formato de número personalizado inválido a la propiedad [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/), Aspose.Cells no lanzará ninguna excepción. Pero si deseas que Aspose.Cells verifique si el formato de número personalizado asignado es válido o no, configura la propiedad [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) en **true**.

## **Comprobar formato de número personalizado al establecer la propiedad Personalizada de Estilo**

El siguiente código de ejemplo asigna un formato de número personalizado inválido a la propiedad [**Style.GetCustom()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getcustom/). Dado que ya configuramos la propiedad [**Workbook.GetCheckCustomNumberFormat()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getcheckcustomnumberformat/) en **true**, lanzará una excepción, por ejemplo, Formato de número inválido. Lee los comentarios dentro del código para más ayuda.

## **Código de muestra**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an instance of Workbook class
    Workbook book;

    // Setting this property to true will make Aspose.Cells to throw exception
    // when invalid custom number format is assigned to Style.Custom property
    book.GetSettings().SetCheckCustomNumberFormat(true);

    // Access first worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Access cell A1 and put some number to it
    Cell cell = sheet.GetCells().Get(u"A1");
    cell.PutValue(2347);

    // Access cell's style and set its Style.Custom property
    Style style = cell.GetStyle();

    // This line will throw exception if Workbook.Settings.CheckCustomNumberFormat is set to true
    style.SetCustom(u"ggg @ fff"); // Invalid custom number format

    std::cout << "Custom number format set." << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
