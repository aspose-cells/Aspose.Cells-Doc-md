---
title: Pivot Alanı Öğelerinin Ayrık Gruplanması
linktitle: Ayrık Gruplanması
description: Aspose.Cells for C++ kullanarak DiscreteGroupItem ve PivotFieldGroupOptions.DiscreteGroupItems ile pivot alanı öğelerini meyve ve sebzeler gibi özel adlı gruplara nasıl gruplandıracağınızı öğrenin.
keywords: Aspose.Cells for C++, özet tablosu, ayrık gruplama, DiscreteGroupItem, PivotFieldGroupOptions, özet tablosu öğelerini gruplandırma, özel gruplar, PivotField.Group, C++, Excel özet tablosu
type: docs
weight: 90
url: /tr/cpp/discrete-group-pivot-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplama, öğeleri veri türüne göre gruplar; örneğin tarihleri aylara ve çeyreklere, sayıları ise aralıklara gruplar. Ayrık gruplama ise bunun tersi sorunu çözer: belirli, birbiriyle ilgisiz öğeleri özel adlı gruplarda toplar. Örneğin ürünleri meyve ve sebze adlı gruplarda, mağazaları bölge adlı gruplarda veya hesapları alan adlı gruplarda toplar. Aspose.Cells, ayrık gruplamayı `DiscreteGroupItem` sınıfı ve `PivotFieldGroupOptions.DiscreteGroupItems` özelliği aracılığıyla sağlar.
- `DiscreteGroupItem`, bir grup adı ile o gruba ait öğelerden oluşur. Öğeler iki şekilde tanımlanabilir: adlarıyla (`DiscreteGroupItem("fruit", { "grape", "cherry" })`) veya kaynak verideki sıfır tabanlı konumlarıyla (`DiscreteGroupItem("fruit", { 0, 3 })`). Her iki biçim de aynı sonucu üretir.
- Ayrık gruplama, seçenekler `PivotField.Group(PivotFieldGroupOptions)` çağrısı aracılığıyla iletilerek özet tablosunun satır veya sütun bölgesindeki bir alana uygulanır.

## **Pivot Alanı Öğelerini Adlarına Göre Gruplandırma**
Aşağıdaki örnek, küçük bir satış listesi (ürün, tarih ve tutar) oluşturur ve bundan, `product` alanının satır alanında, `date` alanının sütun alanında ve `amount` alanının veri alanında bulunduğu bir özet tablosu oluşturur; ardından öğe adlarına göre iki özel grup tanımlar: `fruit` (`grape`, `cherry`) ve `vegetables` (`carrot`, `potato`). Sonuç, iki düzeyli bir satır düzenini gösterir: dış düzeyde grup adı, altında ise özgün öğeler bulunur. Böylece eğilimler özel grup ve öğe bazında incelenebilir.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    cells.Get(1, 1).PutValue(Date{2021, 2, 5, 0, 0, 0, 0});
    cells.Get(2, 1).PutValue(Date{2022, 3, 8, 0, 0, 0, 0});
    cells.Get(3, 1).PutValue(Date{2023, 4, 10, 0, 0, 0, 0});
    cells.Get(4, 1).PutValue(Date{2024, 5, 16, 0, 0, 0, 0});
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, U16String(u"product"));
    pivotTable.AddFieldToArea(PivotFieldType::Column, U16String(u"date"));
    pivotTable.AddFieldToArea(PivotFieldType::Data, U16String(u"amount"));
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<U16String>{u"grape", u"cherry"});
    DiscreteGroupItem vegetable(u"vegetable", Vector<U16String>{u"carrot", u"potato"});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotField.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

`CalculateData()` çağrısından sonra özet tablosunun satır alanında `fruit` (`grape` 50, `cherry` 80) ve `vegetable` (`carrot` 60, `potato` 70) ile genel toplam 260 gösterilir; sütun etiketlerinde ise dört tarih (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) korunur.

## **Pivot Alanı Öğelerini Dizinlerine Göre Gruplandırma**
Öğe adları uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci oluşturucusu öğeleri dizinle tanımlar. Dizinler, öğelerin alfabetik sıra yerine kaynak veride göründükleri sıraya göre sıfır tabanlı konumlarıdır. Yukarıdaki örnek veride `grape` 0. öğe, `carrot` 1. öğe, `potato` 2. öğe ve `cherry` 3. öğedir; dolayısıyla `fruit` grubu `{ 0, 3 }`, `vegetable` grubu `{ 1, 2 }` olur. Sonuç, ada dayalı örnekle aynıdır.

