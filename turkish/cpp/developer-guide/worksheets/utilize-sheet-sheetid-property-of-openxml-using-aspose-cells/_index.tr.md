---
title: OpenXml ile Sheet.SheetId özelliğini C++ kullanarak kullanın
linktitle: OpenXml Sheet.SheetId özelliğini kullanın
type: docs
weight: 200
url: /tr/cpp/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/
description: Bu makale, Excel manipülasyonu C++ API veya Kitaplığı kullanarak OpenXml ile Sheet.SheetId özelliğinin nasıl kullanılacağını gösterir.
keywords: openxml c++, sayfa id özelliği, excel sayfaıd c++
---

## **Olası Kullanım Senaryoları**

*Sheet.SheetId*, *DocumentFormat.OpenXml.Spreadsheet* ad alanı içinde bulunan ve OpenXml'in bir parçası olan bir özelliktir. Bu özelliği ve değerini aşağıdaki ekran görüntüsünde gösterildiği gibi *workbook.xml* içinde görebilirsiniz. Aspose.Cells, bu özelliğin dengi olarak [**Worksheet.GetTabId()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/gettabid/) özelliğini sunar.

![todo:image_alt_text](utilize-sheet-sheetid-property-of-openxml-using-aspose-cells_1.png)

## **Aspose.Cells üzerinde Sheet.SheetId özelliğini kullanarak OpenXml'in faydalanılması**

Aşağıdaki örnek kod, [örnek Excel dosyasını](51740716.xlsx) yükler, Sayfa veya Sekme Kimliğini okur, ardından yeni Sekme Kimliğini atar ve [çıktı Excel dosyası](51740717.xlsx) olarak kaydeder. Ayrıca, aşağıda verilen kodun konsol çıktısını da inceleyin.

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load source Excel file
    Workbook wb(u"sampleSheetId.xlsx");

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Print its Sheet or Tab Id on console
    std::cout << "Sheet or Tab Id: " << ws.GetTabId() << std::endl;

    // Change Sheet or Tab Id
    ws.SetTabId(358);

    // Save the workbook
    wb.Save(u"outputSheetId.xlsx");

    Aspose::Cells::Cleanup();

    return 0;
}
```

## **Konsol Çıktısı**

{{< highlight java >}}

Sheet or Tab Id: 1297

{{< /highlight >}}
