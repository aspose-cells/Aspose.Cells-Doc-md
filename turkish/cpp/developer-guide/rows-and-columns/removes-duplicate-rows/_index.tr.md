---
title: C++ kullanarak Çalışma Sayfasındaki yinelenen satırları kaldırma
linktitle: Çalışma sayfasında tekrarlanan satırları kaldırma
type: docs
weight: 370
url: /tr/cpp/remove-duplicate-rows-in-a-worksheet/
description: Aspose.Cells for C++ kullanarak çalışma sayfasında yinelenen satırları nasıl kaldıracağınızı öğrenin.
---

{{% alert color="primary" %}}

Yinelenen satırları kaldırmak, Microsoft Excel'in birçok kullanışlı özelliklerinden biridir. Kullanıcıların bir Çalışma Sayfasındaki yinelenen satırları kaldırmasına olanak tanır ve hangi sütunların yinelenen bilgiler için kontrol edileceğini seçebilirsiniz.

Aspose.Cells, bu amaçla `Cells::RemoveDuplicates()` metodunu sağlar. Ayrıca, sütunları seçmek için `startRow`, `startColumn`, `endRow` ve `endColumn` ayarlayabilirsiniz.

Bu özelliği test etmek için indirilebilecek örnek dosyalar aşağıda sunulmuştur:

[removeduplicates.xlsx](removeduplicates.xlsx)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create workbook
    Workbook book(u"removeduplicates.xlsx");

    // Remove duplicates from the first worksheet
    book.GetWorksheets().Get(0).GetCells().RemoveDuplicates(0, 0, 5, 3);

    // Save the result
    book.Save(u"removeduplicates-result.xlsx");

    std::cout << "Duplicates removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

{{% /alert %}}
