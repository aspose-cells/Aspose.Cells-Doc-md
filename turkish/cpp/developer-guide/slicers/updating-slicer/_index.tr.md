---
title: C++ ile Dilimleyici Güncelleme
linktitle: Dilimleyici Güncelleme
type: docs
weight: 50
url: /tr/cpp/updating-slicer/
description: Bu makale, Aspose.Cells for C++ API kullanılarak bağlantılı Pivot Tablosunun veya tablonun verilerini filtrelemek için dilimleyicinin nasıl güncelleneceğini gösterir.
keywords: Aspose.Cells C++ Dilimleyici güncelleme, C++ dilimleyici nasıl değiştirilir, C++ dilimleyici ile Pivot Tablosu nasıl filtrelenir, C++ Slicer SelectItems, C++ Slicer ClearFilter, C++ Slicer UnselectItems.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Dilimleyici güncellemek, dilimleyicinin bağlı olduğu Pivot Tablosunun veya tablonun verilerini filtrelemek anlamına gelir. Microsoft Excel'de dilimleyici öğelerini seçtiğinizde veya seçimini kaldırdığınızda, bağlantılı Pivot Tablosu veya tablo buna göre yeniden hesaplanır. Aspose.Cells for C++ ile dilimleyici önbelleği öğeleri arasında yineleme yapmanıza ve dilimleyiciyi elle yenilemenize gerek yoktur — [**Slicer.SelectItems(Vector&lt;U16String&gt;, bool)**](https://reference.aspose.com/cells/cpp/aspose.cells.slicers/slicer/selectitems/) yöntemi dilimleyiciyi günceller ve bağlantılı Pivot Tablosunu veya tabloyu doğrudan filtre öğelerinden yeniden hesaplar:
- `Slicer.SelectItems(labels, append)` — belirtilen etiketleri seçer ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplar. `append` `true` olduğunda, başlangıçta seçili etiketler korunur ve belirtilen etiketler seçime eklenir; `append` `false` olduğunda, tüm başlangıç seçimleri temizlenir ve yalnızca belirtilen etiketler seçili kalır.
- `Slicer.UnselectItems(labels)` — o anda seçili öğelerin bir kısmının seçimini kaldırır.
- `Slicer.ClearFilter()` — filtreyi kaldırır ve tüm öğeleri seçer.

{{% alert color="primary" %}}
Aspose.Cells for C++ 26.10 sürümünden itibaren `SlicerCacheItem.Selected` özelliği salt okunur hale gelir ve ayarlayıcısı artık desteklenmez. `SlicerCacheItem.Selected` özelliğini öğe öğe ayarlamak yerine `Slicer.SelectItems`, `Slicer.UnselectItems` ve `Slicer.ClearFilter` yöntemlerini kullanın.
{{% /alert %}}

## **Dilimleyici Nasıl Güncellenir**
Aşağıdaki örnek kod, bir Pivot Tablosuna bağlı mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Dilimleyicinin yalnızca "Blue" ve "Pink" öğelerini `Slicer.SelectItems(labels, false)` ile seçer — Pivot Tablosu, elle bir `Slicer.Refresh()` çağrısı yapılmadan doğrudan filtre öğelerinden yeniden hesaplanır. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi Pivot Tablosu yalnızca filtrelenmiş öğeleri gösterir.
![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**
Mevcut seçimi değiştirin (yalnızca belirtilen etiketler seçili kalır) ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplayın:

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
    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    Vector<U16String> labels{ u"Blue", u"Pink" };
    slicer.SelectItems(labels, false);
    // Save the modified workbook.
    U16String outputFilePath = u"out.xlsx";
    wb.Save(outputFilePath);
    std::cout << "Slicer updated and workbook saved successfully!" << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Şu anda seçili etiketleri koruyun ve ek olarak daha fazla öğe seçin:

```cpp
// Keep the current selection and add "Red" to it.
Vector<U16String> moreLabels{ u"Red" };
slicer.SelectItems(moreLabels, true);
```

Seçili öğelerin bir kısmının seçimini kaldırın:

```cpp
// Remove "Pink" from the current selection.
Vector<U16String> toRemove{ u"Pink" };
slicer.UnselectItems(toRemove);
```

Filtreyi kaldırın (tüm öğeleri seçin):

```cpp
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter();
```

{{< app/cells/assistant language="cpp" >}}