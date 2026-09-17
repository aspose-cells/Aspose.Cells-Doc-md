---
title: Aspose.Cells for C++ ile Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
linktitle: Aspose.Cells for C++ ile Pivot Tablolarını ve Pivot Önbelleklerini Yenileme
description: Aspose.Cells for C++ ile v26.7+ pivot yenileme API'sini kullanarak pivot tablolarını nasıl yenileyeceğinizi öğrenin. Bu makale RefreshAll, RefreshPivotTables, PivotCache.Refresh, CalculateData ve GetPivotTables yöntemlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, C++, pivot tablosu, yenileme, PivotCache, CalculateData, RefreshAll, RefreshPivotTables, GetPivotTables, v26.7
type: docs
weight: 200
url: /tr/cpp/refresh-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, tüm çalışma kitabından tek bir pivot tablosuna kadar dört farklı kapsamda pivot verilerini yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for C++ v26.7** sürümünden itibaren eski `PivotTable.RefreshData()` yöntemi kullanımdan kaldırılmış (obsolete) olarak işaretlenmiştir ve bu makalede açıklanan daha verimli, önbellek farkındalığına sahip API'lerle değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir pivot tablosunu yenileme nadiren tek bir işlemdir. Sahne arkasında Aspose.Cells, orijinal kaynak verilerinizi çalışma sayfasında gördüğünüz işlenmiş değerlere bağlayan katmanlı bir veri zinciri tutar. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şudur:
1. **Veri Kaynağı** — ham değerlerin bulunduğu orijinal çalışma sayfası aralıkları, veritabanı sorgusu veya konsolidasyon aralığı.
2. **PivotCache** — kaynak verilerin bellek içi anlık görüntüsü. Her pivot tablosu bir `PivotCache` üzerine inşa edilir; tüm veriler burada toplanır ve agrega edilir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache`'inden okur, doğrudan veri kaynağından asla okumaz.
4. **Cells** — `PivotTable`'ın hesaplanan değerlerini ve stillerini işlediği çalışma sayfası `Cells` koleksiyonu.

{{% alert color="primary" %}}
`PivotCache.SourceType` (`PivotTableSourceType` enum değeri) önbellek verilerinin nereden geldiğini belirtir. v26.7 itibarıyla `PivotCache.Refresh()` yalnızca **`Sheet`** ve **`Consolidation`** kaynak türlerini destekler; yani çalışma sayfası aralıklarında bulunan verileri. Dış kaynaklar (veritabanları, dış bağlantılar vb.) önbellek API üzerinden henüz yenilenemez.
{{% /alert %}}

Bu zincir nedeniyle Aspose.Cells'te iki temel yenileme yolu vardır:
- **`PivotTable.CalculateData()`** — veri kaynağına geri dönmeden, zaten önbelleğe alınmış verilerden tek bir `PivotTable`'ın görünümünü yeniden hesaplar.
Bu makaledeki tüm senaryolarda çalışma sayfası hücresi kaynak verileri kullanılır; dolayısıyla kaynak türü `Sheet`'tir ve yenileme işlemleri açıklandığı şekilde çalışır.

## Hızlı Başlangıç
Çalışma kitabındaki her pivot'u yenileyen en kısa olası koda ihtiyacınız varsa, tek bir çağrı yeterlidir:

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
    pivotTable.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Bu makaledeki diğer her şey, bunun yerine ne zaman daha dar kapsamlı bir API seçmeniz gerektiğini açıklar.

## Gerekli Include Direktifleri
Bu makaledeki tüm C++ örnekleri, pivot türlerinin `Aspose::Cells::Pivot` namespace'inde bulunması nedeniyle aşağıdaki başlık include ve namespace direktifleriyle başlar:
- `#include <system/object.h>`
- `#include "Aspose.Cells.h"`
- `using namespace Aspose::Cells;`
- `using namespace Aspose::Cells::Pivot;`

