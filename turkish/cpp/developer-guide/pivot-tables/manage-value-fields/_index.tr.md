---
title: Aspose.Cells for C++'ta Değer Alanları
linktitle: Aspose.Cells for C++'ta Değer Alanları
description: Aspose.Cells for C++ kullanarak bir pivot tablonun veri bölgesine temel alanlar eklemeyi, PivotField.Function ile özetleme fonksiyonunu değiştirmeyi ve değer alanını Satır veya Sütun eksenine yerleştirmeyi öğrenin.
keywords: Aspose.Cells, C++, pivot tablo, değer alanı, PivotField, PivotField.Function, veri alanı, PivotTable.ValuesField, Sum, Average
type: docs
weight: 230
url: /tr/cpp/manage-value-fields/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## Veri Bölgesine Alan Ekleme

Bir temel alanı veri (değer) bölgesine eklemek, pivot tablonun kaynak verilerinizi nasıl topladığını şekillendirmedeki ilk adımdır. Aspose.Cells, `PivotFieldType.Data` sabitini ve kaynak sütun adını kabul eden bir aşırı yükleme olan `PivotTable.AddFieldToArea(PivotFieldType, string)` yöntemini sunar. Bir alan veri bölgesine eklendikten sonra API, onu alanların eklenme sırasıyla `PivotTable.DataFields` koleksiyonu aracılığıyla sunar. Varsayılan olarak, sayısal bir kaynak sütun `ConsolidationFunction.Sum` ile özetlenirken, sayısal olmayan bir sütun varsayılan olarak `Count` olur.

## Özetleme Fonksiyonunu Değiştirme

Veri bölgesine yerleştirilen her alan dahili olarak bir `PivotField` örneği olarak sarmalanır ve onun `Function` özelliği `ConsolidationFunction` enum'undan bir değer döndürür. Aynı `Function` ayarlayıcısı, `Sum`, `Count`, `Average`, `Max`, `Min`, `Product`, `StdDev`, `StdDevp`, `Var` ve `Varp` dahil mevcut toplamalar arasında geçiş yapmanıza olanak tanır.

{{% alert color="primary" %}}
`Function` özelliğini değiştirmek yalnızca toplamayı etkiler, kaynak sütun değişmez.
{{% /alert %}}

Bu nedenle tek bir pivot içinde, bir veri alanını `Sum` olarak bırakırken aynı kaynak sütunu hedefleyen ancak `Count` veya `Average` kullanan ikinci bir veri alanı ekleyebilirsiniz.

## Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme

Bir pivot tablo iki veya daha fazla veri alanı içerdiğinde, Aspose.Cells `PivotTable.ValuesField` adında ek bir sanal alan sunar. Bu sanal alan, veri bölgesinde bulunan her veri alanının toplamını temsil eder. Onu temel bir pivot alanı olarak Satır veya Sütun bölgesine sürükleyebilirsiniz; bu, birden çok ölçümü yan yana düzenlemek için kullanışlıdır.

{{% alert color="primary" %}}
Hiç değer alanı yoksa veya yalnızca bir tane varsa `PivotTable.ValuesField` çalışmaz.
{{% /alert %}}

Aşağıdaki senaryolar, aynı pivot yapısı üzerinde yukarıda açıklanan her yeteneği gösteren üç uçtan uca örneği ele alır.

## Senaryo 1 — Temel Bir Alanı Değer Bölgesine Sürükleme

