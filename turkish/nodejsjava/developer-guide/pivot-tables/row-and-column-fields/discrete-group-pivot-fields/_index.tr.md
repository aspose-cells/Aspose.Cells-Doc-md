---
title: Pivot Alanı Öğelerinin Ayrık Gruplanması
linktitle: Ayrık Gruplanması
description: Aspose.Cells for Node.js via Java kullanılarak DiscreteGroupItem ve PivotFieldGroupOptions.getDiscreteGroupItems() ile özet tablosundaki alan öğelerinin meyve ve sebze gibi özel adlı gruplara nasıl gruplanacağını öğrenin.
keywords: Aspose.Cells, özet tablo, ayrık gruplama, DiscreteGroupItem, PivotFieldGroupOptions, özet tablosu öğelerini gruplama, özel gruplar, PivotField.group, Aspose.Cells for Node.js via Java, Excel özet tablo
type: docs
weight: 90
url: /tr/nodejs-java/discrete-group-pivot-fields/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplama, öğeleri veri türüne göre toplar; örneğin tarihleri aylara ve çeyreklere, sayıları da aralıklara göre gruplar. Ayrık gruplama ise ters bir sorunu çözer: belirli ve birbiriyle ilgisiz öğeleri özel adlı gruplarda toplar. Örneğin ürünler meyve ve sebze adlı gruplara, mağazalar bölgelere veya hesaplar bölümlere göre gruplanabilir. Aspose.Cells, ayrık gruplamayı `DiscreteGroupItem` sınıfı ve `PivotFieldGroupOptions.getDiscreteGroupItems()` özelliği aracılığıyla sağlar.
- Bir `DiscreteGroupItem`, bir grup adından ve o gruba ait öğelerden oluşur. Öğeler iki şekilde belirlenebilir: adlarıyla (`new DiscreteGroupItem("fruit", ["grape", "cherry"])`) veya kaynak verideki sıfırdan başlayan konumlarıyla (`new DiscreteGroupItem("fruit", [0, 3])`). Her iki biçim de aynı sonucu üretir.
- Ayrık gruplama, seçenekler `PivotField.group(PivotFieldGroupOptions)` çağrısında belirtilerek özet tablosunda satır veya sütun alanı olarak yerleştirilen alanlara uygulanır.

## **Pivot Alanı Öğelerini Öğe Adlarına Göre Gruplama**
Aşağıdaki örnek, küçük bir satış listesi (ürün, tarih ve tutar) oluşturur. Bu listeden, `product` alanının satır alanına, `date` alanının sütun alanına ve `amount` alanının veri alanına yerleştirildiği bir özet tablo oluşturur ve ardından öğe adlarına göre iki özel grup tanımlar: meyve (üzüm, kiraz) ve sebze (havuç, patates). Sonuç, grup adının dış düzeyde, özgün öğelerin ise altında iç içe yer aldığı iki düzeyli bir satır düzenidir. Böylece eğilimler özel grup ve öğe bazında incelenebilir.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(44232);
cells.get(2, 1).putValue(44628);
cells.get(3, 1).putValue(45026);
cells.get(4, 1).putValue(45428);
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
pivotTable.calculateData();
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

`calculateData()` çağrısından sonra özet tablosunun satır alanında meyve (üzüm 50, kiraz 80) ve sebze (havuç 60, patates 70) görünür. Genel toplam 260'dır; sütun etiketlerinde ise dört tarih (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) korunur.

## **Pivot Alanı Öğelerini Öğe İndekslerine Göre Gruplama**
Öğe adları uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci kurucusu öğeleri indekslerle tanımlar. İndeksler, öğelerin kaynak veride göründükleri sıraya göre sıfırdan başlayan konumlarıdır; alfabetik sıralama değildir. Yukarıdaki örnek veride üzüm 0, havuç 1, patates 2 ve kiraz 3 numaralı öğedir; dolayısıyla meyve grubu `{ 0, 3 }`, sebze grubu ise `{ 1, 2 }` olarak tanımlanır. Sonuç, ada dayalı örnektekiyle aynıdır.

```javascript
const AsposeCells = require("aspose.cells");
const java = require("java");
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
// Use Excel serial dates because JavaScript Date objects cannot be passed through the bridge.
cells.get(1, 1).putValue(44232); // 2021-02-05
cells.get(2, 1).putValue(44628); // 2022-03-08
cells.get(3, 1).putValue(45026); // 2023-04-10
cells.get(4, 1).putValue(45428); // 2024-05-16
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0).
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(
    AsposeCells.PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10
);
// Calculate the pivot table before grouping.
pivotTable.calculateData();
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data).
// The Node.js bridge requires item names rather than the index-based constructor.
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
const groups = java.newArray("com.aspose.cells.DiscreteGroupItem", [fruit, vegetable]);
groupOptions.setDiscreteGroupItems(groups);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- Herhangi bir özel gruba atanmayan öğeler kaybolmaz. Bunlar özet tablosunda özel gruplarla aynı düzeyde, her biri tek öğelik bir kayıt olarak kalır. Yukarıdaki örnekte yalnızca meyve grubu tanımlanırsa havuç ve patates, meyve grubunun yanında bağımsız kayıtlar olarak satır alanında kalır.
- `PivotFieldGroupOptions.getNewPivotField()` özelliği, ayrık gruplamanın düzenini denetler. Varsayılan değeri `true` olup gruplanmış alanı özgün alanın yanında yeni bir dış alan olarak ekleyerek yukarıda gösterilen iki düzeyli düzeni oluşturur (`getRowFields()` 2'ye çıkar). `PivotFieldGroupOptions.setNewPivotField(false)` kullanıldığında gruplanmış alan özgün alanın yerini alır; böylece satır alanı, yalnızca grup adlarını ve toplulaştırılmış değerlerini içeren tek düzeyli bir yapıya dönüşür: meyve 130 (50 + 80) ve sebze 130 (60 + 70).
- `DiscreteGroupItem` sınıfının ada dayalı ve indeks dayalı kurucuları aynı `getDiscreteGroupItems()` dizisi içinde birlikte kullanılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosunda Pivot Alanlarını Gruplama](/cells/tr/nodejs-java/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-java/pivot-table-add-row-and-column-fields/)
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-java" >}}