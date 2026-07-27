---
title: Aspose.Cells for .NET'te PivotTable'a satır ve sütun alanları ekleme
linktitle: Satır ve Sütun Alanları
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.SetSubtotals in Aspose.Cells for Node.js via C++
keywords: Aspose.Cells, Node.js, C++, pivot table, row field, column field, PivotField, SetSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /tr/nodejs-cpp/pivot-table-add-row-column-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Satır ve sütun alanları bir pivot tablonun yapı taşlarıdır. Satır bölgesine yerleştirilen bir alan pivotun solunda dikey olarak görünür, sütun bölgesine yerleştirilen bir alan ise üstte yatay olarak görünür. Bu makale, bu bölgelere programatik olarak temel alanların nasıl ekleneceğini ve `PivotField.SetSubtotals` yöntemi kullanılarak alan grupları arasında görüntülenen alt toplamların nasıl kontrol edileceğini göstermektedir.

## **Satır veya Sütun Bölgesine Alan Ekleme**

`PivotTable.AddFieldToArea(PivotFieldType fieldType, string fieldName)` yöntemi, kaynak verilerden bir temel alanı dört pivot bölgesinden birine taşır. `fieldType` bağımsız değişkeni aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.

- `Row` — dikey olarak sol tarafa yerleştirilen alanlar
- `Column` — yatay olarak üst tarafa yerleştirilen alanlar
- `Data` — değerleri toplanan alanlar
- `Page` — rapor filtreleri olarak kullanılan alanlar

Alanlar eklendikten sonra, `PivotTable.RowFields` ve `PivotTable.ColumnFields` özellikleri aracılığıyla bunlara erişebilirsiniz. Her özellik bir `PivotFieldCollection` döndürür. `RowFields` koleksiyonunun 0 dizinindeki alan en dıştaki satır alanıdır ve sonraki dizinler onun içine yerleştirilmiş alanları temsil eder. Aynı indeksleme kuralı `ColumnFields` için de geçerlidir.

Alan iç içe geçme sırası önemlidir. Önce `Category`'yi satır bölgesine, sonra `Item`'ı eklemek, dış gruplaması `Category` ve iç gruplaması `Item` olan bir pivot üretir. Sırayı tersine çevirmek hiyerarşiyi de tersine çevirir.

## **Pivot Alanı Alt Toplamları**

`PivotField.SetSubtotals(PivotFieldSubtotalType subtotalType, bool shown)` yöntemi, bir pivot alanı için hangi alt toplam satırlarının görüneceğini kontrol eder. Her çağrı tek bir alt toplam türünü bağımsız olarak değiştirir. `shown = true` geçmek alt toplamı görüntüler, `shown = false` geçmek ise gizler. Her çağrı yalnızca bir türü etkilediğinden, yöntemi farklı `subtotalType` değerleriyle birden çok kez çağırmak özel bir alt toplam alt kümesi oluşturur.

`PivotFieldSubtotalType` numaralandırması kullanılabilir alt toplam türlerini tanımlar.

- `Automatic` — Aspose.Cells varsayılan seçimi seçer (genellikle sayısal alanlar için `Sum`)
- `None` — her alt toplam satırını bastır
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
Alt toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla pivot alanı olduğunda görüntülenir. Tek bir alanın alt toplam alacak anlamlı bir şeyi yoktur, dolayısıyla bu durumda `SetSubtotals` çağrılarının görünür bir etkisi olmaz. Bu nedenle bu makale, her örnekte iki satır alanı (`Category` dış, `Item` iç) yerleştirir; böylece her `Category` grubu arasındaki alt toplam sınırı görünür olur.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Alt Toplamlar**

`SetSubtotals` yöntemini hiç çağırmadığınızda, Aspose.Cells sayısal alanlara `Automatic` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanı üzerinde `SetSubtotals(PivotFieldSubtotalType.Automatic, true)` çağırarak bu davranışı açıkça doğrular.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get(0, 0).putValue("Category");
worksheet.getCells().get(0, 1).putValue("Item");
worksheet.getCells().get(0, 2).putValue("Year");
worksheet.getCells().get(0, 3).putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Automatic, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_automatic.xlsx");
```

## **Senaryo 2 — Tüm Alt Toplamların Bastırılması (None)**

`SetSubtotals(PivotFieldSubtotalType.None, true)` çağrısı, pivottaki tüm alt toplam satırlarını kaldırarak yalnızca alan satırlarını ve alttaki genel toplamı bırakır. Bu, herhangi bir özet satırı olmadan ham gruplandırılmış verileri istediğinizde kullanışlıdır.

```javascript
const AsposeCells = require("aspose.cells");

