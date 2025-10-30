---
title: Firmare digitalmente un progetto di codice VBA con Certificato in C++
linktitle: Firma digitalmente un progetto di codice VBA con certificato
type: docs
weight: 110
url: /it/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Impara come firmare digitalmente il tuo progetto di codice VBA utilizzando Aspose.Cells for C++ con un certificato.
---

{{% alert color="primary" %}} 

Puoi firmare digitalmente il progetto di codice VBA usando Aspose.Cells con il suo metodo [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Segui questi passaggi per verificare se il file Excel è firmato digitalmente con un certificato.

- Clicca su **Visual Basic** dalla scheda **Sviluppatore** per aprire **Visual Basic for Applications IDE**.
- Clicca su **Strumenti** > **Digital Signatures...** di **Visual Basic for Applications IDE**.

Mostrerà il **Modulo Firma Digitale** indicando se il documento è firmato digitalmente con un certificato o meno.

{{% /alert %}} 

## **Firmare digitalmente un progetto di codice VBA con Certificato in C++**

Il seguente esempio di codice illustra come usare il metodo [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Qui ci sono i file di input e output del codice di esempio. Puoi usare qualsiasi file Excel e qualsiasi certificato per testare questo codice.

- [File Excel di origine](5115028.xlsm) utilizzato nel codice di esempio.
- [File pfx di esempio](5115039.pfx) per creare una firma digitale. Si prega di installarlo sul computer per eseguire questo codice. La password è 1234.
- [File Excel di output](5115029.xlsm) generato dal codice di esempio.

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
