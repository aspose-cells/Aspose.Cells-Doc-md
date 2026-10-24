---
title: Dilimleyici Güncelleme
linktitle: Dilimleyici Güncelleme
type: docs
weight: 50
url: /tr/java/updating-slicer/
description: Bu makale, Aspose.Cells for Java API kullanılarak bağlantılı Pivot Tablosunun veya tablonun verilerini filtrelemek için dilimleyicinin nasıl güncelleneceğini gösterir.
keywords: Aspose.Cells Java Dilimleyici güncelleme, Java dilimleyici nasıl değiştirilir, Java dilimleyici ile Pivot Tablosu nasıl filtrelenir, Java Slicer selectItems, Java Slicer clearFilter, Java Slicer unselectItems.
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Dilimleyici güncellemek, dilimleyicinin bağlı olduğu Pivot Tablosunun veya tablonun verilerini filtrelemek anlamına gelir. Microsoft Excel'de dilimleyici öğelerini seçtiğinizde veya seçimini kaldırdığınızda, bağlantılı Pivot Tablosu veya tablo buna göre yeniden hesaplanır. Aspose.Cells for Java ile dilimleyici önbelleği öğeleri arasında yineleme yapmanıza ve dilimleyiciyi elle yenilemenize gerek yoktur — [Slicer.selectItems(String[], boolean)](https://reference.aspose.com/cells/java/com.aspose.cells/slicer/#selectItems-java.lang.String---boolean-) yöntemi dilimleyiciyi günceller ve bağlantılı Pivot Tablosunu veya tabloyu doğrudan filtre öğelerinden yeniden hesaplar:
- `Slicer.selectItems(labels, append)` — belirtilen etiketleri seçer ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplar. `append` `true` olduğunda, başlangıçta seçili etiketler korunur ve belirtilen etiketler seçime eklenir; `append` `false` olduğunda, tüm başlangıç seçimleri temizlenir ve yalnızca belirtilen etiketler seçili kalır.
- `Slicer.unselectItems(labels)` — o anda seçili öğelerin bir kısmının seçimini kaldırır.
- `Slicer.clearFilter()` — filtreyi kaldırır ve tüm öğeleri seçer.

{{% alert color="primary" %}}
Aspose.Cells for Java 26.10 sürümünden itibaren `SlicerCacheItem.Selected` özelliği salt okunur hale gelir ve ayarlayıcısı artık desteklenmez. `SlicerCacheItem.Selected` özelliğini öğe öğe ayarlamak yerine `Slicer.selectItems`, `Slicer.unselectItems` ve `Slicer.clearFilter` yöntemlerini kullanın.
{{% /alert %}}

## **Dilimleyici Güncelleme**
Aşağıdaki örnek kod, bir Pivot Tablosuna bağlı mevcut bir dilimleyici içeren [örnek Excel dosyasını](67338506.xlsx) yükler. Dilimleyicinin yalnızca "Blue" ve "Pink" öğelerini `Slicer.selectItems(labels, false)` ile seçer — Pivot Tablosu, elle bir `Slicer.refresh()` çağrısı yapılmadan doğrudan filtre öğelerinden yeniden hesaplanır. Ardından çalışma kitabını [çıktı Excel dosyası](67338505.xlsx) olarak kaydeder. Aşağıdaki ekran görüntüsü, örnek kodun örnek Excel dosyası üzerindeki etkisini göstermektedir. Ekran görüntüsünde görebileceğiniz gibi Pivot Tablosu yalnızca filtrelenmiş öğeleri gösterir.
![todo:image_alt_text](updating-slicer_1.png)

## **Örnek Kod**
Mevcut seçimi değiştirin (yalnızca belirtilen etiketler seçili kalır) ve bağlantılı Pivot Tablosunu veya tabloyu yeniden hesaplayın:

```java
import com.aspose.cells.Workbook;
import com.aspose.cells.Worksheet;
import com.aspose.cells.Slicer;
// Load sample Excel file containing slicer.
Workbook workbook = new Workbook("sampleUpdatingSlicer.xlsx");
// Access first worksheet.
Worksheet worksheet = workbook.getWorksheets().get(0);
// Access the first slicer inside the slicer collection.
Slicer slicer = worksheet.getSlicers().get(0);
// Select only "Blue" and "Pink"; the linked pivot table or table
// is recalculated directly from the filter items.
slicer.selectItems(new String[] { "Blue", "Pink" }, false);
// Save the modified workbook.
workbook.save("out.xlsx");
```

Şu anda seçili etiketleri koruyun ve ek olarak daha fazla öğe seçin:

```java
// Keep the current selection and add "Red" to it.
slicer.selectItems(new String[] { "Red" }, true);
```

Seçili öğelerin bir kısmının seçimini kaldırın:

```java
// Remove "Pink" from the current selection.
slicer.unselectItems(new String[] { "Pink" });
```

Filtreyi kaldırın (tüm öğeleri seçin):

```java
// Clear the filter; all slicer items become selected again.
slicer.clearFilter();
```

{{< app/cells/assistant language="java" >}}