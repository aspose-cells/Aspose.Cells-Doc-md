---
title: Golang via C++ ile Dilimleyici Güncelleme
linktitle: Dilimleyici Güncelleme
type: docs
weight: 50
url: /tr/go-cpp/updating-slicer/
ai_search_scope: cells_gocpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
description: Bu makale, Aspose.Cells for Go via C++ API kullanılarak bağlantılı Pivot Tablosunun veya tablonun verilerini filtrelemek için dilimleyicinin nasıl güncelleneceğini gösterir.
keywords: Aspose.Cells Go via C++ Dilimleyici güncelleme, Go dilimleyici nasıl değiştirilir, Go dilimleyici ile Pivot Tablosu nasıl filtrelenir, Slicer SelectItems, Slicer ClearFilter, Slicer UnselectItems.
---

## **Olası Kullanım Senaryoları**
Dilimleyici güncellemek, dilimleyicinin bağlı olduğu Pivot Tablosunun veya tablonun verilerini filtrelemek anlamına gelir. Microsoft Excel'de dilimleyici öğelerini seçtiğinizde veya seçimini kaldırdığınızda, bağlantılı Pivot Tablosu veya tablo buna göre yeniden hesaplanır. Aspose.Cells for Go via C++ ile dilimleyici önbelleği öğeleri arasında yineleme yapmanıza ve dilimleyiciyi elle yenilemenize gerek yoktur — [**Slicer.SelectItems(labels, append)**](https://reference.aspose.com/cells/go-cpp/slicer/) yöntemi dilimleyiciyi günceller ve bağlantılı Pivot Tablosunu veya tabloyu doğrudan filtre öğelerinden yeniden hesaplar:
- `Slicer.SelectItems(labels, append)` — belirtilen etiketleri seçer ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplar. `append` `true` olduğunda, başlangıçta seçili etiketler korunur ve belirtilen etiketler seçime eklenir; `append` `false` olduğunda, tüm başlangıç seçimleri temizlenir ve yalnızca belirtilen etiketler seçili kalır.
- `Slicer.UnselectItems(labels)` — o anda seçili öğelerin bir kısmının seçimini kaldırır.
- `Slicer.ClearFilter()` — filtreyi kaldırır ve tüm öğeleri seçer.

{{% alert color="primary" %}}
Aspose.Cells for Go via C++ 26.10 sürümünden itibaren `SlicerCacheItem.Selected` özelliği salt okunur hale gelir ve ayarlayıcısı artık desteklenmez. `SlicerCacheItem.Selected` özelliğini öğe öğe ayarlamak yerine `Slicer.SelectItems`, `Slicer.UnselectItems` ve `Slicer.ClearFilter` yöntemlerini kullanın.
{{% /alert %}}

## **Dilimleyici Nasıl Güncellenir**
Aşağıdaki örnek kod, bir Pivot Tablosuna bağlı mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Dilimleyicinin yalnızca "Blue" ve "Pink" öğelerini `Slicer.SelectItems(labels, false)` ile seçer — Pivot Tablosu, elle bir `Slicer.Refresh()` çağrısı yapılmadan doğrudan filtre öğelerinden yeniden hesaplanır. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi Pivot Tablosu yalnızca filtrelenmiş öğeleri gösterir.
![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**
Mevcut seçimi değiştirin (yalnızca belirtilen etiketler seçili kalır) ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplayın:

```go
package main

import (
    "fmt"

    . "github.com/aspose-cells/aspose-cells-go-cpp/v26"
)

func main() {
    // Load sample Excel file containing slicer.
    wb, _ := NewWorkbook_String("sampleUpdatingSlicer.xlsx")

    // Access first worksheet.
    wss, _ := wb.GetWorksheets()
    ws, _ := wss.Get_Int(0)

    // Access the first slicer inside the slicer collection.
    slicers, _ := ws.GetSlicers()
    slicer, _ := slicers.Get_Int(0)

    // Select only "Blue" and "Pink"; the linked pivot table or table
    // is recalculated directly from the filter items.
    slicer.SelectItems([]string{ "Blue", "Pink" }, false)

    // Save the modified workbook.
    wb.Save_String("out.xlsx")

    fmt.Println("Slicer updated and workbook saved successfully!")
}
```

Şu anda seçili etiketleri koruyun ve ek olarak daha fazla öğe seçin:

```go
// Keep the current selection and add "Red" to it.
slicer.SelectItems([]string{ "Red" }, true)
```

Seçili öğelerin bir kısmının seçimini kaldırın:

```go
// Remove "Pink" from the current selection.
slicer.UnselectItems([]string{ "Pink" })
```

Filtreyi kaldırın (tüm öğeleri seçin):

```go
// Clear the filter; all slicer items become selected again.
slicer.ClearFilter()
```

{{< app/cells/assistant language="go" >}}