---
title: Eliminar espacios redundantes después del salto de línea al importar HTML con C++
linktitle: Eliminar espacios redundantes después de un salto de línea al importar HTML
type: docs
weight: 20
url: /es/cpp/delete-redundant-spaces-after-line-break-while-importing/
description: Aprende cómo eliminar espacios redundantes después de saltos de línea al importar HTML usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Por favor, usa la propiedad [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/) y establece su valor en **true** para eliminar todos los espacios redundantes que vienen después de la etiqueta de salto de línea. Por defecto, esta propiedad está en **false** y los espacios redundantes se conservan en los archivos Excel de salida.

{{% /alert %}}

## Efecto de establecer la propiedad HTMLLoadOptions.DeleteRedundantSpaces en falso y verdadero

La siguiente captura de pantalla muestra el efecto de establecer esta propiedad en **false** y **true**.

![todo:image_alt_text](delete-redundant-spaces-after-line-break-while-importing-html_1.png)

## Eliminar espacios redundantes después de un salto de línea al importar HTML

### Ejemplo de Programación

El siguiente código de muestra muestra el uso de la propiedad [**HTMLLoadOptions.GetDeleteRedundantSpaces()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlloadoptions/getdeleteredundantspaces/). Por favor establézcala como **true** o **false** para obtener la salida como se muestra en la captura de pantalla anterior.

```c++
#include <iostream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String html = u8"<html> <body> <table> <tr> <td> <br>    This is sample data <br>    This is sample data<br>    This is sample data</td> </tr> </table> </body> </html>";

    std::vector<uint8_t> byteArray;
    for (int32_t i = 0; i < html.GetLength(); ++i)
    {
        char16_t c = html[i];
        if (c <= 0x7F)
            byteArray.push_back(static_cast<uint8_t>(c));
    }

    HtmlLoadOptions loadOptions(LoadFormat::Html);
    loadOptions.SetDeleteRedundantSpaces(true);

    Vector<uint8_t> data(byteArray.data(), static_cast<int32_t>(byteArray.size()));
    Workbook workbook(data, loadOptions);

    WorksheetCollection sheets = workbook.GetWorksheets();
    Worksheet sheet = sheets.Get(0);
    sheet.AutoFitColumns();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    workbook.Save(outDir + u"outputDeleteRedundantSpacesWhileImportingFromHtml.xlsx", SaveFormat::Xlsx);

    std::cout << "File saved successfully." << std::endl;

    Cleanup();

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
