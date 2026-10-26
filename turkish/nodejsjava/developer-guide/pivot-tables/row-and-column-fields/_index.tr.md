---
title: Aspose.Cells for Node.js via Java ile Özet Tablosuna Satır ve Sütun Alanları Ekleme
linktitle: Aspose.Cells for Node.js via Java ile Özet Tablosuna Satır ve Sütun Alanları Ekleme
description: Aspose.Cells for Node.js via Java kullanarak bir özet tablonun satır ve sütun bölgelerine temel alanlar eklemeyi ve özet tablo alanlarının alt toplamlarını PivotField.setSubtotals ile kontrol etmeyi öğrenin
keywords: Aspose.Cells, Node.js, Java, özet tablo, satır alanı, sütun alanı, PivotField, setSubtotals, PivotFieldSubtotalType, alt toplamlar
type: docs
weight: 220
url: /tr/nodejs-java/pivot-table-add-row-and-column-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Satır veya Sütun Bölgesine Alan Ekleme**
`PivotTable.addFieldToArea(PivotFieldType fieldType, String fieldName)` yöntemi, kaynak verilerdeki bir temel alanı dört özet tablo bölgesinden birine taşır. `fieldType` argümanı aşağıdaki `PivotFieldType` değerlerinden birini kabul eder.
- `ROW` — sol tarafta dikey olarak yerleştirilen alanlar
- `COLUMN` — üst kısımda yatay olarak yerleştirilen alanlar
- `DATA` — değerleri toplanan alanlar
- `PAGE` — rapor filtreleri olarak kullanılan alanlar
Alanların iç içe yerleştirilme sırası önemlidir. Satır bölgesine önce `Category`, ardından `Item` eklediğinizde, dış gruplaması `Category` ve iç gruplaması `Item` olan bir özet tablo oluşur. Sırayı tersine çevirmek hiyerarşiyi de tersine çevirir.

## **Özet Tablo Alanı Alt Toplamları**
`PivotField.setSubtotals(PivotFieldSubtotalType subtotalType, boolean shown)` yöntemi, bir özet tablo alanı için hangi alt toplam satırlarının görüntüleneceğini kontrol eder. Her çağrı tek bir alt toplam türünü bağımsız olarak açar veya kapatır. `shown = true` değeri belirtildiğinde alt toplam görüntülenir; `shown = false` değerinde ise gizlenir. Her çağrı yalnızca bir türü etkilediğinden, yöntemi farklı `subtotalType` değerleriyle birden fazla kez çağırmak özel bir alt toplam alt kümesi oluşturur.
`PivotFieldSubtotalType` numaralandırması, kullanılabilir alt toplam türlerini tanımlar.
- `AUTOMATIC` — Aspose.Cells varsayılan seçimi uygular (sayısal alanlar için genellikle `SUM`)
- `NONE` — tüm alt toplam satırlarını gizler
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
Alt toplamlar yalnızca satır bölgesinde (veya sütun bölgesinde) iki veya daha fazla özet tablo alanı bulunduğunda görüntülenir. Tek bir alan olduğunda alt toplam oluşturulabilecek anlamlı bir hiyerarşik ayrım bulunmaz. Bu nedenle `setSubtotals` çağrılarının bu durumda görünür bir etkisi olmaz. Bu makale, her örnekte iki satır alanı (`Category` dış, `Item` iç) yerleştirerek her `Category` grubunu ayıran alt toplam sınırının görünmesini sağlar.
{{% /alert %}}

## **Senaryo 1 — Otomatik (Varsayılan) Alt Toplamlar**
`setSubtotals` yöntemini hiç çağırmadığınızda Aspose.Cells, sayısal alanlar için `AUTOMATIC` seçimini uygular. Aşağıdaki örnek, dış `Category` satır alanında `setSubtotals(PivotFieldSubtotalType.AUTOMATIC, true)` çağırarak bu davranışı açıkça doğrular.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AUTOMATIC, true);
pivotTable.calculateData();
workbook.save("output_automatic.xlsx");
```

## **Senaryo 2 — Tüm Alt Toplamları Bastırma (Yok)**
`setSubtotals(PivotFieldSubtotalType.NONE, true)` çağrısı, özet tablosundaki tüm alt toplam satırlarını kaldırarak yalnızca alan satırlarını ve en alttaki genel toplamı bırakır. Özet satırları olmadan yalnızca gruplandırılmış ham verileri görüntülemek istediğinizde bu yöntem yararlıdır.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = worksheet.getPivotTables().add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.NONE, true);
pivotTable.calculateData();
workbook.save("output_none.xlsx");
```

