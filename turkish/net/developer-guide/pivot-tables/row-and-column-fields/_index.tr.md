---
title: Aspose.Cells for .NET'te PivotTable'a satır ve sütun alanları ekleme
linktitle: Satır ve Sütun Alanları
description: Aspose.Cells for .NET'te PivotField.SetSubtotals kullanarak bir pivot tablosunun satır ve sütun bölgelerine temel alanların nasıl ekleneceğini ve pivot alanı alt toplamlarının nasıl kontrol edileceğini öğrenin.
keywords: Aspose.Cells, .NET, pivot tablo, satır alanı, sütun alanı, PivotField, SetSubtotals, PivotFieldSubtotalType, alt toplamlar
type: docs
weight: 220
url: /tr/net/pivot-table-add-row-column-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Satır veya Sütun Bölgesine Alan Ekleme**

`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` yöntemi, kaynak verilerden bir temel alanı dört pivot bölgesinden birine taşır. `fieldType` argümanı aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.

- `Row` — sol tarafta dikey olarak yerleştirilen alanlar
- `Column` — üstte yatay olarak yerleştirilen alanlar
- `Data` — değerleri toplanan alanlar
- `Page` — rapor filtreleri olarak kullanılan alanlar

Alanlar eklendikten sonra `PivotTable.RowFields` ve `PivotTable.ColumnFields` özellikleri aracılığıyla bunlara erişebilirsiniz. Her özellik bir `PivotFieldCollection` döndürür. `RowFields` koleksiyonunun 0 indeksindeki alan en dıştaki satır alanıdır ve sonraki indisler onun içine yerleştirilmiş alanları temsil eder. Aynı indeksleme kuralı `ColumnFields` için de geçerlidir.

Alan iç içe geçme sırası önemlidir. Önce `Category` alanını satır bölgesine, ardından `Item` alanını eklemek, dış gruplandırması `Category` ve iç gruplandırması `Item` olan bir pivot oluşturur. Sırayı tersine çevirmek hiyerarşiyi de tersine çevirir.

## **Pivot Alanı Alt Toplamları**

`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` yöntemi, bir pivot alanı için hangi alt toplam satırlarının görüneceğini kontrol eder. Her çağrı tek bir alt toplam türünü bağımsız olarak değiştirir. `shown = true` değerini geçmek alt toplamı gösterirken, `shown = false` değerini geçmek onu gizler. Her çağrı yalnızca bir türü etkilediğinden, yöntemi farklı `subtotalType` değerleriyle birden çok kez çağırmak özel bir alt toplam alt kümesi oluşturur.

`PivotFieldSubtotalType` numaralandırması kullanılabilir alt toplam türlerini tanımlar.

- `Automatic` — Aspose.Cells varsayılan seçimi belirler (genellikle sayısal alanlar için `Sum`)
- `None` — tüm alt toplam satırlarını gizler
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
Alt toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla pivot alanı olduğunda görüntülenir. Tek bir alanın arasında toplanacak anlamlı bir şey yoktur, dolayısıyla bu durumda `SetSubtotals` çağrılarının görünür bir etkisi olmaz. Bu nedenle bu makale, her `Category` grubu arasındaki alt toplam sınırının görünür olması için her örnekte iki satır alanı (`Category` dış, `Item` iç) yerleştirir.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Alt Toplamlar**

Hiç `SetSubtotals` çağırmadığınızda Aspose.Cells sayısal alanlara `Automatic` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanı üzerinde `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` çağırarak bu davranışı açıkça doğrular.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells[0, 0].PutValue("Category");
worksheet.Cells[0, 1].PutValue("Item");
worksheet.Cells[0, 2].PutValue("Year");
worksheet.Cells[0, 3].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Automatic, true);

pivotTable.CalculateData();

workbook.Save("output_automatic.xlsx");
```

## **Senaryo 2 — Tüm Alt Toplamları Gizleme (None)**

`SetSubtotals(PivotFieldSubtotalType.None, true)` çağırmak, pivot'tan her alt toplam satırını kaldırarak yalnızca alan satırlarını ve alttaki genel toplamı bırakır. Bu, ham gruplandırılmış verileri herhangi bir özet satır olmadan istediğinizde kullanışlıdır.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

string[] headers = { "Category", "Item", "Year", "Amount" };
for (int j = 0; j < headers.Length; j++)
{
    worksheet.Cells[0, j].PutValue(headers[j]);
}

object[,] data = {
    { "Fruit",     "Apple",  2020, 100 },
    { "Fruit",     "Apple",  2021, 150 },
    { "Fruit",     "Banana", 2020, 80  },
    { "Fruit",     "Banana", 2021, 90  },
    { "Vegetable", "Carrot", 2020, 50  },
    { "Vegetable", "Carrot", 2021, 60  },
    { "Vegetable", "Daikon", 2020, 40  },
    { "Vegetable", "Daikon", 2021, 45  }
};

for (int i = 0; i < data.GetLength(0); i++)
{
    for (int j = 0; j < data.GetLength(1); j++)
    {
        worksheet.Cells[i + 1, j].PutValue(data[i, j]);
    }
}

int pivotIndex = worksheet.PivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = worksheet.PivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.None, true);
pivotTable.CalculateData();

workbook.Save("output_none.xlsx");
```

