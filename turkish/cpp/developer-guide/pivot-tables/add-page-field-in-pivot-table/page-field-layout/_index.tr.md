---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for C++ kullanarak bir pivot tabloda sayfa alanı düzenini nasıl kontrol edeceğinizi öğrenin; görüntüleme sırasını, kaydırma sayısını ve sayfa alanlarının pivot tablonun üst kısmındaki sırasını ayarlama dahil.
keywords: Aspose.Cells, C++ kütüphanesi, elektronik tablo, pivot tablosu, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/cpp/change-page-field-layout/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Pivot tablonun üst kısmındaki filtre kontrolleri şeridi olan sayfa alanı düzeninin nasıl kontrol edileceğini gösterir; görüntüleme sırası, kaydırma sayısı ve alan yeniden sıralaması dahil.
{{% /alert %}}

## **Introduction**
Microsoft Excel'deki bir pivot tablo, tablonun satır/sütun/veri gövdesinin üzerinde yer alan özel bir **sayfa alanı** sunar. Bu alan, açılır filtre kontrollerinden oluşan bir şerit olarak (her sayfa alanı için bir tane) işlenir ve son kullanıcıların pivot tabloyu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells for C++, bu alanı `PivotTable.PageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl düzenleneceğini kontrol eden üç özellik sunar:
- `PivotTable.PageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut olanların *yanına* mı yoksa *altına* mı yerleştirileceğine karar verir.
- `PivotTable.PageFieldWrapCount`, kaydırmadan önce satır veya sütun başına kaç sayfa alanı yerleştirileceğini ayarlar.
- `PivotTable.PageFields.Move(currIndex, destIndex)`, sıra modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, ortak bir veri kümesi üzerinde bu işlemlerin her birini gösteren üç kod örneğini adım adım anlatır; böylece elde edilen düzenleri yan yana karşılaştırabilirsiniz.

## **Source Data**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Her kod örneğinde aynı sırada olmak üzere sekiz satırın tamamı doldurulur; dolayısıyla kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklılık gösterir.

## **Example 1: Over Then Down**
İlk senaryoda, iki sayfa alanını (`Year`, `Region`) pivot tablonun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Fruit` alanını satır eksenine atar, `Year` alanını birinci ve `Region` alanını ikinci olarak sayfa eksenine yerleştiririz (`AddFieldToArea` çağrılarının sırası başlangıç indisini belirler), `Amount` (Sum) alanını veri alanı olarak ekler ve ardından `PageFieldOrder` değerini `PrintOrderType.OverThenDown`, `PageFieldWrapCount` değerini `2` olarak ayarlarız. `OverThenDown` ve kaydırma sayısı 2 ile, iki sayfa alanı pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana düzenlenir; dolayısıyla şerit iki genişliğinde bir satır kaplar.

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
    // Headers (row 0)
    pivotDataCells.Get(0, 0).PutValue(u"Fruit");
    pivotDataCells.Get(0, 1).PutValue(u"Year");
    pivotDataCells.Get(0, 2).PutValue(u"Region");
    pivotDataCells.Get(0, 3).PutValue(u"Amount");
    // Row 1: Apple, 2022, North, 150
    pivotDataCells.Get(1, 0).PutValue(u"Apple");
    pivotDataCells.Get(1, 1).PutValue(2022);
    pivotDataCells.Get(1, 2).PutValue(u"North");
    pivotDataCells.Get(1, 3).PutValue(150);
    // Row 2: Apple, 2023, North, 180
    pivotDataCells.Get(2, 0).PutValue(u"Apple");
    pivotDataCells.Get(2, 1).PutValue(2023);
    pivotDataCells.Get(2, 2).PutValue(u"North");
    pivotDataCells.Get(2, 3).PutValue(180);
    // Row 3: Banana, 2022, South, 120
    pivotDataCells.Get(3, 0).PutValue(u"Banana");
    pivotDataCells.Get(3, 1).PutValue(2022);
    pivotDataCells.Get(3, 2).PutValue(u"South");
    pivotDataCells.Get(3, 3).PutValue(120);
    // Row 4: Banana, 2023, South, 140
    pivotDataCells.Get(4, 0).PutValue(u"Banana");
    pivotDataCells.Get(4, 1).PutValue(2023);
    pivotDataCells.Get(4, 2).PutValue(u"South");
    pivotDataCells.Get(4, 3).PutValue(140);
    // Row 5: Cherry, 2022, East, 200
    pivotDataCells.Get(5, 0).PutValue(u"Cherry");
    pivotDataCells.Get(5, 1).PutValue(2022);
    pivotDataCells.Get(5, 2).PutValue(u"East");
    pivotDataCells.Get(5, 3).PutValue(200);
    // Row 6: Cherry, 2023, East, 220
    pivotDataCells.Get(6, 0).PutValue(u"Cherry");
    pivotDataCells.Get(6, 1).PutValue(2023);
    pivotDataCells.Get(6, 2).PutValue(u"East");
    pivotDataCells.Get(6, 3).PutValue(220);
    // Row 7: Grape, 2022, West, 90
    pivotDataCells.Get(7, 0).PutValue(u"Grape");
    pivotDataCells.Get(7, 1).PutValue(2022);
    pivotDataCells.Get(7, 2).PutValue(u"West");
    pivotDataCells.Get(7, 3).PutValue(90);
    // Row 8: Grape, 2023, West, 110
    pivotDataCells.Get(8, 0).PutValue(u"Grape");
    pivotDataCells.Get(8, 1).PutValue(2023);
    pivotDataCells.Get(8, 2).PutValue(u"West");
    pivotDataCells.Get(8, 3).PutValue(110);
    // Add PivotTableReport sheet
    Worksheet pivotTableSheet = worksheets.Add(u"PivotTableReport");
    PivotTableCollection pivotTables = pivotTableSheet.GetPivotTables();
    // Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
    int pivotIndex = pivotTables.Add(u"PivotData!A1:D9", u"A1", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);
    // Add fields
    pivotTable.AddFieldToArea(PivotFieldType::Row, 0);   // Fruit
    pivotTable.AddFieldToArea(PivotFieldType::Page, 1);  // Year
    pivotTable.AddFieldToArea(PivotFieldType::Page, 2);  // Region
    pivotTable.AddFieldToArea(PivotFieldType::Data, 3);  // Amount
    pivotTable.GetDataFields().Get(0).SetFunction(ConsolidationFunction::Sum);
    // Configure page field area layout: place page fields across first, wrap after every 2
    pivotTable.SetPageFieldOrder(PrintOrderType::OverThenDown);
    pivotTable.SetPageFieldWrapCount(2);
    // Refresh and calculate
    pivotTable.CalculateData();
    // Save
    std::string filePath = dataDir + "/pageFieldLayout_overThenDown.xlsx";
    workbook.Save(U16String(filePath.c_str()));
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Example 2: Down Then Over**
Bu örnekte, Örnek 1'deki gibi tam olarak `Fruit` alanını satır eksenine, `Year` ve `Region` alanlarını sayfa eksenine (`Year` birinci olacak şekilde) ve `Amount` (Sum) alanını veri alanı olarak yerleştiririz. Ardından `PageFieldOrder` değerini `PrintOrderType.DownThenOver`, `PageFieldWrapCount` değerini `2` olarak ayarlarız. `DownThenOver` ve kaydırma sayısı 2 ile, iki sayfa alanı dikey olarak istiflenir — üstte `Year`, doğrudan altında `Region` — pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine, bir genişliğinde iki satır kaplar.

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

## **Example 3: Move a Page Field**
Üçüncü senaryoda, bu veri kümesini ve alan atamasını korur, nötr bir düzen ayarlarız (`OverThenDown` ile kaydırma sayısı `2`) ve ardından `PageFields.Move` işlemini gösteririz. `Move(0, 1)` çağrısı, 0 konumundaki sayfa alanını (`Year`) 1 konumuna taşır ve 1 konumunda bulunan sayfa alanı (`Region`) 0 konumuna kayar. Bu çağrıdan sonra, `Region` birinci sayfa alanı, `Year` ise ikinci sayfa alanı olur. Kaydırma ve sıra modu değişmediğinden, şerit hâlâ yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiştir.

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

## **Related Articles**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/cpp/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan üst sayfa.
- [Pivot Tablosunda Satır ve Sütun Alanları](/cells/tr/cpp/row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan şekilde, alanların satır ve sütun eksenlerine atanmasını ele alır.
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/cpp/manage-value-fields/) — bu makalede kullanılan `Sum` toplama işlemi dahil, veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/cpp/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `RefreshData` ve `CalculateData` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/) — sayfa alanı şeridi düzenlendikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="" >}}