---
title: C++ ile Sayfa Sekmesi Çubuğunu Nasıl Kontrol Edilir
linktitle: Sayfa Sekmesi Çubuğunu Nasıl Kontrol Edilir
type: docs
weight: 600
url: /tr/cpp/how-to-control-sheet-tab-bar/
description: Aspose.Cells for C++ API aracılığıyla Sayfa Sekmesi Çubuğunu Kontrol etmeyi öğrenin.
keywords: Sayfa Sekmesi Çubuğunu Kontrol Etme, Sayfa Sekmesi Çubuğunu Yönetme, Sayfa Sekmesi Çubuğunu Ayarlama, Sayfa Sekmesi Çubuğunu Kontrol Etme. 
---

## **Olası Kullanım Senaryoları**
Excel sayfa çubuğunun görüntüsünü ayarlamanız gerektiğinde, sayfa sekmesi çubuğunu nasıl kontrol edeceğinizi bilmeniz gerekir; örneğin, sayfa sekmesi çubuğunu gizleme veya gösterme, sayfa sekmesi genişliğini değiştirme, ilk görünür sekmeyi belirleme ve bunun gibi. Aspose.Cells bu özellikleri destekler. Aspose.Cells, hedeflerinize ulaşmanız için aşağıdaki özellikleri ve yöntemleri sağlar.

- [**WorkbookSettings.GetShowTabs()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getshowtabs/)
- [**WorkbookSettings.GetSheetTabBarWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getsheettabbarwidth/)
- [**WorkbookSettings.GetFirstVisibleTab()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getfirstvisibletab/)

## **Aspose.Cells for C++ kullanarak Sayfa Sekmesi Çubuğunu Nasıl Kontrol Edilir**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Sayfa sekmesini görüntüleyin ve sekme çubuğunun genişliğini ayarlayın.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a Workbook object
    Workbook workbook;

    // Obtain the reference to the newly added worksheet
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

    // Display the sheet tab and set the width of the tab bar
    workbook.GetSettings().SetShowTabs(true);
    workbook.GetSettings().SetSheetTabBarWidth(150);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

Sonuç dosyası önizlemesi:
<br>
<image src="result.png" width="70%" />

{{< app/cells/assistant language="cpp" >}}
