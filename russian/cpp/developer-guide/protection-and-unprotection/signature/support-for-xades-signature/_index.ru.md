---
title: Поддержка подписи XAdES с помощью C++
linktitle: Поддержка подписи XAdES
type: docs
weight: 110
url: /ru/cpp/support-for-xades-signature/
description: Эта статья описывает поддержку подписи XAdES с помощью кода C++ и Aspose.Cells for C++.
keywords: Поддержка подписи XAdES, Как подписать Excel подписью XAdES, Как добавить подпись XAdES.
---

## **Введение**

Aspose.Cells поддерживает подпись рабочих книг с помощью подписи XAdES. Для этого API предоставляет класс [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) и перечисление [**XAdESType**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/xadestype/).

## **Как добавить подпись XAdES для Excel**

Следующий пример кода демонстрирует использование класса [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) для подписи рабочей книги [source](101089323.xlsx).

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