## **Senaryo 3 — Özel Alt Toplam Alt Kümesi (Sum + Average)**

Tek bir alt toplam türüyle sınırlı değilsiniz. Her `SetSubtotals` çağrısı bir tür üzerinde bağımsız olarak çalışır, dolayısıyla yöntemi iki kez çağırmak — bir kez `Sum` ile ve bir kez `Average` ile — her `Category` grubu için iki alt toplam satırından oluşan özel bir alt küme oluşturur.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Name = "Data";

worksheet.Cells["A1"].PutValue("Category");
worksheet.Cells["B1"].PutValue("Item");
worksheet.Cells["C1"].PutValue("Year");
worksheet.Cells["D1"].PutValue("Amount");

worksheet.Cells[1, 0].PutValue("Fruit");
worksheet.Cells[1, 1].PutValue("Apple");
worksheet.Cells[1, 2].PutValue(2020);
worksheet.Cells[1, 3].PutValue(100);

worksheet.Cells[2, 0].PutValue("Fruit");
worksheet.Cells[2, 1].PutValue("Apple");
worksheet.Cells[2, 2].PutValue(2021);
worksheet.Cells[2, 3].PutValue(150);

worksheet.Cells[3, 0].PutValue("Fruit");
worksheet.Cells[3, 1].PutValue("Banana");
worksheet.Cells[3, 2].PutValue(2020);
worksheet.Cells[3, 3].PutValue(80);

worksheet.Cells[4, 0].PutValue("Fruit");
worksheet.Cells[4, 1].PutValue("Banana");
worksheet.Cells[4, 2].PutValue(2021);
worksheet.Cells[4, 3].PutValue(90);

worksheet.Cells[5, 0].PutValue("Vegetable");
worksheet.Cells[5, 1].PutValue("Carrot");
worksheet.Cells[5, 2].PutValue(2020);
worksheet.Cells[5, 3].PutValue(50);

worksheet.Cells[6, 0].PutValue("Vegetable");
worksheet.Cells[6, 1].PutValue("Carrot");
worksheet.Cells[6, 2].PutValue(2021);
worksheet.Cells[6, 3].PutValue(60);

worksheet.Cells[7, 0].PutValue("Vegetable");
worksheet.Cells[7, 1].PutValue("Daikon");
worksheet.Cells[7, 2].PutValue(2020);
worksheet.Cells[7, 3].PutValue(40);

worksheet.Cells[8, 0].PutValue("Vegetable");
worksheet.Cells[8, 1].PutValue("Daikon");
worksheet.Cells[8, 2].PutValue(2021);
worksheet.Cells[8, 3].PutValue(45);

PivotTableCollection pivotTables = worksheet.PivotTables;
int pivotIndex = pivotTables.Add("A1:D9", "F3", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

pivotTable.AddFieldToArea(PivotFieldType.Row, "Category");
pivotTable.AddFieldToArea(PivotFieldType.Row, "Item");
pivotTable.AddFieldToArea(PivotFieldType.Column, "Year");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Amount");

PivotField categoryField = pivotTable.RowFields[0];
categoryField.SetSubtotals(PivotFieldSubtotalType.Sum, true);
categoryField.SetSubtotals(PivotFieldSubtotalType.Average, true);

pivotTable.CalculateData();

workbook.Save("output_custom.xlsx");
```

## **Özet**

Yukarıdaki üç senaryo aynı veri kümesini ve pivot tablo yapısını paylaşır. Aralarındaki tek fark, dış `Category` satır alanına uygulanan `SetSubtotals` çağrısıdır. İki alan kuralını unutmayın: bir bölgedeki tek alanın arasında toplanacak bir şey yoktur, dolayısıyla `SetSubtotals`'ın görünür bir etkiye sahip olmasını istediğinizde her zaman satır veya sütun bölgesine en az iki alan yerleştirin.

## **İlgili Makaleler**

- [Pivot Tablolardaki Sayfa Alanları](/cells/tr/net/add-page-field-in-pivot-table/)
- [Aspose.Cells for .NET'te Pivot Tabloları Yenileme](/cells/tr/net/refresh-pivot-table/)
- [Pivot Tablolara Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)

{{< app/cells/assistant language="csharp" >}}
