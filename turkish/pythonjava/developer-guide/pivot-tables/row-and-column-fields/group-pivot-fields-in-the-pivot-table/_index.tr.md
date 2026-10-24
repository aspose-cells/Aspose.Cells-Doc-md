---
title: Pivot Tablosunda Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Pivot Alanlarını Gruplama
description: Aspose.Cells for Python via Java'da PivotField.group ve PivotFieldGroupOptions kullanarak bir pivot tablodaki satır ve sütun pivot alanlarını aylar ve çeyrekler gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplayacağınızı öğrenin.
keywords: Aspose.Cells, pivot tablosu, pivot alanı gruplama, PivotField.group, PivotFieldGroupOptions, tarih gruplama, sayı gruplama, aylar, çeyrekler, sayısal aralık, Python
type: docs
weight: 80
url: /tr/python-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplamak, bir pivot tablosunun satır veya sütun alanı çok sayıda farklı öğe içerdiğinde kullanışlıdır; örneğin yüzlerce tarih içeren bir tarih alanı veya birçok dağınık değere sahip bir sayısal alan. Gruplama bu öğeleri anlamlı bölümlere daraltır: tarihleri aylara, çeyreklere ve yıllara; sayıları ise 0-1, 2-3, 4-5 gibi aralıklara dönüştürür. Bu, büyük bir pivot tablosunu kompakt ve analiz edilmesi kolay hale getirir. Aspose.Cells bu yeteneği `PivotField.group()` yöntemi (veri türüne göre otomatik gruplama) ve `PivotField.group(PivotFieldGroupOptions)` (özel gruplama seçenekleri) aracılığıyla sağlar.
- Tarih gruplama, tek tek tarihleri günler, aylar, çeyrekler ve yıllar gibi daha büyük dönemlere yuvarlar ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zaman içindeki eğilimler bir bakışta görünür hale gelir ve her dönem seviyesi pivot tablosunun satır veya sütun alanında kendi pivot alanı olur.
- Gruplama yalnızca pivot tablosunun SATIR veya SÜTUN alanına yerleştirilmiş alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplanamaz. Böyle bir alanı gruplamak için önce onu pivot tablosunun satır veya sütun alanına eklemelisiniz.