## Çalışma Kitabındaki Tüm Pivot Tablolarını Yenileme
Çalışma kitabındaki her pivot önbelleğinin ve her pivot tablosunun en güncel kaynak verileri yansıttığından emin olmanız gerektiğinde, en basit ve en kapsamlı API `Workbook.RefreshAll()` yöntemidir. Tek bir çağrı tüm çalışma kitabını dolaşır — her `PivotCache`'i kendi kaynağından yeniler ve ardından ona bağlı her `PivotTable`'ı yeniden hesaplar. Performansın sorun olmadığı genel, tam belge yenilemeleri için önerilen yaklaşım budur.
Aşağıdaki örnek, Meyve/Yıl/Tutar kaynak aralığıyla bir çalışma kitabı oluşturur, bir pivot tablo oluşturur, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek bir çağrıyla güncel hale getirmek için `RefreshAll()` yöntemini kullanır.

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

## Tek Bir Çalışma Sayfasındaki Tüm Pivot Tablolarını Yenileme
Bazen yalnızca belirli bir çalışma sayfasında bulunan pivot tablolarını yenilemeniz gerekir — örneğin, diğer çalışma sayfalarındaki pivot tablolarının ilgisiz olduğu biliniyorsa ve bunlara dokunulmaması gerektiğinde. Bu durum için Aspose.Cells, tek bir `Worksheet` örneğiyle sınırlı olan `Worksheet.RefreshPivotTables()` yöntemini sağlar.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
int main() {
    Aspose::Cells::Startup();
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    // Meyve / Yıl / Miktar başlık satırını yaz
    worksheet.GetCells().Get(u"A1").PutValue(u"Fruit");
    worksheet.GetCells().Get(u"B1").PutValue(u"Year");
    worksheet.GetCells().Get(u"C1").PutValue(u"Amount");
    // 8 veri satırı yaz (2-9. satırlar, kaynak aralığı A1:C9'a uyuyor)
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
    // Hedef hücre E3'e yerleştirilen, A1:C9'dan veri alan "Pivot1" adlı bir özet tablo ekle
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C9", u"E3", u"Pivot1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);
    // Alanları ata: Satır için Meyve, Sütun için Yıl, Veri için Miktar
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    // Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunumla ilgili bir değişikliktir,
    // bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
    pivotTable.SetRefreshDataOnOpeningFile(false);
    // CalculateData(), BU özet tablosunun görüntüsünü (veri + stil) PivotCache'te zaten
    // tutulan verilerden yeniden oluşturur. Kaynak veriler değişmediğinden,
    // kaynağa gidiş-dönüş yapılmaz — yalnızca önbelleğe alınmış değerler çalışma sayfası
    // hücrelerine yeniden hesaplanır.
    pivotTable.CalculateData();
    // Çalışma kitabını diske kaydet
    workbook.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## Tek Bir Pivot Tablosunu Yenileme
Tek bir pivot tablosu üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Aralarındaki seçim, gerçekte neyin değiştiğine bağlıdır: altta yatan kaynak veriler mi yoksa yalnızca pivot tablosunun görünüm/düzen ayarları mı.

