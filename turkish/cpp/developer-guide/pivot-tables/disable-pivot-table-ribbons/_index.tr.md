---
title: C++ ile Pivot Tablo Şeridlerini Devre Dışı Bırak
linktitle: Pivot Tablo Şeritlerini Devre Dışı Bırak
type: docs
weight: 90
url: /tr/cpp/disable-pivot-table-ribbons/
description: Aspose.Cells for C++ kullanarak Excel dosyalarında pivot tablo şeritlerini nasıl devre dışı bırakacağınızı öğrenin.
---

{{% alert color="primary" %}}

Pivot tablo tabanlı raporlar kullanışlıdır ancak hedef kullanıcılar bu raporları yapılandırmak için Excel hakkında detaylı bilgiye sahip olmadığında hata yapmaya yatkındır. Bu durumda, kuruluşlar kullanıcıların pivot tablo tabanlı raporları değiştirmesini engellemek isteyebilir. Ek filtreler, dilimler, alanlar eklemek veya rapordaki bazı sıralamaları değiştirmek gibi yaygın özellikler genellikle tüm kullanıcılar için önerilmez. Öte yandan, bu kullanıcılar da raporu yenileme ve mevcut filtreleri veya dilimleri kullanma yetisine sahip olmalıdır. Aspose.Cells, bu raporları değiştirmenin engellenmesi için geliştiricilere bu yeteneği sağlar. Bu amaçla, Excel pivot tablo şeridini devre dışı bırakma özelliği sunar ve bu özellik Aspose.Cells tarafından da sağlanmıştır. Geliştiriciler, bu raporları değiştirme kontrollerini içeren şeridi devre dışı bırakabilir.

{{% /alert %}}

## **PivotTable.EnableWizard Kullanarak Pivot Tablo Şeridini Devre Dışı Bırakma**

Aşağıdaki kod, bir sayfadan pivot tabloya erişerek [**GetEnableWizard()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivottable/getenablewizard/) değerini **false** yapar. Bir örnek pivot tablo dosyasını buradan indirebilirsiniz: [bağlantı](pivot_table_test.xlsx).

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input excel file
    U16String inputFilePath = srcDir + u"pivot_table_test.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"out.xlsx";

    // Create workbook
    Workbook wb(inputFilePath);

    // Access the pivot table in the first sheet
    PivotTable pt = wb.GetWorksheets().Get(0).GetPivotTables().Get(0);

    // Disable ribbon for this pivot table
    pt.SetEnableWizard(false);

    // Save output file
    wb.Save(outputFilePath);

    std::cout << "Pivot table ribbon disabled successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
