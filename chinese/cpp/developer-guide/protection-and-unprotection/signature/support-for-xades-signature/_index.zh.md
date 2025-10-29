---
title: 支持C++中的XAdES签名
linktitle: 支持对Excel XP以来的高级保护设置
type: docs
weight: 110
url: /zh/cpp/support-for-xades-signature/
description: 本文介绍如何使用C++代码结合Aspose.Cells for C++支持XAdES签名。
keywords: 支持XAdES签名，如何使用XAdES签名签署Excel，如何添加XAdES签名。
---

## **介绍**

 Aspose.Cells支持使用XAdES签名对工作簿进行签名。API提供了 [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) 类和 [**XAdESType**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/xadestype/) 枚举。

## **如何为Excel添加XAdES签名**

 下列代码片段演示了使用 [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) 类对[源文件](101089323.xlsx)工作簿进行签名。

```cpp
#include <iostream>
#include <chrono>
#include <ctime>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    Workbook workbook(srcDir + u"sourceFile.xlsx");
    U16String password(u"pfxPassword");
    U16String pfxFile(u"pfxFile");
    Vector<uint8_t> pfxData;

    auto now = std::chrono::system_clock::now();
    std::time_t now_time = std::chrono::system_clock::to_time_t(now);
    std::tm local_tm;
    localtime_s(&local_tm, &now_time);

    int year = local_tm.tm_year + 1900;
    int month = local_tm.tm_mon + 1;
    int day = local_tm.tm_mday;
    int hour = local_tm.tm_hour;
    int minute = local_tm.tm_min;
    int second = local_tm.tm_sec;
    auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(now.time_since_epoch()) % 1000;

    DigitalSignature signature(pfxData, password, u"testXAdES", Date{ year, month, day, hour, minute, second, static_cast<int>(ms.count()) });
    signature.SetXAdESType(XAdESType::XAdES);
    DigitalSignatureCollection dsCollection;
    dsCollection.Add(signature);
    workbook.SetDigitalSignature(dsCollection);
    workbook.Save(outDir + u"XAdESSignatureSupport_out.xlsx");

    std::cout << "Digital signature added successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
