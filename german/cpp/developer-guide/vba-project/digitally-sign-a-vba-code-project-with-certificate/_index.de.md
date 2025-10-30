---
title: Digitale Signatur eines VBA Codeprojekts mit Zertifikat in C++
linktitle: Digitale Signatur eines VBA Codeprojekts mit Zertifikat
type: docs
weight: 110
url: /de/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Erfahren Sie, wie Sie Ihr VBA Codeprojekt mit Aspose.Cells for C++ und einem Zertifikat digital signieren.
---

{{% alert color="primary" %}} 

Sie können Ihr VBA-Codeprojekt mit Aspose.Cells und seiner [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/) Methode digital signieren. Bitte folgen Sie diesen Schritten, um zu prüfen, ob Ihre Excel-Datei mit einem Zertifikat digital signiert ist.

- Klicken Sie im Ribbon auf die Registerkarte **Entwicklertools** und dann auf **Visual Basic** im Abschnitt **Code**.
- Klicken Sie auf **Extras** > **Digitale Signaturen...** im **Visual Basic for Applications IDE**.

Es erscheint das **Digital Signature Formular**, das anzeigt, ob das Dokument mit einem Zertifikat digital signiert ist oder nicht.

{{% /alert %}} 

## **Digitale Signatur eines VBA-Codeprojekts mit Zertifikat in C++**

Das folgende Beispiel zeigt, wie die [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/) Methode verwendet wird. Hier sind die Eingabe- und Ausgabedateien des Codes. Sie können jede Excel-Datei und jedes Zertifikat verwenden, um diesen Code zu testen.

- [Quell-Excel-Datei](5115028.xlsm), die im Beispielcode verwendet wird.
- [Beispiel-PFX-Datei](5115039.pfx) zur Erstellung einer digitalen Signatur. Bitte installieren Sie diese auf Ihrem Computer, um diesen Code auszuführen. Das Kennwort lautet 1234.
- [Ausgabe-Excel-Datei](5115029.xlsm), die vom Beispielcode generiert wurde.

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
{{< app/cells/assistant language="cpp" >}}
