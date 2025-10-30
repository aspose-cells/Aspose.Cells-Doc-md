---
title: C++ ile Çalışma Kitabı Görünümünü Nasıl Kontrol Edilir
linktitle: Çalışma Kitabı Görünümünü Kontrol Etme
type: docs
weight: 600
url: /tr/cpp/how-to-control-workbook-view/
description: Aspose.Cells for C++ API kullanarak çalışma kitabı görünümünü nasıl kontrol edeceğinizi öğrenin.
keywords: Çalışma Kitabı Görünümünü Kontrol Etme, Excel Görünümü Ayarlama, Çalışma Kitabı Görünümünü İşletme, Çalışma Kitabı Görünümü Ayarlama, Excel Görünümünü Kontrol Etme.
---

## **Olası Kullanım Senaryoları**
Excel sayfalarının görüntüsünü ayarlamanız gerektiğinde, her modülü nasıl kontrol edeceğinizi bilmeniz gerekir; örneğin, yatay ve dikey kaydırıcılar, açık Excel dosyalarını gizleyip gizlememe ve diğerleri. Aspose.Cells bu özelliği sunar. Aspose.Cells, hedeflerinize ulaşmanız için aşağıdaki özellikleri ve yöntemleri sağlar.

- [**WorkbookSettings.IsHScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishscrollbarvisible/)
- [**WorkbookSettings.IsVScrollBarVisible**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isvscrollbarvisible/)
- [**WorkbookSettings.IsHidden**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/ishidden/)
- [**WorkbookSettings.IsMinimized**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/isminimized/)
- [**WorkbookSettings.GetWindowHeight()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowheight/)
- [**WorkbookSettings.GetWindowWidth()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowwidth/)
- [**WorkbookSettings.GetWindowLeft()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowleft/)
- [**WorkbookSettings.GetWindowTop()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getwindowtop/)

## **Aspose.Cells for C++ kullanarak Çalışma Kitabı Görünümünü Nasıl Kontrol Edilir**
Bu örnek aşağıdakileri göstermektedir:

1. Bir çalışma kitabı oluşturma.
1. İlk çalışma sayfasındaki hücrelere veri ekleme.
1. Çalışma Kitabı Görünümünün yatay ve dikey kaydırma çubuklarını gizleme.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    // Set values to cells
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

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    // Apply style to cell E10
    cell = cells.Get(u"E10");
    Style temp = workbook.CreateStyle();
    temp.GetFont().SetColor(Color::Red());
    cell.SetStyle(temp);

    // Hide horizontal and vertical scrollbars
    workbook.GetSettings().SetIsHScrollBarVisible(false);
    workbook.GetSettings().SetIsVScrollBarVisible(false);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
}
```

Sonuç dosyası önizlemesi:
<br>
<image src="result.png" width="70%" />
{{< app/cells/assistant language="cpp" >}}
