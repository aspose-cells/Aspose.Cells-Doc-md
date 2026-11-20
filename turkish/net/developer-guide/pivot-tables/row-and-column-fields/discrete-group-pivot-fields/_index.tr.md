---
title: Pivot Alanı Öğelerinin Ayrık Gruplanması
linktitle: Ayrık Gruplanması
description: Aspose.Cells for .NET içinde DiscreteGroupItem ve PivotFieldGroupOptions.DiscreteGroupItems kullanılarak pivot alanı öğelerinin meyve ve sebze gibi özel adlı gruplar halinde nasıl gruplandırılacağını öğrenin.
keywords: Aspose.Cells, özet tablo, ayrık gruplama, DiscreteGroupItem, PivotFieldGroupOptions, pivot öğelerini gruplama, özel gruplar, PivotField.Group, C#, Excel özet tablo
type: docs
weight: 90
url: /tr/net/discrete-group-pivot-fields/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
- Otomatik gruplama, öğeleri veri türüne göre gruplar; örneğin tarihleri aylara ve çeyreklere, sayıları ise aralıklara gruplar. Ayrık gruplama ise otomatik gruplamanın aksine, belirli, birbirinden ilişkisiz öğeleri özel adlı gruplar halinde toplar; örneğin ürünleri meyve ve sebzelere, mağazaları bölgelere veya hesapları alanlara ayırır. Aspose.Cells, ayrık gruplama desteğini `DiscreteGroupItem` sınıfı ve `PivotFieldGroupOptions.DiscreteGroupItems` özelliği aracılığıyla sağlar.
- `DiscreteGroupItem`, bir grup adı ve ona ait öğelerden oluşur. Öğeler iki şekilde belirlenebilir: adlarıyla (`new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" })`) veya kaynak verideki sıfır tabanlı konumlarıyla (`new DiscreteGroupItem("fruit", new int[] { 0, 3 })`). Her iki biçim de aynı sonucu verir.
- Ayrık gruplama, seçenekler `PivotField.Group(PivotFieldGroupOptions)` yöntemine geçirilerek özet tablosunun satır veya sütun alanında bulunan bir alana uygulanır.

