---
title: Pivot Tablosunda Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Pivot Alanlarını Gruplama
description: Aspose.Cells for Java kullanarak bir pivot tablosunda satır ve sütun pivot alanlarını aylar ve çeyrekler gibi tarih dönemleriyle ve sayısal aralıklarla nasıl gruplandıracağınızı PivotField.group ve PivotFieldGroupOptions aracılığıyla öğrenin.
keywords: Aspose.Cells, pivot tablosu, pivot alanını gruplama, PivotField.group, PivotFieldGroupOptions, tarih gruplama, sayı gruplama, aylar, çeyrekler, sayısal aralık, Java
type: docs
weight: 80
url: /tr/java/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplamak, bir pivot tablosunun satır veya sütun alanı çok sayıda farklı öğe içerdiğinde kullanışlıdır; örneğin yüzlerce tarih içeren bir tarih alanı veya birçok dağınık değer içeren sayısal bir alan. Gruplama bu öğeleri anlamlı bölümlere daraltır: tarihleri aylara, çeyreklere ve yıllara; sayıları ise 0-1, 2-3, 4-5 gibi aralıklara dönüştürür. Bu sayede büyük bir pivot tablosu daha kompakt ve analiz edilmesi kolay hale gelir. Aspose.Cells bu yeteneği `PivotField.group()` yöntemi (veri türüne göre otomatik gruplama) ve `PivotField.group(PivotFieldGroupOptions)` (özel gruplama seçenekleri) aracılığıyla sunar.
- Tarih gruplama, tek tek tarihleri günler, aylar, çeyrekler ve yıllar gibi daha büyük dönemlere yuvarlar ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zaman içindeki eğilimler bir bakışta görünür hale gelir ve her dönem seviyesi pivot tablosunun satır veya sütun alanında kendi pivot alanı olur.
- Gruplama yalnızca pivot tablosunun SATIR veya SÜTUN alanına yerleştirilen alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplanamaz. Böyle bir alanı gruplamak için önce onu pivot tablosunun satır veya sütun alanına eklemeniz gerekir.

## **Pivot Alanlarını Otomatik Olarak Gruplama**
Parametresiz `PivotField.group()` aşırı yüklemesi, alanın veri türünü inceler ve otomatik olarak gruplar. Yalnızca tarih (ve boşluk) içeren bir alan aylara göre gruplanır. Yalnızca sayı (ve boşluk) içeren bir alan, otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotField field = pt.getRowFields().get(0);
field.group();
pt.calculateData();
wb.save("outputAutoGroupPivotField.xlsx");
```

## **Pivot Alanlarını Özel Seçeneklerle Gruplama**
`PivotFieldGroupOptions` sınıfı özel gruplama yapılandırması sunar. Tarih alanları için `startDate`, `endDate` ve `groupTypes` ayarlayın. Sayısal alanlar için `startNumber`, `endNumber` ve `interval` ayarlayın. `newPivotField` özelliği, gruplamanın orijinalin yanında yeni pivot alanları oluşturup oluşturmayacağını kontrol eder (bu makalenin sonundaki Not bölümüne bakın).

### **Tarih Alanını Aylara ve Çeyreklere Göre Gruplama**
Aşağıdaki örnek, örnek pivot tablosunun tarih satır alanını bir başlangıç ve bitiş tarihi arasında aylara ve çeyreklere göre gruplar. Kod [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplamayı gerçekleştirir, pivot tablo verilerini hesaplar ve gruplanmış sonucu kaydeder. Ekran görüntüsü etkiyi göstermektedir: tarih satır alanı artık çeyreklere ve aylara göre gruplanmıştır.
`options.groupTypes` içindeki değerlerin sırasının yok sayıldığını unutmayın. Grup türleri hangi sırayla listelenirse listelensin, gruplanmış alanlar her zaman en büyük dönemden en küçüğe doğru görüntülenir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte `options.groupTypes` içinde aylar çeyreklerden önce listelenmiştir, ancak çeyrekler dış seviye, aylar ise iç seviye olarak görüntülenir.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartDate(new com.aspose.cells.DateTime(2008, 1, 1));
options.setEndDate(new com.aspose.cells.DateTime(2008, 9, 5));
options.setGroupTypes(new int[] { PivotGroupByType.MONTHS, PivotGroupByType.QUARTERS });
pt.getRowFields().get(0).group(options);
pt.calculateData();
wb.save("outputGroupPivotFieldsInPivotTable.xlsx");
```

![Pivot tablosu aylara ve çeyreklere göre gruplanmış](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Alanı Aralıklara Gruplama**
Örnek pivot tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplanabildiğinden, kod önce `PivotTable.addFieldToArea(PivotFieldType.ROW, "FieldTwo")` çağırarak `FieldTwo`'yu satır alanına taşır, pivot'u yeniler, ardından sayısal alanı `startNumber = 0`, `endNumber = 5` ve `interval = 2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplar.

```java
import com.aspose.cells.*;
// Örnek çalışma kitabını yükle
Workbook wb = new Workbook("sampleGroupPivotFieldsInPivotTable.xlsx");
// İkinci çalışma sayfasına ve onun özet tablosuna eriş
PivotTable pt = wb.getWorksheets().get(1).getPivotTables().get(0);
// FieldTwo bir veri alanıdır: önce satır alanına taşı,
// çünkü yalnızca satır/sütun alanları gruplanabilir
pt.addFieldToArea(PivotFieldType.ROW, "FieldTwo");
pt.calculateData();
// Sayısal alanı 0-1, 2-3, 4-5 aralıklarına grupla
PivotFieldGroupOptions options = new PivotFieldGroupOptions();
options.setStartNumber(0);
options.setEndNumber(5);
options.setInterval(2);
pt.getRowFields().get(1).group(options);
// Özet tablosu verilerini hesapla ve çıktı dosyasını kaydet
pt.calculateData();
wb.save("outputNumberGroupPivotField.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- `PivotField.groupBy()` yöntemi aşırı yüklemeleri kullanımdan kaldırılmıştır ve API yüzeyinden kaldırılmıştır. `PivotField.group()` ve `PivotField.group(PivotFieldGroupOptions)` bunların yerini almıştır.
- Microsoft Excel'de, sayısal bir alanı gruplamak orijinal pivot alanını gruplanmış aralıklarla DEĞİŞTİRİR; tarih alanını gruplamak ise orijinal alanın yanında yeni pivot alanları (her grup seviyesi için bir tane, örneğin Çeyrekler ve Aylar) oluşturur. Aspose.Cells 26.10'dan itibaren, `PivotField.group()` yöntemleri Excel ile aynı davranışı izler. `PivotFieldGroupOptions.newPivotField` özelliği eski sürümlerle uyumluluk için mevcuttur: sayısal gruplama için varsayılan olarak false, tarih-saat gruplama için true değerini alır; tarih gruplamasının orijinal pivot alanını değiştirmesini ve yeni pivot alanları oluşturmamasını istiyorsanız bunu false olarak ayarlayın.
- `PivotFieldGroupOptions.interval` özelliği yalnızca sayısal gruplamada ve tarihlerin günlere göre gruplanmasında (örneğin tarihlerin 7 günlük dönemlere gruplanması) etkilidir; tarihler aylara, çeyreklere veya yıllara göre gruplandığında yok sayılır.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/java/pivot-table-add-row-and-column-fields/)
- [Pivot Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/java/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/java/add-page-field-in-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}