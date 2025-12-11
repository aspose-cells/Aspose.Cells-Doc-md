---
title: Export VBA Certificate to File or Stream with C++
linktitle: Export VBA Certificate to File or Stream
type: docs
weight: 90
url: /cpp/export-vba-certificate-to-file-or-stream/
description: Learn how to export a VBA digital certificate to a file or memory stream using Aspose.Cells for C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells allows you to export a VBA digital certificate to a stream, such as a file or a memory stream. You can access the raw data of the VBA digital certificate using the [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/) property.

{{% /alert %}}

## **Export VBA Certificate to File or Stream in C++**

Please see the following sample code that saves the raw data of the VBA certificate into a file. You can download the [sample Excel file used in this code](5115031.xlsm) from the provided link.

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

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"sampleVBAProjectSigned.xlsm";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Retrieve the byte data of the digital certificate of the VBA project
    Vector<uint8_t> certBytes = workbook.GetVbaProject().GetCertRawData();

    // Save certificate data into a file stream
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