### Kaynak Veriler Değişti — `PivotCache.Refresh()` Kullanın
Alttaki kaynak veriler değiştiyse, doğru giriş noktası `pivotTable.GetPivotCache().Refresh()` çağrısıdır. Bu çağrı, kaynak verileri önbelleğe geri okur ve ardından o önbelleğe bağlı olan her `PivotTable`'ı yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `CalculateData()` Kullanın
Kaynak veriler değişmediyse ancak yalnızca pivot tablosunun görünüm veya düzen ayarları değiştirildiyse (örneğin, bir alan farklı bir bölgeye taşındıysa veya açılışta yenileme ayarı değiştirildiyse), veri kaynağına geri dönmek gerekmez. Önbellek zaten doğru verileri tutar; yalnızca işlenmiş `PivotTable`'ın yeniden hesaplanması gerekir. Bu durumda `pivotTable.CalculateData()` doğru seçimdir.
Aşağıdaki örnek, pivot tablosunun kaynak olmayan bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden işlemek için `CalculateData()` yöntemini çağırır.

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
    pivotTable2.CalculateData();
    wb.Save(u"output.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

Bir çalışma kitabı genellikle tek bir paylaşılan önbelleğin üzerinde oturan birçok pivot tablosu içerir. Bunları numaralandırmak için — örneğin, toplu bir yenileme gerçekleştirmeden önce veya paylaşılan önbellek etkisini tanılamak için — `PivotCache.GetPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı olan her `PivotTable`'ın koleksiyonunu döndürür.

## Kullanımdan Kaldırılan `PivotTable.RefreshData()` Yönteminden Geçiş
Aspose.Cells for C++ v26.7'den önce, bir pivot tablosunu yenilemenin standart yolu her pivot tablosunda ayrı ayrı `PivotTable.RefreshData()` çağırmaktı. v26.7 itibarıyla bu yöntem **kullanımdan kaldırılmış (obsolete)** olarak işaretlenmiştir ve yukarıda açıklanan önbellek farkındalığına sahip API'lerle değiştirilmelidir.
Tablo başına `RefreshData()` yaklaşımının gerçek dünya çalışma kitaplarında sorunlu olmasının iki nedeni vardır:
- Kaynak değişmemiş olsa bile her çağrıldığında verileri kaynaktan yeniden getirir.
Önerilen alternatifler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden çok pivot tablosuna sahip çalışma kitapları için yeni ve verimli kalıbı gösterir.

```cpp
using Aspose.Cells;
Workbook workbook = new Workbook("input.xlsx");
workbook.RefreshAll();
workbook.Save("output.xlsx");
```

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tablo, mevcut yenileme API'lerini özetler ve her birinin ne zaman seçilmesi gerektiğini gösterir.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenileme | `Workbook.RefreshAll()` | Tek çağrı; tüm önbellekleri ve tabloları kapsar. |
| Yalnızca tek bir sayfadaki pivot tablolarını yenileme | `Worksheet.RefreshPivotTables()` | Tek bir çalışma sayfasıyla sınırlı. |
| Bir önbellek için kaynak veriler değişti | `pivotTable.GetPivotCache().Refresh()` | O paylaşılan önbellekteki TÜM pivot tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.CalculateData()` | Gereksiz kaynak geri dönüşünü atlar. |
| Paylaşılan önbellekteki tüm pivot tablolarını listeleme | `pivotCache.GetPivotTables()` | Toplu yenilemeden önce numaralandırmak için kullanın. |
Uygulamada, kullanımdan kaldırılan tablo başına `RefreshData()` yerine önbellek tabanlı API'leri tercih edin. Bunlar paylaşılan önbelleklerin farkındadır, gereksiz kaynak getirmelerini önler ve yenileme gereksiniminizi karşılayan en küçük kapsamı seçmenize olanak tanır.

## Yaygın Tuzaklar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir pivot tablosu, veri zinciri yenilendiğinde işlenmiş değerlerini çalışma sayfasına yalnızca o zaman yazar. Kaynak hücreleri değiştirdiyseniz, `Workbook.Save()` çağrısından önce `PivotCache.Refresh()` (veya `Workbook.RefreshAll()`) çağırın; aksi takdirde kaydedilen dosya hâlâ eski agrega edilmiş değerleri içerir.
- **Tablo başına kullanımdan kaldırılan `RefreshData()` çağrısı.** v26.7'de `PivotTable.RefreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrı için kaynağı yeniden getirir. Bir önbelleği paylaşan birden çok pivot tablosuyla bu, N adet gereksiz kaynak getirmesi anlamına gelir. Bunun yerine tek bir `PivotCache.Refresh()` ve ardından her tablo için `CalculateData()` kullanın.
- **Yalnızca düzen değiştiğinde yenileme yapmak.** Kaynak verilere dokunmadan yalnızca pivot tablosunun görünümünü (sütun sırası, `ConsolidationFunction` vb.) değiştirdiyseniz `PivotCache.Refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden işlemek için `pivotTable.CalculateData()` çağırın.
- **`PivotCache.Refresh()` tarafından desteklenmeyen dış kaynak.** Pivot tablosunun kaynağı dış bir bağlantıdan (veritabanı, OLAP küpü vb.) geliyorsa, `PivotCache.Refresh()` bunu v26.7'de yenileyemez — şu anda yalnızca `Sheet` ve `Consolidation` kaynak türlerini destekler. Dış kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="cpp" >}}