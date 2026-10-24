---
title: Pivot Tablosunda Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Pivot Alanlarını Gruplama
description: Python via .NET için Aspose.Cells'de PivotField.Group ve PivotFieldGroupOptions kullanarak bir pivot tablodaki satır ve sütun pivot alanlarını aylar ve çeyrekler gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplayacağınızı öğrenin.
keywords: Aspose.Cells, pivot tablosu, pivot alanını gruplama, PivotField.Group, PivotFieldGroupOptions, tarih gruplama, sayı gruplama, aylar, çeyrekler, sayısal aralık, Python via .NET
type: docs
weight: 80
url: /tr/python-net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplamak, bir pivot tablosunun satır veya sütun alanı yüzlerce tarih içeren bir tarih alanı veya çok sayıda dağınık değer içeren bir sayısal alan gibi birçok farklı öğe içerdiğinde faydalıdır. Gruplama, bu öğeleri anlamlı bölümlere indirir: tarihleri aylara, çeyreklere ve yıllara, sayıları ise 0-1, 2-3, 4-5 gibi aralıklara ayırır. Bu, büyük bir pivot tablosunu kompakt ve analiz edilmesi kolay hale getirir. Python via .NET için Aspose.Cells, bu yeteneği `pivot_field.group()` metodu (veri türüne göre otomatik gruplama) ve `pivot_field.group(pivot_field_group_options)` (özel gruplama seçenekleri) aracılığıyla sağlar.
- Tarih gruplama, tek tek tarihleri günler, aylar, çeyrekler ve yıllar gibi daha büyük dönemlere yuvarlar ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zaman içindeki eğilimler bir bakışta görünür hale gelir ve her dönem seviyesi pivot tablosunun satır veya sütun alanında kendi pivot alanı olur.
- Gruplama yalnızca bir pivot tablosunun SATIR veya SÜTUN alanına yerleştirilmiş alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplanamaz. Böyle bir alanı gruplamak için önce onu pivot tablosunun satır veya sütun alanına eklemeniz gerekir.

## **Pivot Alanlarını Otomatik Olarak Gruplama**
Parametresiz `pivot_field.group()` aşırı yüklemesi, alanın veri türünü inceler ve onu otomatik olarak gruplar. Yalnızca tarihler (ve boşluklar) içeren bir alan aylara göre gruplanır. Yalnızca sayılar (ve boşluklar) içeren bir alan, otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

```python
import aspose.cells as ac
# Örnek çalışma kitabını yükle
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# İkinci çalışma sayfasına ve özet tablosuna eriş
pt = wb.worksheets[1].pivot_tables[0]
# İlk satır alanını otomatik olarak grupla.
# Alan tarihler içeriyor, bu nedenle aylara göre gruplanır.
field = pt.row_fields[0]
field.group()
# Özet tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.calculate_data()
wb.save("outputAutoGroupPivotField.xlsx")
```

## **Pivot Alanlarını Özel Seçeneklerle Gruplama**
`PivotFieldGroupOptions` sınıfı özel gruplama yapılandırması sağlar. Tarih alanları için `start_date`, `end_date` ve `group_types` ayarlayın. Sayısal alanlar için `start_number`, `end_number` ve `interval` ayarlayın. `new_pivot_field` özelliği, gruplamanın orijinal alanın yanında yeni pivot alanları oluşturup oluşturmadığını kontrol eder (bu makalenin sonundaki Not bölümüne bakın).

