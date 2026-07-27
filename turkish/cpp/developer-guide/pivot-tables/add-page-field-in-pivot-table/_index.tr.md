---
title: Aspose.Cells for .NET'te PivotTable'a filtre alanları ekleme
linktitle: Filtre Alanları Ekleme
description: Aspose.Cells for C++ kullanarak pivot tablolarda filtre alanlarını nasıl ekleyeceğinizi ve yapılandıracağınızı öğrenin, filtre alanı ekleme, tek seçimli filtreleme ve çoklu seçim filtreleme dahil.
keywords: Aspose.Cells, C++, pivot tablosu, filtre alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/cpp/add-filter-field-in-pivot-table/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, pivot tablolardaki filtre alanlarının tüm yaşam döngüsünü destekler. Bir filtre alanını üst düzey kolaylık API'si veya alt düzey `PageFields` koleksiyonu aracılığıyla ekleyebilir ve filtreni tek seçim modunda yönetebilir, her sayfa öğesini göstermek için temizleyebilir ya da Excel'deki onay kutusu kullanıcı arayüzü aracılığıyla kullanıcıların aynı anda birden fazla sayfa öğesi seçmesine izin vermek için alanı çoklu seçime geçirebilirsiniz.
{{% /alert %}}

## **Giriş**

filtre alanı, pivot gövdesinin kaynak verilerin *hangi alt kümesini* görüntüleyeceğini kontrol eden bir pivot alanıdır. Son kullanıcılar bunu Excel'de oluşturulan bir pivotun üst kısmında bir açılır menü olarak görür ve kullanılabilir sayfa öğelerinden birini seçmek pivot gövdesini yalnızca o sayfa öğesine ait kayıtların özetleneceği şekilde yeniden oluşturur. Bir pivot alanı, `PivotFieldType.Row`, `PivotFieldType.Column` veya `PivotFieldType.Data` yerine `PivotFieldType.Page` olarak kaydedildiğinde filtre alanı haline gelir.

Bir filtre alanı iki davranışta çalışabilir. Varsayılan **tek seçim** davranışında aynı anda yalnızca bir sayfa öğesi görünür, dolayısıyla pivot gövdesi tam olarak bir alt kümeyi özetler. **Çoklu seçim** davranışında ise alan bir onay kutusu listesi sunar ve pivot gövdesi işaretlenen her sayfa öğesinin birleşimini özetler. Aynı kaynak alan, tek bir özellik değiştirilerek bu davranışlar arasında ileri geri taşınabilir.

Aspose.Cells for C++, bir filtre alanını kaydetmek için iki eşdeğer yol sunar. Üst düzey API, kaynak sütun adını alan ve alanı tek bir çağrıyla ekleyen `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` yöntemidir. Alt düzey API ise zaten bir `PivotField` referansına sahip olduğunuzda ve aynı alan örneğini filtre alanına eklemek istediğinizde kullanılan `PivotTable.PageFields.Add(PivotField)` yöntemidir. Her iki API de aynı `PageFields` koleksiyonunu doldurur ve bu makalenin devamı aralarında nasıl seçim yapılacağını ve her filtreleme modunun nasıl yönetileceğini gösterir.

## **filtre alanı Ekleme**

Bir pivot alanını filtre alanına kaydetmenin iki yolu vardır. Üst düzey çağrı, kaynak sütun adını bir dize olarak alır ve en yaygın yoldur. Alt düzey çağrı, mevcut bir `PivotField` örneğini kabul eder ve aynı alan nesnesinin birden fazla pivot alanında yeniden kullanılması gerektiğinde kullanışlıdır. Her iki çağrı da alanı `PivotTable.PageFields` koleksiyonuna yerleştirir ve ardından alan, oluşturulan pivotun üst kısmında sayfa açılır menüsü olarak görünür.

### AddFieldToArea ile filtre alanı Ekleme

