---
title: Support for XAdES Signature with C++
linktitle: Support for XAdES Signature
type: docs
weight: 110
url: /cpp/support-for-xades-signature/
description: This article describes support for XAdES signatures using C++ code with Aspose.Cells for C++.
keywords: Support for XAdES Signature, How to sign Excel with XAdES Signature, How to add XAdES signature.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

Aspose.Cells provides support for signing workbooks with XAdES signatures. To do this, the API provides the [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) class and the [**XAdESType**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/xadestype/) enumeration.

## **How to Add XAdES Signature for Excel**

The following code snippet demonstrates the use of the [**DigitalSignature**](https://reference.aspose.com/cells/cpp/aspose.cells.digitalsignatures/digitalsignature/) class to sign the source workbook.

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