Bu senaryo, tek bir temel alanın (`Amount`) mevcut bir pivot tablonun veri bölgesine nasıl yerleştirileceğini gösterir. Paylaşılan pivot yapısı, `Category` ve `Item` alanlarını Satır eksenine, `Year` alanını ise Sütun eksenine yerleştirir. İşlemden sonra `Amount` veri bölgesinde görünür ve varsayılan olarak `Amount` değerinin `Sum` olarak hesaplanır.

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Aspose::Cells::Startup();

 Workbook workbook;
 Worksheet worksheet = workbook.GetWorksheets().Get(0);
 worksheet.SetName(u"Data");

 Cells cells = worksheet.GetCells();

 // A1:D1 aralığındaki başlıklar
 cells.Get(0, 0).PutValue(U16String("Category"));
 cells.Get(0, 1).PutValue(U16String("Item"));
 cells.Get(0, 2).PutValue(U16String("Year"));
 cells.Get(0, 3).PutValue(U16String("Amount"));

 // j üzerinde dallanan iç içe döngüler kullanarak A2:D9 veri satırları
 for (int i = 1; i <= 8; i++)
 {
 for (int j = 0; j < 4; j++)
 {
 switch (j)
 {
 case 0:
 cells.Get(i, j).PutValue(U16String(i <= 4 ? "Fruit" : "Vegetable"));
 break;
 case 1:
 if (i == 1 || i == 2) cells.Get(i, j).PutValue(U16String("Apple"));
 else if (i == 3 || i == 4) cells.Get(i, j).PutValue(U16String("Banana"));
 else if (i == 5 || i == 6) cells.Get(i, j).PutValue(U16String("Carrot"));
 else cells.Get(i, j).PutValue(U16String("Daikon"));
 break;
 case 2:
 cells.Get(i, j).PutValue(2020 + ((i - 1) % 2));
 break;
 case 3:
 if (i == 1) cells.Get(i, j).PutValue(100);
 else if (i == 2) cells.Get(i, j).PutValue(150);
 else if (i == 3) cells.Get(i, j).PutValue(80);
 else if (i == 4) cells.Get(i, j).PutValue(90);
 else if (i == 5) cells.Get(i, j).PutValue(50);
 else if (i == 6) cells.Get(i, j).PutValue(60);
 else if (i == 7) cells.Get(i, j).PutValue(40);
 else cells.Get(i, j).PutValue(45);
 break;
 }
 }
 }

 // F3 konumunda PivotTable1 adında bir pivot tablo ekle
 int pivotIndex = worksheet.GetPivotTables().Add(u"A1:D9", u"F3", u"PivotTable1");
 PivotTable pivotTable = worksheet.GetPivotTables().Get(pivotIndex);

 // Pivot düzeni: Satırda Category ve Item, Sütunda Year, veri alanı olarak Amount
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Category");
 pivotTable.AddFieldToArea(PivotFieldType::Row, u"Item");
 pivotTable.AddFieldToArea(PivotFieldType::Column, u"Year");
 pivotTable.AddFieldToArea(PivotFieldType::Data, u"Amount");

 pivotTable.CalculateData();
 workbook.Save(u"output_drag.xlsx");

 Aspose::Cells::Cleanup();
 return 0;
}
```

## Senaryo 2 — Özetleme Fonksiyonunu Değiştirme

Bu senaryo, Senaryo 1 ile aynı pivot yapısından başlar ancak `Amount` alanını veri bölgesine iki kez ekler. Her iki veri alanı da aynı kaynak sütuna başvurur, ancak ikinci alan `PivotField.Function` ayarlayıcısı kullanılarak geçersiz kılınır ve varsayılan `Sum` yerine `Count` olur.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 Vector<String> headers{ "Category", "Item", "Year", "Amount" };
 for (int j = 0; j < 4; j++) ws->GetCells()->Get(0, j)->PutValue(headers[j]);

 Vector<Vector<Object*>> data;
 // Verileri doldur...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 PivotField countField = pivotTable.GetDataFields().Get(1);
 countField->SetFunction(ConsolidationFunction_Count);
 pivotTable->CalculateData();
 workbook->Save("output_function.xlsx");
}
```

## Senaryo 3 — Değer Alanlarını Satır veya Sütun Eksenine Yerleştirme

İki veri alanı yerinde olduğunda, `PivotTable.ValuesField` kullanılabilir hale gelir. Bu senaryo, söz konusu toplama sanal alanını Sütun bölgesine sürükler, böylece veri bölgesindeki her ölçüm `Year` alanının yanında kendi sütun bloku olarak görünür.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Pivot;

int main() {
 Workbook workbook;
 Worksheet ws = workbook.GetWorksheets().Get(0);
 ws->SetName("Data");
 // ... veri oluştur ...
 int pivotIndex = ws->GetPivotTables()->Add("A1:D9", "F3", "PivotTable1");
 PivotTable pivotTable = ws.GetPivotTables().Get(pivotIndex);
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Category");
 pivotTable->AddFieldToArea(PivotFieldType::Row, "Item");
 pivotTable->AddFieldToArea(PivotFieldType::Column, "Year");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->AddFieldToArea(PivotFieldType::Data, "Amount");
 pivotTable->GetDataFields()->Get(1)->SetFunction(ConsolidationFunction_Count);
 pivotTable->AddFieldToArea(PivotFieldType::Column, pivotTable->GetValuesField()->GetName());
 pivotTable->CalculateData();
 workbook->Save("output_plot.xlsx");
}
```

Bu üç senaryo birlikte, varsayılan `Sum` ile tek bir veri alanından, sanal `ValuesField`'ın Satır veya Sütun eksenindeki düzeni kontrol ettiği çok ölçümlü bir pivota kadar Aspose.Cells for C++'ta değer alanı işlemenin her yönünü kapsar.

{{< app/cells/assistant language="cpp" >}}
