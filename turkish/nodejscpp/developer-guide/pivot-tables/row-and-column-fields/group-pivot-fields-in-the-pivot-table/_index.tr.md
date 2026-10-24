---
title: Pivot Tablosunda Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Pivot Alanlarını Gruplama
description: Aspose.Cells for Node.js via C++ ile PivotField.Group ve PivotFieldGroupOptions kullanarak bir pivot tablodaki satır ve sütun pivot alanlarını aylar ve çeyrekler gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplayacağınızı öğrenin.
keywords: Aspose.Cells, pivot tablosu, pivot alanını gruplama, PivotField.Group, PivotFieldGroupOptions, tarih gruplama, sayı gruplama, aylar, çeyrekler, sayısal aralık, JavaScript
type: docs
weight: 80
url: /tr/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplamak, bir pivot tablosunun satır veya sütun alanında yüzlerce tarih içeren bir tarih alanı ya da birçok dağınık değer içeren sayısal alan gibi birçok farklı öğe içerdiğinde kullanışlıdır. Gruplama bu öğeleri anlamlı bölümler halinde daraltır: tarihleri aylara, çeyreklere ve yıllara; sayıları ise 0-1, 2-3, 4-5 gibi aralıklara dönüştürür. Bu, büyük bir pivot tablosunu kompakt ve analiz edilmesi daha kolay hale getirir. Aspose.Cells bu yeteneği `pivotField.group()` yöntemi (veri türüne göre otomatik gruplama) ve `pivotField.group(PivotFieldGroupOptions)` (özel gruplama seçenekleri) aracılığıyla sağlar.
- Tarih gruplama, tek tek tarihleri günler, aylar, çeyrekler ve yıllar gibi daha büyük dönemler halinde toplar ve bir zaman hiyerarşisi (örneğin Yıllar, Çeyrekler, Aylar) oluşturur. Zaman içindeki eğilimler bir bakışta görünür hale gelir ve her dönem düzeyi, pivot tablosunun satır veya sütun alanında kendi pivot alanı olur.
- Gruplama yalnızca bir pivot tablosunun SATIR veya SÜTUN alanına yerleştirilmiş alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplanamaz. Bu tür bir alanı gruplamak için önce onu pivot tablosunun satır veya sütun alanına eklemeniz gerekir.

## **Pivot Alanlarını Otomatik Olarak Gruplama**
Parametresiz `pivotField.group()` aşırı yüklemesi, alanın veri türünü inceler ve otomatik olarak gruplar. Yalnızca tarihleri (ve boşlukları) içeren bir alan aylara göre gruplanır. Yalnızca sayıları (ve boşlukları) içeren bir alan, otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

```javascript
const AsposeCells = require("aspose.cells.node");
// Örnek çalışma kitabını yükle
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve onun özet tablosuna erişim sağla
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// İlk satır alanını otomatik olarak grupla.
// Alan tarihleri içeriyor, bu nedenle aylara göre gruplandırılır.
const field = pt.getRowFields().get(0);
field.group();
// Özet tablosu verilerini hesapla ve çıktı dosyasını kaydet
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Pivot Alanlarını Özel Seçeneklerle Gruplama**
`PivotFieldGroupOptions` sınıfı özel gruplama yapılandırması sağlar. Tarih alanları için `startDate`, `endDate` ve `groupTypes` ayarlayın. Sayısal alanlar için `startNumber`, `endNumber` ve `interval` ayarlayın. `newPivotField` özelliği, gruplamanın orijinalin yanında yeni pivot alanları oluşturup oluşturmadığını kontrol eder (bu makalenin sonundaki Not bölümüne bakın).

### **Tarih Alanını Aylara ve Çeyreklere Göre Gruplama**
Aşağıdaki örnek, örnek pivot tablosunun tarih satır alanını bir başlangıç ve bitiş tarihi arasında aylara ve çeyreklere göre gruplar. Kod [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplamayı gerçekleştirir, pivot tablo verisini hesaplar ve gruplanmış sonucu kaydeder. Ekran görüntüsü etkiyi göstermektedir: tarih satır alanı artık çeyreklere ve aylara göre gruplanmıştır. `options.groupTypes` içindeki değerlerin sırasının yok sayıldığını unutmayın. Grup türleri hangi sırayla listelenirse listelensin, gruplanmış alanlar her zaman en büyük dönemden en küçüğe doğru görüntülenir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte aylar, `options.groupTypes` içinde çeyreklerden önce listelenmiştir, ancak çeyrekler dış düzey, aylar ise iç düzey olarak görüntülenir.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve pivot tablosuna erişim
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// İlk satır alanını (tarih alanı) aylar ve çeyrekler olarak grupla
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.Months, AsposeCells.PivotGroupByType.Quarters]);
pt.getRowFields().get(0).group(options);
// Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Aylara ve çeyreklere göre gruplanmış pivot tablo](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Alanı Aralıklara Gruplama**
Örnek pivot tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplanabildiğinden, kod önce `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` çağırarak `FieldTwo` alanını satır alanına taşır, pivotu yeniler, ardından sayısal alanı `startNumber = 0`, `endNumber = 5` ve `interval = 2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplar.

```javascript
const AsposeCells = require("aspose.cells.node");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve özet tablosuna erişin
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo bir veri alanıdır: önce satır alanına taşıyın,
// çünkü yalnızca satır/sütun alanları gruplanabilir
pt.addFieldToArea(AsposeCells.PivotFieldType.Row, "FieldTwo");
pt.calculateData();
// Sayısal alanı 0-1, 2-3, 4-5 aralıklarına gruplayın
let options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Özet tablosu verilerini hesaplayın ve çıktı dosyasını kaydedin
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- `pivotField.groupBy()` yöntemi aşırı yüklemeleri kullanımdan kaldırılmıştır ve API yüzeyinden kaldırılmıştır. `pivotField.group()` ve `pivotField.group(PivotFieldGroupOptions)` bunların yerini almaktadır.
- Microsoft Excel'de, sayısal bir alanı gruplamak orijinal pivot alanını gruplanmış aralıklarla DEĞİŞTİRİR; tarih alanını gruplamak ise orijinal alanın yanında yeni pivot alanları (örneğin Çeyrekler ve Aylar gibi her grup düzeyi için bir tane) OLUŞTURUR. Aspose.Cells 26.10'dan itibaren, `pivotField.group()` yöntemleri Excel ile aynı davranışı izler. `pivotFieldGroupOptions.newPivotField` özelliği eski sürümlerle uyumluluk için mevcuttur: sayısal gruplama için varsayılan değeri false, tarih-saat gruplama için true'dur; tarih gruplamasının yeni pivot alanları oluşturmak yerine orijinal pivot alanını değiştirmesini istiyorsanız bunu false olarak ayarlayın.
- `pivotFieldGroupOptions.interval` özelliği yalnızca sayısal gruplama ve tarihlerin günlere göre gruplanması (örneğin, tarihlerin 7 günlük dönemlere gruplanması) için geçerlidir; tarihler aylara, çeyreklere veya yıllara göre gruplandığında yok sayılır.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Pivot Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}