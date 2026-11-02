---
title: Özet Tabloda İlk 10'u Gösterme veya Filtreleme
linktitle: Özet Tabloda İlk 10'u Gösterme veya Filtreleme
description: Aspose.Cells for C++ ile bir özet tablo alanının yalnızca en yüksek veya en düşük sıralı öğelerini nasıl göstereceğinizi öğrenin. Bu makale; Excel 97-2003 Top10AutoShow yöntemini, GetTop10AutoShowSettings ile seçeneklerin okunmasını ve Excel 2007-365 İlk 10 Filtresi'nin FilterTop10 aracılığıyla kullanılmasını ele alır.
keywords: Aspose.Cells, C++, özet tablo, ilk 10, otomatik gösterim, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, GetTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField
type: docs
weight: 20
url: /tr/cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alanın onlarca üyesi bulunduğunda okunması zor olabilir. İlk 10 raporu yalnızca en yüksek veya en düşük sıralı öğeleri tutar; bu da sıralama raporlarının tam olarak ihtiyaç duyduğu şeydir — "gelire göre ilk 5 ürün" veya "satış sayısına göre son 3 bölge". Aspose.Cells bunun için iki mekanizma destekler; bu mekanizmalar Microsoft Excel'in iki nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `PivotField.Top10AutoShow()` yöntemi. Bu, özet tablo alanı üzerinde doğrudan saklanan klasik "En üst/alt N öğeyi göster" ayarıdır. Özgün özet tablo biçiminin bir parçası olduğundan eski ve yeni dâhil her Excel sürümünde çalışır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.FilterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri altında bulunan modern İlk 10 değer filtresidir. Alana bağlı bir `PivotFilter` nesnesi olarak saklanır ve öğe sayısına ve yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te İlk 10'u Gösterme (Top10AutoShow)**
Klasik AutoShow, `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int32_t count, int32_t rankBy)` çağrısıyla tek çağrıda yapılandırılır:
- `isAutoShow` — alan üzerindeki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `true` olduğunda en yüksek sıralı öğeleri (Üst), `false` olduğunda en düşük sıralı öğeleri (Alt) korur.
- `count` — korunacak öğe sayısı; örneğin klasik İlk 10 raporu için 10.
- `rankBy` — değerleriyle öğeleri sıralayan **veri alanının** sıfırdan başlayan dizini. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama bir değer alanına veya alanın kendisine göre belirlenebilir. Aşağıda iki doğal varyant gösterilmektedir.

### **Değer Alanına Göre Sıralama**
Satır alanının öğelerini, "Satışların Toplamı" gibi olağan bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur, ardından satışlara göre ilk 2 sporu gösterir. `rankBy` değeri 0'dır, çünkü "Satışların Toplamı", 0. dizindeki veri alanıdır.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // "Satışların Toplamı" ölçütüne göre sıralanan ilk 2 öğeyi göster (veri alanı dizini 0)
    sportField.Top10AutoShow(true, true, 2, 0);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-value-field.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisi de sıralanabilir — `rankBy` parametresine -1 değerini geçirin. Bu varyant için ek veri alanı gerekmez; alanın satır (veya sütun) alanında bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde `rankBy` özniteliği özet tablonun XML'inden çıkarılır; çünkü -1, ilgili biçimde varsayılan değerdir. `GetTop10AutoShowSettings().GetRankBy()` -1 döndürür.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // Alanın kendisiyle sıralanan en alt 3 öğeyi göster (rankBy = -1)
    sportField.Top10AutoShow(true, false, 3, -1);
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-by-field-itself.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Geçerli Seçeneklerin Okunması (GetTop10AutoShowSettings)**
`PivotField.GetTop10AutoShowSettings()` yöntemi, alan üzerinde saklanan geçerli AutoShow seçeneklerini içeren bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabının veya yeni yapılandırdığınız bir özet tablonun öğelerini nasıl sunacağını incelemek için bunu kullanın — dosyadan yüklenen çalışma kitapları da dâhil.

```cpp
#include "Aspose.Cells.h"
#include <iostream>
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook(u"output-top10-by-value-field.xlsx");
    PivotTable pivotTable = workbook.GetWorksheets().Get(0).GetPivotTables().Get(0);
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    PivotFieldTop10AutoShowSettings settings = sportField.GetTop10AutoShowSettings();
    std::cout << "AutoShow enabled: " << settings.IsAutoShow() << std::endl;
    std::cout << "Direction: " << (settings.IsTop() ? "Top" : "Bottom") << std::endl;
    std::cout << "Item count: " << settings.GetAutoShowCount() << std::endl;
    std::cout << "Ranking data field index: " << settings.GetRankBy() << std::endl;
    Aspose::Cells::Cleanup();
    return 0;
}
```

Dört üye, özet tablo XML'indeki klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir; dolayısıyla okunan değerler, her Excel sürümünün esas alacağı değerlerdir.

## **Not**

