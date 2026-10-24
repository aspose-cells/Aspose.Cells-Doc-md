---
title: Pivot Tablosunda Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Pivot Alanlarını Gruplama
description: Aspose.Cells for Node.js via Java'da PivotField.group ve PivotFieldGroupOptions kullanarak bir pivot tablosundaki satır ve sütun pivot alanlarını aylar ve çeyrekler gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplayacağınızı öğrenin.
keywords: Aspose.Cells, pivot tablosu, pivot alanı gruplama, PivotField.group, PivotFieldGroupOptions, tarih gruplama, sayı gruplama, aylar, çeyrekler, sayısal aralık, Node.js
type: docs
weight: 80
url: /tr/nodejs-java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplamak, bir pivot tablosunun satır veya sütun alanı yüzlerce tarih içeren bir tarih alanı ya da birçok dağınık değere sahip bir sayısal alan gibi birçok farklı öğe içerdiğinde kullanışlıdır. Gruplama bu öğeleri anlamlı bölümlere ayırır: tarihleri aylara, çeyreklere ve yıllara; sayıları ise 0-1, 2-3, 4-5 gibi aralıklara dönüştürür. Bu, büyük bir pivot tablosunu kompakt ve analiz edilmesi kolay hale getirir. Aspose.Cells for Node.js via Java bu yeteneği `PivotField.group()` metodu (veri türüne göre otomatik gruplama) ve `PivotField.group(PivotFieldGroupOptions)` (özel gruplama seçenekleri) aracılığıyla sağlar.
- Tarih gruplama, tek tek tarihleri günler, aylar, çeyrekler ve yıllar gibi daha büyük dönemlere yuvarlar ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zaman içindeki eğilimler bir bakışta görünür hale gelir ve her dönem seviyesi pivot tablosunun satır veya sütun alanında kendi pivot alanı olur.
- Gruplama yalnızca pivot tablosunun SATIR veya SÜTUN alanına yerleştirilen alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplanamaz. Böyle bir alanı gruplamak için önce onu pivot tablosunun satır veya sütun alanına eklemeniz gerekir.

## **Pivot Alanlarını Otomatik Olarak Gruplama**
Parametresiz `PivotField.group()` aşırı yüklemesi, alanın veri türünü inceler ve onu otomatik olarak gruplar. Yalnızca tarihler (ve boşluklar) içeren bir alan aylara göre gruplanır. Yalnızca sayılar (ve boşluklar) içeren bir alan, otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

```javascript
const AsposeCells = require("aspose.cells");
let wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve pivot tablosuna erişin
let pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// İlk satır alanını otomatik olarak gruplandırın.
// Alan tarihler içerdiğinden aylara göre gruplandırılır.
let field = pt.getRowFields().get(0);
field.group();
// Pivot tablo verisini hesaplayın ve çıktı dosyasını kaydedin
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Pivot Alanlarını Özel Seçeneklerle Gruplama**
`PivotFieldGroupOptions` sınıfı özel gruplama yapılandırması sağlar. Tarih alanları için `StartDate`, `EndDate` ve `GroupTypes` ayarlayın. Sayısal alanlar için `StartNumber`, `EndNumber` ve `Interval` ayarlayın. `NewPivotField` özelliği, gruplamanın orijinalin yanında yeni pivot alanları oluşturup oluşturmayacağını kontrol eder (bu makalenin sonundaki Not bölümüne bakın).

### **Tarih Alanını Aylara ve Çeyreklere Göre Gruplama**
Aşağıdaki örnek, örnek pivot tablosunun tarih satır alanını bir başlangıç ve bitiş tarihi arasında aylara ve çeyreklere göre gruplar. Kod, [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplamayı gerçekleştirir, pivot tablo verilerini hesaplar ve gruplanmış sonucu kaydeder. Ekran görüntüsü etkiyi göstermektedir: tarih satır alanı artık çeyreklere ve aylara göre gruplanmıştır.
`options.GroupTypes` içindeki değerlerin sırasının göz ardı edildiğini unutmayın. Grup türleri hangi sırayla listelenirse listelensin, gruplanmış alanlar her zaman en büyük dönemden en küçüğe doğru görüntülenir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte aylar `options.GroupTypes` içinde çeyreklerden önce listelenmiştir, ancak çeyrekler dış seviye, aylar ise iç seviye olarak görüntülenir.

```javascript
const AsposeCells = require("aspose.cells");
// Örnek çalışma kitabını yükle
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve onun pivot tablosuna eriş
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// İlk satır alanını (bir tarih alanı) aylar ve çeyrekler olarak grupla
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartDate(new Date(2008, 0, 1));
options.setEndDate(new Date(2008, 8, 5));
options.setGroupTypes([AsposeCells.PivotGroupByType.MONTHS, AsposeCells.PivotGroupByType.QUARTERS]);
pt.getRowFields().get(0).group(options);
// Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivot tablosu aylar ve çeyreklere göre gruplanmış](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Bir Alanı Aralıklara Gruplama**
Örnek pivot tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplanabildiğinden, kod önce `pivotTable.addFieldToArea(PivotFieldType.Row, "FieldTwo")` çağırarak `FieldTwo`'yu satır alanına taşır, pivot'u yeniler, ardından sayısal alanı `StartNumber = 0`, `EndNumber = 5` ve `Interval = 2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplar.

```javascript
const AsposeCells = require("aspose.cells");
// Örnek çalışma kitabını yükle
const wb = new AsposeCells.Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve onun pivot tablosuna eriş
const pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo bir veri alanıdır: önce satır alanına taşı,
// çünkü yalnızca satır/sütun alanları gruplanabilir
pt.addFieldToArea(AsposeCells.PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Sayısal alanı 0-1, 2-3, 4-5 aralıklarına grupla
const options = new AsposeCells.PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Pivot tablo verilerini hesapla ve çıktı dosyasını kaydet
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` metodu aşırı yüklemeleri kullanımdan kaldırılmış olup API yüzeyinden kaldırılmıştır. Yerine `PivotField.group()` ve `PivotField.group(PivotFieldGroupOptions)` kullanılır.
- Microsoft Excel'de, sayısal bir alanı gruplamak orijinal pivot alanını gruplanmış aralıklarla DEĞİŞTİRİR, tarih alanını gruplamak ise orijinal alanın yanında yeni pivot alanları (her grup seviyesi için bir tane, örneğin Çeyrekler ve Aylar) oluşturur. Aspose.Cells for Node.js via Java 26.10'dan başlayarak, `PivotField.group()` metotları Excel ile aynı davranışı izler. `PivotFieldGroupOptions.NewPivotField` özelliği eski sürümlerle uyumluluk için bulunur; sayısal gruplama için varsayılan olarak false, tarih-saat gruplama için true değerindedir; tarih gruplamasının yeni pivot alanları oluşturmak yerine orijinal pivot alanını değiştirmesini istiyorsanız bunu false olarak ayarlayın.
- `PivotFieldGroupOptions.Interval` özelliği yalnızca sayısal gruplamada ve tarihlerin günlere göre gruplanmasında (örneğin, tarihlerin 7 günlük dönemlere gruplanması) etkilidir; tarihler aylara, çeyreklere veya yıllara göre gruplandığında göz ardı edilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Pivot Tablolarını Etiket veya Değere Göre Filtreleme](/cells/tr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}