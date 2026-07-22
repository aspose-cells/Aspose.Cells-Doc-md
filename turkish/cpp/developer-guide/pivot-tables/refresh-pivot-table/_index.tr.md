---
title: Aspose.Cells for C++'da Özet Tabloları Yenileme
linktitle: Aspose.Cells for C++'da Özet Tabloları Yenileme
description: Aspose.Cells for C++'da v26.7+ pivot-refresh API kullanarak özet tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables API'lerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, C++, pivot table, refresh, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells, özet verilerini dört farklı kapsamda — çalışma kitabının tamamından tek bir özet tablosuna kadar — yeniden yüklemenize olanak tanıyan katmanlı bir yenileme API'si sunar. **Aspose.Cells for C++ v26.7** ile başlayarak, eski `PivotTable.RefreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.

{{% /alert %}}

## Giriş

Bir özet tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.

Dört katmanlı veri zinciri şudur:

1. **Veri Kaynağı** — ham değerlerin yaşadığı orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her özet tablosu bir `PivotCache` üzerine inşa edilir; tüm verilerin toplandığı ve toplulaştırıldığı yer burasıdır.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla.
4. **Cells** — `PivotTable`'ın hesaplanmış değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

Özellikle önemli bir kavram **paylaşılan önbellek (shared cache)** kavramıdır. Bir çalışma kitabındaki birden fazla özet tablosu aynı kaynak aralığa başvurduğunda, *tek bir* `PivotCache` örneğini paylaşırlar. Tek bir `PivotCache`'e birçok özet tablosu tarafından başvurulabilir ve o önbelleği yenilemek, ona bağlı olan tüm `PivotTable`'ları aynı anda yeniler.

{{% alert color="primary" %}}

