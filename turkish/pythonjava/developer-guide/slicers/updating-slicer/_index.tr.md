---
title: Dilimleyici Güncelleme
linktitle: Dilimleyici Güncelleme
type: docs
weight: 60
url: /tr/python-java/updating-slicer/
description: Bu makale, Aspose.Cells for Python via Java API kullanılarak bağlantılı Pivot Tablosunun veya tablonun verilerini filtrelemek için dilimleyicinin nasıl güncelleneceğini gösterir.
keywords: Aspose.Cells for Python via Java Dilimleyici güncelleme, Python Java dilimleyici güncelleme, Python dilimleyici ile Pivot Tablosu nasıl filtrelenir, Slicer selectItems, Slicer clearFilter, Slicer unselectItems.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Dilimleyici Güncelleme**
Dilimleyici güncellemek, dilimleyicinin bağlı olduğu Pivot Tablosunun veya tablonun verilerini filtrelemek anlamına gelir. Aspose.Cells for Python via Java, dilimleyiciyi günceller ve bağlantılı Pivot Tablosunu veya tabloyu doğrudan filtre öğelerinden yeniden hesaplar:
- `Slicer.selectItems(labels, append)` — belirtilen etiketleri seçer ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplar. `append` `True` olduğunda, başlangıçta seçili etiketler korunur ve belirtilen etiketler seçime eklenir; `append` `False` olduğunda, tüm başlangıç seçimleri temizlenir ve yalnızca belirtilen etiketler seçili kalır.
- `Slicer.unselectItems(labels)` — o anda seçili öğelerin bir kısmının seçimini kaldırır.
- `Slicer.clearFilter()` — filtreyi kaldırır ve tüm öğeleri seçer.

{{% alert color="primary" %}}
Aspose.Cells for Python via Java 26.10 sürümünden itibaren `SlicerCacheItem.Selected` özelliği salt okunur hale gelir ve ayarlayıcısı artık desteklenmez. `SlicerCacheItem.Selected` özelliğini öğe öğe ayarlamak yerine `Slicer.selectItems`, `Slicer.unselectItems` ve `Slicer.clearFilter` yöntemlerini kullanın.
Aşağıdaki kod parçası, bir Pivot Tablosuna bağlı bir dilimleyici içeren [örnek Excel dosyasını](106365050.xlsx) yükler. Dilimleyicinin yalnızca "Blue" ve "Pink" öğelerini `Slicer.selectItems(labels, False)` ile seçer — Pivot Tablosu, elle bir `Slicer.refresh()` çağrısı yapılmadan doğrudan filtre öğelerinden yeniden hesaplanır. Ardından çalışma kitabını [çıktı Excel dosyası](106365051.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi Pivot Tablosu yalnızca filtrelenmiş öğeleri gösterir.
![todo:image_alt_text](Updating-Slicer-using-Aspose.Cells.png)
{{% /alert %}}

## **Örnek Kod**
Mevcut seçimi değiştirin (yalnızca belirtilen etiketler seçili kalır) ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplayın:

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Load sample Excel file containing slicer.
workbook = Workbook("sampleUpdatingSlicer.xlsx")
# Access first worksheet.
worksheet = workbook.getWorksheets().get(0)
# Access the first slicer inside the slicer collection.
slicer = worksheet.getSlicers().get(0)
# Select only "Blue" and "Pink"; the linked pivot table or table
# is recalculated directly from the filter items.
slicer.selectItems(["Blue", "Pink"], False)
# Save the modified workbook.
workbook.save("out.xlsx")
jpype.shutdownJVM()
```

Şu anda seçili etiketleri koruyun ve ek olarak daha fazla öğe seçin:

```python
# Keep the current selection and add "Red" to it.
slicer.selectItems(["Red"], True)
```

Seçili öğelerin bir kısmının seçimini kaldırın:

```python
# Remove "Pink" from the current selection.
slicer.unselectItems(["Pink"])
```

Filtreyi kaldırın (tüm öğeleri seçin):

```python
# Clear the filter; all slicer items become selected again.
slicer.clearFilter()
```

{{< app/cells/assistant language="python" >}}