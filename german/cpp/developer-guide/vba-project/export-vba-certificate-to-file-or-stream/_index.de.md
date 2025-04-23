---
title: Exportieren Sie das VBA Zertifikat in eine Datei oder einen Stream mit C++
linktitle: Exportieren Sie VBA Zertifikat in eine Datei oder einen Stream
type: docs
weight: 90
url: /de/cpp/export-vba-certificate-to-file-or-stream/
description: Lernen Sie, wie Sie das VBA Digitalzertifikat mit Aspose.Cells for C++ in eine Datei oder einen Speicherstream exportieren.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht den Export des VBA-Digitalzertifikats in einen Stream wie eine Datei oder einen Speicherstream. Sie können die Rohdaten des VBA-Digitalzertifikats mit der [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/) Eigenschaft abrufen.

{{% /alert %}}

## **VBA-Zertifikat in C++ in eine Datei oder einen Stream exportieren**

Bitte sehen Sie sich den folgenden Beispielscode an, der die Rohdaten des VBA-Zertifikats in einer Datei speichert. Sie können die [Beispiel-Excel-Datei, die in diesem Code verwendet wird](5115031.xlsm) von dem bereitgestellten Link herunterladen.

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
