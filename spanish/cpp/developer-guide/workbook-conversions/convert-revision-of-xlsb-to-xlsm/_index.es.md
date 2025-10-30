---
title: Convertir revisión de XLSB a XLSM con C++
linktitle: Convertir revisión de XLSB a XLSM
type: docs
weight: 290
url: /es/cpp/convert-revision-of-xlsb-to-xlsm/
description: Aprende a convertir revisiones de archivos XLSB en formato XLSM usando Aspose.Cells con C++.
---

{{% alert color="primary" %}} 

Aspose.Cells ahora soporta la conversión completa de revisiones de archivos XLSB en archivos XLSM. Las revisiones se encuentran dentro de la ruta \xl\revisions. Puedes visualizarlas cambiando la extensión de tu archivo XLSB a ZIP. La ruta \xl\revisions contiene archivos que terminan con extensiones .bin.

Cuando conviertes tu archivo XLSB en un archivo XLSM usando Aspose.Cells, estos archivos .bin se convierten con éxito a archivos .xml como se muestra en estas dos capturas de pantalla.

{{% /alert %}} 

El siguiente ejemplo de código muestra cómo convertir el archivo XLSB a formato XLSM usando Aspose.Cells.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"sample.xlsb";

    // Create workbook from the input file
    Workbook workbook(inputFilePath);

    // Save Workbook to XLSM format
    workbook.Save(outDir + u"output_out.xlsm", SaveFormat::Xlsm);

    std::cout << "Workbook saved successfully in XLSM format!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
