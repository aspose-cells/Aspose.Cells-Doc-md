---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for C++ kullanarak bir Pivot Tablosundaki sayfa alanı bölgesi düzenini, Pivot Tablosunun üst kısmındaki sayfa alanlarının görüntüleme sırası, sarma sayısı ve alan sırası dahil olmak üzere nasıl kontrol edeceğinizi öğrenin.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, Pivot Tablosu, sayfa alanı, sayfa alanı sırası, sayfa alanı sarma sayısı, sayfa alanı taşıma
type: docs
weight: 191
url: /tr/cpp/change-page-field-layout/
---

For the table headers, I'll go with my decision to translate them:
| Meyve  | Yıl | Bölge | Tutar |
|--------|-----|-------|-------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |

Looking at the original markdown:
## **Example 1: Over Then Down**

"Down Then Over" means "down first, then over" - vertically first, then wrap to the right. In Turkish: "Dikey Sonra Yatay" or "Önce Aşağı Sonra Yan Yana".

For other headings:

One thing I want to double-check - the headings in the source. They are:
- ## **Introduction**
- ## **Source Data**
- ## **Example 1: Over Then Down**
- ## **Example 2: Down Then Over**
- ## **Example 3: Move a Page Field**
- ## **Related Articles**

- ## **Giriş**
- ## **Kaynak Veri**
- ## **Örnek 1: Önce Yatay Sonra Dikey**
- ## **Örnek 2: Önce Dikey Sonra Yatay**
- ## **Örnek 3: Sayfa Alanını Taşıma**
- ## **İlgili Makaleler**

| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
...

The pipe separators are there, and the data has specific spacing. I'll preserve the exact same structure but with Turkish headers and English values.

- Table: Meyve, Yıl, Bölge, Tutar | Elma, 2022, Kuzey, 150
- Code: would put "Apple", 2022, "North", 150 into cells

This is awkward but it follows the rules.

Alternatively, I could keep the data table in English entirely. The argument is that the data is sample data and the column headers are technically also data values (they go into row 0 of the cells).

- Headers (Fruit, Year, Region, Amount) should be translated since they're labels
- Data values (Apple, Banana, North, South, etc.) should stay in English since they're data that matches code

But the data values are inconsistent with the code... 

- Translated documentation explaining how to use pivot tables
- Code (in English) that demonstrates the example
- Table (in Turkish) showing the data structure

Final table:
| Meyve  | Yıl  | Bölge  | Tutar |
|--------|------|--------|-------|
| Elma   | 2022 | Kuzey  | 150   |
| Elma   | 2023 | Kuzey  | 180   |
| Muz    | 2022 | Güney  | 120   |
| Muz    | 2023 | Güney  | 140   |
| Kiraz  | 2022 | Doğu   | 200   |
| Kiraz  | 2023 | Doğu   | 220   |
| Üzüm   | 2022 | Batı   | 90    |
| Üzüm   | 2023 | Batı   | 110   |

But the rule says translate everything. 

Final answer: Translate everything in the table.

- "page fields" - "sayfa alanları"  
- "filter controls" - "filtre kontrolleri"
- "data body" - "veri gövdesi"
- "row axis" - "satır ekseni"
- "column axis" - "sütun ekseni"
- "page axis" - "sayfa ekseni"
- "data field" - "veri alanı"
- "row field" - "satır alanı"
- "wrap count" - "sarma sayısı"
- "field reordering" - "alan yeniden sıralaması"
- "side-by-side" - "yan yana"
- "stacked vertically" - "dikey olarak dizilmiş"
- "horizontal" - "yatay"
- "vertical" - "dikey"
- "dataset" - "veri kümesi"
- "side-by-side comparison" - "yan yana karşılaştırma"
- "shared dataset" - "ortak veri kümesi"

{{% alert color="primary" %}}

Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Pivot Tablosunun üst kısmındaki filtre kontrolleri şeridi olan sayfa alanı bölgesinin düzenini — görüntüleme sırası, sarma sayısı ve alan yeniden sıralaması dahil — kontrol etme yöntemlerini göstermektedir.

{{% /alert %}}

## **Giriş**

Microsoft Excel'deki bir Pivot Tablosu, tablonun satır/sütun/veri gövdesinin üzerinde konumlanan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, açılır filtre kontrollerinden oluşan bir şerit (her sayfa alanı için bir tane) olarak işlenir ve son kullanıcıların Pivot Tablosunu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells for C++, bu bölgeyi `PivotTable.PageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl yerleştirileceğini kontrol eden üç özellik sunar:

