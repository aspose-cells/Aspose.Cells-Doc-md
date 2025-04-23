---
title: 用C++将VBA证书导出到文件或流
linktitle: 将VBA证书导出到文件或流
type: docs
weight: 90
url: /zh/cpp/export-vba-certificate-to-file-or-stream/
description: 了解如何使用Aspose.Cells for C++将VBA数字证书导出到文件或内存流。
---

{{% alert color="primary" %}}

Aspose.Cells允许您将VBA数字证书导出到文件或内存流。您可以使用[**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/)属性访问VBA数字证书的原始数据。

{{% /alert %}}

## **用C++将VBA证书导出到文件或流**

请参阅以下示例代码，将VBA证书的原始数据保存到文件中。您可以从提供的链接下载使用此代码的[示例excel文件](5115031.xlsm)。

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
