---
title: Özet Tabloları Etikete veya Değere Göre Filtreleme
linktitle: Özet Tabloları Etikete veya Değere Göre Filtreleme
description: Aspose.Cells for C++ kapsamlı özet tablo filtreleme yeteneklerini destekler. Bu makale, özet tablo verilerini etiket filtreleri, tarih filtreleri, değer filtreleri, ilk 10 filtreleri ve özet öğeleri gizleyerek veya göstererek filtrelemeyi açıklar.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet öğesi, özet öğesini gizle
type: docs
weight: 10
url: /tr/cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, bir özet tablosunda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücreleri veya boşluklar içerdiğinde tarih filtreleri kullanabilir, toplanan sayılara karşı değer filtreleri uygulayabilir, bir değer alanına göre sıralamak için ilk 10 filtrelerini kullanabilir veya `IsHidden` özelliğini kullanarak tek tek özet öğelerini manuel olarak gizleyebilir ve gösterebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıfları üzerindeki özel API'ler aracılığıyla kullanıma sunulur.

{{% /alert %}}

## **Giriş**

Özet tablolar güçlü analitik araçlardır, ancak ham özetler genellikle sunmanız gerekenden çok daha fazla bilgi içerir. Filtreleme, bir özet tablosunu belirli bir rapor için önemli olan satır, sütun veya değerlere daraltmanın birincil mekanizmasıdır. Aspose.Cells for C++, Microsoft Excel'de bulunan filtreleme yeteneklerini yansıtır ve rapor oluşturmanın tamamen otomatikleştirilebilmesi için bunları programlı olarak sunar.

Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:

1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boşluklar) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplanan değerlerine göre filtreler.
4. **İlk 10 Filtresi** — yalnızca bir değer alanına göre sıralanan en üst veya en alt N öğeyi gösterir.
5. **Özet Öğelerini Gizleme / Gösterme** — bir alandaki her bir öğenin görünürlüğünü manuel olarak kontrol eder.

Her yaklaşım, `PivotField` sınıfında farklı bir yöntem veya `PivotItem` sınıfında bir özellik kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınan verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tabloda `RefreshData()` ve `CalculateData()` çağrısı yapmalısınız.

## **Etiket Filtresi**

Etiket filtresi, bir satır veya sütun alanının öğelerini metin başlıklarını bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir başlık tabanlı ölçütle eşleşen ürünleri görüntülemek istediğinizde kullanışlıdır.

Aspose.Cells, etiket filtrelemeyi `PivotField.FilterByLabel(PivotFilterType, const char16_t*)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` gibi değerler içerir. İkinci bağımsız değişken, karşılaştırma için kullanılan etiket dizesini sağlar.

Aşağıdaki örnek, mevcut bir özet tablo içeren bir çalışma kitabını yükler, yalnızca başlıkları belirli bir önekle başlayan öğelerin görünür kalması için bir etiket filtresi uygular, özet tabloyu yeniler ve sonucu kaydeder.

```cpp
ells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    U16String fileName(u"sample.xlsx");
    U16String prefix(u"B");

    // Pivot tablo içeren mevcut çalışma kitabını yükle
    Workbook wb(fileName);

    // Çalışma sayfasına dizin ile erişim (ilk çalışma sayfası)
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Pivot tabloya dizin ile erişim
    PivotTable pt = ws.GetPivotTables().Get(0);

    // İlk satır PivotField alanını al
    PivotField rowField = pt.GetRowFields().Get(0);

    // Etiket filtresini uygula — yalnızca etiketleri belirtilen önekle başlayan satır öğelerini göster
    rowField.FilterByLabel(PivotFilterType::CaptionBeginsWith, prefix, U16String(u""));

    // Filtrenin etkili olması için pivot tablo verilerini yenile ve yeniden hesapla
    pt.RefreshData();

    // Çalışma kitabını tekrar diske kaydet
    wb.Save(fileName);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Tarih Filtresi**

Tarih filtreleri, özet tablosunu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarih tabanlı ölçütlerle daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgisi depolayan alanlara karşı çalışan özel filtrelerdir.

{{% alert color="primary" %}}

Tarih filtresi yalnızca satır veya sütun alanı yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde çalışır. Temel alan sayılar veya metin gibi başka veri türleri içeriyorsa, tarih filtresi beklenen sonucu üretmez. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.

{{% /alert %}}

Aspose.Cells, tarih filtrelemeyi `PivotField.FilterByDate(PivotFilterType, const Vector<DateTime>& values)` yöntemi aracılığıyla sunar. `PivotFilterType` numaralandırması `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerleri içerir. Seçilen filtre türüne bağlı olarak bir veya iki `DateTime` değeri iletirsiniz (`Between` için başlangıç ve bitiş tarihlerini iletirsiniz).