- `PivotTable.PageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut olanların *yanına mı* yoksa *altına mı* yerleştirileceğine karar verir.
- `PivotTable.PageFieldWrapCount`, sarma işleminden önce satır veya sütun başına kaç sayfa alanı yerleştirileceğini ayarlar.
- `PivotTable.PageFields.Move(currIndex, destIndex)`, sipariş modunu değiştirmeden sayfa alanlarını yeniden sıralar.

Bu makale, her bir işlemi ortak bir veri kümesi üzerinde gösteren üç kod örneğini adım adım açıklar; böylece elde edilen düzenleri yan yana karşılaştırabilirsiniz.

## **Kaynak Veri**

Aşağıdaki üç örnek de bu sekiz satırlık satış verisini `PivotData` adlı bir çalışma sayfasına yükler. Veriler, iki sayfa alanı adayı (`Year`, `Region`), bir satır alanı adayı (`Fruit`) ve bir ölçü (`Amount`) içerir; bu da sayfa alanı şeridinin incelenmesini anlamlı kılar.

| Meyve | Yıl  | Bölge  | Tutar |
|-------|------|--------|-------|
| Elma  | 2022 | Kuzey  | 150   |
| Elma  | 2023 | Kuzey  | 180   |
| Muz   | 2022 | Güney  | 120   |
| Muz   | 2023 | Güney  | 140   |
| Kiraz | 2022 | Doğu   | 200   |
| Kiraz | 2023 | Doğu   | 220   |
| Üzüm  | 2022 | Batı   | 90    |
| Üzüm  | 2023 | Batı   | 110   |

Tüm sekiz satır, her kod örneğinde aynı sırada doldurulur; dolayısıyla senaryolar arasında kaynak veri hiçbir zaman farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklıdır.

## **Örnek 1: Önce Yatay Sonra Dikey**

İlk senaryoda, iki sayfa alanını (`Year`, `Region`) Pivot Tablosunun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Fruit` öğesini satır eksenine atıyoruz, `Year` öğesini sayfa ekseninde birinci, `Region` öğesini ikinci sıraya yerleştiriyoruz (`AddFieldToArea` çağrılarının sırası başlangıç indisini belirler), `Amount` (Sum) öğesini veri alanı olarak ekliyoruz ve ardından `PageFieldOrder` öğesini `PrintOrderType.OverThenDown` ve `PageFieldWrapCount` öğesini `2` olarak ayarlıyoruz. `OverThenDown` ve sarma sayısı 2 ile, iki sayfa alanı Pivot Tablosunun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir; dolayısıyla şerit bir satır ve iki sütun genişliğinde yer kaplar.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "output";
    if (!std::filesystem::exists(dataDir)) {
        std::filesystem::create_directories(dataDir);
    }

    Workbook workbook;
    WorksheetCollection worksheets = workbook.GetWorksheets();

    Worksheet pivotDataSheet = worksheets.Add(u"PivotData");
    Cells pivotDataCells = pivotDataSheet.GetCells();

    // Başlıklar (satır 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");

    // Satır 1: Elma, 2022, Kuzey, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);

    // Satır 2: Elma, 2023, Kuzey, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);

    // Satır 3: Muz, 2022, Güney, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);

    // Satır 4: Muz, 2023, Güney, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);

    // Satır 5: Kiraz, 2022, Doğu, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);

    // Satır 6: Kiraz, 2023, Doğu, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);

    // Satır 7: Üzüm, 2022, Batı, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);

    // Satır 8: Üzüm, 2023, Batı, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);

    // PivotTableReport sayfası ekle
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();

    // PivotData!A1:D9'dan alınan ve PivotTableReport üzerinde A1'e yerleştirilen pivot tablo oluştur
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    // Alanları ekle
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Meyve
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Yıl
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Bölge
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Tutar
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);

    // Sayfa alanı düzenini yapılandır: sayfa alanlarını önce yatay olarak yerleştir, her 2 alandan sonra kaydır
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    // Yenile ve hesapla
    pivotTable.CalculateData();

    // Kaydet
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Örnek 2: Önce Dikey Sonra Yatay**

