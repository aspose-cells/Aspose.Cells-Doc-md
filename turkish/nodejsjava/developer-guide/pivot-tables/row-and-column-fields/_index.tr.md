---
title: Row and Column Fields in Aspose.Cells for Node.js via Java
linktitle: Satır ve Sütun Alanları
description: Learn how to add base fields to the row and column regions of a pivot table and control pivot field subtotals using PivotField.setSubtotals in Aspose.Cells for Node.js via Java
keywords: Aspose.Cells, Node.js, Java, pivot table, row field, column field, PivotField, setSubtotals, PivotFieldSubtotalType, subtotals
type: docs
weight: 220
url: /tr/nodejs-java/row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---


Satır ve sütun alanları, bir pivot tablosunun yapı taşlarıdır. Satır bölgesine yerleştirilen bir alan, pivot tablonun sol tarafında dikey olarak görünür; sütun bölgesine yerleştirilen bir alan ise üstte yatay olarak görünür. Bu makale, bu bölgelere programatik olarak temel alanların nasıl ekleneceğini ve `PivotField.setSubtotals` yöntemi kullanılarak alan grupları arasında işlenen alt toplamların nasıl kontrol edileceğini gösterir.

## **Satır veya Sütun Bölgesine Alan Ekleme**

`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` yöntemi, kaynak verideki bir temel alanı dört pivot bölgesinden birine taşır. `fieldType` bağımsız değişkeni aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.

- `ROW` — solda dikey olarak yerleştirilen alanlar
- `COLUMN` — üstte yatay olarak yerleştirilen alanlar
- `DATA` — değerleri toplanan alanlar
- `PAGE` — rapor filtreleri olarak kullanılan alanlar

Alanlar eklendikten sonra, `PivotTable.getRowFields()` ve `PivotTable.getColumnFields()` özellikleri aracılığıyla bunlara erişebilirsiniz. Her özellik bir `PivotFieldCollection` döndürür. `RowFields`'in 0 indeksindeki alan en dıştaki satır alanıdır ve sonraki indeksler onun içine yerleştirilmiş alanları temsil eder. Aynı indeksleme kuralı `ColumnFields` için de geçerlidir.

Alan iç içe geçme sırası önemlidir. Önce `Category` alanını satır bölgesine, ardından `Item` alanını eklemek, dış gruplaması `Category` ve iç gruplaması `Item` olan bir pivot tablosu üretir. Sırayı tersine çevirmek hiyerarşiyi tersine çevirir.

## **Pivot Alan Alt Toplamları**

`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` yöntemi, bir pivot alanı için hangi alt toplam satırlarının görüneceğini kontrol eder. Her çağrı tek bir alt toplam türünü bağımsız olarak değiştirir. `shown = true` değerini geçmek alt toplamı görüntüler, `shown = false` ise gizler. Her çağrı yalnızca bir türü etkilediğinden, yöntemi farklı `subtotalType` değerleriyle birden çok kez çağırmak özel bir alt toplam alt kümesi oluşturur.

`PivotFieldSubtotalType` numaralandırması, kullanılabilir alt toplam türlerini tanımlar.

- `AUTOMATIC` — Aspose.Cells varsayılan seçimi seçer (genellikle sayısal alanlar için `SUM`)
- `NONE` — her alt toplam satırını gizle
- `SUM`
- `COUNT`
- `AVERAGE`
- `MAX`
- `MIN`
- `PRODUCT`
- `STD_DEV`
- `STD_DEVP`
- `VAR`
- `VARP`

{{% alert color="primary" %}}
Alt toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla pivot alanı olduğunda görüntülenir. Tek bir alanın arasında alt toplanacak anlamlı bir şey yoktur, dolayısıyla bu durumda `setSubtotals` çağrılarının görünür bir etkisi olmaz. Bu nedenle bu makale, her örnekte iki satır alanı (`Category` dış, `Item` iç) yerleştirir; böylece her `Category` grubu arasındaki alt toplam sınırı görünür hale gelir.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Alt Toplamlar**

`setSubtotals` yöntemini hiç çağırmadığınızda, Aspose.Cells sayısal alanlar için `AUTOMATIC` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanında `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` çağırarak bu davranışı açıkça doğrular.

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

## **Senaryo 2 — Tüm Alt Toplamların Gizlenmesi (Yok)**

`setSubtotals(PivotFieldSubtotalType.NONE, true)` çağrısı, pivot tablodan her alt toplam satırını kaldırarak yalnızca alan satırlarını ve alttaki genel toplamı bırakır. Bu, özet satırları olmadan ham gruplanmış verileri istediğinizde kullanışlıdır.

```javascript
let workbook = new AsposeCells.Workbook();
let worksheet = workbook.getWorksheets().get(0);
worksheet.setName("Data");

let headers = ["Category", "Item", "Year", "Amount"];
for (let j = 0; j < headers.length; j++)
{
    worksheet.getCells().get(0, j).putValue(headers[j]);
}

let data = [
    ["Fruit", "Apple", 2020, 100],
    ["Fruit", "Apple", 2021, 150],
    ["Fruit", "Banana", 2020, 80],
    ["Fruit", "Banana", 2021, 90],
    ["Vegetable", "Carrot", 2020, 50],
    ["Vegetable", "Carrot", 2021, 60],
    ["Vegetable", "Daikon", 2020, 40],
    ["Vegetable", "Daikon", 2021, 45]
];

for (let i = 0; i < data.length; i++)
{
    for (let j = 0; j < data[i].length; j++)
    {
        worksheet.getCells().get(i + 1, j).putValue(data[i][j]);
    }
}

let pivotIndex = worksheet.getPivotTables().add("A1:D9", "F3", "PivotTable1");
let pivotTable = worksheet.getPivotTables().get(pivotIndex);

pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");

let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.None, true);
pivotTable.refreshData();
pivotTable.calculateData();

workbook.save("output_none.xlsx");
```

## **Senaryo 3 — Özel Alt Toplam Alt Kümesi (Toplam + Ortalama)**

Tek bir alt toplam türüyle sınırlı değilsiniz. Her `setSubtotals` çağrısı tek bir tür üzerinde bağımsız olarak çalışır; dolayısıyla yöntemi iki kez çağırmak — bir kez `SUM` ile, bir kez `AVERAGE` ile — her `Category` grubu için iki alt toplam satırından oluşan özel bir alt küme üretir.

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

Yukarıdaki üç senaryo aynı veri kümesini ve pivot tablo yapısını paylaşır. Aralarındaki tek fark, dış `Category` satır alanına uygulanan `setSubtotals` çağrısıdır. İki alan kuralını unutmayın: bir bölgedeki tek bir alanın arasında alt toplanacak bir şey yoktur; bu nedenle `setSubtotals`'ın görünür bir etkiye sahip olmasını istediğinizde, satır veya sütun bölgesine her zaman en az iki alan yerleştirin.

## **İlgili Makaleler**

- [Pivot Tablolarda Sayfa Alanları](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java'da Pivot Tabloları Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)
- [Pivot Tablolarına Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
{{< app/cells/assistant language="csharp" >}}
