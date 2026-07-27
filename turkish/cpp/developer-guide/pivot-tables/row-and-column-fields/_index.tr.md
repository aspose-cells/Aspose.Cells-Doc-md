---
title: Aspose.Cells for .NET'te PivotTable'a satır ve sütun alanları ekleme
linktitle: Satır ve Sütun Alanları
description: Aspose.Cells for C++'da bir özet tablonun satır ve sütun bölgelerine temel alanlar eklemeyi ve PivotField.SetSubtotals kullanarak özet tablo alanı ara toplamlarını kontrol etmeyi öğrenin.
keywords: Aspose.Cells, C++, özet tablo, satır alanı, sütun alanı, PivotField, SetSubtotals, PivotFieldSubtotalType, ara toplamlar
type: docs
weight: 220
url: /tr/cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Satır veya Sütun Bölgesine Alan Ekleme**

`PivotTable.AddFieldToArea(PivotFieldType fieldType, intrusive_ptr<Aspose::Cells::Systems::String> fieldName)` yöntemi, kaynak verilerdeki bir temel alanı dört özet tablo bölgesinden birine taşır. `fieldType` argümanı aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.

- `Row` — dikey olarak solda yer alan alanlar
- `Column` — yatay olarak üstte yer alan alanlar
- `Data` — değerlerinin toplandığı alanlar
- `Page` — rapor filtreleri olarak kullanılan alanlar

Alanlar eklendikten sonra, `PivotTable.RowFields` ve `PivotTable.ColumnFields` özellikleri aracılığıyla bunlara erişebilirsiniz. Her özellik bir `PivotFieldCollection` döndürür. `RowFields` öğesinin 0 dizinindeki alan en dış satır alanıdır ve sonraki dizinler onun içinde iç içe geçmiş alanları temsil eder. Aynı indeksleme kuralı `ColumnFields` için de geçerlidir.

Alan iç içe geçme sırası önemlidir. Önce `Category` alanını satır bölgesine, ardından `Item` alanını eklemek, dış gruplaması `Category` ve iç gruplaması `Item` olan bir özet tablo üretir. Sıranın tersine çevrilmesi hiyerarşiyi de tersine çevirir.

## **Özet Tablo Alanı Ara Toplamları**

`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` yöntemi, bir özet tablo alanı için hangi ara toplam satırlarının görüneceğini kontrol eder. Her çağrı tek bir ara toplam türünü bağımsız olarak değiştirir. `shown = true` geçilmesi ara toplamı görüntülerken, `shown = false` geçilmesi onu gizler. Her çağrı yalnızca bir türü etkilediğinden, yöntemin farklı `subtotalType` değerleriyle birden çok kez çağrılması özel bir ara toplam alt kümesi oluşturur.

`PivotFieldSubtotalType` numaralandırması, kullanılabilir ara toplam türlerini tanımlar.

- `Automatic` — Aspose.Cells varsayılan seçimi seçer (genellikle sayısal alanlar için `Sum`)
- `None` — tüm ara toplam satırlarını bastırır
- `Sum`
- `Count`
- `Average`
- `Max`
- `Min`
- `Product`
- `StdDev`
- `StdDevp`
- `Var`
- `Varp`

{{% alert color="primary" %}}
Ara toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla özet tablo alanı olduğunda görüntülenir. Tek bir alanın ara toplam oluşturacak anlamlı bir şeyi yoktur, dolayısıyla bu durumda `SetSubtotals` çağrılarının görünür bir etkisi olmaz. Bu nedenle bu makale, her örnekte iki satır alanı (`Category` dış, `Item` iç) yerleştirir; böylece her `Category` grubu arasındaki ara toplam sınırı görünür olur.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Ara Toplamlar**

`SetSubtotals` yöntemini hiç çağırmadığınızda, Aspose.Cells sayısal alanlar için `Automatic` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanında `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` çağırarak bu davranışı açıkça doğrular.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(0, 0).PutValue(u"Category");
    worksheet.GetCells().Get(0, 1).PutValue(u"Item");
    worksheet.GetCells().Get(0, 2).PutValue(u"Year");
    worksheet.GetCells().Get(0, 3).PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Automatic, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_automatic.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Senaryo 2 — Tüm Ara Toplamların Bastırılması (None)**