## **Pivot Alanı Öğelerini Öğe Adlarına Göre Gruplama**
Aşağıdaki örnek, küçük bir satış listesi (ürün, tarih ve tutar) oluşturur ve bu listeden, `product` alanını satır alanına, `date` alanını sütun alanına ve `amount` alanını veri alanına yerleştiren bir özet tablosu oluşturur. Ardından öğe adlarına göre iki özel grup tanımlar: meyve (üzüm, kiraz) ve sebzeler (havuç, patates). Sonuç, grup adının dış düzeyde yer aldığı, özgün öğelerin ise bu düzeyin altında iç içe gösterildiği iki düzeyli bir satır düzenidir; böylece eğilimler özel grup ve öğe bazında okunabilir.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// Group specific items into custom groups by item names
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new string[] { "grape", "cherry" });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new string[] { "carrot", "potato" });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotField.xlsx");
```

`CalculateData()` çağrısından sonra özet tablosunun satır alanında meyve (üzüm 50, kiraz 80) ve sebze (havuç 60, patates 70) görünür; genel toplam 260'dır. Sütun etiketlerinde ise dört tarih (2/5/2021, 3/8/2022, 4/10/2023, 5/16/2024) yer alır.

## **Pivot Alanı Öğelerini Öğe İndekslerine Göre Gruplama**
Öğe adları uzun veya yerelleştirilmiş olduğunda, `DiscreteGroupItem` sınıfının ikinci kurucusu öğeleri indeksle tanımlar. İndeksler, öğelerin kaynak veride göründükleri sıradaki sıfır tabanlı konumlarıdır; alfabetik sırayı yansıtmaz. Yukarıdaki örnekteki veride üzüm 0, havuç 1, patates 2 ve kiraz 3 numaralı öğelerdir; dolayısıyla meyve `{ 0, 3 }`, sebze ise `{ 1, 2 }` olur. Sonuç, ada dayalı örnekle birebir aynıdır.

```csharp
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook wb = new Workbook();
Worksheet sheet = wb.Worksheets[0];
Cells cells = sheet.Cells;
cells[0, 0].Value = "product";
cells[1, 0].Value = "grape";
cells[2, 0].Value = "carrot";
cells[3, 0].Value = "potato";
cells[4, 0].Value = "cherry";
Style dateStyle = wb.CreateStyle();
dateStyle.Custom = "m/d/yyyy";
cells[0, 1].Value = "date";
cells[1, 1].Value = new DateTime(2021, 2, 5);
cells[2, 1].Value = new DateTime(2022, 3, 8);
cells[3, 1].Value = new DateTime(2023, 4, 10);
cells[4, 1].Value = new DateTime(2024, 5, 16);
for (int r = 1; r <= 4; r++) cells[r, 1].SetStyle(dateStyle);
cells[0, 2].Value = "amount";
cells[1, 2].Value = 50;
cells[2, 2].Value = 60;
cells[3, 2].Value = 70;
cells[4, 2].Value = 80;
// Add a pivot table with the destination cell A12 (row 11, column 0)
PivotTable pivotTable = sheet.PivotTables.Add("=Sheet1!A1:C5", 11, 0);
pivotTable.AddFieldToArea(PivotFieldType.Row, "product");
pivotTable.AddFieldToArea(PivotFieldType.Column, "date");
pivotTable.AddFieldToArea(PivotFieldType.Data, "amount");
pivotTable.PivotTableStyleType = PivotTableStyleType.PivotTableStyleMedium10;
// grape is item 0, carrot is item 1, potato is item 2, cherry is item 3
// (zero-based positions in the order the items appear in the source data)
DiscreteGroupItem fruit = new DiscreteGroupItem("fruit", new int[] { 0, 3 });
DiscreteGroupItem vegetable = new DiscreteGroupItem("vegetable", new int[] { 1, 2 });
PivotFieldGroupOptions groupOptions = new PivotFieldGroupOptions();
groupOptions.DiscreteGroupItems = new DiscreteGroupItem[] { fruit, vegetable };
pivotTable.RowFields[0].Group(groupOptions);
pivotTable.CalculateData();
wb.Save("outputDiscreteGroupPivotFieldByIndex.xlsx");
```

## **Not**

{{% alert color="primary" %}}
- Hiçbir özel gruba atanmayan öğeler kaybolmaz. Özel gruplarla aynı düzeyde kalırlar ve her biri özet tablosunda kendi tek öğelik girdisi olarak yer alır. Yukarıdaki örnekte yalnızca meyve grubu tanımlanırsa havuç ve patates, meyve grubunun yanında bağımsız girdiler olarak satır alanında kalır.
- `PivotFieldGroupOptions.NewPivotField` özelliği, ayrık gruplamanın düzenini belirler. Varsayılan değeri true olan bu özellik, gruplanan alanı özgün alanın yanında yeni bir dış alan olarak ekler ve yukarıdaki iki düzeyli düzeni oluşturur (`RowFields` 2'ye büyür). Özgün alanın değiştirilmesini sağlamak için değeri false olarak ayarlayın; bu durumda satır alanı, yalnızca grup adlarını ve toplanan değerlerini içeren tek düzeyli bir düzen gösterir: meyve 130 (50 + 80) ve sebze 130 (60 + 70).
- `DiscreteGroupItem` sınıfının ada dayalı ve indeks tabanlı kurucuları aynı `DiscreteGroupItems` dizisi içinde birlikte kullanılabilir.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablosunda Pivot Alanlarını Gruplama](/cells/tr/net/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekleme](/cells/tr/net/pivot-table-add-row-and-column-fields/)
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/net/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/)
- [Özet Tablosunu Yenileme](/cells/tr/net/refresh-pivot-table/)

{{< app/cells/assistant language="csharp" >}}