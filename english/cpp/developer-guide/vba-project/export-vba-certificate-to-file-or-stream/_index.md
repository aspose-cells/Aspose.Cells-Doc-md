---
title: Export VBA Certificate to File or Stream with C++
linktitle: Export VBA Certificate to File or Stream
type: docs
weight: 90
url: /cpp/export-vba-certificate-to-file-or-stream/
description: Learn how to export VBA Digital Certificate to a file or memory stream using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to export VBA Digital Certificate to a stream such as a file or memory stream. You can access the raw data of the VBA digital certificate using the [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/) property.

{{% /alert %}}

## **Export VBA Certificate to File or Stream in C++**

Please see the following sample code that saves the raw data of the VBA Certificate into a file. You can download the [sample excel file used in this code](5115031.xlsm) from the provided link.

```c++
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
        outFile.write(reinterpret_cast<const char*>(certBytes.data()), certBytes.size());
        outFile.close();
    }

    Aspose::Cells::Cleanup();
}
```