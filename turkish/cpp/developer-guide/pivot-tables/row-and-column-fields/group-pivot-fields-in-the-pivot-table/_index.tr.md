---
title: Pivot Tablosunda Pivot Alanlarını Gruplama
linktitle: Pivot Tablosunda Pivot Alanlarını Gruplama
description: Aspose.Cells for C++ kullanarak PivotField.Group ve PivotFieldGroupOptions ile bir pivot tablosundaki satır ve sütun pivot alanlarını aylar ve çeyrekler gibi tarih dönemlerine ve sayısal aralıklara nasıl gruplayacağınızı öğrenin.
keywords: Aspose.Cells, pivot tablosu, pivot alanını gruplama, PivotField.Group, PivotFieldGroupOptions, tarihe göre gruplama, sayıya göre gruplama, aylar, çeyrekler, sayısal aralık, C++
type: docs
weight: 80
url: /tr/cpp/group-pivot-fields-in-the-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Pivot alanlarını gruplamak, bir pivot tablosunun satır veya sütun alanında yüzlerce tarih içeren bir tarih alanı ya da dağınık birçok değer içeren bir sayısal alan gibi birçok farklı öğe bulunduğunda faydalıdır. Gruplama bu öğeleri anlamlı bölümlere dönüştürür: tarihleri aylara, çeyreklere ve yıllara; sayıları ise 0-1, 2-3, 4-5 gibi aralıklara. Bu, büyük bir pivot tablosunu kompakt ve analiz edilmesi kolay hale getirir. Aspose.Cells bu yeteneği `PivotField.Group()` metodu (veri türüne göre otomatik gruplama) ve `PivotField.Group(PivotFieldGroupOptions)` (özel gruplama seçenekleri) aracılığıyla sağlar.
- Tarihe göre gruplama, tek tek tarihleri günler, aylar, çeyrekler ve yıllar gibi daha geniş dönemlere toplar ve bir zaman hiyerarşisi oluşturur (örneğin Yıllar, Çeyrekler, Aylar). Zamana göre eğilimler bir bakışta görünür hale gelir ve her dönem seviyesi, pivot tablosunun satır veya sütun alanında kendi pivot alanı olur.
- Gruplama yalnızca bir pivot tablosunun SATIR veya SÜTUN alanına yerleştirilmiş alanlar için kullanılabilir. Bir veri (değer) alanı doğrudan gruplanamaz. Böyle bir alanı gruplamak için önce onu pivot tablosunun satır veya sütun alanına eklemeniz gerekir.

