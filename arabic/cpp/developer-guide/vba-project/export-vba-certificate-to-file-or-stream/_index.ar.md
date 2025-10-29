---
title: تصدير شهادة VBA إلى ملف أو تدفق مع C++
linktitle: تصدير شهادة VBA إلى ملف أو تيار
type: docs
weight: 90
url: /ar/cpp/export-vba-certificate-to-file-or-stream/
description: تعلم كيفية تصدير شهادة VBA الرقمية إلى ملف أو تدفق ذاكرة باستخدام Aspose.Cells for C++.
---

{{% alert color="primary" %}}

يسمح Aspose.Cells لك بتصدير شهادة VBA الرقمية إلى تدفق مثل ملف أو تدفق ذاكرة. يمكنك الوصول إلى البيانات الخام لشهادة VBA الرقمية باستخدام خاصية [**Workbook.GetCertRawData()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/getcertrawdata/).

{{% /alert %}}

## **تصدير شهادة VBA إلى ملف أو تدفق في C++**

يرجى الاطلاع على الرمز العيني التالي الذي يحفظ البيانات الخام لشهادة VBA في ملف. يمكنك تنزيل [ملف الإكسل العيني المستخدم في هذا الرمز](5115031.xlsm) من الرابط المقدم.

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
