---
title: C++ ile Sayfa Diyalog Sayfası olup olmadığını bulun
linktitle: Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma
type: docs
weight: 90
url: /tr/cpp/find-if-the-worksheet-is-dialog-sheet/
description: Diyalog Sayfası eski bir sayfa formatıdır. Bu makale, C++ API kullanarak bir Excel çalışma sayfasının Diyalog Sayfası olup olmadığını programlı olarak belirlemek için talimatlar ve örnek kodlar sağlar.
keywords: Excel çalışma sayfası diyaloğu türünü bulma C++, çalışma sayfası diyaloğu C++ ile
---

## **Olası Kullanım Senaryoları**

Diyalog Sayfa, içinde bir diyalog kutusu bulunan eski bir sayfa formatıdır. Bu tür bir sayfa, Microsoft Excel'in eski bir sürümü olan örneğin 2003'ün bir görüntüsünde gösterildiği gibi eklenebilir. Ayrıca, Microsoft Excel 2016 gibi yeni sürümlerde VBA ile de eklenebilir.

![todo:image_alt_text](find-if-the-worksheet-is-dialog-sheet_1.png)

Aspose.Cells tarafından sağlanan [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) özelliği kullanılarak, sayfanın diyaloğu sayfası mı yoksa başka bir türü mü olduğu bulunabilir. Eğer belge, [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) değerini döndürüyorsa, bu, diyaloğu sayfası ile ilgilendiğinizi gösterir.

## **Çalışma Sayfasının Diyaloğu Sayfa Olup Olmadığını Bulma**

Aşağıdaki örnek kod, diyaloğu sayfası içeren örnek Excel dosyasını (64716820.xlsx) yükler. [**Worksheet.GetType()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettype/) özelliğini kontrol eder, [**SheetType.Dialog**](https://reference.aspose.com/cells/cpp/aspose.cells/sheettype/) ile karşılaştırır ve ardından mesajı yazdırır. Daha fazla yardım için aşağıdaki örnek kodun konsol çıktısına bakın.

## **Örnek Kod**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load Excel file containing Dialog Sheet
    Workbook workbook(u"sampleFindIfWorksheetIsDialogSheet.xlsx");

    // Access first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);

    // Find if the sheet type is dialog and print the message
    if (ws.GetType() == SheetType::Dialog)
    {
        std::cout << "Worksheet is a Dialog Sheet." << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Worksheet is a Dialog Sheet.

{{< /highlight >}}
