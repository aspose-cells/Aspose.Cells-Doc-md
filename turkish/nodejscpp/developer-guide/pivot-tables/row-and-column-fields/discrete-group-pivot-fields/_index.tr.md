---
title: Pivot Alan Öğelerinin Ayrık Gruplandırılması
linktitle: Ayrık Gruplandırılması
description: DiscreteGroupItem ve PivotFieldGroupOptions.DiscreteGroupItems kullanarak meyve ve sebze gibi özel adlandırılmış gruplara pivot alan öğelerini nasıl gruplayacağınızı öğrenin, Aspose.Cells for Node.js via C++ içinde.
keywords: Aspose.Cells, özet tablo, ayrık gruplama, DiscreteGroupItem, PivotFieldGroupOptions, özet tablo öğelerini grupla, özel gruplar, PivotField.Group, Node.js, Excel özet tablo
type: docs
weight: 90
url: /tr/nodejs-cpp/discrete-group-pivot-fields/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplama, tarihleri aylar ve çeyrekler gibi, sayıları aralıklar gibi veri tipine göre öğeleri toplar. Ayrık gruplama ise ters problemi çözer; belirli, ilişkili olmayan öğeleri özel adlandırılmış gruplara toplar; örneğin ürünleri meyve ve sebze gruplarına, mağazaları bölgelere veya hesapları bölgelere. Aspose.Cells for Node.js via C++ , `DiscreteGroupItem` sınıfı ve `PivotFieldGroupOptions.discreteGroupItems` özelliği aracılığıyla ayrık gruplama sağlar.
- `DiscreteGroupItem` bir grup adı ve ona ait öğelerdir. Öğeler iki şekilde tanımlanabilir, isimleriyle (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) ya da kaynak verideki sıfır‑tabanlı konumlarıyla (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Her iki biçim aynı sonucu üretir.
- Ayrık gruplama, pivot tablosunun satır veya sütun alanındaki bir alana, seçenekleri `pivotField.group(pivotFieldGroupOptions)` metoduna geçirerek uygulanır.

## **Öğe İsimlerine Göre Pivot Alan Öğelerini Gruplandırma**
Aşağıdaki örnek, küçük bir satış listesi (ürün, tarih ve tutar) oluşturur, `product` satır alanında, `date` sütun alanında ve `amount` veri alanında olacak şekilde bir özet tablo yaratır, ardından öğe isimlerine göre iki özel grup tanımlar: meyve (grape, cherry) ve sebzeler (carrot, potato). Sonuç, iki seviyeli bir satır düzeni gösterir; grup adı dış seviye, orijinal öğeler ise alt seviyede yer alır, böylece trendler her özel grup ve öğe başına okunabilir.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create a new workbook and get the first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Populate data
cells.get(0, 0).setValue("product");
cells.get(1, 0).setValue("grape");
cells.get(2, 0).setValue("carrot");
cells.get(3, 0).setValue("potato");
cells.get(4, 0).setValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Add date header and values
cells.get(0, 1).setValue("date");
cells.get(1, 1).setValue(new Date(2021, 1, 5));   // February is month 1
cells.get(2, 1).setValue(new Date(2022, 2, 8));
cells.get(3, 1).setValue(new Date(2023, 3, 10));
cells.get(4, 1).setValue(new Date(2024, 4, 16));
// Apply date style to the date column
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Add amount header and values
cells.get(0, 2).setValue("amount");
cells.get(1, 2).setValue(50);
cells.get(2, 2).setValue(60);
cells.get(3, 2).setValue(70);
cells.get(4, 2).setValue(80);
// Add a pivot table at cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// Group specific items into custom groups by item names
const fruit = new AsposeCells.DiscreteGroupItem("fruit", ["grape", "cherry"]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", ["carrot", "potato"]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
// Calculate pivot data and save the workbook
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

`calculateData()` işleminden sonra pivot tablonun satır alanı, meyve (grape 50, cherry 80) ve sebze (carrot 60, potato 70) öğelerini toplam 260 ile gösterir ve sütun etiketleri dört tarihi (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) korur.

## **Öğe İndekslerine Göre Pivot Alan Öğelerini Gruplandırma**
Öğe isimleri uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci yapıcı yöntemi öğeleri indeksle tanımlar. İndeksler, öğelerin kaynak veride görüldüğü sıradaki sıfır‑tabanlı konumlarıdır, alfabetik sıraya göre değil. Yukarıdaki örnek veride üzüm öğe 0, havuç öğe 1, patates öğe 2 ve kiraz öğe 3 olduğundan, meyve `{ 0, 3 }` ve sebze `{ 1, 2 }` şeklindedir. Sonuç, isim‑bazlı örnekle aynıdır.

```javascript
const AsposeCells = require("aspose.cells.node");
// Create workbook and get first worksheet
const wb = new AsposeCells.Workbook();
const sheet = wb.getWorksheets().get(0);
const cells = sheet.getCells();
// Fill data
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
// Create a date style
const dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
// Date column header
cells.get(0, 1).putValue("date");
// Date values
cells.get(1, 1).putValue(new Date(2021, 1, 5));   // Feb 5, 2021
cells.get(2, 1).putValue(new Date(2022, 2, 8));   // Mar 8, 2022
cells.get(3, 1).putValue(new Date(2023, 3, 10));  // Apr 10, 2023
cells.get(4, 1).putValue(new Date(2024, 4, 16));  // May 16, 2024
// Apply date style to date cells
for (let r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
// Amount column header and values
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
const pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "product");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "date");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "amount");
pivotTable.setPivotTableStyleType(AsposeCells.PivotTableStyleType.PivotTableStyleMedium10);
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
const fruit = new AsposeCells.DiscreteGroupItem("fruit", [0, 3]);
const vegetable = new AsposeCells.DiscreteGroupItem("vegetable", [1, 2]);
const groupOptions = new AsposeCells.PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems([fruit, vegetable]);
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
// Save the workbook
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- Herhangi bir özel gruba atanamayan öğeler kaybolmaz. Özel gruplarla aynı seviyede pivot tabloda kalırlar ve her biri tek öğeli bir giriş olarak bulunur. Yukarıdaki örnekte yalnızca meyve grubu tanımlandığında, havuç ve patates satır alanında meyve grubunun yanında bağımsız girişler olarak kalır.
- `PivotFieldGroupOptions.newPivotField` özelliği, ayrık gruplamanın düzenini kontrol eder. Varsayılan olarak true değerindedir; bu, gruplandırılan alanı orijinal alanın yanına yeni bir dış alan olarak ekler ve yukarıda gösterilen iki‑seviyeli düzeni oluşturur (`rowFields` 2’ye çıkar). False olarak ayarlandığında ise orijinal alanı değiştirir; satır alanı yalnızca grup adlarını ve bunların toplam değerlerini içeren tek bir seviye gösterir; meyve 130 (50 + 80) ve sebze 130 (60 + 70).
- `DiscreteGroupItem` sınıfının isim‑bazlı ve indeks‑bazlı yapıcıları aynı `PivotFieldGroupOptions.discreteGroupItems` dizisi içinde karıştırılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Pivot Tablosunda Pivot Alanlarını Gruplama](/cells/tr/nodejs-cpp/group-pivot-fields-in-the-pivot-table/)
- [Pivot Tablosunda Satır ve Sütun Alanları Ekleme](/cells/tr/nodejs-cpp/pivot-table-add-row-and-column-fields/)
- [Pivot Tablosunu Etiket veya Değere Göre Filtreleme](/cells/tr/nodejs-cpp/filter-by-label-or-value-of-pivot-table/)
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/)
- [Pivot Tablosunu Yenile](/cells/tr/nodejs-cpp/refresh-pivot-table/)

{{< app/cells/assistant language="nodejs-cpp" >}}