Aşağıdaki örnek küçük bir Fruit / Year / Amount veri kümesi oluşturur, E3 hücresine bir pivot tablo yerleştirir (satır alanında `Fruit`, veri alanında `Amount` ve filtre alanında `Year`), pivot'u yeniler ve çalışma kitabını kaydeder.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    // Yeni bir çalışma kitabı oluştur
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    Cells cells = worksheet.GetCells();

    // Başlık satırını ayarla
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // 9 satır örnek veri doldur: Meyve, Yıl, Tutar
    const char* fruits[] = { "apple", "banana", "apple", "grape", "orange", "banana", "grape", "apple", "orange" };
    int years[]   = { 2020, 2021, 2021, 2020, 2022, 2020, 2021, 2022, 2021 };
    int amounts[] = { 100, 200, 150, 120, 180, 90, 130, 170, 110 };

    for (int i = 0; i < 9; ++i)
    {
        cells.Get(i + 1, 0).PutValue(U16String(fruits[i]));
        cells.Get(i + 1, 1).PutValue(years[i]);
        cells.Get(i + 1, 2).PutValue(amounts[i]);
    }

    // E3 hücresine sabitlenmiş bir pivot tablo ekle
    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:C10", u"E3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    // Alanları bölgelerine ekle: Meyve Satır olarak, Tutar Veri olarak, Yıl Sayfa alanı olarak
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // Pivot tablo verilerini yenile ve hesapla
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    // Çalışma kitabını kaydet
    workbook.Save(u"pageFieldSample.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### PageFields.Add ile filtre alanı Ekleme

Zaten bir `PivotField` örneği ile çalışıyorsanız, bunu doğrudan `PivotTable.PageFields.Add` yöntemine geçebilirsiniz. Pivot tablo ve filtre alanı, önceki senaryodakiyle tam olarak aynı şekilde oluşturulur; yalnızca son filtre alanı kaydı alt düzey API çağrısıyla değiştirilir.

```cpp
#include "Aspose.Cells.h"
#include <string>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Başlıklar
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    // Örnek veri (9 satır)
    cells.Get(u"A2").PutValue(u"apple");     cells.Get(u"B2").PutValue(u"2020"); cells.Get(u"C2").PutValue(100);
    cells.Get(u"A3").PutValue(u"apple");     cells.Get(u"B3").PutValue(u"2021"); cells.Get(u"C3").PutValue(150);
    cells.Get(u"A4").PutValue(u"apple");     cells.Get(u"B4").PutValue(u"2022"); cells.Get(u"C4").PutValue(200);
    cells.Get(u"A5").PutValue(u"grape");     cells.Get(u"B5").PutValue(u"2020"); cells.Get(u"C5").PutValue(300);
    cells.Get(u"A6").PutValue(u"grape");     cells.Get(u"B6").PutValue(u"2021"); cells.Get(u"C6").PutValue(400);
    cells.Get(u"A7").PutValue(u"grape");     cells.Get(u"B7").PutValue(u"2022"); cells.Get(u"C7").PutValue(500);
    cells.Get(u"A8").PutValue(u"blueberry"); cells.Get(u"B8").PutValue(u"2020"); cells.Get(u"C8").PutValue(250);
    cells.Get(u"A9").PutValue(u"blueberry"); cells.Get(u"B9").PutValue(u"2021"); cells.Get(u"C9").PutValue(350);
    cells.Get(u"A10").PutValue(u"blueberry");cells.Get(u"B10").PutValue(u"2022");cells.Get(u"C10").PutValue(450);

    // E3 konumunda A1:C10 aralığını kapsayacak şekilde pivot tablo ekle
    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String(u"E3"), U16String(u"A1:C10"), U16String(u"PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Fruit -> Satır, Amount -> Veri
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"Amount"));

    // Düşük seviyeli yaklaşım: BaseFields içindeki mevcut Year PivotField'ını bul
    // ve PageFields.Add(PivotField) aracılığıyla Sayfa alanına kaydet.
    PivotFieldCollection baseFields = pivotTable.GetBaseFields();
    int baseFieldCount = baseFields.GetCount();
    for (int i = 0; i < baseFieldCount; ++i) {
        PivotField f = baseFields.Get(i);
        if (f.GetName().ToUtf8() == "Year") {
            pivotTable.GetPageFields().Add(f);
            break;
        }
    }

    // Yeni sayfa alanının kaydedilen çalışma kitabına yansıtılması için yenile
    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Tek Seçimli Filtreleme (Bir Sayfa Öğesi Gösterme)**

Varsayılan tek seçim davranışında filtre alanı tek bir açılır menü olarak işlenir ve `PivotField.CurrentPageItem` tamsayısı, pivot gövdesini hangi sayfa öğesinin yöneteceğini seçer. Belirli bir indeks atamak o öğeyi seçer; özel sentinel değeri `0x7FFD` (ondalık 32765) atamak filtreyi temizler, böylece her sayfa öğesi aynı anda özetlenir. Tek seçim varsayılandır; açıkça etkinleştirmenize gerek yoktur.

### Tüm Öğeleri Gösterme

`CurrentPageItem` öğesini sihirli değer `0x7FFD` olarak ayarlamak, filtreni temizlemeye eşdeğerdir: pivot gövdesi, hiçbir filtre uygulanmamış gibi her sayfa öğesini özetler.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    Cells cells = sheet.GetCells();
    cells.Get(u"A1").PutValue(u"Fruit");
    cells.Get(u"B1").PutValue(u"Year");
    cells.Get(u"C1").PutValue(u"Amount");

    U16String fruits[6] = {u"Apple", u"Apple", u"Banana", u"Banana", u"Cherry", u"Cherry"};
    int years[6] = {2022, 2023, 2022, 2023, 2022, 2023};
    int amounts[6] = {100, 150, 80, 120, 200, 250};

    for (int r = 0; r < 6; r++) {
        cells.Get(r + 1, 0).PutValue(fruits[r]);
        cells.Get(r + 1, 1).PutValue(years[r]);
        cells.Get(r + 1, 2).PutValue(amounts[r]);
    }

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int index = pivotTables.Add(u"=A1:C7", u"E3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(index);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(0x7FFD);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Belirli Bir Öğeyi Gösterme

`CurrentPageItem` öğesini gerçek bir indekse ayarlamak yalnızca o sayfa öğesini seçer. İndeks, filtre alanının sıralanmış öğe listesindeki öğenin konumudur, dolayısıyla örneğin `1` sıralamadan sonra ikinci öğeyi seçer.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    cells.Get(u"A1").PutValue(U16String("Fruit"));
    cells.Get(u"B1").PutValue(U16String("Year"));
    cells.Get(u"C1").PutValue(U16String("Amount"));

    cells.Get(u"A2").PutValue(U16String("Apple"));
    cells.Get(u"B2").PutValue(U16String("2020"));
    cells.Get(u"C2").PutValue(U16String("100"));

    cells.Get(u"A3").PutValue(U16String("Apple"));
    cells.Get(u"B3").PutValue(U16String("2021"));
    cells.Get(u"C3").PutValue(U16String("150"));

    cells.Get(u"A4").PutValue(U16String("Banana"));
    cells.Get(u"B4").PutValue(U16String("2020"));
    cells.Get(u"C4").PutValue(U16String("200"));

    cells.Get(u"A5").PutValue(U16String("Banana"));
    cells.Get(u"B5").PutValue(U16String("2021"));
    cells.Get(u"C5").PutValue(U16String("250"));

    PivotTableCollection pivotTables = sheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(U16String("A1:C5"), U16String("E3"), U16String("PivotTable1"));
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String("Fruit"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String("Amount"));
    pivotTable.AddFieldToArea(PivotFieldType::Page, U16String("Year"));

    pivotTable.GetPageFields().Get(0).SetCurrentPageItem(1);

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Çoklu Seçim Filtreleme**

Çoklu seçim filtreleme, sayfa açılır menüsünü bir onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birkaç sayfa öğesi seçmesine olanak tanır. Aspose.Cells birlikte çalışan iki özellik sunar. Çoklu seçim kullanıcı arayüzünün geçerli olabilmesi için `PivotField.IsMultipleItemSelectionAllowed` öğesinin `true` olarak ayarlanması gerekir. Etkinleştirildikten sonra, `PivotItem.IsHidden` onay kutusu listesinde hangi öğelerin görüneceğini kontrol eder; böylece her öğeyi gösterebilir veya yalnızca belirli öğeleri beyaz listeye alabilirsiniz.

Aşağıdaki kod, Senaryo 1a'da oluşturulan aynı Year filtre alanında çoklu seçimi etkinleştirir ve ardından iki desen gösterir: A Bölümü, her giriş için `IsHidden` öğesini `false` olarak bırakarak her sayfa öğesini ortaya çıkarırken, B Bölümü yalnızca seçtiğiniz kaynak değerlerini beyaz listeye alır ve bir `switch (pivotItems[i].GetStringValue())` bloğu aracılığıyla diğer her şeyi gizler.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <vector>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet sheet = workbook.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Örnek veri: Meyve | Yıl | Miktar
    cells.Get(0, 0).PutValue(u"Fruit");
    cells.Get(0, 1).PutValue(u"Year");
    cells.Get(0, 2).PutValue(u"Amount");

    std::vector<std::vector<std::string>> data = {
        {"apple",  "2019", "100"},
        {"apple",  "2020", "150"},
        {"apple",  "2021", "200"},
        {"banana", "2019", "110"},
        {"banana", "2020", "160"},
        {"banana", "2021", "210"},
        {"grape",  "2019", "120"},
        {"grape",  "2020", "170"},
        {"grape",  "2021", "220"}
    };

    for (int i = 0; i < (int)data.size(); i++) {
        cells.Get(i + 1, 0).PutValue(U16String(data[i][0].c_str()));
        cells.Get(i + 1, 1).PutValue(std::stoi(data[i][1]));
        cells.Get(i + 1, 2).PutValue(std::stoi(data[i][2]));
    }

    Worksheet pivotSheet = workbook.GetWorksheets().Add(u"Pivot");
    PivotTableCollection pivots = pivotSheet.GetPivotTables();
    int pivotIndex = pivots.Add(u"E3", u"A1:C10", u"PivotTable1");
    PivotTable pivotTable = pivots.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Fruit");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");
    pivotTable.AddFieldToArea(PivotFieldType::Page, u"Year");

    // — Sayfa alanında çoklu seçimi etkinleştir
    pivotTable.GetPageFields().Get(0).SetIsMultipleItemSelectionAllowed(true);

    // Bölüm A — TÜM öğeleri seç (her öğeyi görünür yap)
    PivotItemCollection pivotItems = pivotTable.GetPageFields().Get(0).GetPivotItems();
    int itemCount = pivotItems.GetCount();
    for (int i = 0; i < itemCount; i++) {
        pivotItems.Get(i).SetIsHidden(false);
    }

    // Bölüm B — Yalnızca kaynak değerine göre belirli öğeleri seç
    for (int i = 0; i < itemCount; i++) {
        U16String val = pivotItems.Get(i).GetStringValue();
        std::string s = val.ToUtf8();
        if (s == "2020" || s == "grape" || s == "blueberry") {
            pivotItems.Get(i).SetIsHidden(false);
        } else {
            pivotItems.Get(i).SetIsHidden(true);
        }
    }

    pivotTable.RefreshData();
    pivotTable.CalculateData();

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

> **Not:** `PivotItem.IsHidden` aracılığıyla çoklu seçim filtreleme kullanırken **en az bir `PivotItem` görünür kalmalıdır** (`IsHidden == false`). Her öğe gizlenmişse Excel dosyayı açarken ya çöker ya da boş bir pivot oluşturur. Çoklu seçim beyaz listenizin kaynak verilerinizden en az bir öğe içerdiğini her zaman doğrulayın.

## **Hangi API'yi ve Hangi Modu Kullanmalıyım?**

Aşağıdaki tablo, her senaryoyu ayrıntılı olarak okumadan doğru kombinasyonu seçebilmeniz için her API'nin ve modun ne zaman kullanılacağını özetler.

| Senaryo / Kullanım Durumu | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| filtre alanını kaynak sütun adına göre ekleme (en yaygın) | `PivotTable.AddFieldToArea(PivotFieldType.Page, "fieldName")` | yok | Üst düzey, tek satır. Bir `PivotField` referansına ihtiyacınız olmadıkça bunu kullanın. |
| Zaten bir `PivotField` nesneniz varken filtre alanı ekleme | `PivotTable.PageFields.Add(PivotField)` | yok | Alan nesnesi başka bir yerden alındığında veya yeniden kullanılması gerektiğinde kullanın. |
| Tek bir sayfa öğesine filtreleme (varsayılan mod) | `PivotField.CurrentPageItem` | belirli bir indekse ayarlayın | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreni temizleme | `PivotField.CurrentPageItem` | `0x7FFD` olarak ayarlayın | Sihirli değer `0x7FFD` (ondalık 32765) "tüm öğeler" için sentinel değerdir. |
| Excel'de çoklu seçim kullanıcı arayüzünü etkinleştirme | `PivotField.IsMultipleItemSelectionAllowed` | `true` olarak ayarlayın | Herhangi bir `IsHidden` çağrısının geçerli olabilmesi için gereklidir. |
| Çoklu seçim listesinde tek tek öğeleri gizleme / gösterme | `PivotItem.IsHidden` | öğe başına ayarlayın | En az bir öğe görünür kalmalıdır (`IsHidden == false`). |

{{% alert color="primary" %}}
Çoklu seçim filtrelemeyi yapılandırırken görünürlük kısıtını her zaman hatırlayın. Çoklu seçim filtre alanındaki her `PivotItem` gizlenmişse Excel açılırken çöker veya boş bir pivot oluşturur. Beyaz listenizi kaynak verilerinize göre oluşturun, böylece en az bir öğe görünür kalsın ve kaydedilen çalışma kitaplarınız her makinede güvenilir şekilde açılsın.
{{% /alert %}}



{{< app/cells/assistant language="cpp" >}}