{{% alert color="primary" %}}
- `PivotField` üzerindeki doğrudan `IsAutoShow`, `IsAscendShow`, `GetAutoShowCount` ve `GetAutoShowField` özellikleri kullanımdan kaldırılmıştır. Bunun yerine `PivotFieldTop10AutoShowSettings` nesnesini kullanın: `IsAutoShow`, `GetTop10AutoShowSettings().IsAutoShow()` olarak değiştirilir; `IsAscendShow`, `GetTop10AutoShowSettings().IsTop()` olarak değiştirilir; `GetAutoShowCount`, `GetTop10AutoShowSettings().GetAutoShowCount()` olarak değiştirilir ve `GetAutoShowField`, `GetTop10AutoShowSettings().GetRankBy()` olarak değiştirilir. `Top10AutoShow()` yöntemi, ayarları değiştirmek için desteklenen yöntemdir.
- `Top10AutoShow`, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan, öğeleri özet tablonun gövdesinde yer almadığı için bu şekilde sıralanamaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (FilterTop10)**
Modern Excel sürümleri, İlk 10'u alan menüsünde bir değer filtresi olarak sunar (Değer Filtreleri, İlk 10...). Aspose.Cells, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.FilterTop10(int32_t valueFieldIndex, PivotFilterType type, bool isTop, int32_t itemCount)` yöntemiyle bu özelliği modeller:
- `valueFieldIndex` — öğeleri birikmiş değerlerine göre sıralayan veri alanının sıfırdan başlayan dizini.
- `type` — `itemCount` değerinin ne anlama geldiğini belirtir. `PivotFilterType::Count`, sabit sayıda öğeyi (iletişim kutusunun Öğeler seçeneği) korur. `PivotFilterType::Percent`, öğelerin belirli bir yüzdesini korur; bu nedenle `itemCount` doğrudan yüzde değeridir — 30 değeri, öğelerin en üst %30'unu korur. `PivotFilterType::Sum`, öğeleri kümülatif değer kapsamasına göre sıralar.
- `isTop` — `true` değeri Üst, `false` değeri Alt seçeneğini belirtir.
- `itemCount` — İlk N ifadesindeki N değeridir; birimi `type` değerine bağlıdır.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(0, 0).PutValue(u"Sport");
    worksheet.GetCells().Get(0, 1).PutValue(u"Quarter");
    worksheet.GetCells().Get(0, 2).PutValue(u"Sales");
    worksheet.GetCells().Get(1, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(1, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(1, 2).PutValue(2554);
    worksheet.GetCells().Get(2, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(2, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(2, 2).PutValue(3331);
    worksheet.GetCells().Get(3, 0).PutValue(u"Golf");
    worksheet.GetCells().Get(3, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(3, 2).PutValue(4108);
    worksheet.GetCells().Get(4, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(4, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(4, 2).PutValue(4885);
    worksheet.GetCells().Get(5, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(5, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(5, 2).PutValue(5662);
    worksheet.GetCells().Get(6, 0).PutValue(u"Tennis");
    worksheet.GetCells().Get(6, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(6, 2).PutValue(6439);
    worksheet.GetCells().Get(7, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(7, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(7, 2).PutValue(7216);
    worksheet.GetCells().Get(8, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(8, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(8, 2).PutValue(7993);
    worksheet.GetCells().Get(9, 0).PutValue(u"Rugby");
    worksheet.GetCells().Get(9, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(9, 2).PutValue(8770);
    worksheet.GetCells().Get(10, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(10, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(10, 2).PutValue(9547);
    worksheet.GetCells().Get(11, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(11, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(11, 2).PutValue(10324);
    worksheet.GetCells().Get(12, 0).PutValue(u"Cricket");
    worksheet.GetCells().Get(12, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(12, 2).PutValue(11101);
    worksheet.GetCells().Get(13, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(13, 1).PutValue(u"Qtr1");
    worksheet.GetCells().Get(13, 2).PutValue(11878);
    worksheet.GetCells().Get(14, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(14, 1).PutValue(u"Qtr2");
    worksheet.GetCells().Get(14, 2).PutValue(12655);
    worksheet.GetCells().Get(15, 0).PutValue(u"Boxing");
    worksheet.GetCells().Get(15, 1).PutValue(u"Qtr3");
    worksheet.GetCells().Get(15, 2).PutValue(13432);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C16", 2, 5);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Sport");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Sales");
    pivotTable.CalculateData();
    PivotField sportField = pivotTable.GetRowFields().Get(0);
    // İlk 10 Filtresi — "Satışların Toplamı"na göre en üstteki 2 öğeyi tut (veri alanı indeksi 0)
    PivotFilter filter = sportField.FilterTop10(0, PivotFilterType::Count, true, 2);
    // Bunun yerine yüzdeye dayalı bir filtre kullanırsanız, öğelerin en üst %30'unu tutun:
    // sportField.FilterTop10(0, PivotFilterType::Percent, true, 30);
    pivotTable.GetPivotCache().Refresh();
    pivotTable.CalculateData();
    workbook.Save(u"output-top10-filter.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}
`Top10AutoShow` ve `FilterTop10` iki ayrı özelliktir. AutoShow, özet tablo alanı üzerinde ayarlanan klasik `autoShow` özniteliği kümesini yazar ve Excel 97 ve sonrası tüm Excel sürümleri tarafından desteklenir. `FilterTop10`, Excel 2007 veya sonraki sürümlerini gerektiren modern bir `PivotFilter` girdisi yazar. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan özet tablo tüm öğeleri göstermeye geri döner. Eski yazılım araçlarıyla belge üzerinde gidiş-dönüş yapılması gereken durumlarda `Top10AutoShow` tercih edin; modern çalışma kitaplarında ise diğer değer filtreleriyle birlikte kullanılabilmesi nedeniyle `FilterTop10` tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tabloları Etiket veya Değere Göre Filtreleme](/cells/tr/cpp/filter-by-label-or-value-of-pivot-table/)
- [Özet Tabloya Satır ve Sütun Alanları Ekleme](/cells/tr/cpp/pivot-table-add-row-and-column-fields/)
- [Özet Tablodaki Özet Alanlarını Gruplandırma](/cells/tr/cpp/group-pivot-fields-in-the-pivot-table/)
- [Özet Tabloyu Yenileme](/cells/tr/cpp/refresh-pivot-table/)
- [Özet Tabloya Sayfa Alanı Ekleme](/cells/tr/cpp/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="cpp" >}}