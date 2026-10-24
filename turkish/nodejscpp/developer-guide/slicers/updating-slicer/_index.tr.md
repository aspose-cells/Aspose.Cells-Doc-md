---
title: Node.js via C++ ile Dilimleyici Güncelleme
linktitle: Dilimleyici Güncelleme
type: docs
weight: 50
url: /tr/nodejs-cpp/updating-slicer/
description: Bu makale, Aspose.Cells for Node.js via C++ kullanılarak bağlantılı Pivot Tablosunun veya tablonun verilerini filtrelemek için dilimleyicinin nasıl güncelleneceğini gösterir.
keywords: Aspose.Cells Node.js via C++, Node.js dilimleyici güncelleme, Node.js dilimleyici nasıl değiştirilir, Node.js dilimleyici ile Pivot Tablosu nasıl filtrelenir, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Dilimleyici güncellemek, dilimleyicinin bağlı olduğu Pivot Tablosunun veya tablonun verilerini filtrelemek anlamına gelir. Microsoft Excel'de dilimleyici öğelerini seçtiğinizde veya seçimini kaldırdığınızda, bağlantılı Pivot Tablosu veya tablo buna göre yeniden hesaplanır. Aspose.Cells for Node.js via C++ ile dilimleyici önbelleği öğeleri arasında yineleme yapmanıza ve dilimleyiciyi elle yenilemenize gerek yoktur — [**Slicer.selectItems(labels, append)**](https://reference.aspose.com/cells/nodejs-cpp/slicer/) yöntemi dilimleyiciyi günceller ve bağlantılı Pivot Tablosunu veya tabloyu doğrudan filtre öğelerinden yeniden hesaplar:
- `Slicer.selectItems(labels, append)` — belirtilen etiketleri seçer ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplar. `append` `true` olduğunda, başlangıçta seçili etiketler korunur ve belirtilen etiketler seçime eklenir; `append` `false` olduğunda, tüm başlangıç seçimleri temizlenir ve yalnızca belirtilen etiketler seçili kalır.
- `Slicer.unselectItems(labels)` — o anda seçili öğelerin bir kısmının seçimini kaldırır.
- `Slicer.clearFilter()` — filtreyi kaldırır ve tüm öğeleri seçer.

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ 26.10 sürümünden itibaren `SlicerCacheItem.Selected` özelliği salt okunur hale gelir ve ayarlayıcısı artık desteklenmez. `SlicerCacheItem.Selected` özelliğini öğe öğe ayarlamak yerine `Slicer.selectItems`, `Slicer.unselectItems` ve `Slicer.clearFilter` yöntemlerini kullanın.
{{% /alert %}}

## **Dilimleyici Nasıl Güncellenir**
Aşağıdaki örnek kod, bir Pivot Tablosuna bağlı mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Dilimleyicinin yalnızca "Blue" ve "Pink" öğelerini `Slicer.selectItems(labels, false)` ile seçer — Pivot Tablosu, elle bir `Slicer.refresh()` çağrısı yapılmadan doğrudan filtre öğelerinden yeniden hesaplanır. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi Pivot Tablosu yalnızca filtrelenmiş öğeleri gösterir.
![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**
Mevcut seçimi değiştirin (yalnızca belirtilen etiketler seçili kalır) ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplayın:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], false);
// Save the modified workbook.
wb.save("out.xlsx");
```

Şu anda seçili etiketleri koruyun ve ek olarak daha fazla öğe seçin:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], true);
```

Seçili öğelerin bir kısmının seçimini kaldırın:

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"]);
```

Filtreyi kaldırın (tüm öğeleri seçin):

```javascript
const AsposeCells = require("aspose.cells.node");
// Load sample Excel file containing slicer.
const wb = new AsposeCells.Workbook("sampleUpdatingSlicer.xlsx");
// Access the first worksheet.
const ws = wb.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
const slicer = ws.getSlicers().get(0);
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="nodejs-cpp" >}}