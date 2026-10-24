---
title: Dilimleyici Güncelleme
linktitle: Dilimleyici Güncelleme
type: docs
weight: 50
url: /tr/python-net/updating-slicer/
description: Aspose.Cells for Python via .NET ile bağlantılı Pivot Tablosunun veya tablonun verilerini filtrelemek için dilimleyicinin nasıl güncelleneceğini öğrenin.
keywords: Aspose.Cells for Python Excel, Excel Python kitaplığı, Excel olmadan Python ile dilimleyici güncelleme, Python dilimleyici ile Pivot Tablosu filtreleme, Slicer select_items, Slicer clear_filter.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Dilimleyici güncellemek, dilimleyicinin bağlı olduğu Pivot Tablosunun veya tablonun verilerini filtrelemek anlamına gelir. Microsoft Excel'de dilimleyici öğelerini seçtiğinizde veya seçimini kaldırdığınızda, bağlantılı Pivot Tablosu veya tablo buna göre yeniden hesaplanır. Aspose.Cells for Python via .NET ile dilimleyici önbelleği öğeleri arasında yineleme yapmanıza ve dilimleyiciyi elle yenilemenize gerek yoktur — [**Slicer.select_items(labels, append)**](https://reference.aspose.com/cells/python-net/aspose.cells.slicers/slicer/selectitems/) yöntemi dilimleyiciyi günceller ve bağlantılı Pivot Tablosunu veya tabloyu doğrudan filtre öğelerinden yeniden hesaplar:
- `Slicer.select_items(labels, append)` — belirtilen etiketleri seçer ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplar. `append` `True` olduğunda, başlangıçta seçili etiketler korunur ve belirtilen etiketler seçime eklenir; `append` `False` olduğunda, tüm başlangıç seçimleri temizlenir ve yalnızca belirtilen etiketler seçili kalır.
- `Slicer.unselect_items(labels)` — o anda seçili öğelerin bir kısmının seçimini kaldırır.
- `Slicer.clear_filter()` — filtreyi kaldırır ve tüm öğeleri seçer.

{{% alert color="primary" %}}
Aspose.Cells for Python via .NET 26.10 sürümünden itibaren `SlicerCacheItem.selected` özelliği salt okunur hale gelir ve ayarlayıcısı artık desteklenmez. `SlicerCacheItem.selected` özelliğini öğe öğe ayarlamak yerine `Slicer.select_items`, `Slicer.unselect_items` ve `Slicer.clear_filter` yöntemlerini kullanın.
{{% /alert %}}

## **Aspose.Cells for Python Excel Kitaplığı Kullanılarak Dilimleyici Nasıl Güncellenir**
Aşağıdaki örnek kod, bir Pivot Tablosuna bağlı mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338475.xlsx) yükler. Dilimleyicinin yalnızca "Blue" ve "Pink" öğelerini `Slicer.select_items(labels, False)` ile seçer — Pivot Tablosu, elle bir `Slicer.refresh()` çağrısı yapılmadan doğrudan filtre öğelerinden yeniden hesaplanır. Ardından çalışma kitabını [çıktı Excel dosyası](67338476.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi Pivot Tablosu yalnızca filtrelenmiş öğeleri gösterir.
![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**
Mevcut seçimi değiştirin (yalnızca belirtilen etiketler seçili kalır) ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplayın:

```python
import aspose.cells as ac
# Load sample Excel file containing slicer.
workbook = ac.Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.worksheets[0]
# Access the first slicer inside the slicer collection.
slicer = worksheet.slicers[0]
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.select_items(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
```

Şu anda seçili etiketleri koruyun ve ek olarak daha fazla öğe seçin:

```python
# Keep the current selection and add "Red" to it.
slicer.select_items(["Red"], True)
```

Seçili öğelerin bir kısmının seçimini kaldırın:

```python
# Remove "Pink" from the current selection.
slicer.unselect_items(["Pink"])
```

Filtreyi kaldırın (tüm öğeleri seçin):

```python
# Clear the filter; all slicer items become selected again.
slicer.clear_filter()
```

{{< app/cells/assistant language="python-net" >}}