## **Pivot Alanlarını Otomatik Olarak Gruplama**
Parametresiz `PivotField.group()` aşırı yüklemesi, alanın veri türünü inceler ve onu otomatik olarak gruplar. Yalnızca tarihler (ve boşluklar) içeren bir alan aylara göre gruplanır. Yalnızca sayılar (ve boşluklar) içeren bir alan, otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
# Örnek çalışma kitabını yükle
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# İkinci çalışma sayfasına ve özet tablosuna erişin
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# İlk satır alanını otomatik olarak gruplayın.
# Alan tarihler içerdiğinden aylara göre gruplanır.
field = pt.getRowFields().get(0)
field.group()
# Özet tablo verilerini hesaplayın ve çıktı dosyasını kaydedin
pt.calculateData()
wb.save("outputAutoGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Pivot Alanlarını Özel Seçeneklerle Gruplama**
`PivotFieldGroupOptions` sınıfı özel gruplama yapılandırması sağlar. Tarih alanları için `StartDate`, `EndDate` ve `GroupTypes` ayarlayın. Sayısal alanlar için `StartNumber`, `EndNumber` ve `Interval` ayarlayın. `NewPivotField` özelliği, gruplamanın orijinal alanın yanında yeni pivot alanları oluşturup oluşturmadığını kontrol eder (bu makalenin sonundaki Not bölümüne bakın).

### **Tarih Alanını Aylara ve Çeyreklere Göre Gruplama**
Aşağıdaki örnek, örnek pivot tablosunun tarih satır alanını bir başlangıç ve bitiş tarihi arasında aylara ve çeyreklere göre gruplar. Kod [örn. Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplamayı gerçekleştirir, pivot tablo verilerini hesaplar ve gruplanmış sonucu kaydeder. Ekran görüntüsü etkiyi gösterir: tarih satır alanı artık çeyreklere ve aylara göre gruplanmıştır.
`options.GroupTypes` içindeki değerlerin sırasının yok sayıldığını unutmayın. Grup türleri hangi sırayla listelenirse listelensin, gruplanmış alanlar her zaman en büyük dönemden en küçüğe doğru görüntülenir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte aylar `options.GroupTypes` içinde çeyreklerden önce listelenir, ancak çeyrekler dış seviye, aylar ise iç seviye olarak görüntülenir.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldGroupOptions, PivotGroupByType, DateTime
# Örnek çalışma kitabını yükle
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# İkinci çalışma sayfasına ve pivot tablosuna eriş
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# İlk satır alanını (bir tarih alanı) aylara ve çeyreklere göre grupla
options = PivotFieldGroupOptions()
options.setStartDate(DateTime(2008, 1, 1))
options.setEndDate(DateTime(2008, 9, 5))
options.setGroupTypes([PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS])
pt.getRowFields().get(0).group(options)
# Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.calculateData()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
jpype.shutdownJVM()
```

![Pivot tablosu aylara ve çeyreklere göre gruplanmış](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Alanı Aralıklara Gruplama**
Örnek pivot tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplanabildiğinden, kod önce `FieldTwo` alanını satır alanına taşımak için `pivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` çağırır, pivot tabloyu yeniler, ardından sayısal alanı `StartNumber = 0`, `EndNumber = 5` ve `Interval = 2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplar.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType, PivotFieldGroupOptions
# Örnek çalışma kitabını yükle
wb = Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# İkinci çalışma sayfasına ve pivot tablosuna eriş
pt = wb.getWorksheets().get(1).getPivotTables().get(0)
# FieldTwo bir veri alanıdır: önce onu satır alanına taşı,
# çünkü yalnızca satır/sütun alanları gruplanabilir
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo")
pt.calculateData()
# Sayısal alanı 0-1, 2-3, 4-5 aralıklarına grupla
options = PivotFieldGroupOptions()
options.setStartNumber(0)
options.setEndNumber(5)
options.setInterval(2)
pt.getRowFields().get(1).group(options)
# Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.calculateData()
wb.save("outputNumberGroupPivotField.xlsx")
jpype.shutdownJVM()
```

## **Not**

{{% alert color="primary" %}}
- `PivotField.groupBy()` yöntemi aşırı yüklemeleri kullanımdan kaldırılmış ve API yüzeyinden kaldırılmıştır. `PivotField.group()` ve `PivotField.group(PivotFieldGroupOptions)` bunların yerini almıştır.
- Microsoft Excel'de, bir sayısal alanı gruplamak orijinal pivot alanını gruplanmış aralıklarla DEĞİŞTİRİR, ancak bir tarih alanını gruplamak orijinal alanın yanında YENİ pivot alanları (her grup seviyesi için bir tane, örneğin Çeyrekler ve Aylar) oluşturur. Aspose.Cells 26.10'dan başlayarak, `PivotField.group()` yöntemleri Excel ile aynı davranışı izler. `PivotFieldGroupOptions.NewPivotField` özelliği eski sürümlerle uyumluluk için mevcuttur: sayısal gruplama için varsayılan olarak false, tarih-saat gruplama için true'dur; tarih gruplamasının yeni pivot alanları oluşturmak yerine orijinal pivot alanını değiştirmesini istiyorsanız bunu false olarak ayarlayın.
- `PivotFieldGroupOptions.Interval` özelliği yalnızca sayısal gruplama ve tarihlerin günlere göre gruplanması (örneğin, tarihlerin 7 günlük dönemlere gruplanması) için geçerlidir; tarihler aylara, çeyreklere veya yıllara göre gruplanırken yok sayılır.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-java/pivot-table-add-row-and-column-fields/)
- [Pivot Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/python-java/add-page-field-in-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-java/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/python-java/refresh-pivot-table/)

{{< app/cells/assistant language="python" >}}