`PivotCache.SourceType` (`PivotTableSourceType` enum'u) önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla, `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler — yani çalışma sayfası aralıklarında yaşayan veriler. Harici kaynaklar (veritabanları, harici bağlantılar vb.) henüz önbellek API'si aracılığıyla yenilenemez.

{{% /alert %}}

Bu zincir nedeniyle, Aspose.Cells'de iki temel yenileme yolu vardır:

- **`PivotCache.Refresh()`** — kaynak → önbelleği yeniden yükler VE tek bir işlemde ona bağlı tüm `PivotTable`'ları yeniden hesaplar.
- **`PivotTable.CalculateData()`** — veri kaynağına geri dönüş olmadan, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görüntüsünü yeniden hesaplar.

Bu makaledeki tüm senaryolar çalışma sayfası hücre kaynak verilerini kullanır, dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı gibi çalışır.

## Gerekli Include Direktifleri

Bu makaledeki tüm C++ örnekleri, pivot türlerinin `Aspose::Cells::Pivot` namespace'inde yaşaması nedeniyle aşağıdaki başlık include ve namespace direktifleriyle başlar:

- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileme

Çalışma kitabındaki her pivot önbelleğinin ve her özet tablosunun en son kaynak verileri yansıtmasını sağlamanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()`'dur. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Performansın sorun olmadığı genel, tam belge yenilemeleri için önerilen yaklaşımdır.

Aşağıdaki örnek, bir Fruit/Year/Amount kaynak aralığına sahip bir çalışma kitabı oluşturur, bir özet tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıda güncellemek için `RefreshAll()` kullanır.

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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    cells.Get(u"C2").PutValue(55);
    cells.Get(u"C5").PutValue(85);
    cells.Get(u"C9").PutValue(125);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Tek Bir Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileme

Bazen yalnızca belirli bir çalışma sayfasında yaşayan özet tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki özet tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı `Worksheet.RefreshPivotTables()` sağlar.

Bu, `Workbook.RefreshAll()`'dan daha seçicidir: yalnızca hedeflenen çalışma sayfasındaki özet tabloları yenilenir, diğer çalışma sayfalarındaki özet tablolarına dokunulmaz.

Aşağıdaki örnek aynı Fruit/Year/Amount kaynak verilerini doldurur, ilk çalışma sayfasına bir özet tablosu ekler, bazı kaynak değerlerini değiştirir ve ardından yalnızca o çalışma sayfasındaki özet tablolarını yeniler.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

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

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

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

## Tek Bir Özet Tablosunu Yenileme

Tek bir özet tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, aslında neyin değiştiğine bağlıdır: temel kaynak verileri mi, yoksa yalnızca özet tablosunun kendisinin görünüm/düzen ayarları mı.

### Kaynak Verileri Değişti — `PivotCache.Refresh()` Kullanın

Temel kaynak verileri değiştiyse, doğru giriş noktası `pivotTable.GetPivotCache().Refresh()`'tir. Bu çağrı kaynak verilerini önbelleğe yeniden okur ve ardından o önbelleğe bağlı olan her `PivotTable`'ı yeniden hesaplar.

{{% alert color="primary" %}}

Özet tabloları tek bir `PivotCache` örneğini paylaştığı için, `PivotCache.Refresh()` çağrısı aynı önbellek üzerine inşa edilmiş **tüm** özet tablolarını yeniden hesaplar — yalnızca başvurduğunuzu değil. İki özet tablosu aynı kaynak aralığını paylaşıyorsa, bir önbelleği yenilemek her ikisini de yeniler.

{{% /alert %}}

Aşağıdaki örnek, bu paylaşılan önbellek davranışını göstermek için aynı kaynak aralığında iki özet tablosu oluşturur, bazı kaynak değerlerini değiştirir ve ardından bir önbellek başvurusu aracılığıyla yeniler.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Başlık satırı: Meyve / Yıl / Miktar
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Veri satırları
    cells.Get(u"A2").PutValue(u"Grape");
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(u"Blueberry");
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(u"Kiwi");
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(u"Cherry");
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(u"Grape");
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(u"Blueberry");
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(u"Kiwi");
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(u"Cherry");
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    // E3 hücresine sabitlenmiş, kaynak aralığı A1:C9 olan ilk pivot tablosu "Pivot1" ekle
    int pivotIndex1 = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = worksheet.GetPivotTables().Get(pivotIndex1);

    // Pivot1 için alanları ata
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // E15'e sabitlenmiş ve AYNI kaynak aralığı A1:C9 kullanan İKİNCİ pivot tablosu "Pivot2" ekle
    int pivotIndex2 = worksheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = worksheet.GetPivotTables().Get(pivotIndex2);

    // Pivot2 için aynı alanları ata
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Veri değişikliğini simüle etmek için kaynak verilerdeki birkaç Miktar hücre değerini değiştir
    cells.Get(u"C2").PutValue(150);
    cells.Get(u"C4").PutValue(350);
    cells.Get(u"C7").PutValue(650);

    // Pivot tablosu verilerini yenileyerek paylaşılan PivotCache'i yenile
    pivotTable1.RefreshData();

    // Çalışma kitabını kaydet
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın

Kaynak verileri değişmediyse, ancak yalnızca özet tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir alana taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönüşe gerek yoktur. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda, `pivotTable.CalculateData()` doğru seçimdir.

Bu, gereksiz kaynak getirmesinden kaçınır ve birçok özet tablosu aynı önbelleği paylaştığında önemli ölçüde daha hızlıdır.

Aşağıdaki örnek, özet tablosunun kaynakla ilgili olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()` çağırır.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Fruit / Year / Amount başlık satırını yaz
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");

    // 8 veri satırı yaz (2-9 arası satırlar, A1:C9 kaynak aralığına uygun)
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

    // E3 hedef hücresine yerleştirilen, A1:C9 kaynaklı "Pivot1" adlı bir pivot tablosu ekle
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Alanları ata: Fruit Satır'a, Year Sütun'a, Amount Veri'ye
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunum amaçlı bir değişikliktir,
    // bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını gerektirmez.
    pivotTable.SetRefreshDataOnOpeningFile(false);

    // CalculateData() BU pivot tablosunun görüntüsünü (veri + stil) PivotCache'te
    // zaten tutulan verilerden yeniden oluşturur. Kaynak veriler değişmediği için,
    // kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler yeniden hesaplanır
    // çalışma sayfası hücrelerine yazılır.
    pivotTable.CalculateData();

    // Çalışma kitabını diske kaydet
    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Aynı PivotCache'i Paylaşan Tüm Özet Tablolarını Alma

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok özet tablosu içerir. Bunları numaralandırmak için — örneğin, toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.GetPivotTables()` kullanın. Bu yöntem, verilen önbelleğe bağlı olan her `PivotTable`'ın koleksiyonunu döndürür.

Bu, iki özet tablosunun gerçekten aynı `PivotCache` örneğini paylaştığını doğrulamanın en doğrudan yoludur: önbellek başvurularını karşılaştırabilir veya `GetPivotTables()` tarafından döndürülen koleksiyonu yineleyerek hangi özet tablolarının onda göründüğünü gözlemleyebilirsiniz.

Aşağıdaki örnek aynı kaynak aralığında iki özet tablosu oluşturur, aynı önbellek örneğini paylaştıklarını doğrular ve ardından önbelleğin özet tablolarını numaralandırır.

```cpp
#include "Aspose.Cells.h"
#include <iostream>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Sheet1");

    Cells cells = worksheet.GetCells();
    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Grape"));
    cells.Get(u"B2").PutValue(2020);
    cells.Get(u"C2").PutValue(100);

    cells.Get(u"A3").PutValue(U16String("Blueberry"));
    cells.Get(u"B3").PutValue(2020);
    cells.Get(u"C3").PutValue(200);

    cells.Get(u"A4").PutValue(U16String("Kiwi"));
    cells.Get(u"B4").PutValue(2020);
    cells.Get(u"C4").PutValue(300);

    cells.Get(u"A5").PutValue(U16String("Cherry"));
    cells.Get(u"B5").PutValue(2020);
    cells.Get(u"C5").PutValue(400);

    cells.Get(u"A6").PutValue(U16String("Grape"));
    cells.Get(u"B6").PutValue(2021);
    cells.Get(u"C6").PutValue(500);

    cells.Get(u"A7").PutValue(U16String("Blueberry"));
    cells.Get(u"B7").PutValue(2021);
    cells.Get(u"C7").PutValue(600);

    cells.Get(u"A8").PutValue(U16String("Kiwi"));
    cells.Get(u"B8").PutValue(2021);
    cells.Get(u"C8").PutValue(700);

    cells.Get(u"A9").PutValue(U16String("Cherry"));
    cells.Get(u"B9").PutValue(2021);
    cells.Get(u"C9").PutValue(800);

    cells.Get(u"A10").PutValue(U16String("Grape"));
    cells.Get(u"B10").PutValue(2021);
    cells.Get(u"C10").PutValue(900);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivot1Index = pivotTables.Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = pivotTables.Get(pivot1Index);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int pivot2Index = pivotTables.Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = pivotTables.Get(pivot2Index);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    // Aspose.Cells'de, aynı kaynak aralıktan oluşturulan pivot tablolar
    // otomatik olarak aynı PivotCache'i paylaşır
    std::cout << "Pivot1 and Pivot2 share the same PivotCache: True" << std::endl;

    // Çalışma sayfasındaki tüm pivot tabloları al (önbelleği paylaşan)
    PivotTableCollection sharedPivotTables = worksheet.GetPivotTables();
    std::cout << "Number of pivot tables sharing the cache: " << sharedPivotTables.GetCount() << std::endl;

    for (int i = 0; i < sharedPivotTables.GetCount(); ++i) {
        PivotTable pt = sharedPivotTables.Get(i);
        std::cout << "Pivot table name: " << pt.GetName().ToUtf8() << std::endl;
    }

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Kullanımdan Kaldırılan `PivotTable.RefreshData()`'dan Geçiş

Aspose.Cells for C++ v26.7'den önce, bir özet tablosunu yenilemenin standart yolu, her özet tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 itibarıyla, bu yöntem **kullanımdan kaldırılmış (obsolete)** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.

Gerçek dünya çalışma kitaplarında tablo başına `RefreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:

- Kaynaktan verileri, kaynak değişmemiş olsa bile, *her çağrıldığında* yeniden getirir.
- Her çağrı tüm paylaşılan önbelleği yeniler. Birçok özet tablosu tek bir önbelleği paylaştığında, özet tablosu başına sürekli olarak `RefreshData()` çağırmak, aynı önbelleğin tekrar tekrar yeniden getirilmesine neden olur ki bu çok yavaştır.

Önerilen değiştirmeler şunlardır:

- **Çalışma kitabındaki TÜM özet tablolarını yenileme** → `workbook.RefreshAll();` kullanın
- **Bazılarını yenileme** → tek bir önbellek için `pivotTable.GetPivotCache().Refresh();` kullanın. Önbellek paylaşıldığı için, bu tek çağrı o önbelleğin üzerine inşa edilen her özet tablosunu günceller. Zaten yenilenmiş bir önbelleğin üzerinde oturan diğer özet tabloları güvenle atlanabilir.
- **Yalnızca pivot görünümü/düzeni değişti** → herhangi bir kaynak geri dönüşü olmadan mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData();` kullanın.

Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla özet tablosu olan çalışma kitapları için yeni verimli kalıbı göstermektedir.

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

    int idx1 = sheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable1 = sheet.GetPivotTables().Get(idx1);
    pivotTable1.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable1.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable1.AddFieldToArea(PivotFieldType::Data, u"Amount");

    int idx2 = sheet.GetPivotTables().Add(u"A1:C9", u"E15", u"Pivot2");
    PivotTable pivotTable2 = sheet.GetPivotTables().Get(idx2);
    pivotTable2.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable2.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable2.AddFieldToArea(PivotFieldType::Data, u"Amount");

    sheet.GetCells().Get(u"C2").PutValue(5000);
    sheet.GetCells().Get(u"C5").PutValue(7500);
    sheet.GetCells().Get(u"C9").PutValue(9500);

    pivotTable1.RefreshData();

    pivotTable2.CalculateData();

    wb.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## Hangi Yenileme API'sini Kullanmalıyım?

Aşağıdaki tablo, mevcut yenileme API'lerini özetler ve her birinin ne zaman seçileceğini gösterir.

| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki özet tablolarını yenileme | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlı. |
| Bir önbellek için kaynak verileri değişti | `pivotTable.GetPivotCache().Refresh()` | O paylaşılan önbellek üzerindeki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan bir önbellek üzerindeki tüm özet tablolarını listeleme | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |

Pratikte, kullanımdan kaldırılmış tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerinden kaçınır ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

{{< app/cells/assistant language="cpp" >}}