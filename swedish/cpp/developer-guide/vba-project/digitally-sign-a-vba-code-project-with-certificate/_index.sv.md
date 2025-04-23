---
title: Digitalt signera ett VBA kodprojekt med certifikat i C++
linktitle: Signera digitalt ett VBA kodprojekt med certifikat
type: docs
weight: 110
url: /sv/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Lär dig hur du digitalt signerar ditt VBA kodprojekt med hjälp av Aspose.Cells for C++ med ett certifikat.
---

{{% alert color="primary" %}} 

Du kan digitalt signera ditt VBA-kodprojekt med Aspose.Cells med dess [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/)-metod. Följ dessa steg för att kontrollera om din Excel-fil är digitalt signerad med ett certifikat.

- Klicka på **Visual Basic** från fliken **Utvecklare** för att öppna **Visual Basic for Applications IDE**.
- Klicka på **Verktyg** > **Digitala signaturer...** i **Visual Basic for Applications IDE**.

Den visar **Digital Signature Form** som indikerar om dokumentet är digitalt signerat med ett certifikat eller inte.

{{% /alert %}} 

## **Digitalt signera ett VBA-kodprojekt med certifikat i C++**

Följande exempel på kod visar hur man använder [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/) metod. Här är in- och utdatafilerna för exemplet. Du kan använda vilken Excel-fil och certifikat som helst för att testa denna kod.

- [Källa Excel-fil](5115028.xlsm) använd i exempelkoden.
- [Exempel pfx-fil](5115039.pfx) för att skapa digital signatur. Installera den på din dator för att köra denna kod. Dess lösenord är 1234.
- [Utdatat Excel-fil](5115029.xlsm) genererad av exempelkoden.

```cpp
#include <iostream>
#include <ctime>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::DigitalSignatures;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");
    U16String password(u"1234");
    U16String pfxPath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.pfx";
    U16String comment(u"Signing Digital Signature using Aspose.Cells");

    Vector<uint8_t> certData;

    std::time_t now = std::time(nullptr);
    std::tm* now_tm = std::localtime(&now);
    int year = now_tm->tm_year + 1900;
    int month = now_tm->tm_mon + 1;
    int day = now_tm->tm_mday;
    int hour = now_tm->tm_hour;
    int minute = now_tm->tm_min;
    int second = now_tm->tm_sec;

    DigitalSignature digitalSignature(certData, password, comment, Date{year, month, day, hour, minute, second, 0});

    U16String inputFilePath = srcDir + u"sampleDigitallySignVbaProjectWithCertificate.xlsm";
    Workbook workbook(inputFilePath);

    workbook.GetVbaProject().Sign(digitalSignature);

    U16String outputFilePath = outDir + u"outputDigitallySignVbaProjectWithCertificate.xlsm";
    workbook.Save(outputFilePath);

    std::cout << "VBA project digitally signed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
