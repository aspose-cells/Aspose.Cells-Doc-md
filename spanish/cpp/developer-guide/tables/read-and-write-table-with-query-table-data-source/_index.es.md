---
title: Leer y Escribir Tabla con Fuente de Datos Query Table con C++
linktitle: Leer y Escribir Tabla con Origen de Datos de Tabla de Consulta
type: docs
weight: 30
url: /es/cpp/read-and-write-table-with-query-table-data-source/
description: Aprende cómo leer y escribir tablas con queryTable como fuente de datos usando Aspose.Cells for C++.
---

## **Leer y Escribir Tabla con Origen de Datos de Tabla de Consulta**
Con Aspose.Cells, puedes leer y escribir una tabla que tiene un QueryTable como fuente de datos. El soporte para esta función también existe para archivos XLS. El siguiente fragmento de código demuestra cómo leer y escribir dicha tabla primero leyendo la tabla y luego modificándola para añadir la fila de totales.

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

    // Load workbook object
    Workbook workbook(srcDir + u"SampleTableWithQueryTable.xls");

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get the first ListObject (Table) in the worksheet
    ListObject table = worksheet.GetListObjects().Get(0);

    // Check the data source type if it is query table
    if (table.GetDataSourceType() == TableDataSourceType::QueryTable)
    {
        table.SetShowTotals(true);
    }

    // Save the file
    workbook.Save(outDir + u"SampleTableWithQueryTable_out.xls");

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

 Los archivos de Excel de origen y salida están adjuntos para referencia.

[Archivo de origen](96928091.xls)

[Archivo de salida](96928092.xls)
{{< app/cells/assistant language="cpp" >}}
