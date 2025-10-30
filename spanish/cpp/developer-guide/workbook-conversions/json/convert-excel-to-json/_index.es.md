---
title: Convertir Excel a JSON con C++
linktitle: Convertir Excel a JSON
type: docs
weight: 300
url: /es/cpp/convert-excel-to-json/
description: Aprende a convertir archivos Excel a JSON con Aspose.Cells usando C++.
keywords: Exportar Libro a JSON sin office 2013, office 2016, office 2019 y office 365
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de una hoja de cálculo a un archivo JSON (JavaScript Object Notation).

{{% /alert %}}

## **Convertir Libro de Excel a JSON**

No hay necesidad de preguntarse cómo convertir un Libro de Excel a JSON, porque la biblioteca Aspose.Cells for C++ tiene la mejor solución. La API de Aspose.Cells soporta la conversión de hojas de cálculo a formato JSON. Para exportar el libro a JSON, pasa [**SaveFormat.Json**](https://reference.aspose.com/cells/cpp/aspose.cells/saveformat/) como el segundo parámetro del método [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). También puedes usar la clase [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) para especificar configuraciones adicionales al exportar la hoja de trabajo a JSON.

El siguiente ejemplo de código demuestra cómo exportar un Libro de Excel a JSON. Consulta el código para convertir [archivo fuente](sample.xlsx) al archivo JSON generado por el código como referencia.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"sample.xlsx");
    Workbook workbook(inputFilePath);

    // Convert the workbook to JSON file.
    U16String outputFilePath(u"sample_out.json");
    workbook.Save(outputFilePath, SaveFormat::Json);

    std::cout << "Workbook converted to JSON successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

El siguiente ejemplo de código, que utiliza la clase JsonSaveOptions para especificar configuraciones adicionales, demuestra cómo exportar un Libro de Excel a JSON. Consulta el código para convertir [archivo fuente](sample.xlsx) al archivo JSON generado por el código como referencia.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Create an options of saving the file.
    JsonSaveOptions options;

    // Set the exporting range.
    options.SetExportArea(CellArea::CreateCellArea(u"B1", u"C4"));

    // Load your source workbook
    Workbook workbook(u"sample.xlsx");

    // Convert the workbook to json file.
    workbook.Save(u"sample_out.json", options);

    std::cout << "Workbook successfully converted to JSON!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{< app/cells/assistant language="cpp" >}}