Bu örnekte, Örnek 1'deki gibi `Fruit` öğesini satır eksenine, `Year` ve `Region` öğelerini sayfa eksenine (`Year` birinci olacak şekilde) ve `Amount` (Sum) öğesini veri alanı olarak yerleştiriyoruz. Ardından `PageFieldOrder` öğesini `PrintOrderType.DownThenOver` ve `PageFieldWrapCount` öğesini `2` olarak ayarlıyoruz. `DownThenOver` ve sarma sayısı 2 ile, iki sayfa alanı dikey olarak dizilir — `Year` üstte, `Region` doğrudan altta — ve Pivot Tablosunun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine, bir sütun ve iki satır genişliğinde yer kaplar.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet pivotData = workbook.GetWorksheets().Get(0);
    pivotData.SetName(u"PivotData");
    Worksheet pivotReport = workbook.GetWorksheets().Add(u"PivotTableReport");

    const char* headers[] = { "Fruit", "Year", "Region", "Amount" };
    for (int c = 0; c < 4; c++)
    {
        pivotData.GetCells().Get(0, c).PutValue(U16String(headers[c]));
    }

    struct DataRow {
        U16String fruit;
        int year;
        U16String region;
        int amount;
    };

    DataRow data[] = {
        {U16String("Apple"),  2022, U16String("North"), 150},
        {U16String("Apple"),  2023, U16String("North"), 180},
        {U16String("Banana"), 2022, U16String("South"), 120},
        {U16String("Banana"), 2023, U16String("South"), 140},
        {U16String("Cherry"), 2022, U16String("East"),  200},
        {U16String("Cherry"), 2023, U16String("East"),  220},
        {U16String("Grape"),  2022, U16String("West"),  90},
        {U16String("Grape"),  2023, U16String("West"),  110}
    };

    for (int r = 0; r < 8; r++)
    {
        pivotData.GetCells().Get(r + 1, 0).PutValue(data[r].fruit);
        pivotData.GetCells().Get(r + 1, 1).PutValue(data[r].year);
        pivotData.GetCells().Get(r + 1, 2).PutValue(data[r].region);
        pivotData.GetCells().Get(r + 1, 3).PutValue(data[r].amount);
    }

    int idx = pivotReport.GetPivotTables().Add(u"PivotData!A1:D9", u"A1", u"PivotTable");
    PivotTable pivotTable = pivotReport.GetPivotTables().Get(idx);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::DownThenOver);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.CalculateData();

    workbook.Save(u"pageFieldLayout_downThenOver.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Örnek 3: Sayfa Alanını Taşıma**

Üçüncü senaryoda bu veri kümesini ve alan atamasını koruyoruz, nötr bir düzen ayarlıyoruz (`OverThenDown` ve sarma sayısı `2`) ve ardından `PageFields.Move` işlemini gösteriyoruz. `Move(0, 1)` çağrısı, 0 indisindeki sayfa alanını (`Year`) 1 konumuna taşır ve 1 konumundaki sayfa alanı (`Region`) 0 konumuna kayar. Bu çağrıdan sonra `Region` birinci sayfa alanı, `Year` ise ikinci sayfa alanı olur. Sarma ve sıralama modu değişmediğinden, şerit hâlâ yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiştir.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;

    Worksheet dataSheet = wb.GetWorksheets().Get(0);
    dataSheet.SetName(u"PivotData");

    Cells dataCells = dataSheet.GetCells();

    dataCells.Get(u"A1").PutValue(u"Fruit");
    dataCells.Get(u"B1").PutValue(u"Year");
    dataCells.Get(u"C1").PutValue(u"Region");
    dataCells.Get(u"D1").PutValue(u"Amount");

    dataCells.Get(u"A2").PutValue(u"Apple");
    dataCells.Get(u"B2").PutValue(2022);
    dataCells.Get(u"C2").PutValue(u"North");
    dataCells.Get(u"D2").PutValue(150);

    dataCells.Get(u"A3").PutValue(u"Apple");
    dataCells.Get(u"B3").PutValue(2023);
    dataCells.Get(u"C3").PutValue(u"North");
    dataCells.Get(u"D3").PutValue(180);

    dataCells.Get(u"A4").PutValue(u"Banana");
    dataCells.Get(u"B4").PutValue(2022);
    dataCells.Get(u"C4").PutValue(u"South");
    dataCells.Get(u"D4").PutValue(120);

    dataCells.Get(u"A5").PutValue(u"Banana");
    dataCells.Get(u"B5").PutValue(2023);
    dataCells.Get(u"C5").PutValue(u"South");
    dataCells.Get(u"D5").PutValue(140);

    dataCells.Get(u"A6").PutValue(u"Cherry");
    dataCells.Get(u"B6").PutValue(2022);
    dataCells.Get(u"C6").PutValue(u"East");
    dataCells.Get(u"D6").PutValue(200);

    dataCells.Get(u"A7").PutValue(u"Cherry");
    dataCells.Get(u"B7").PutValue(2023);
    dataCells.Get(u"C7").PutValue(u"East");
    dataCells.Get(u"D7").PutValue(220);

    dataCells.Get(u"A8").PutValue(u"Grape");
    dataCells.Get(u"B8").PutValue(2022);
    dataCells.Get(u"C8").PutValue(u"West");
    dataCells.Get(u"D8").PutValue(90);

    dataCells.Get(u"A9").PutValue(u"Grape");
    dataCells.Get(u"B9").PutValue(2023);
    dataCells.Get(u"C9").PutValue(u"West");
    dataCells.Get(u"D9").PutValue(110);

    Worksheet pivotSheet = wb.GetWorksheets().Add(u"PivotTableReport");

    int32_t pivotIndex = pivotSheet.GetPivotTables().Add(u"PivotData!A1:D9", u"A3", u"PivotTable");
    PivotTable pivotTable = pivotSheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);

    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);

    pivotTable.GetPageFields().Move(0, 1);

    pivotTable.CalculateData();

    wb.Save(u"pageFieldLayout_move.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **İlgili Makaleler**

- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/cpp/add-page-field-in-pivot-table/) — sayfa alanlarının bir Pivot Tablosuna nasıl eklendiğini tanıtan üst sayfa.
- [Pivot Tablosundaki Satır ve Sütun Alanları](/cells/tr/cpp/row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan, alanların satır ve sütun eksenlerine atanmasını ele alır.
- [Pivot Tablosundaki Değer Alanlarını Yönetme](/cells/tr/cpp/manage-value-fields/) — bu makalede kullanılan `Sum` toplama dahil olmak üzere veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/cpp/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `RefreshData` ve `CalculateData` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra işlenmiş Pivot Tablosunun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="" >}}