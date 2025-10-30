---
title: Leer y Escribir Tablas de Consultas en la Hoja de C++
linktitle: Leer y Escribir Tabla de Consulta de Hoja de Cálculo
type: docs
weight: 40
url: /es/cpp/reading-and-writing-query-table-of-worksheet/
description: Aprenda cómo leer y escribir tablas de consultas en hojas de Excel usando Aspose.Cells con C++.
---

{{% alert color="primary" %}}

Aspose.Cells proporciona la colección `Worksheet.QueryTables`, que devuelve un objeto de tipo `QueryTable` por índice. Tiene las siguientes dos propiedades:

- `QueryTable.AdjustColumnWidth`
- `QueryTable.PreserveFormatting`

Ambas son valores booleanos. Puedes visualizarlas en Microsoft Excel a través de **Datos > Conexiones > Propiedades**.

{{% /alert %}}

## Lectura y Escritura de Tabla de Consulta de Hoja de Cálculo

El siguiente ejemplo de código lee la primera `QueryTable` de la primera hoja y luego imprime ambas propiedades de `QueryTable`. Luego establece `QueryTable.PreserveFormatting` en `true`.

Puedes descargar el archivo de Excel fuente utilizado en este código y el archivo de Excel de salida generado por el código desde los siguientes enlaces.

- [Archivo de Excel Fuente](5115533.xlsx)
- [Archivo de Excel de Salida](5115537.xlsx)

```c++
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

    // Create workbook from source excel file
    Workbook workbook(srcDir + u"Sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access first Query Table
    QueryTable qt = worksheet.GetQueryTables().Get(0);

    // Print Query Table Data
    std::cout << "Adjust Column Width: " << qt.GetAdjustColumnWidth() << std::endl;
    std::cout << "Preserve Formatting: " << qt.GetPreserveFormatting() << std::endl;

    // Now set Preserve Formatting to true
    qt.SetPreserveFormatting(true);

    // Save the workbook
    workbook.Save(outDir + u"Output_out.xlsx");

    std::cout << "Query Table properties updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### Salida en Consola

Aquí está la salida de la consola del código de ejemplo anterior:

{{< highlight java >}}

Adjust Column Width: True

Preserve Formatting: False

{{< /highlight >}}

## Obtener rango de resultados de la tabla de consulta

Aspose.Cells proporciona una opción para leer la dirección (es decir, rango de resultados de las celdas) de una tabla de consulta. El siguiente código demuestra esta función leyendo la dirección del rango de resultados de una tabla de consulta. El archivo de muestra se puede descargar [aquí](72417290.xlsx).

```cpp
#include <iostream>
#include <locale>
#include <codecvt>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

std::string convert_u16_to_string(const char16_t* data) {
    std::wstring_convert<std::codecvt_utf8_utf16<char16_t>, char16_t> converter;
    return converter.to_bytes(data);
}

int main()
{
    Aspose::Cells::Startup();

    Workbook wb(u"Query TXT.xlsx");
    std::cout << convert_u16_to_string(wb.GetWorksheets().Get(0).GetQueryTables().Get(0).GetResultRange().GetAddress().GetData()) << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