### **Bir Tarih Alanını Aylara ve Çeyreklere Göre Gruplama**
Aşağıdaki örnek, örnek pivot tablosunun tarih satır alanını bir başlangıç ve bitiş tarihi arasında aylara ve çeyreklere göre gruplar. Kod, [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplamayı gerçekleştirir, pivot tablo verilerini hesaplar ve gruplanmış sonucu kaydeder. Ekran görüntüsü etkiyi gösterir: tarih satır alanı artık çeyreklere ve aylara göre gruplanmıştır.
`options.group_types` içindeki değerlerin sırasının göz ardı edildiğini unutmayın. Grup türleri hangi sırayla listelenirse listelensin, gruplanmış alanlar her zaman en büyük dönemden en küçüğe doğru görüntülenir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte, aylar `options.group_types` içinde çeyreklerden önce listelenmiştir, ancak çeyrekler dış seviye olarak, aylar ise iç seviye olarak görüntülenir.

```python
import aspose.cells as ac
from datetime import datetime
from aspose.cells.pivot import PivotGroupByType
from aspose.cells.pivot import PivotFieldGroupOptions
# Örnek çalışma kitabını yükle
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# İkinci çalışma sayfasına ve pivot tablosuna eriş
pt = wb.worksheets[1].pivot_tables[0]
# İlk satır alanını (bir tarih alanı) aylara ve çeyreklere göre gruplandır
options = PivotFieldGroupOptions()
options.start_date = datetime(2008, 1, 1)
options.end_date = datetime(2008, 9, 5)
options.group_types = [PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS]
pt.row_fields[0].group(options)
# Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.calculate_data()
wb.save("outputGroupPivotFieldsInPivotTable.xlsx")
```

![Aylara ve çeyreklere göre gruplanmış pivot tablosu](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Bir Alanı Aralıklara Gruplama**
Örnek pivot tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplanabildiğinden, kod önce `pivot_table.add_field_to_area(PivotFieldType.ROW, "FieldTwo")` çağrısını yaparak `FieldTwo`'yu satır alanına taşır, pivot'u yeniler ve ardından sayısal alanı `start_number=0`, `end_number=5` ve `interval=2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplar.

```python
import aspose.cells as ac
from aspose.cells.pivot import PivotFieldType
from aspose.cells.pivot import PivotFieldGroupOptions
# Örnek çalışma kitabını yükle
wb = ac.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx")
# İkinci çalışma sayfasına ve özet tablosuna erişin
pt = wb.worksheets[1].pivot_tables[0]
# FieldTwo bir veri alanıdır: önce onu satır alanına taşıyın,
# çünkü yalnızca satır/sütun alanları gruplanabilir
pt.add_field_to_area(PivotFieldType.ROW, "FieldTwo")
pt.calculate_data()
# Sayısal alanı 0-1, 2-3, 4-5 aralıklarına gruplayın
options = PivotFieldGroupOptions()
options.start_number = 0.0
options.end_number = 5.0
options.interval = 2.0
pt.row_fields[1].group(options)
# Özet tablo verilerini hesaplayın ve çıktı dosyasını kaydedin
pt.calculate_data()
wb.save("outputNumberGroupPivotField.xlsx")
```

## **Not**

{{% alert color="primary" %}}
- `pivot_field.group_by()` metodu aşırı yüklemeleri kullanım dışı bırakılmıştır ve API yüzeyinden kaldırılmıştır. `pivot_field.group()` ve `pivot_field.group(pivot_field_group_options)` bunların yerini almıştır.
- Microsoft Excel'de, sayısal bir alanı gruplamak orijinal pivot alanını gruplanmış aralıklarla DEĞİŞTİRİR, tarih alanını gruplamak ise orijinal alanın yanında yeni pivot alanları (her grup seviyesi için bir tane, örneğin Çeyrekler ve Aylar) OLUŞTURUR. Aspose.Cells 26.10'dan başlayarak, `pivot_field.group()` metotları Excel ile aynı davranışı izler. `PivotFieldGroupOptions.new_pivot_field` özelliği, eski sürümlerle uyumluluk için mevcuttur: sayısal gruplama için varsayılan olarak false, tarih-saat gruplaması için true değerini alır; tarih gruplamasının orijinal pivot alanını yeni pivot alanları oluşturmak yerine değiştirmesini istiyorsanız bunu false olarak ayarlayın.
- `PivotFieldGroupOptions.interval` özelliği yalnızca sayısal gruplamada ve tarihlerin günlere göre gruplanmasında (örneğin, tarihlerin 7 günlük dönemlere gruplanması) etkilidir; tarihler aylara, çeyreklere veya yıllara göre gruplandığında göz ardı edilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/python-net/pivot-table-add-row-and-column-fields/)
- [Pivot Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/python-net/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/python-net/add-page-field-in-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/python-net/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/python-net/refresh-pivot-table/)

{{< app/cells/assistant language="python-net" >}}