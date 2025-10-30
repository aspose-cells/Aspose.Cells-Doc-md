---
title: C++ ile VBA Sertifikasını Dosyaya veya Akışa Dışa Aktarın
linktitle: VBA Sertifikasını Dosyaya veya Akışa Aktar
type: docs
weight: 90
url: /tr/cpp/export-vba-certificate-to-file-or-stream/
description: Aspose.Cells for C++ kullanarak VBA Dijital Sertifikasının dosyaya veya bellek akışına nasıl dışa aktarılacağını öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, VBA Dijital Sertifikasını bir dosya veya bellek akışı gibi akışlara dışa aktarmanıza izin verir. VBA dijital sertifikasının ham verisine [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/) özelliği kullanılarak erişebilirsiniz.

{{% /alert %}}

## **C++ ile VBA Sertifikasını Dosyaya veya Akışa Dışa Aktarın**

Lütfen, VBA Sertifikasının ham verilerini bir dosyaya kaydeden aşağıdaki örnek kodu inceleyin. Bu kodu içeren [örnek excel dosyasını buradaki bağlantıdan](5115031.xlsm) indirebilirsiniz.

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
