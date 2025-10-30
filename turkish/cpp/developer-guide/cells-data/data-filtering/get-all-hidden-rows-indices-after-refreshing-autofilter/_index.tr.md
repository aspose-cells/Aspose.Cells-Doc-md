---
title: AutoFilter ile yenilendikten sonra C++ kullanarak Gizli Satırların Tüm Dizilerini Alın
linktitle: Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın
type: docs
weight: 320
url: /tr/cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Aspose.Cells for C++ API’sini kullanarak AutoFilter yenilendikten sonra tüm gizli satır dizilerini nasıl alacağınızı öğrenin.
keywords: AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Alın, AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Elde Edin, AutoFilter Yenilendikten Sonra Tüm Gizli Satır Dizinlerini Alın
---

## **Olası Kullanım Senaryoları**

Çalışma sayfası hücrelerine otomatik filtre uyguladığınızda, bazı satırlar otomatik olarak gizlenir. Ancak bazı durumlarda, bazı satırlar otomatik filtre ile gizlenmeden önce Excel kullanıcısı tarafından manuel olarak gizlenmiş olabilir. Bu durumda, hangi satırların otomatik filtre tarafından gizlendiğini ve hangilerinin Excel kullanıcısı tarafından manuel olarak gizlendiğini bilmek zor olabilir. Aspose.Cells, bu problemi int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/) yöntemi ile çözer. Bu yöntem, otomatik filtre tarafından gizlenen tüm satırların dizinlerini ve Excel kullanıcısı tarafından manuel olarak gizlenmeyen tüm satırların dizinlerini döndürür.

## **Yenileme Otomatik Filtre Sonrası Tüm Gizli Satır Dizinleri Alın**

Aşağıdaki örnek kod, Excel kullanıcısı tarafından manuel olarak gizlenen bazı satırları içeren [örnek Excel dosyasını](64716909.xlsx) yükler. Kod, otomatik filtre uygular, int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/cpp/aspose.cells/autofilter/refresh/) yöntemini kullanarak otomatik olarak gizlenen tüm satırların dizarlarını döndürür. Daha sonra gizli satırların dizinlerini hücre adları ve değerleri ile birlikte konsola yazdırır.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String inputFilePath = srcDir + U16String(u"sampleGetAllHiddenRowsIndicesAfterRefreshingAutoFilter.xlsx");
    Workbook workbook(inputFilePath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    AutoFilter autoFilter = worksheet.GetAutoFilter();
    autoFilter.AddFilter(0, u"Orange");

    Vector<int32_t> rowIndices = autoFilter.Refresh(true);

    std::cout << "Printing Rows Indices, Cell Names and Values Hidden By AutoFilter." << std::endl;
    std::cout << "--------------------------" << std::endl;

    for (int32_t i = 0; i < rowIndices.GetLength(); i++)
    {
        int32_t r = rowIndices[i];
        Cell cell = worksheet.GetCells().Get(r, 0);
        std::cout << r << "\t" << cell.GetName().ToUtf8() << "\t" << cell.GetStringValue().ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
