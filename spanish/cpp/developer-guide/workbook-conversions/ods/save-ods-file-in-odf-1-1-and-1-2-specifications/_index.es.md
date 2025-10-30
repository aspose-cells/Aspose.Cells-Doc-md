---
title: Guardar archivo ODS en las especificaciones ODF 1.1, 1.2 y 1.3 con C++
linktitle: Guardar como ODF 1.1, 1.2 y 1.3
description: Convertir Excel a ODF 1.1, 1.2 y 1.3 con Aspose.Cells usando C++.
type: docs
weight: 230
url: /es/cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells soporta guardar un archivo ODS (**Hoja de cálculo del Documento Abierto**) en las especificaciones ODF (**Formato del Documento Abierto**) 1.1, 1.2 y 1.3. Aspose.Cells tiene una propiedad [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/cpp/aspose.cells/odssaveoptions/getodfstrictversion/) que especifica la versión ODF para guardar archivos ODS. El valor predeterminado de esta propiedad es [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), por lo que el archivo ODS guardado sin esta configuración utiliza las especificaciones 1.2.

{{% /alert %}}

El código de ejemplo a continuación crea un objeto de libro de trabajo, añade algunos valores a la celda A1 en la primera hoja y luego guarda el archivo ODS en las especificaciones ODF 1.1, 1.2 y 1.3. Por defecto, el archivo ODS se guarda en la especificación ODF 1.2.

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

    // Create workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put some value in cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");
    cell.PutValue(u"Welcome to Aspose!");

    // Save ODS in ODF 1.2 version which is default
    OdsSaveOptions options;
    workbook.Save(outDir + u"ODF1.2_out.ods", options);

    // Save ODS in ODF 1.1 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf11);
    workbook.Save(outDir + u"ODF1.1_out.ods", options);

    // Save ODS in ODF 1.3 version
    options.SetOdfStrictVersion(OpenDocumentFormatVersionType::Odf13);
    workbook.Save(outDir + u"ODF1.3_out.ods", options);

    std::cout << "ODS files saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