`SetSubtotals(PivotFieldSubtotalType.None, true)` çağrılması, özet tablosundaki tüm ara toplam satırlarını kaldırarak yalnızca alan satırlarını ve alttaki genel toplamı bırakır. Bu, özet satırları olmadan ham gruplanmış verileri istediğinizde kullanışlıdır.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    sheet.SetName(u"Data");

    U16String headers[] = { u"Category", u"Item", u"Year", u"Amount" };
    for (int j = 0; j < 4; j++) {
        sheet.GetCells().Get(0, j).PutValue(headers[j]);
    }

    U16String categories[] = { u"Fruit", u"Fruit", u"Fruit", u"Fruit",
                               u"Vegetable", u"Vegetable", u"Vegetable", u"Vegetable" };
    U16String items[] = { u"Apple", u"Apple", u"Banana", u"Banana",
                          u"Carrot", u"Carrot", u"Daikon", u"Daikon" };
    int years[]   = { 2020, 2021, 2020, 2021, 2020, 2021, 2020, 2021 };
    int amounts[] = {  100,  150,   80,   90,   50,   60,   40,   45 };

    for (int i = 0; i < 8; i++) {
        sheet.GetCells().Get(i + 1, 0).PutValue(categories[i]);
        sheet.GetCells().Get(i + 1, 1).PutValue(items[i]);
        sheet.GetCells().Get(i + 1, 2).PutValue(years[i]);
        sheet.GetCells().Get(i + 1, 3).PutValue(amounts[i]);
    }

    int pivotIndex = sheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = sheet.GetPivotTables().Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::None, true);
    pivotTable.CalculateData();

    wb.Save(u"output_none.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Senaryo 3 — Özel Ara Toplam Alt Kümesi (Sum + Average)**

Tek bir ara toplam türüyle sınırlı değilsiniz. Her `SetSubtotals` çağrısı bir tür üzerinde bağımsız olarak çalışır; dolayısıyla yöntemin bir kez `Sum` ve bir kez `Average` ile iki kez çağrılması, her `Category` grubu için iki ara toplam satırından oluşan özel bir alt küme üretir.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    worksheet.SetName(u"Data");

    worksheet.GetCells().Get(u"A1").PutValue(u"Category");
    worksheet.GetCells().Get(u"B1").PutValue(u"Item");
    worksheet.GetCells().Get(u"C1").PutValue(u"Year");
    worksheet.GetCells().Get(u"D1").PutValue(u"Amount");

    worksheet.GetCells().Get(1, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(1, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(1, 2).PutValue(2020);
    worksheet.GetCells().Get(1, 3).PutValue(100);

    worksheet.GetCells().Get(2, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(2, 1).PutValue(u"Apple");
    worksheet.GetCells().Get(2, 2).PutValue(2021);
    worksheet.GetCells().Get(2, 3).PutValue(150);

    worksheet.GetCells().Get(3, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(3, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(3, 2).PutValue(2020);
    worksheet.GetCells().Get(3, 3).PutValue(80);

    worksheet.GetCells().Get(4, 0).PutValue(u"Fruit");
    worksheet.GetCells().Get(4, 1).PutValue(u"Banana");
    worksheet.GetCells().Get(4, 2).PutValue(2021);
    worksheet.GetCells().Get(4, 3).PutValue(90);

    worksheet.GetCells().Get(5, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(5, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(5, 2).PutValue(2020);
    worksheet.GetCells().Get(5, 3).PutValue(50);

    worksheet.GetCells().Get(6, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(6, 1).PutValue(u"Carrot");
    worksheet.GetCells().Get(6, 2).PutValue(2021);
    worksheet.GetCells().Get(6, 3).PutValue(60);

    worksheet.GetCells().Get(7, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(7, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(7, 2).PutValue(2020);
    worksheet.GetCells().Get(7, 3).PutValue(40);

    worksheet.GetCells().Get(8, 0).PutValue(u"Vegetable");
    worksheet.GetCells().Get(8, 1).PutValue(u"Daikon");
    worksheet.GetCells().Get(8, 2).PutValue(2021);
    worksheet.GetCells().Get(8, 3).PutValue(45);

    PivotTableCollection pivotTables = worksheet.GetPivotTables();
    int pivotIndex = pivotTables.Add(u"A1:D9", u"F3", u"PivotTable1");
    PivotTable pivotTable = pivotTables.Get(pivotIndex);

    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

    PivotField categoryField = pivotTable.GetRowFields().Get(0);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Sum, true);
    categoryField.SetSubtotals(PivotFieldSubtotalType::Average, true);

    pivotTable.CalculateData();

    workbook.Save(u"output_custom.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Özet**

Yukarıdaki üç senaryo aynı veri kümesini ve özet tablo yapısını paylaşır. Aralarındaki tek fark, dış `Category` satır alanına uygulanan `SetSubtotals` çağrısıdır. İki alan kuralını unutmayın: bir bölgedeki tek bir alanın ara toplam oluşturacak bir şeyi yoktur; dolayısıyla `SetSubtotals` öğesinin görünür bir etkiye sahip olmasını istediğinizde, satır veya sütun bölgesine her zaman en az iki alan yerleştirin.

## **İlgili Makaleler**

- [Özet Tablolardaki Sayfa Alanları](/cells/tr/cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for C++'da Özet Tabloları Yenileme](/cells/tr/cpp/refresh-pivot-table/)
- [Özet Tablolarına Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
