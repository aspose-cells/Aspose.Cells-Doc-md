---
title: C++ kullanarak Bağlantı Türünü tespit edin
linktitle: Bağlantı Türünü Algıla
type: docs
weight: 160
url: /tr/cpp/detect-hyperlink-type/
description: Aspose.Cells for C++ API ile bağlantı türünü nasıl tespit edeceğinizi öğrenin.
keywords: Bağlantı türünü algıla, Bağlantı türünü algıla, Bağlantı türünü al
---

## **Bağlantı Türünü Algılamak**

Bir Excel dosyası, dış, hücre referansı, dosya yolu vb. gibi farklı türde bağlantılara sahip olabilir. Aspose.Cells, bağlantı türünü algılama özelliğini destekler. Bağlantı türleri, [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) Numaralandırması tarafından temsil edilir. [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) Numaralandırması, aşağıdaki üyeleri içerir.

- Dış: Dış bağlantı
- DosyaYolu: Dosya/klasörün yerel ve tam yolu.
- E-posta: E-posta
- HücreReferansı: Hücre veya adlandırılmış aralığa bağlantı.

Bağlantı türünü kontrol etmek için, [**Hyperlink**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/) sınıfı [**LinkType**](https://reference.aspose.com/cells/cpp/aspose.cells/hyperlink/getlinktype/) özelliğini [**TargetModeType**](https://reference.aspose.com/cells/cpp/aspose.cells/targetmodetype/) geri dönüş türü ile sağlar. Aşağıdaki kod parçası, bu özelliğin kullanımını gösterir.

### Kaynak Kodu

```c++
#include <iostream>
#include <codecvt>
#include <locale>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    Workbook workbook(srcDir + u"LinkTypes.xlsx");

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    if (!worksheet)
    {
        std::cerr << "Worksheet not found!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Range range = worksheet.GetCells().CreateRange(u"A1", u"A7");
    if (!range)
    {
        std::cerr << "Range creation failed!" << std::endl;
        Aspose::Cells::Cleanup();
        return 1;
    }

    Vector<Hyperlink> hyperlinks = range.GetHyperlinks();


    for (int i = 0; i < hyperlinks.GetLength(); ++i)
    {
        Hyperlink link = hyperlinks[i];
        if (link)
        {
            std::cout << link.GetTextToDisplay().ToUtf8() << ": "
                << static_cast<int>(link.GetLinkType()) << std::endl;
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

Yukarıda verilen kod parçası tarafından üretilen çıktı aşağıdaki gibidir.

### Konsol Çıktısı
```
LinkTypes.xlsx: FilePath </br>
C:\Windows\System32\cmd.exe: FilePath </br>
C:\Program Files\Common Files: FilePath </br>
'Test Sheet'!B2: CellReference </br>
FullPathExample: CellReference </br>
https://products.aspose.com/cells/ : External </br>
mailto:test@test.com?subject=TestLink: Email </br>
```