## **Senaryo 3 — Özel Alt Toplam Alt Kümesi (Toplam + Ortalama)**
Tek bir alt toplam türüyle sınırlı değilsiniz. Her `setSubtotals` çağrısı yalnızca bir tür üzerinde bağımsız olarak etki gösterir. Bu nedenle yöntemi iki kez — sırasıyla `SUM` ve `AVERAGE` türleriyle — çağırdığınızda her `Category` grubu için iki alt toplam satırından oluşan özel bir alt küme elde edersiniz.

```javascript
const AsposeCells = require("aspose.cells");
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
let pivotTable = pivotTables.add("A1:D9", 2, 5);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Category");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Item");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Year");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Amount");
let categoryField = pivotTable.getRowFields().get(0);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.SUM, true);
categoryField.setSubtotals(AsposeCells.PivotFieldSubtotalType.AVERAGE, true);
pivotTable.calculateData();
workbook.save("output_custom.xlsx");
```

## **Özet**
Ü senaryo, tek bir noktada farklılık gösterir: `setSubtotals` çağrıları. Diğer tüm unsurlar — veri kümesi, alanlar ve bunların atan olduğu bölgeler — aynıdır, bu da düzenlerin doğrudan karşılaştırılabilir olmasını sağlar.
- **Alanların yerleştirilmesi.** `PivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, fieldName)` kaynağındaki bir sütunu bir bölgeye Taşır. Bir bölgede içinde, çağrıların sırası gösterim sırasını belirler, böylece ilk çağrı en dıştaki grubu oluşturur. Subtotal’lar, aynı bölgede iki veya daha fazla alanı gerektirir: tek bir alanla, gruplar arasında subtotal alınacak hiçbir şey bulunmaz.
- **Senaryo 1 — otomatik subtotal’lar.** `setSubtotals` çağrısının yapılmaması, seçeneği Excel’e bırakır, Excel bu durumda sayısal alanlara kendi varsayılan subtotal’ını uygular. `AsposeCells.PivotFieldSubtotalType.AUTOMATIC` ile `setSubtotals`’ın çağrılması, bu seçimi açıkça kaydeder; dolayısıyla seçimi örtük bırakmaz.
- **Senaryo 2 — subtotal yok.** `AsposeCells.PivotFieldSubtotalType.NONE` ile `setSubtotals`'ın çağrılması, varsayılan subtotal’ı kapatır; bu da pivot’un alanı satırlarını ve toplamı tuttururken, Excel’inkinin aksine araya ekleyeceği subtotal satırlarını düşürmesine neden olur.
- **Senaryo 3 — seçilmiş bir alt küme.** Her çağrı, tam olarak bir subtotal türünü değiştirir ve çağrılar birbirlerini sıfırlamak yerine birikir. Bu nedenle bir kez `AsposeCells.PivotFieldSubtotalType.SUM` ve bir kez `AsposeCells.PivotFieldSubtotalType.AVERAGE` ile çağrılması, her ikisinin de etkin kalmasına neden olur ve pivot, bir Toplam subtotal, bir Ortalama subtotal ve bir toplam rendered eder.

{{% alert color="primary" %}}
Subtotal’larla ilgili hiçbir şey, satır bölgesine özgü değildir. `PivotTable.ColumnFields`’tan alınan bir alanda aynı `setSubtotals` çağrıları, ayarların pivot alanı ait olduğu ve üzerinde durduğu eksenin değil, sütun ekseninde aynı üç düzeni üretir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablolarında Sayfa Alanları](/cells/tr/nodejs-java/add-page-field-in-pivot-table/)
- [Aspose.Cells for Node.js via Java Kullanılarak Özet Tablolarını Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)
- [Özet Tablolarına Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}