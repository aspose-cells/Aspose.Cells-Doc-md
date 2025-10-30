---
title: Lägg till signaturlinje i arbetsblad med C++
linktitle: Lägg till signaturlinje
type: docs
weight: 200
url: /sv/cpp/add-signature-line/
description: Denna artikel beskriver hur man lägger till en signaturlinje i arbetsbladet med hjälp av C++ koder med Aspose.Cells for C++.
keywords: Lägg till signeringsrad i arket, Hur du lägger till en signeringsrad i arket, Hur man lägger till en signeringsrad i arket, Hur man lägger till signaturrad på arket.
---

## **Introduktion**

Aspose.Cells tillhandahåller egenskapen [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) för att lägga till signaturlinjen i kalkylarket.

## **Hur man lägger till signeringsrad i arket**

Följande kodexempel visar hur man använder egenskapen [**Picture.SignatureLine**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/signatureline/) för att lägga till signature-linjen i arbetsbladet. Skärmdumpen visar effekten av kodexemplet på det provexempel-Excel-filen efter körning.

![todo:image_alt_text](add-signature-line.png)

## **Exempelkod**

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook wb;

    SignatureLine signatureLine;
    signatureLine.SetSigner(u"Aspose.Cells");
    signatureLine.SetTitle(u"signed by Aspose.Cells");

    wb.GetWorksheets().Get(0).GetShapes().AddSignatureLine(1, 1, signatureLine);

    U16String certificatePath = srcDir + u"rsa2048.pfx";
    U16String password = u"123456";

    std::time_t now = std::time(nullptr);
    struct tm now_tm;
    localtime_s(&now_tm, &now);

    Date currentDate{
        now_tm.tm_year + 1900,
        now_tm.tm_mon + 1,
        now_tm.tm_mday,
        now_tm.tm_hour,
        now_tm.tm_min,
        now_tm.tm_sec,
        0
    };

    DigitalSignature signature(certificatePath, password, u"test Microsoft Office signature line", currentDate);

    DigitalSignatureCollection dsCollection;
    dsCollection.Add(signature);

    wb.SetDigitalSignature(dsCollection);

    U16String outputPath = srcDir + u"signatureLine.xlsx";
    wb.Save(outputPath);

    std::cout << "Workbook with signature line saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
