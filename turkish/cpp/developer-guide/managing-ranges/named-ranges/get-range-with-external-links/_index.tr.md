---
title: C++ ile Dış Bağlantılı Aralıkları Almak
linktitle: Harici Bağlantıları İçeren Menzil Al
type: docs
weight: 120
url: /tr/cpp/get-range-with-external-links/
description: Aspose.Cells kullanarak Excel dosyalarında dış bağlantılı aralıkları nasıl alacağınızı öğrenin.
---

## **Harici Bağlantıları Olan Aralığı Al**

Birçok durumda Excel dosyaları, dış bağlantılar kullanarak başka Excel dosyalarından veri erişir. Aspose.Cells, bu dış bağlantıları almak için [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) metodunu kullanma seçeneği sunar. [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) metodu, [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) türünde bir dizi döner. [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) sınıfı, dış dosya adını döndüren [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/) özelliği sağlar. [**ReferredArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/) sınıfı ise aşağıdaki üyeleri gözler önüne serer.

- [**GetEndColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendcolumn/): Bölgenin son sütunu
- [**GetEndRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getendrow/): Bölgenin son satırı
- [**GetExternalFileName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getexternalfilename/): Bu dış referanssa, dış dosya adını al
- [**IsArea**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isarea/): Bu, bir alan mı gösterir
- [**IsExternalLink**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/isexternallink/): Bu, dış bağlantı mı gösterir
- [**GetSheetName()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getsheetname/): Bu, hangi sayfada olduğunu gösterir
- [**GetStartColumn()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartcolumn/): Bölgenin başlangıç sütunu
- [**GetStartRow()**](https://reference.aspose.com/cells/cpp/aspose.cells/referredarea/getstartrow/): Bölgenin başlangıç satırı

Aşağıda verilen örnek kod, Dış Bağlantılı Aralıkları almak için [**Name.GetReferredAreas**](https://reference.aspose.com/cells/cpp/aspose.cells/name/getreferredareas/) metodunun kullanımını gösterir.

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook workbook(srcDir + u"SampleExternalReferences.xlsx");

    WorksheetCollection sheets = workbook.GetWorksheets();
    NameCollection namedRanges = sheets.GetNames();

    for (int i = 0; i < namedRanges.GetCount(); ++i)
    {
        Name namedRange = namedRanges.Get(i);
        Vector<ReferredArea> referredAreas = namedRange.GetReferredAreas(true);

        if (!referredAreas.IsNull())
        {
            for (int j = 0; j < referredAreas.GetLength(); ++j)
            {
                ReferredArea referredArea = referredAreas[j];
                std::cout << "IsExternalLink: " << referredArea.IsExternalLink() << std::endl;
                std::cout << "IsArea: " << referredArea.IsArea() << std::endl;
                std::cout << "SheetName: " << referredArea.GetSheetName().ToUtf8() << std::endl;
                std::cout << "ExternalFileName: " << referredArea.GetExternalFileName().ToUtf8() << std::endl;
                std::cout << "StartColumn: " << referredArea.GetStartColumn() << std::endl;
                std::cout << "StartRow: " << referredArea.GetStartRow() << std::endl;
                std::cout << "EndColumn: " << referredArea.GetEndColumn() << std::endl;
                std::cout << "EndRow: " << referredArea.GetEndRow() << std::endl;
            }
        }
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