## **Pivot Alanlarını Otomatik Olarak Gruplama**
Parametresiz `PivotField.Group()` aşırı yüklemesi, alanın veri türünü inceler ve onu otomatik olarak gruplar. Yalnızca tarihler (ve boşluklar) içeren bir alan aylara göre gruplanır. Yalnızca sayılar (ve boşluklar) içeren bir alan, otomatik bir aralık kullanılarak sayısal aralıklara gruplanır.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    PivotField field = pt.GetRowFields().Get(0);
    field.Group();
    pt.CalculateData();
    wb.Save(u"outputAutoGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Pivot Alanlarını Özel Seçeneklerle Gruplama**
`PivotFieldGroupOptions` sınıfı özel gruplama yapılandırması sağlar. Tarih alanları için `StartDate`, `EndDate` ve `GroupTypes` ayarlayın. Sayısal alanlar için `StartNumber`, `EndNumber` ve `Interval` ayarlayın. `NewPivotField` özelliği, gruplamanın orijinal alanın yanında yeni pivot alanları oluşturup oluşturmayacağını kontrol eder (bu makalenin sonundaki Not bölümüne bakın).

### **Tarih Alanını Aylara ve Çeyreklere Göre Gruplama**
Aşağıdaki örnek, örnek pivot tablosunun tarih satırı alanını bir başlangıç ve bitiş tarihi arasında aylara ve çeyreklere göre gruplar. Kod, [örnek Excel dosyasını](sampleGroupPivotFieldsInPivotTable.xlsx) yükler, gruplamayı gerçekleştirir, pivot tablo verilerini hesaplar ve gruplanmış sonucu kaydeder. Ekran görüntüsü etkiyi göstermektedir: tarih satırı alanı artık çeyreklere ve aylara göre gruplanmıştır.
`options.GroupTypes` içindeki değerlerin sırasının yok sayıldığını unutmayın. Grup türleri hangi sırayla listelenmiş olursa olsun, gruplanmış alanlar her zaman en büyük dönemden en küçüğe doğru görüntülenir: yıllar, çeyrekler, aylar, günler, saatler, dakikalar, saniyeler. Bu örnekte `options.GroupTypes` içinde aylar çeyreklerden önce listelenmiştir, ancak çeyrekler dış seviye, aylar ise iç seviye olarak görüntülenir.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    // Örnek çalışma kitabını yükle
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    // İkinci çalışma sayfasına ve özet tablosuna eriş
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    // İlk satır alanını (bir tarih alanı) aylara ve çeyreklere göre grupla
    PivotFieldGroupOptions options;
    Date startDate{2008, 1, 1, 0, 0, 0, 0};
    Date endDate{2008, 9, 5, 0, 0, 0, 0};
    options.SetStartDate(startDate);
    options.SetEndDate(endDate);
    // Grup türlerini ayarla: Aylar ve Çeyrekler
    Vector<PivotGroupByType> groupTypes{ PivotGroupByType::Months, PivotGroupByType::Quarters };
    options.SetGroupTypes(groupTypes);
    // Gruplamayı ilk satır alanına uygula
    PivotField rowField = pt.GetRowFields().Get(0);
    rowField.Group(options);
    // Özet tablosu verilerini hesapla ve çıktı dosyasını kaydet
    pt.CalculateData();
    wb.Save(u"outputGroupPivotFieldsInPivotTable.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

![Pivot tablosu aylara ve çeyreklere göre gruplanmış](group-pivot-fields-in-the-pivot-table_1.png)

### **Sayısal Alanı Aralıklara Gruplama**
Örnek pivot tablosunun `FieldTwo` alanı başlangıçta bir veri (değer) alanıdır. Yalnızca satır veya sütun alanları gruplanabildiğinden, kod önce `FieldTwo` alanını satır alanına taşımak için `PivotTable.AddFieldToArea(PivotFieldType.Row, "FieldTwo")` çağırır, pivot'u yeniler, ardından sayısal alanı `StartNumber = 0`, `EndNumber = 5` ve `Interval = 2` kullanarak 0-1, 2-3 ve 4-5 aralıklarına gruplar.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb(u"sampleGroupPivotFieldsInPivotTable.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(1);
    PivotTable pt = ws.GetPivotTables().Get(0);
    pt.AddFieldToArea(PivotFieldType::Row, U16String("FieldTwo"));
    pt.CalculateData();
    PivotFieldGroupOptions options;
    options.SetStartNumber(0);
    options.SetEndNumber(5);
    options.SetInterval(2);
    pt.GetRowFields().Get(1).Group(options);
    pt.CalculateData();
    wb.Save(u"outputNumberGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Not**

{{% alert color="primary" %}}
- `PivotField.GroupBy()` metodunun aşırı yüklemeleri kullanımdan kaldırılmıştır ve API yüzeyinden kaldırılmıştır. `PivotField.Group()` ve `PivotField.Group(PivotFieldGroupOptions)` bunların yerine geçmektedir.
- Microsoft Excel'de, sayısal bir alanı gruplamak orijinal pivot alanını gruplanmış aralıklarla DEĞİŞTİRİR; tarih alanını gruplamak ise orijinal alanın yanında YENİ pivot alanları (her grup seviyesi için bir tane, örneğin Çeyrekler ve Aylar) oluşturur. Aspose.Cells 26.10'dan itibaren, `PivotField.Group()` metotları Excel ile aynı davranışı izler. `PivotFieldGroupOptions.NewPivotField` özelliği eski sürümlerle uyumluluk için mevcuttur: sayısal gruplama için varsayılan olarak false, tarih-saat gruplaması için ise true değerindedir; tarih gruplamasının orijinal pivot alanını değiştirmesini ve yeni pivot alanları oluşturmamasını istiyorsanız bunu false olarak ayarlayın.
- `PivotFieldGroupOptions.Interval` özelliği yalnızca sayısal gruplamada ve tarihlerin günlere göre gruplanmasında (örneğin, tarihlerin 7 günlük dönemlere gruplanması) geçerlidir; tarihler aylara, çeyreklere veya yıllara göre gruplandığında yok sayılır.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosunda Satır ve Sütun Alanları Ekleme](/cells/tr/cpp/pivot-table-add-row-and-column-fields/)
- [Pivot Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/cpp/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/cpp/add-page-field-in-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenileme](/cells/tr/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}