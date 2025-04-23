---
title: C++ ile Hücreler HTML Dizgisi Yönetimi
linktitle: Hücreleri Html Dizesi Yönetme
type: docs
weight: 600
url: /tr/cpp/manage-cells-html-string/
description: Aspose.Cells for C++ API ile Hücreler HTML Dizgisi Yönetimini nasıl öğrenilir.
keywords: Hücreye HTML Dizesi Ekle, Hücre İçine HTML Dizesi Ayarla, HTML Dizesi Ekle, Hücrenin HTML Dizesini Al, Hücreleri Html Dizesi Yönet
---

## **Olası Kullanım Senaryoları**
Belirli bir Hücre için biçimlendirilmiş veri ayarlamanız gerektiğinde, Hücreye bir HTML dizgisi atayabilirsiniz. Elbette, hücrenin HTML dizgisini de alabilirsiniz. Aspose.Cells bu özelliği sunar. Aspose.Cells, hedeflerinize ulaşmanıza yardımcı olacak aşağıdaki özellikleri ve metodları sağlar.
- [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)
- [**Cell::SetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/sethtmlstring/)

## **Aspose.Cells kullanarak html dizesini alın ve ayarlayın**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturun ve bazı verileri ekleyin.
1. İlk çalışma sayfasındaki belirli hücreyi alın.
1. HTML dizesini hücreye ayarlayın.
1. Hücrenin HTML dizisini alın.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a Workbook object
    Workbook workbook;

    // Obtain the reference of the newly added worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Setting the value to the cells
    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");

    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");

    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");

    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");

    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");

    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    Cell c3 = cells.Get(u"C3");
    // Set HTML string for C3 cell
    c3.SetHtmlString(u"<b>test bold</b>");

    Cell c4 = cells.Get(u"C4");
    // Set HTML string for C4 cell
    c4.SetHtmlString(u"<i>test italic</i>");

    // Get the HTML string of specific cell
    std::cout << c3.GetHtmlString().ToUtf8() << std::endl;
    std::cout << c4.GetHtmlString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

Örneğin ürettiği çıktı

Yukarıdaki örnek kodun çıktısını aşağıdaki ekran görüntüsünde görebilirsiniz.

![todo:image_alt_text](htmlstring.png)
