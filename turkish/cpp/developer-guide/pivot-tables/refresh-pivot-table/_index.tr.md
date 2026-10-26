---
title: Aspose.Cells for C++ ile Pivot Tablolarını ve Pivot Önbelleklerini Yenileyin
linktitle: Aspose.Cells for C++ ile Pivot Tablolarını ve Pivot Önbelleklerini Yenileyin
description: Aspose.Cells for C++ ile v26.7+ pivot yenileme API'sini kullanarak Pivot Tablolarının nasıl yenilendiğini öğrenin. Bu makale, RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables işlevlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, C++, Pivot Tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, pivot verisini çalışma kitabının tamamından tek bir Pivot Tablosuna kadar dört farklı kapsamda yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for C++ v26.7** sürümünden başlayarak eski `PivotTable.RefreshData()` yöntemi eskimiş olarak işaretlenir ve bu makalede açıklanan daha verimli, önbellek farkındalıklı API'lerle değiştirilmelidir.
{{% /alert %}}

## Introduction
Bir Pivot Tablosunu yenileme nadiren tek işlemden oluşur. Aspose.Cells arka planda, özgün kaynak verinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri korur. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şöyledir:
1. **Veri Kaynağı** — özgün değerlerin bulunduğu çalışma sayfası aralıkları, veritabanı sorgusu veya birleştirme aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her Pivot Tablosu bir `PivotCache` üzerine kuruludur; tüm verilerin toplandığı ve özetlendiği yer burasıdır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` nesnesi yalnızca kendi `PivotCache` verisinden okur, hiçbir zaman doğrudan veri kaynağından okumaz.
4. **Cells** — `PivotTable` nesnesinin hesaplanan değerlerini ve biçimlerini oluşturduğu çalışma sayfası `Cells` koleksiyonu.

{{% alert color="primary" %}}
`PivotCache.SourceType` (`PivotTableSourceType` türündeki enum), önbellek verisinin nereden geldiğini gösterir. v26.7 sürümünde `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini, başka bir ifadeyle çalışma sayfası aralıklarında bulunan verileri destekler. Harici kaynaklar (veritabanları, harici bağlantılar vb.) önbellek API'si aracılığıyla henüz yenilenemez.
Bu veri zinciri nedeniyle Aspose.Cells için iki temel yenileme yolu vardır:
- **`PivotTable.CalculateData()`** — bir `PivotTable` nesnesinin görüntülenmesini, veri kaynağına geri dönülmeden önbelleğe alınmış verilerden yeniden hesaplar.
Bu makaledeki tüm senaryolar çalışma sayfası hücrelerini kaynak olarak kullandığından kaynak türü `Sheet` olur ve yenileme işlemleri açıklandığı gibi davranır.
{{% /alert %}}

## Quick Start
Yalnızca çalışma kitabındaki tüm Pivot Tablolarını yenileyen en kısa kodu istiyorsanız, tek çağrı yeterlidir:

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();
    Workbook workbook(u"input.xlsx");
    workbook.RefreshAll();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Bu makalenin geri kalanı, daha dar kapsamlı bir API'nin ne zaman seçilmesi gerektiğini açıklar.

