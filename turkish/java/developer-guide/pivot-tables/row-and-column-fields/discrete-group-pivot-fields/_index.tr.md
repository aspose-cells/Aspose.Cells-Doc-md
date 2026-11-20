---
title: Özet Alanı Öğelerinin Ayrık Gruplanması
linktitle: Ayrık Gruplanması
description: Aspose.Cells for Java kitaplığında DiscreteGroupItem ve PivotFieldGroupOptions.DiscreteGroupItems kullanarak özet alanı öğelerini meyve ve sebze gibi özel adlandırılmış gruplara nasıl gruplandıracağınızı öğrenin.
keywords: Aspose.Cells for Java, özet tablo, ayrık gruplama, DiscreteGroupItem, PivotFieldGroupOptions, özet alanı öğelerini gruplandırma, özel gruplar, PivotField.group, Java, Excel özet tablo
type: docs
weight: 90
url: /tr/java/discrete-group-pivot-fields/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplama, öğeleri veri türüne göre gruplar; örneğin tarihleri aylara ve çeyreklere, sayıları ise aralıklara göre gruplar. Ayrık gruplama ise bunun tersini gerçekleştirir: belirli ve birbiriyle ilişkisiz öğeleri özel adlandırılmış gruplarda toplar. Örneğin ürünleri meyve ve sebze gruplarına, mağazaları bölgelere veya hesapları bölümlere gruplar. Aspose.Cells, ayrık gruplamayı `DiscreteGroupItem` sınıfı ve `PivotFieldGroupOptions.getDiscreteGroupItems()` özelliği aracılığıyla sunar.
- `DiscreteGroupItem`, bir grup adı ve o gruba ait öğelerden oluşur. Öğeler iki şekilde belirlenebilir: adlarıyla (`new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" })`) veya kaynak verideki sıfırdan başlayan konumlarıyla (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Her iki biçim de aynı sonucu verir.
- Ayrık gruplama, seçenekler `PivotField.group(PivotFieldGroupOptions)` çağrısına aktarılarak özet tablonun satır veya sütun alanında yer alan bir alana uygulanır.

## **Öğe Adlarına Göre Özet Alanı Öğelerini Gruplama**
Bu örnekte küçük bir satış listesi (ürün, tarih ve tutar) oluşturulur ve bu listeden, `product` alanı satır alanında, `date` alanı sütun alanında ve `amount` alanı veri alanında bulunan bir özet tablo oluşturulur. Ardından öğe adlarına göre iki özel grup tanımlanır: meyve (üzüm, kiraz) ve sebzeler (havuç, patates). Sonuç iki düzeyli bir satır düzenidir: dış düzeyde grup adı, altında ise orijinal öğeler bulunur. Böylece eğilimlerin özel grup ve öğe bazında okunması sağlanır.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) cells.get(r, 1).setStyle(dateStyle);
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new String[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new String[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotField.xlsx");
```

`calculateData()` çağrısından sonra özet tablonun satır alanında meyve (üzüm 50, kiraz 80) ve sebze (havuç 60, patates 70) grupları, ayrıca genel toplam 260 görülür. Sütun etiketlerinde dört tarih (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) korunur.

## **Öğe İndekslerine Göre Özet Alanı Öğelerini Gruplama**
Öğe adları uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci oluşturucusu öğeleri indekse göre belirler. İndeksler, öğelerin kaynak veride göründükleri sıraya göre sıfırdan başlayan konumlarıdır; alfabetik sıra değildir. Yukarıdaki örnek veride üzüm 0, havuç 1, patates 2 ve kiraz 3 numaralı öğedir; dolayısıyla meyve `{ 0, 3 }`, sebze ise `{ 1, 2 }` olur. Sonuç, ada dayalı örnekle birebir aynıdır.

```java
import com.aspose.cells.*;
Workbook wb = new Workbook();
Worksheet sheet = wb.getWorksheets().get(0);
Cells cells = sheet.getCells();
cells.get(0, 0).putValue("product");
cells.get(1, 0).putValue("grape");
cells.get(2, 0).putValue("carrot");
cells.get(3, 0).putValue("potato");
cells.get(4, 0).putValue("cherry");
Style dateStyle = wb.createStyle();
dateStyle.setCustom("m/d/yyyy");
cells.get(0, 1).putValue("date");
cells.get(1, 1).putValue(new DateTime(2021, 2, 5));
cells.get(2, 1).putValue(new DateTime(2022, 3, 8));
cells.get(3, 1).putValue(new DateTime(2023, 4, 10));
cells.get(4, 1).putValue(new DateTime(2024, 5, 16));
for (int r = 1; r <= 4; r++) {
    cells.get(r, 1).setStyle(dateStyle);
}
cells.get(0, 2).putValue("amount");
cells.get(1, 2).putValue(50);
cells.get(2, 2).putValue(60);
cells.get(3, 2).putValue(70);
cells.get(4, 2).putValue(80);
PivotTable pivotTable = sheet.getPivotTables().add("=Sheet1!A1:C5", 11, 0);
pivotTable.addFieldToArea(PivotFieldType.ROW, "product");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "date");
pivotTable.addFieldToArea(PivotFieldType.DATA, "amount");
pivotTable.setPivotTableStyleType(PivotTableStyleType.PIVOT_TABLE_STYLE_MEDIUM_10);
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.setDiscreteGroupItems(new DiscreteGroupItem[] { fruit, vegetable });
pivotTable.getRowFields().get(0).group(groupOptions);
pivotTable.calculateData();
wb.save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- Herhangi bir özel gruba atanmayan öğeler kaybolmaz. Bu öğeler, özel gruplarla aynı düzeyde özet tablo içinde kalır ve her biri tek öğeden oluşan ayrı bir giriş olarak yer alır. Yukarıdaki örnekte yalnızca meyve grubu tanımlanırsa havuç ve patates, meyve grubunun yanında ayrı girişler olarak satır alanında kalır.
- `PivotFieldGroupOptions.getNewPivotField()` özelliği ayrık gruplama düzenini kontrol eder. Varsayılan değeri `true` olduğundan gruplandırılmış alan, orijinal alanın yanında yeni bir dış alan olarak eklenir ve yukarıda gösterilen iki düzeyli düzeni oluşturur (`getRowFields()` çağrısı artık 2 alan döndürür). Orijinal alanın yerine geçmesi için `setNewPivotField(false)` kullanılarak bu özellik `false` olarak ayarlanır. Bu durumda satır alanı, yalnızca grup adlarını ve toplulaştırılmış değerlerini içeren tek düzeyli bir düzen gösterir: meyve 130 (50 + 80) ve sebze 130 (60 + 70).
- `DiscreteGroupItem` sınıfının ada dayalı ve indekse dayalı oluşturucuları, aynı `getDiscreteGroupItems()` dizisi içinde birlikte kullanılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosunda Özet Alanlarını Gruplama](/cells/tr/java/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/java/pivot-table-add-row-and-column-fields/)
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/java/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/java/apply-style-to-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/java/refresh-pivot-table/)

{{< app/cells/assistant language="java" >}}