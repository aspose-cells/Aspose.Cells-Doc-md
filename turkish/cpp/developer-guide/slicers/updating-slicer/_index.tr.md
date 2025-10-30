---
title: Dilımleyiciyi Güncelleme (C++)
linktitle: Süzgeci Güncelleme
type: docs
weight: 50
url: /tr/cpp/updating-slicer/
description: Bu makale, Aspose.Cells for C++ API sini kullanarak dilimleyici güncelleyerek bağlı pivot tablolarını nasıl güncelleyeceğinizi gösterir.
keywords: Aspose.Cells C++ kullanarak dilimleyiciyi güncelleyin, C++ dilimleyiciyi nasıl değiştirilir, C++ kullanarak dilimleyiciyi nasıl ayarlarsınız, dilimleyici öğelerini seçip kaldırmak nasıl yapılır.
---

## **Olası Kullanım Senaryoları**

Microsoft Excel'de bir dilimleyiciyi güncellemek istiyorsanız, öğelerini seçin veya kaldırın, ardından dilimleyici tablosunu veya pivot tablosunu buna göre günceller. Lütfen Aspose.Cells ile dilimleyici öğelerini seçip kaldırmak için [**Slicer.GetSlicerCacheItems()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicercache/getslicercacheitems/) kullanın ve ardından [**Slicer.Refresh()**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/refresh/) yöntemini çağırarak dilimleyici tablosunu veya pivot tablosunu güncelleyin.

## **Süzgeci Nasıl Güncellenir**

Aşağıdaki örnek kod, mevcut bir süzgeç içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Süzgecin 2. ve 3. öğelerini seçmez ve süzgeci yeniler. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Ekran görüntüsünde, örnek kodun örnek Excel dosyasındaki etkisini görebilirsiniz. Ekran görüntüsünde, seçili öğelerle süzgeci yenilemenin aynı zamanda özet tabloyu da yenilediğini görebilirsiniz.

![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load sample Excel file containing slicer.
    U16String inputFilePath = u"sampleUpdatingSlicer.xlsx";
    Workbook wb(inputFilePath);

    // Access first worksheet.
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Access the first slicer inside the slicer collection.
    Slicer slicer = ws.GetSlicers().Get(0);

    // Access the slicer items.
    SlicerCacheItemCollection scItems = slicer.GetSlicerCache().GetSlicerCacheItems();

    SlicerCacheItemCollection items = slicer.GetSlicerCache().GetSlicerCacheItems();

    for (int i = 0; i < items.GetCount(); ++i)
    {
        SlicerCacheItem item = items.Get(i);
        if (item.GetValue() == u"Pink" || item.GetValue() == u"Green")
        {
            item.SetSelected(false);
        }
    }

    slicer.Refresh();

    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);

    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