## Required Include Directives
Bu makaledeki tüm C++ örnekleri, Pivot türlerinin `Aspose::Cells::Pivot` namespace içinde yer alması nedeniyle aşağıdaki üst bilgi include ve namespace yönergeleriyle başlar:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Refresh All Pivot Tables in the Workbook
Çalışma kitabındaki her Pivot önbelleğinin ve her Pivot Tablosunun en güncel kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()` yöntemidir. Tek çağrı çalışma kitabının tamamını tarar ve her `PivotCache` nesnesini kendi kaynağından yeniler; ardından bu önbelleğe bağlı her `PivotTable` nescesini yeniden hesaplar. Performansın bir sorun teşkil etmediği genel belge düzeyindeki yenilemelerde bu yaklaşım önerilir.
Aşağıdaki örnek, Fruit/Year/Amount kaynak aralığı bulunan bir çalışma kitabı oluşturur, bir Pivot Tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından `RefreshAll()` çağırarak her şeyi tek çağrıda güncel hâle getirir.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));
    cells.Get(u"A2").PutValue(U16String("grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(50);
    cells.Get(u"A3").PutValue(U16String("blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(60);
    cells.Get(u"A4").PutValue(U16String("kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(70);
    cells.Get(u"A5").PutValue(U16String("cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(80);
    cells.Get(u"A6").PutValue(U16String("grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(90);
    cells.Get(u"A7").PutValue(U16String("blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(100);
    cells.Get(u"A8").PutValue(U16String("kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(110);
    cells.Get(u"A9").PutValue(U16String("cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(120);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh All Pivot Tables on a Single Worksheet
Bazen yalnızca belirli bir çalışma sayfasında bulunan Pivot Tablolarını yenilemeniz gerekir. Örneğin diğer çalışma sayfalarındaki Pivot Tablolarının ilişkisiz olduğu bilinir ve bunlara dokunulmamalıdır. Bu durumda Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.RefreshPivotTables()` yöntemini sunar.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    worksheet.GetCells().Get(u"A2").PutValue(u"grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2021);
    worksheet.GetCells().Get(u"C3").PutValue(150);
    worksheet.GetCells().Get(u"A4").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(200);
    worksheet.GetCells().Get(u"A5").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2021);
    worksheet.GetCells().Get(u"C5").PutValue(120);
    worksheet.GetCells().Get(u"A6").PutValue(u"grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(180);
    worksheet.GetCells().Get(u"A7").PutValue(u"blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2020);
    worksheet.GetCells().Get(u"C7").PutValue(130);
    worksheet.GetCells().Get(u"A8").PutValue(u"kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(220);
    worksheet.GetCells().Get(u"A9").PutValue(u"cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2020);
    worksheet.GetCells().Get(u"C9").PutValue(140);
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    worksheet.GetCells().Get(u"C2").PutValue(300);
    worksheet.GetCells().Get(u"C5").PutValue(250);
    worksheet.GetCells().Get(u"C9").PutValue(400);
    worksheet.RefreshPivotTables();
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Refresh a Single Pivot Table
Tek bir Pivot Tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: temel kaynak veriler mi, yoksa yalnızca Pivot Tablosunun kendi görünüm veya düzen ayarları mı?

### Source Data Changed — Use `PivotCache.Refresh()`
Temel kaynak verileri değiştiyse doğru giriş noktası `pivotTable.GetPivotCache().Refresh()` yöntemidir. Bu çağrı kaynak verileri önbelleğe yeniden okur ve ardından bu önbelleğe bağlı her `PivotTable` nesnesini yeniden hesaplar.

### Only View/Layout Changed — Use `CalculateData()`
Kaynak verileri değişmemişse ve yalnızca Pivot Tablosunun görünüm veya düzen ayarları değiştirilmişse, örneğin bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı açılıp kapatıldıysa, veri kaynağına geri dönmeniz gerekmez. Önbellek zaten doğru verileri içerir; yalnızca işlenmiş `PivotTable` nesnesinin yeniden hesaplanması gerekir. Bu durumda doğru seçim `pivotTable.CalculateData()` yöntemidir.
Aşağıdaki örnek, Pivot Tablosunun kaynak dışı bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()` işlevini çağırır.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Write Fruit / Year / Amount header row
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // Write 8 data rows (rows 2-9, fitting the source range A1:C9)
    worksheet.GetCells().Get(u"A2").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B2").PutValue(2020);
    worksheet.GetCells().Get(u"C2").PutValue(100);
    worksheet.GetCells().Get(u"A3").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B3").PutValue(2020);
    worksheet.GetCells().Get(u"C3").PutValue(200);
    worksheet.GetCells().Get(u"A4").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B4").PutValue(2020);
    worksheet.GetCells().Get(u"C4").PutValue(300);
    worksheet.GetCells().Get(u"A5").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B5").PutValue(2020);
    worksheet.GetCells().Get(u"C5").PutValue(400);
    worksheet.GetCells().Get(u"A6").PutValue(u"Grape");
    worksheet.GetCells().Get(u"B6").PutValue(2021);
    worksheet.GetCells().Get(u"C6").PutValue(150);
    worksheet.GetCells().Get(u"A7").PutValue(u"Blueberry");
    worksheet.GetCells().Get(u"B7").PutValue(2021);
    worksheet.GetCells().Get(u"C7").PutValue(250);
    worksheet.GetCells().Get(u"A8").PutValue(u"Kiwi");
    worksheet.GetCells().Get(u"B8").PutValue(2021);
    worksheet.GetCells().Get(u"C8").PutValue(350);
    worksheet.GetCells().Get(u"A9").PutValue(u"Cherry");
    worksheet.GetCells().Get(u"B9").PutValue(2021);
    worksheet.GetCells().Get(u"C9").PutValue(450);
 // Add a pivot table placed at destination cell E3, sourcing from A1:C9
    PivotTable pivotTable = worksheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    // Assign fields: Fruit to Row, Year to Column, Amount to Data
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Modify a view/layout property — this is a presentation-only change,
    // so it does NOT require re-reading the source data through PivotCache.Refresh().
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData() re-renders THIS pivot table's display (data + style) from the
    // data already held in the PivotCache. Because the source data did not change,
    // no round-trip to the source is performed — only the cached values are recalculated
    // into worksheet cells.
    pivotTable.CalculateData();
    // Save the workbook to disk
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerine kurulmuş birçok Pivot Tablosu içerir. Bunları sıralamak için — örneğin toplu yenileme yapmadan önce veya paylaşılan önbelleğin etkisini tanılamak için — `PivotCache.GetPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı her `PivotTable` nesnesinin koleksiyonunu döndürür.

## Migrating from the Obsolete `PivotTable.RefreshData()`
Aspose.Cells for C++ v26.7 sürümünden önce, bir Pivot Tablosunu yenilemenin standart yolu her Pivot Tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 itibarıyla bu yöntem **eskimiş** olarak işaretlenir ve yukarıda açıklanan önbellek farkındalıklı API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Her çağrıldığında, kaynak değişmemiş olsa bile verileri kaynaktan *yeniden getirir*.
Önerilen değiştirmeler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla Pivot Tablosu içeren çalışma kitapları için yeni ve verimli kalıbı gösterir.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    sheet.GetCells().Get(u"B1").PutValue(u"Year");
    sheet.GetCells().Get(u"C1").PutValue(u"Amount");
    sheet.GetCells().Get(u"A2").PutValue(u"Grape");      sheet.GetCells().Get(u"B2").PutValue(2020); sheet.GetCells().Get(u"C2").PutValue(1000);
    sheet.GetCells().Get(u"A3").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B3").PutValue(2020); sheet.GetCells().Get(u"C3").PutValue(2000);
    sheet.GetCells().Get(u"A4").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B4").PutValue(2020); sheet.GetCells().Get(u"C4").PutValue(1500);
    sheet.GetCells().Get(u"A5").PutValue(u"Cherry");     sheet.GetCells().Get(u"B5").PutValue(2020); sheet.GetCells().Get(u"C5").PutValue(2500);
    sheet.GetCells().Get(u"A6").PutValue(u"Grape");      sheet.GetCells().Get(u"B6").PutValue(2021); sheet.GetCells().Get(u"C6").PutValue(3000);
    sheet.GetCells().Get(u"A7").PutValue(u"Blueberry");  sheet.GetCells().Get(u"B7").PutValue(2021); sheet.GetCells().Get(u"C7").PutValue(1800);
    sheet.GetCells().Get(u"A8").PutValue(u"Kiwi");       sheet.GetCells().Get(u"B8").PutValue(2021); sheet.GetCells().Get(u"C8").PutValue(2200);
    sheet.GetCells().Get(u"A9").PutValue(u"Cherry");     sheet.GetCells().Get(u"B9").PutValue(2021); sheet.GetCells().Get(u"C9").PutValue(2700);
    PivotTable pivotTable1 = sheet.GetPivotTables().Add(u"A1:C9", 2, 4);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");
    PivotTable pivotTable2 = sheet.GetPivotTables().Add(u"A1:C9", 14, 4);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");
    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Which Refresh API Should I Use?
Aşağıdaki tablo, kullanılabilir yenileme API'lerini ve her birinin ne zaman seçilmesi gerektiğini özetler.
| Amaç | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenile | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir çalışma sayfasındaki Pivot Tablolarını yenile | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlıdır. |
| Bir önbelleğin kaynak verileri değişti | `pivotTable.GetPivotCache().Refresh()` | Paylaşılan önbellekteki TÜM Pivot Tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak gidiş-dönüşünü atlar. |
| Paylaşılan önbellekteki tüm Pivot Tablolarını listele | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce sıralamak için kullanın. |
Uygulamada eskimiş tablo başına `RefreshData()` yöntemi yerine önbellek tabanlı API'leri tercih edin. Bu API'ler paylaşılan önbelleklerin farkındadır, gereksiz kaynak veri getirme işlemlerini önler ve yenileme gereksiniminizi karşılayan en dar kapsamı seçmenizi sağlar.

## Common Pitfalls
- **Kaydetmeden önce yenilemeyi unutmak.** Bir Pivot Tablosu, veri zinciri yenilendiğinde hesaplanmış değerlerini çalışma sayfasına yazar. Kaynak hücrelerini değiştirirseniz `Workbook.Save()` çağrısından önce `PivotCache.Refresh()` (veya `Workbook.RefreshAll()`) çağırın; aksi takdirde kaydedilen dosya eski özetlenmiş değerleri içermeye devam eder.
- **Eskimiş `RefreshData()` yöntemini tablo başına çağırmak.** v26.7 sürümünde `PivotTable.RefreshData()` eskimiş olarak işaretlenir ve her çağrıda kaynağı yeniden getirir. Bir önbelleği paylaşan birden fazla Pivot Tablosu bulunduğunda bu, N adet gereksiz kaynak veri getirme işlemi anlamına gelir. Bunun yerine tek bir `PivotCache.Refresh()` çağrısı ve ardından her tablo için `CalculateData()` kullanın.
- **Yalnızca düzen değiştiğinde yenilemek.** Kaynak verilerine dokunmadan yalnızca Pivot Tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()` çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen harici kaynak.** Pivot Tablosunun kaynağı harici bir bağlantıdan geliyorsa (veritabanı, OLAP küpü vb.) `PivotCache.Refresh()` bunu v26.7 sürümünde yenileyemez; yöntem şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="cpp" >}}