---
title: Экспортируйте сертификат VBA в файл или поток с помощью C++
linktitle: Экспорт сертификата VBA в файл или поток
type: docs
weight: 90
url: /ru/cpp/export-vba-certificate-to-file-or-stream/
description: Узнайте, как экспортировать цифровой сертификат VBA в файл или поток памяти с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет экспортировать цифровой сертификат VBA в поток, такой как файл или поток памяти. Вы можете получить необработанные данные цифрового сертификата VBA через свойство [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/).

{{% /alert %}}

## **Экспортировать сертификат VBA в файл или поток в C++**

Пожалуйста, ознакомьтесь с приведенным ниже образцом кода, который сохраняет сырые данные сертификата VBA в файл. Вы можете загрузить [образец excel файла, используемого в этом коде](5115031.xlsm) по предоставленной ссылке.

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
