---
title: Firmar digitalmente un proyecto de código VBA con certificado en C++
linktitle: Firmar digitalmente un proyecto de código VBA con un certificado
type: docs
weight: 110
url: /es/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aprenda cómo firmar digitalmente su proyecto de código VBA usando Aspose.Cells for C++ con un certificado.
---

{{% alert color="primary" %}} 

Puede firmar digitalmente su proyecto de código VBA usando Aspose.Cells con su método [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Siga estos pasos para verificar si su archivo de Excel está firmado digitalmente con un certificado.

- Haga clic en **Visual Basic** en la pestaña **Desarrollador** para abrir el **IDE de Visual Basic para Aplicaciones**.
- Haga clic en **Herramientas** > **Firmas Digitales...** en **IDE de Visual Basic para Aplicaciones**.

Se mostrará el **Formulario de Firma Digital** indicando si el documento está firmado digitalmente con un certificado o no.

{{% /alert %}} 

## **Firmar digitalmente un proyecto de código VBA con certificado en C++**

El siguiente código de ejemplo ilustra cómo usar el método [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Aquí están los archivos de entrada y salida del código de ejemplo. Puede usar cualquier archivo Excel y cualquier certificado para probar este código.

- [Archivo de Excel de origen](5115028.xlsm) utilizado en el código de ejemplo.
- [Archivo pfx de ejemplo](5115039.pfx) para crear la Firma Digital. Por favor, instálelo en su computadora para ejecutar este código. Su contraseña es 1234.
- [Archivo de Excel de salida](5115029.xlsm) generado por el código de ejemplo.

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
