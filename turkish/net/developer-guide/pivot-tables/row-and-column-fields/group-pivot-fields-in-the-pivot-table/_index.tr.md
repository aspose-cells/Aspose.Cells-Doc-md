---
title: Pivot Tablosunda Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Pivot Alanlarını Gruplama
description: Aspose.Cells for .NET'te PivotField.Group ve PivotFieldGroupOptions kullanarak bir pivot tablodaki satır ve sütun pivot alanlarını aylar ve çeyrekler gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplayacağınızı öğrenin.
keywords: Aspose.Cells, pivot tablo, pivot alanı gruplama, PivotField.Group, PivotFieldGroupOptions, tarih gruplama, sayı gruplama, aylar, çeyrekler, sayısal aralık, C#
type: docs
weight: 80
url: /tr/net/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplamak, bir pivot tablonun satır veya sütun alanı yüzlerce tarih içeren bir tarih alanı ya da birçok dağınık değer içeren sayısal bir alan gibi birçok farklı öğe içerdiğinde kullanışlıdır. Gruplama bu öğeleri anlamlı bölümlere daraltır: tarihleri aylara, çeyreklere ve yıllara; sayıları ise 0-1, 2-3, 4-5 gibi aralıklara. Bu, büyük bir pivot tablosunu kompakt ve analiz edilmesi daha kolay hale getirir. Aspose.Cells bu yeteneği `PivotField.Group()` yöntemi (veri türüne göre otomatik gruplama) ve `PivotField.Group(PivotFieldGroupOptions)` (özel gruplama seçenekleri) aracılığıyla sağlar.
- Tarih gruplama, tek tek tarihleri günler, aylar, çeyrekler ve yıllar gibi daha büyük dönemlere toplar ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zaman içindeki trendler bir bakışta görünür hale gelir ve her dönem seviyesi pivot tablosunun satır veya sütun alanında kendi pivot alanı olur.
- Gruplama yalnızca bir pivot tablosunun ROW veya COLUMN alanına yerleştirilmiş alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplanamaz. Böyle bir alanı gruplamak için önce onu pivot tablosunun satır veya sütun alanına eklemeniz gerekir.

## **Pivot Alanlarını Otomatik Gruplama**
Parametresiz `PivotField.Group()` aşırı yüklemesi, alanın veri türünü inceler ve onu otomatik olarak gruplar. Yalnızca tarihler (ve boşluklar) içeren bir alan aylara göre gruplanır. Yalnızca sayılar (ve boşluklar) içeren bir alan, otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

```csharp
// Örnek çalışma kitabını yükle
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve onun pivot tablosuna eriş
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// İlk satır alanını otomatik olarak grupla.
// Alan tarihler içerdiğinden aylara göre gruplanır.
PivotField field = pt.RowFields[0];
field.Group();
// Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.CalculateData();
wb.Save("outputAutoGroupPivotField.xlsx");
```

## **Pivot Alanlarını Özel Seçeneklerle Gruplama**
`PivotFieldGroupOptions` sınıfı özel gruplama yapılandırması sağlar. Tarih alanları için `StartDate`, `EndDate` ve `GroupTypes` ayarlayın. Sayısal alanlar için `StartNumber`, `EndNumber` ve `Interval` ayarlayın. `NewPivotField` özelliği, gruplamanın orijinal alanın yanında yeni pivot alanları oluşturup oluşturmadığını kontrol eder (bu makalenin sonundaki Not bölümüne bakın).

### **Bir Tarih Alanını Aylara ve Çeyreklere Göre Gruplama**
Aşağıdaki örnek, örnek pivot tablosunun tarih satır alanını bir başlangıç ve bitiş tarihi arasında aylara ve çeyreklere göre gruplar. Kod [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplamayı gerçekleştirir, pivot tablo verilerini hesaplar ve gruplanmış sonucu kaydeder. Ekran görüntüsü etkiyi gösterir: tarih satır alanı artık çeyreklere ve aylara göre gruplanmıştır.
`options.GroupTypes` içindeki değerlerin sırasının göz ardı edildiğini unutmayın. Grup türleri hangi sırayla listelenmiş olursa olsun, gruplanmış alanlar her zaman en büyük dönemden en küçüğe doğru görüntülenir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte, `options.GroupTypes` içinde aylar çeyreklerden önce listelenmiştir, ancak çeyrekler dış seviye, aylar ise iç seviye olarak görüntülenir.

```csharp
// Örnek çalışma kitabını yükle
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve özet tablosuna erişim
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// İlk satır alanını (bir tarih alanı) aylar ve çeyrekler bazında grupla
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartDate = new DateTime(2008, 1, 1);
options.EndDate = new DateTime(2008, 9, 5);
options.GroupTypes = new PivotGroupByType[] { PivotGroupByType.Months, PivotGroupByType.Quarters };
pt.RowFields[0].Group(options);
// Özet tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.CalculateData();
wb.Save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Aylara ve çeyreklere göre gruplanmış pivot tablosu](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Bir Alanı Aralıklara Gruplama**
Örnek pivot tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplanabildiğinden, kod önce `FieldTwo` öğesini satır alanına taşımak için `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` çağırır, pivot tabloyu yeniler, ardından `StartNumber = 0`, `EndNumber = 5` ve `Interval = 2` kullanarak sayısal alanı 0-1, 2-3 ve 4-5 aralıklarına gruplar.

```csharp
// Örnek çalışma kitabını yükle
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve onun pivot tablosuna eriş
PivotTable pt = wb.Worksheets[1].PivotTables[0];
// FieldTwo bir veri alanıdır: önce onu satır alanına taşı,
// çünkü yalnızca satır/sütun alanları gruplanabilir
pt.AddFieldToArea(PivotFieldType.Row, "FieldTwo");
pt.CalculateData();
// Sayısal alanı 0-1, 2-3, 4-5 aralıklarına grupla
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.StartNumber = 0;
options.EndNumber = 5;
options.Interval = 2;
pt.RowFields[1].Group(options);
// Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.CalculateData();
wb.Save("outputNumberGroupPivotField.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` yöntemi aşırı yüklemeleri kullanımdan kaldırıldı ve API yüzeyinden kaldırıldı. `PivotField.Group()` ve `PivotField.Group(PivotFieldGroupOptions)` bunların yerini alır.
- Microsoft Excel'de, sayısal bir alanı gruplamak orijinal pivot alanını gruplanmış aralıklarla DEĞİŞTİRİR, tarih alanını gruplamak ise orijinal alanın yanında YENİ pivot alanları (grup seviyesi başına bir tane, örneğin Çeyrekler ve Aylar) oluşturur. Aspose.Cells 26.10'dan başlayarak, `PivotField.Group()` yöntemleri Excel ile aynı davranışı izler. `PivotFieldGroupOptions.NewPivotField` özelliği eski sürümlerle uyumluluk amacıyla mevcuttur: sayısal gruplama için varsayılan olarak false, tarih-saat gruplaması için true değerindedir; tarih gruplamasının orijinal pivot alanını değiştirmesini ve yeni pivot alanları oluşturmamasını istiyorsanız false olarak ayarlayın.
- `PivotFieldGroupOptions.Interval` özelliği yalnızca sayısal gruplamada ve tarihlerin günlere göre gruplanmasında (örneğin, tarihlerin 7 günlük dönemlere gruplanması) etkilidir; tarihler aylara, çeyreklere veya yıllara göre gruplandığında göz ardı edilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/net/pivot-table-add-row-and-column-fields/)
- [Pivot Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/net/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/net/add-page-field-in-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}