const workbook = new AsposeCells.Workbook();
const worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

const headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++) {
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

const data = [
    ["Fruit",     "Apple",  2020, 100],
    ["Fruit",     "Apple",  2021, 150],
    ["Fruit",     "Banana", 2020, 80],
    ["Fruit",     "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];

for (let i = 0; i < data.length; i++) {
    for (let j = 0; j < data[i].length; j++) {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

const pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
const pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

const categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Senaryo 3 — Özel Alt Toplam Alt Kümesi (Sum + Average)**

Tek bir alt toplam türüyle sınırlı değilsiniz. Her `SetSubtotals` çağrısı bir tür üzerinde bağımsız olarak çalışır, dolayısıyla yöntemi iki kez çağırmak — bir kez `Sum` ve bir kez `Average` ile — her `Category` grubu için iki alt toplam satırlık özel bir alt küme üretir.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

worksheet.getCells().get("A1").putValue("Category");
worksheet.getCells().get("B1").putValue("Item");
worksheet.getCells().get("C1").putValue("Year");
worksheet.getCells().get("D1").putValue("Amount");

worksheet.getCells().get(1, 0).putValue("Fruit");
worksheet.getCells().get(1, 1).putValue("Apple");
worksheet.getCells().get(1, 2).putValue(2020);
worksheet.getCells().get(1, 3).putValue(100);

worksheet.getCells().get(2, 0).putValue("Fruit");
worksheet.getCells().get(2, 1).putValue("Apple");
worksheet.getCells().get(2, 2).putValue(2021);
worksheet.getCells().get(2, 3).putValue(150);

worksheet.getCells().get(3, 0).putValue("Fruit");
worksheet.getCells().get(3, 1).putValue("Banana");
worksheet.getCells().get(3, 2).putValue(2020);
worksheet.getCells().get(3, 3).putValue(80);

worksheet.getCells().get(4, 0).putValue("Fruit");
worksheet.getCells().get(4, 1).putValue("Banana");
worksheet.getCells().get(4, 2).putValue(2021);
worksheet.getCells().get(4, 3).putValue(90);

worksheet.getCells().get(5, 0).putValue("Vegetable");
worksheet.getCells().get(5, 1).putValue("Carrot");
worksheet.getCells().get(5, 2).putValue(2020);
worksheet.getCells().get(5, 3).putValue(50);

worksheet.getCells().get(6, 0).putValue("Vegetable");
worksheet.getCells().get(6, 1).putValue("Carrot");
worksheet.getCells().get(6, 2).putValue(2021);
worksheet.getCells().get(6, 3).putValue(60);

worksheet.getCells().get(7, 0).putValue("Vegetable");
worksheet.getCells().get(7, 1).putValue("Daikon");
worksheet.getCells().get(7, 2).putValue(2020);
worksheet.getCells().get(7, 3).putValue(40);

worksheet.getCells().get(8, 0).putValue("Vegetable");
worksheet.getCells().get(8, 1).putValue("Daikon");
worksheet.getCells().get(8, 2).putValue(2021);
worksheet.getCells().get(8, 3).putValue(45);

let pivotTables = worksheet.getPivotTables();
let pivotIndex = pivotTables.add("A1:D9", "F3", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Sum, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.Average, true);

pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_custom.xlsx");
## **Özet**

Yukarıdaki üç senaryo aynı veri kümesini ve pivot tablo yapısını paylaşır. Aralarındaki tek fark, dış `Category` satır alanına uygulanan `SetSubtotals` çağrısıdır. İki alan kuralını unutmayın: bir bölgedeki tek alanın alt toplam alacak bir şeyi yoktur, dolayısıyla `SetSubtotals`'ın görünür bir etkiye sahip olmasını istediğinizde satır veya sütun bölgesine her zaman en az iki alan yerleştirin.

## **İlgili Makaleler**

- [Pivot Tablolardaki Sayfa Alanları](/cells/tr/nodejs-cpp/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via C++'da Pivot Tabloları Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/)
- [Pivot Tablolara Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
