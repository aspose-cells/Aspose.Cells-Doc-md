---
title: Цифровая подпись проекта VBA с сертификатом в C++
linktitle: Цифровая подпись проекта VBA с помощью сертификата
type: docs
weight: 110
url: /ru/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Узнайте, как цифрово подписать ваш проект VBA, используя Aspose.Cells for C++ с сертификатом.
---

{{% alert color="primary" %}} 

Вы можете цифрово подписать ваш проект VBA с помощью Aspose.Cells и его метода [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Пожалуйста, следуйте этим шагам, чтобы проверить, подписан ли ваш файл Excel с помощью сертификата.

- Нажмите **Visual Basic** на вкладке **Developer**, чтобы открыть **Visual Basic for Applications IDE**.
- Нажмите **Tools** > **Digital Signatures...** в **Visual Basic for Applications IDE**.

Это покажет **Digital Signature Form**, указывающую, подписан ли документ с помощью сертификата или нет.

{{% /alert %}} 

## **Цифровая подпись проекта VBA с сертификатом в C++**

Следующий пример кода иллюстрирует, как использовать метод [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/). Вот входные и выходные файлы примера кода. Вы можете использовать любой файл Excel и любой сертификат для тестирования этого кода.

- [Исходный файл Excel](5115028.xlsm), используемый в образцовом коде.
- [Образец файла pfx](5115039.pfx) для создания цифровой подписи. Пожалуйста, установите его на ваш компьютер, чтобы запустить этот код. Пароль - 1234.
- [Файл Excel вывода](5115029.xlsm), сгенерированный образцовым кодом.

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