```cpp
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;
int main() {
    Aspose::Cells::Startup();
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();
    cells.Get(0, 0).PutValue(u"product");
    cells.Get(1, 0).PutValue(u"grape");
    cells.Get(2, 0).PutValue(u"carrot");
    cells.Get(3, 0).PutValue(u"potato");
    cells.Get(4, 0).PutValue(u"cherry");
    Style dateStyle = wb.CreateStyle();
    dateStyle.SetCustom(u"m/d/yyyy");
    cells.Get(0, 1).PutValue(u"date");
    Date firstDate{2021, 2, 5, 0, 0, 0, 0};
    Date secondDate{2022, 3, 8, 0, 0, 0, 0};
    Date thirdDate{2023, 4, 10, 0, 0, 0, 0};
    Date fourthDate{2024, 5, 16, 0, 0, 0, 0};
    cells.Get(1, 1).PutValue(firstDate);
    cells.Get(2, 1).PutValue(secondDate);
    cells.Get(3, 1).PutValue(thirdDate);
    cells.Get(4, 1).PutValue(fourthDate);
    for (int r = 1; r <= 4; ++r) {
        cells.Get(r, 1).SetStyle(dateStyle);
    }
    cells.Get(0, 2).PutValue(u"amount");
    cells.Get(1, 2).PutValue(50);
    cells.Get(2, 2).PutValue(60);
    cells.Get(3, 2).PutValue(70);
    cells.Get(4, 2).PutValue(80);
    PivotTable pivotTable = sheet.GetPivotTables().Add(u"=Sheet1!A1:C5", 11, 0);
    pivotTable.AddFieldToArea(PivotFieldType::Row, u"product");
    pivotTable.AddFieldToArea(PivotFieldType::Column, u"date");
    pivotTable.AddFieldToArea(PivotFieldType::Data, u"amount");
    pivotTable.SetPivotTableStyleType(PivotTableStyleType::PivotTableStyleMedium10);
    DiscreteGroupItem fruit(u"fruit", Vector<int32_t>{0, 3});
    DiscreteGroupItem vegetable(u"vegetable", Vector<int32_t>{1, 2});
    PivotFieldGroupOptions groupOptions;
    groupOptions.SetDiscreteGroupItems(Vector<DiscreteGroupItem>{fruit, vegetable});
    pivotTable.GetRowFields().Get(0).Group(groupOptions);
    pivotTable.CalculateData();
    wb.Save(u"outputDiscreteGroupPivotFieldByIndex.xlsx");
    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Not**

{{% alert color="primary" %}}
- Herhangi bir özel gruba atanmayan öğeler kaybolmaz. Bu öğeler, özet tablosunda özel gruplarla aynı düzeyde, her biri kendi başına tek öğelik bir kayıt olarak kalır. Yukarıdaki örnekte yalnızca `fruit` grubu tanımlanırsa `carrot` ve `potato`, `fruit` grubunun yanında bağımsız kayıtlar olarak satır alanında kalır.
- `PivotFieldGroupOptions.NewPivotField` özelliği, ayrık gruplamanın düzenini denetler. Varsayılan değeri `true` olup gruplandırılan alanı özgün alanın yanında yeni bir dış alan olarak ekler ve yukarıda gösterilen iki düzeyli düzeni oluşturur (`RowFields` 2'ye çıkar). Özgün alanın yerine geçmesi için bu özelliği `false` olarak ayarlayın. Bu durumda satır alanı, yalnızca grup adlarını ve bunların toplam değerlerini içeren tek düzeyli bir düzen gösterir: `fruit` 130 (50 + 80) ve `vegetable` 130 (60 + 70).
- `DiscreteGroupItem` sınıfının ada ve dizine dayalı oluşturucuları aynı `DiscreteGroupItems` koleksiyonu içinde birlikte kullanılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosunda Pivot Alanlarını Gruplandırma](/cells/tr/cpp/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/cpp/pivot-table-add-row-and-column-fields/)
- [Etiket veya Değere Göre Özet Tablolarını Filtreleme](/cells/tr/cpp/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/cpp/apply-style-to-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/cpp/refresh-pivot-table/)

{{< app/cells/assistant language="cpp" >}}