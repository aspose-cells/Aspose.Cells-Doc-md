---
title: C++ ile Bir VBA Kod Projesini Sertifikayla Dijital Olarak İmza Atın
linktitle: Sertifika ile bir VBA Kod Projesini Dijital Olarak İmzalama
type: docs
weight: 110
url: /tr/cpp/digitally-sign-a-vba-code-project-with-certificate/
description: Aspose.Cells for C++ kullanarak ve bir sertifika ile VBA kod projenizi nasıl dijital olarak imzalayacağınızı öğrenin.
---

{{% alert color="primary" %}} 

Aspose.Cells kullanarak ve [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/) yöntemi ile VBA kod projenizi dijital olarak imzalayabilirsiniz. Excel dosyanızın dijital olarak sertifika ile imzalanıp imzalanmadığını kontrol etmek için lütfen bu adımları izleyin.

- **Geliştirici** sekmesinden **Visual Basic** üzerine tıklayın ve **Visual Basic for Applications IDE**'yi açın.
- **Visual Basic for Applications IDE** içerisinde **Araçlar** > **Dijital İmzalar...** seçeneğine tıklayın.

Bu, belgenin dijital olarak sertifikayla imzalanıp imzalanmadığını gösteren **Dijital İmza Formu**nu gösterecektir.

{{% /alert %}} 

## **C++ ile Bir VBA Kod Projesini Sertifikayla Dijital Olarak İmza Atın**

Aşağıdaki örnek kod, [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/cpp/aspose.cells.vba/vbaproject/sign/) metodunun nasıl kullanılacağını gösterir. Bu örneğin giriş ve çıkış dosyaları burada verilmiştir. Bu kodu test etmek için herhangi bir Excel dosyası ve herhangi bir sertifika kullanabilirsiniz.

- Örnek Excel dosyası](5115028.xlsm) örnek kodda kullanılan.
- [Örnek pfx dosyası](5115039.pfx) Dijital İmza oluşturmak için. Bu kodu çalıştırmak için lütfen bilgisayarınıza kurun. Şifresi 1234'tür.
- [Çıktı Excel dosyası](5115029.xlsm) örnek kod tarafından oluşturulan.

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
