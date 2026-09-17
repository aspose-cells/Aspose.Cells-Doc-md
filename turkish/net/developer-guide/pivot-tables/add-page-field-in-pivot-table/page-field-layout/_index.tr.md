---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for .NET kullanarak bir pivot tabloda sayfa alanı düzenini kontrol etmeyi, görüntüleme sırasını, kaydırma sayısını ve pivot tablonun üst kısmındaki sayfa alanlarının alan sırasını ayarlamayı öğrenin.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, pivot tablo, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Pivot tablonun üst kısmındaki filtre denetimleri şeridi olan sayfa alanı düzeninin nasıl kontrol edileceğini, görüntüleme sırası, kaydırma sayısı ve alanların yeniden sıralanması dahil olmak üzere gösterir.
{{% /alert %}}

## **Introduction**
Microsoft Excel'deki bir pivot tablo, tablonun satır/sütun/veri gövdesinin üzerinde yer alan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, her sayfa alanı için bir tane olmak üzere açılır filtre denetimlerinden oluşan bir şerit olarak işlenir ve son kullanıcıların pivotu yıl veya bölge gibi ölçütlerle dilimlemek için tıkladığı yerdir. Aspose.Cells bu bölgeyi `PivotTable.PageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl düzenleneceğini kontrol eden üç özellik sunar:
- `PivotTable.PageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut olanların *yanına* mı yoksa *altına* mı yerleştirileceğine karar verir.
- `PivotTable.PageFieldWrapCount`, kaydırmadan önce satır veya sütun başına yerleştirilecek sayfa alanı sayısını ayarlar.
- `PivotTable.PageFields.Move(currIndex, destIndex)`, sıra modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, her bir işlemi paylaşılan bir veri kümesi üzerinde gösteren ve sonuçtaki düzenleri yan yana karşılaştırabilmenizi sağlayan üç kod örneğini ele alır.

## **Source Data**
| Fruit  | Year | Region | Amount |
|--------|------|--------|--------|
| Apple  | 2022 | North  | 150    |
| Apple  | 2023 | North  | 180    |
| Banana | 2022 | South  | 120    |
| Banana | 2023 | South  | 140    |
| Cherry | 2022 | East   | 200    |
| Cherry | 2023 | East   | 220    |
| Grape  | 2022 | West   | 90     |
| Grape  | 2023 | West   | 110    |
Tüm sekiz satır her kod örneğinde, aynı sırada doldurulur; böylece kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklılık gösterir.

## **Example 1: Over Then Down**
İlk senaryoda, iki sayfa alanını (`Year`, `Region`) pivot tablonun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Fruit` öğesini satır eksenine atıyoruz, `Year` ve `Region` öğelerini sayfa eksenine ilk sırada `Year` ve ikinci sırada `Region` olacak şekilde yerleştiriyoruz (`AddFieldToArea` çağrılarının sırası başlangıç dizinini belirler), `Amount` (Sum) öğesini veri alanı olarak ekliyoruz ve ardından `PageFieldOrder` öğesini `PrintOrderType.OverThenDown`, `PageFieldWrapCount` öğesini ise `2` olarak ayarlıyoruz. `OverThenDown` ve 2'lik bir kaydırma sayısı ile, iki sayfa alanı pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir; böylece şerit iki genişliğinde bir satır kaplar.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
string dataDir = "output";
if (!Directory.Exists(dataDir)) Directory.CreateDirectory(dataDir);
Workbook workbook = new Workbook();
WorksheetCollection worksheets = workbook.Worksheets;
int pivotDataIdx = worksheets.Add("PivotData");
Worksheet pivotDataSheet = worksheets[pivotDataIdx];
Cells pivotDataCells = pivotDataSheet.Cells;
// Headers (row 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");
// Row 1: Apple, 2022, North, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);
// Row 2: Apple, 2023, North, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);
// Row 3: Banana, 2022, South, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);
// Row 4: Banana, 2023, South, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);
// Row 5: Cherry, 2022, East, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);
// Row 6: Cherry, 2023, East, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);
// Row 7: Grape, 2022, West, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);
// Row 8: Grape, 2023, West, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);
// Add PivotTableReport sheet
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;
// Create pivot table sourced from PivotData!A1:D9 placed at A1 on PivotTableReport
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];
// Add fields
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Fruit
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Year
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Region
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Amount
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;
// Configure page field area layout: place page fields across first, wrap after every 2
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;
// Refresh and calculate
pivotTable.CalculateData();
// Save
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Example 2: Down Then Over**
Bu örnekte, Örnek 1'deki gibi `Fruit` öğesini satır eksenine, `Year` ve `Region` öğelerini sayfa eksenine (önce `Year`), `Amount` (Sum) öğesini ise veri alanı olarak yerleştiriyoruz. Ardından `PageFieldOrder` öğesini `PrintOrderType.DownThenOver` ve `PageFieldWrapCount` öğesini `2` olarak ayarlıyoruz. `DownThenOver` ve 2'lik bir kaydırma sayısı ile, iki sayfa alanı dikey olarak istiflenir — üstte `Year`, doğrudan altında `Region` — ve pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine, bir genişliğinde iki satır kaplar.

