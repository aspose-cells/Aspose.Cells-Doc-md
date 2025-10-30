---
title: Esporta il Certificato VBA in un file o stream con C++
linktitle: Esporta il certificato VBA su File o Stream
type: docs
weight: 90
url: /it/cpp/export-vba-certificate-to-file-or-stream/
description: Impara come esportare il Certificato Digitale VBA in un file o stream di memoria usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells consente di esportare il Certificato Digitale VBA in uno stream come un file o uno stream di memoria. Puoi accedere ai dati raw del certificato digitale VBA usando la proprietà [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/).

{{% /alert %}}

## **Esporta il Certificato VBA in un file o stream in C++**

Consulta il seguente codice di esempio che salva i dati grezzi del certificato VBA in un file. Puoi scaricare il [file di esempio di Excel utilizzato in questo codice](5115031.xlsm) dal link fornito.

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
{{< app/cells/assistant language="cpp" >}}
