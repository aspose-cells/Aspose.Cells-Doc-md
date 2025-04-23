---
title: Exportar Certificado VBA a Archivo o Flujo con C++
linktitle: Exportar Certificado VBA a Archivo o Secuencia
type: docs
weight: 90
url: /es/cpp/export-vba-certificate-to-file-or-stream/
description: Aprenda cómo exportar el Certificado Digital VBA a un archivo o flujo de memoria usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells te permite exportar el Certificado Digital VBA a un flujo, como un archivo o flujo de memoria. Puedes acceder a los datos en bruto del certificado digital VBA usando la propiedad [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/).

{{% /alert %}}

## **Exportar Certificado VBA a Archivo o Flujo en C++**

Consulte el siguiente código de muestra que guarda los datos en bruto del Certificado VBA en un archivo. Puede descargar el [archivo de Excel de muestra utilizado en este código](5115031.xlsm) desde el enlace proporcionado.

```cpp
#include <iostream>
#include <fstream>
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
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Retrieve bytes data of Digital Certificate of VBA Project
    Vector<uint8_t> certBytes = workbook.GetVbaProject().GetCertRawData();

    // Save Certificate Data into FileStream
    U16String outputFilePath = outDir + u"Cert_out_";
    std::ofstream outFile(outputFilePath.ToUtf8(), std::ios::binary);
    if (outFile.is_open())
    {
        outFile.write(reinterpret_cast<const char*>(certBytes.GetData()), certBytes.GetLength());
        outFile.close();
    }

    Aspose::Cells::Cleanup();
}
```