```csharp
using System;
using System.IO;
using Aspose.Cells;
using Aspose.Cells.Pivot;
var workbook = new Workbook();
var pivotData = workbook.Worksheets[0];
pivotData.Name = "PivotData";
int pivotReportIdx = workbook.Worksheets.Add("PivotTableReport");
var pivotReport = workbook.Worksheets[pivotReportIdx];
var headers = new[] { "Fruit", "Year", "Region", "Amount" };
for (int c = 0; c < headers.Length; c++)
{
    pivotData.Cells[0, c].PutValue(headers[c]);
}
var data = new object[,]
{
    {"Apple", 2022, "North", 150},
    {"Apple", 2023, "North", 180},
    {"Banana", 2022, "South", 120},
    {"Banana", 2023, "South", 140},
    {"Cherry", 2022, "East", 200},
    {"Cherry", 2023, "East", 220},
    {"Grape", 2022, "West", 90},
    {"Grape", 2023, "West", 110}
};
for (int r = 0; r < data.GetLength(0); r++)
{
    for (int c = 0; c < data.GetLength(1); c++)
    {
        pivotData.Cells[r + 1, c].PutValue(data[r, c]);
    }
}
int idx = pivotReport.PivotTables.Add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.PivotTables[idx];
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);
pivotTable.PageFieldOrder = PrintOrderType.DownThenOver;
pivotTable.PageFieldWrapCount = 2;
pivotTable.CalculateData();
workbook.Save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**
Üçüncü senaryoda bu veri kümesini ve alan tahsisini koruyoruz, nötr bir düzen (`OverThenDown` ve kaydırma sayısı `2`) ayarlıyoruz ve ardından `PageFields.Move` işlemini gösteriyoruz. `Move(0, 1)` çağrısı, 0 dizinindeki sayfa alanını (`Year`) 1 konumuna taşır ve 1 konumundaki sayfa alanı (`Region`) 0 konumuna kayar. Bu çağrıdan sonra `Region` ilk sayfa alanı, `Year` ise ikinci sayfa alanı olur. Kaydırma ve sıra modu değişmediğinden, şerit yine yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiştir.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet dataSheet = workbook.Worksheets[0];
dataSheet.Name = "PivotData";
dataSheet.Cells["A1"].PutValue("Fruit");
dataSheet.Cells["B1"].PutValue("Year");
dataSheet.Cells["C1"].PutValue("Region");
dataSheet.Cells["D1"].PutValue("Amount");
dataSheet.Cells["A2"].PutValue("Apple");
dataSheet.Cells["B2"].PutValue(2022);
dataSheet.Cells["C2"].PutValue("North");
dataSheet.Cells["D2"].PutValue(150);
dataSheet.Cells["A3"].PutValue("Apple");
dataSheet.Cells["B3"].PutValue(2023);
dataSheet.Cells["C3"].PutValue("North");
dataSheet.Cells["D3"].PutValue(180);
dataSheet.Cells["A4"].PutValue("Banana");
dataSheet.Cells["B4"].PutValue(2022);
dataSheet.Cells["C4"].PutValue("South");
dataSheet.Cells["D4"].PutValue(120);
dataSheet.Cells["A5"].PutValue("Banana");
dataSheet.Cells["B5"].PutValue(2023);
dataSheet.Cells["C5"].PutValue("South");
dataSheet.Cells["D5"].PutValue(140);
dataSheet.Cells["A6"].PutValue("Cherry");
dataSheet.Cells["B6"].PutValue(2022);
dataSheet.Cells["C6"].PutValue("East");
dataSheet.Cells["D6"].PutValue(200);
dataSheet.Cells["A7"].PutValue("Cherry");
dataSheet.Cells["B7"].PutValue(2023);
dataSheet.Cells["C7"].PutValue("East");
dataSheet.Cells["D7"].PutValue(220);
dataSheet.Cells["A8"].PutValue("Grape");
dataSheet.Cells["B8"].PutValue(2022);
dataSheet.Cells["C8"].PutValue("West");
dataSheet.Cells["D8"].PutValue(90);
dataSheet.Cells["A9"].PutValue("Grape");
dataSheet.Cells["B9"].PutValue(2023);
dataSheet.Cells["C9"].PutValue("West");
dataSheet.Cells["D9"].PutValue(110);
int pivotSheetIdx = workbook.Worksheets.Add("PivotTableReport");
Worksheet pivotSheet = workbook.Worksheets[pivotSheetIdx];
int pivotIdx = pivotSheet.PivotTables.Add("PivotData!A1:D9", "A3", "PivotTable");
PivotTable pivotTable = pivotSheet.PivotTables[pivotIdx];
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;
pivotTable.PageFields.Move(0, 1);
pivotTable.CalculateData();
workbook.Save("pageFieldLayout_move.xlsx");
```

## **Related Articles**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/net/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan ana sayfa.
- [Pivot Tablosundaki Satır ve Sütun Alanları](/cells/tr/net/pivot-table-add-row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan, alanların satır ve sütun eksenlerine atanmasını kapsar.
- [Pivot Tablosundaki Değer Alanlarını Yönetme](/cells/tr/net/manage-value-fields/) — bu makalede kullanılan `Sum` toplama işlemi dahil, veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/net/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `RefreshData` ve `CalculateData` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="csharp" >}}