Aşağıdaki örnek, satır alanında bir tarih alanı bulunan özet tablo içeren bir çalışma kitabını yükler, görünür öğeleri belirli bir tarih aralığıyla kısıtlayan bir tarih filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string inputPath = "sample.xlsx";
    std::string outputPath = "output_filtered.xlsx";

    if (!std::filesystem::exists(inputPath))
    {
        // Kaynak çalışma kitabı bulunamadı.
        Aspose::Cells::Cleanup();
        return -1;
    }

    // Pivot tablosunu içeren mevcut çalışma kitabını yükle
    Workbook workbook(U16String(inputPath.c_str()));

    // Pivot tablosunu tutan çalışma sayfasına eriş (dizine göre)
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Pivot tablosuna dizine göre eriş
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    // Tarih PivotField'ını satır alanından al
    PivotField dateField = pivotTable.GetRowFields().Get(0);

    // Between filtresi için tarih kriterini tanımla
    Date startDate{2020, 1, 1, 0, 0, 0, 0};
    Date endDate{2020, 12, 31, 0, 0, 0, 0};

    // Pivot alanına tarih filtresini uygula
    dateField.FilterByDate(PivotFilterType::DateBetween, startDate, endDate);

    // Filtrenin geçerli olması için pivot tablosunu yenile ve yeniden hesapla
    pivotTable.RefreshData();

    // Çalışma kitabını kaydet
    workbook.Save(U16String(outputPath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Değer Filtresi**

Değer filtreleri, bir özet tablosunun veri alanında hesapladığı toplanan değerler üzerinde çalışır. Metin etiketlerini eşleştirmek yerine, sayısal toplamları bir eşikle karşılaştırırlar. Tipik kullanım durumları arasında yalnızca satış toplamı bir hedef miktarı aşan ürünleri veya işlem sayısı belirli bir aralıkta olan bölgeleri göstermek yer alır.

Aspose.Cells, değer filtrelemeyi `PivotField.FilterByValue(PivotField valueField, PivotFilterType filterType, const Vector<Variant>& values)` yöntemi aracılığıyla sunar. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerler kullanır. `valueField` parametresi, hangi veri alanının değerlendirileceğini belirtir ve son bağımsız değişken(ler) eşik değerini(lerini) sağlar.

Aşağıdaki örnek, bir özet tablo içeren bir çalışma kitabını yükler, yalnızca toplanan satışları sayısal bir eşiği aşan öğeleri tutan bir değer filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.

```cpp
#include "Aspose.Cells.h"
#include <cfloat>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb(u"sample.xlsx");
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    PivotField rowField = pivotTable.GetRowFields().Get(0);
    PivotField dataField = pivotTable.GetDataFields().Get(0);

    int dataFieldIndex = -1;
    int dataFieldCount = pivotTable.GetDataFields().GetCount();
    for (int i = 0; i < dataFieldCount; i++)
    {
        PivotField current = pivotTable.GetDataFields().Get(i);
        if (current.GetName() == dataField.GetName())
        {
            dataFieldIndex = i;
            break;
        }
    }

    if (dataFieldIndex >= 0)
    {
        rowField.FilterByValue(dataFieldIndex, PivotFilterType::ValueGreaterThan, 5000, DBL_MAX);
    }

    pivotTable.RefreshData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **İlk 10 Filtresi**

İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan özel bir değer filtresi biçimidir. "Gelire göre ilk 10 ürün" veya "Satış sayısına göre en alt 5 bölge" gibi sıralama raporları için yaygın olarak kullanılır.

{{% alert color="primary" %}}

İlk 10 filtresi yalnızca özet tablosunun veri alanında bir veya daha fazla değer özet alanı olduğunda etkilidir. En az bir değer alanı olmadan, öğeleri sıralamak için toplanan bir ölçü yoktur ve filtre uygulanamaz.

{{% /alert %}}

Aspose.Cells, ilk 10 filtrelemeyi `PivotField.FilterTop10(int32_t itemCount, bool isTop, PivotField valueField, PivotFilterType filterType)` yöntemi aracılığıyla sunar. `itemCount` parametresi kaç öğenin tutulacağını tanımlar, `isTop` en üst öğelerin (true) mi yoksa en alt öğelerin (false) mi tutulacağını belirtir, `valueField` sıralama için kullanılan veri alanına referans verir ve `filterType` değerin nasıl hesaplanacağını kontrol eder (genellikle `Sum`, ayrıca `Count` ve `Percent`).

Aşağıdaki örnek, bir değer alanı içeren özet tablo bulunan bir çalışma kitabını yükler, satış toplamına göre yalnızca en yüksek 10 öğeyi tutmak için bir ilk 10 filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.

```cpp
#include "Aspose.Cells.h"
#include <stdexcept>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    U16String inputPath(u"input.xlsx");
    U16String outputPath(u"output.xlsx");

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PivotTable pivotTable = worksheet.GetPivotTables().Get(0);

    if (pivotTable.GetDataFields().GetCount() == 0) {
        throw std::runtime_error("Pivot table has no value (data) PivotField.");
    }

    PivotField valueField = pivotTable.GetDataFields().Get(0);
    PivotField rowField = pivotTable.GetRowFields().Get(0);

    int valueFieldIndex = 0;

    rowField.FilterTop10(10, PivotFilterType::Sum, true, valueFieldIndex);

    pivotTable.RefreshData();

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Özet Öğelerini Gizleyerek veya Göstererek Filtreleme**

Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her bir özet öğesinin görünürlüğünü doğrudan kontrol etmenize olanak tanır. Bir `PivotField`'ın `PivotItems` koleksiyonunda yineleyerek ve `IsHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `IsHidden = true` olarak ayarlamak öğeyi özet tablosundan gizler; `IsHidden = false` olarak ayarlamak onu gösterir ve tekrar görünür hale getirir.

Bu yaklaşım, filtreleme kuralı düzensiz veya öğeye özgü olduğunda, örneğin belirli bir raporda görünmemesi gereken küçük bir sayıda adlandırılmış kategoriyi gizlerken kullanışlıdır. Aşağıdaki örnek bir özet tabloyu yükler, ada göre belirli bir öğeyi gizler, onu nasıl göstereceğinizi gösterir, özet tabloyu yeniler ve çalışma kitabını kaydeder.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Pivot tablo içeren mevcut bir çalışma kitabını yükle
    Workbook workbook(u"pivot_table_sample.xlsx");

    // Pivot tabloyu içeren ilk çalışma sayfasına eriş
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Pivot tabloya dizine göre eriş (sayfadaki ilk pivot tablo)
    PivotTable pivotTable = sheet.GetPivotTables().Get(0);

    // Hedef PivotField'ı al (öğelerini gizleyeceğimiz/göstereceğimiz ilk satır etiketi alanı)
    PivotField pivotField = pivotTable.GetRowFields().Get(0);

    // Seçilen PivotField'ın PivotItems koleksiyonu üzerinde yineleme yap
    int itemCount = pivotField.GetPivotItems().GetCount();
    for (int i = 0; i < itemCount; i++)
    {
        PivotItem item = pivotField.GetPivotItems().Get(i);

        U16String name = item.GetName();
        std::string nameStr = name.ToUtf8();

        // Belirli bir ad/ölçütle eşleşen pivot öğelerini gizle
        if (nameStr == "Item1" || nameStr == "Item2")
        {
            item.SetIsHidden(true);
        }

        // Gizlemeyi kaldırmayı göster: daha önce gizlenmiş bir pivot öğesini tekrar göster
        if (nameStr == "Item3")
        {
            item.SetIsHidden(false);
        }
    }

    // Değişikliklerin etkili olması için pivot tabloyu yenile ve yeniden hesapla
    pivotTable.CalculateData();

    // Çalışma kitabını kaydet — gizli öğeler alttaki verilerde kalır
    // ancak görüntülenen pivot tablo çıktısından hariç tutulur
    workbook.Save(u"output_pivot_filtered.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Özet**

Aspose.Cells for C++, Microsoft Excel'de bulunanlarla eşleşen eksiksiz bir özet tablo filtreleme yetenekleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsar, ilk 10 filtresi ise sıralama raporlarını işler. Filtreleme kuralı düzensiz olduğunda, `PivotItem.IsHidden` özelliği esnek, öğe düzeyinde bir yedek sunar. Bu stratejileri birleştirmek — örneğin bir etiket filtresi uygulamak ve ardından belirli öğeleri gizlemek — tamamen koddan hassas hedefli özet tablo raporları oluşturmanıza olanak tanır.
{{< app/cells/assistant language="cpp" >}}