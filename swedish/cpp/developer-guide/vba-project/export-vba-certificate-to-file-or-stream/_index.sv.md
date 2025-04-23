---
title: Exportera VBA certifikat till fil eller ström med C++
linktitle: Exportera VBA certifikat till fil eller ström
type: docs
weight: 90
url: /sv/cpp/export-vba-certificate-to-file-or-stream/
description: Lär dig hur du exporterar VBA digitalt certifikat till en fil eller minnesström med Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter att du exporterar VBA digitalt certifikat till en ström, till exempel en fil eller minnesström. Du kan få tillgång till den råa datan av VBA digitala certifikat med [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/) egenskapen.

{{% /alert %}}

## **Exportera VBA-certifikat till fil eller ström i C++**

Vänligen se följande exempelkod som sparar rådata för VBA-certifikatet i en fil. Du kan ladda ned [provexelfilen som används i denna kod](5115031.xlsm) från den angivna länken.

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
