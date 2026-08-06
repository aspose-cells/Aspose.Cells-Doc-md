---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for .NET kullanarak bir pivot tabloda sayfa alanı düzenini nasıl kontrol edeceğinizi öğrenin; görüntüleme sırasını, kaydırma sayısını ve pivot tablonun üst kısmındaki sayfa alanlarının alan sırasını ayarlamayı içerir.
keywords: Aspose.Cells, .NET kütüphanesi, elektronik tablo, pivot tablo, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/net/change-page-field-layout/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Sayfa alanı bölgesinin — pivot tablonun üst kısmındaki filtre denetimleri şeridinin — düzenini; görüntüleme sırası, kaydırma sayısı ve alanların yeniden sıralanması dahil olmak üzere nasıl kontrol edileceğini gösterir.

{{% /alert %}}

## **Giriş**

Microsoft Excel'deki bir pivot tablo, tablonun satır/sütun/veri gövdesinin üzerinde bulunan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, açılır filtre denetimlerinden oluşan bir şerit (her sayfa alanı için bir tane) olarak işlenir ve son kullanıcıların pivot tabloyu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells bu bölgeyi `PivotTable.PageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl düzenlendiğini kontrol eden üç özellik sunar:

- `PivotTable.PageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut olanların *yanına* mı yoksa *altına* mı yerleştirileceğine karar verir.
- `PivotTable.PageFieldWrapCount`, kaydırmadan önce satır veya sütun başına kaç sayfa alanı yerleştirileceğini ayarlar.
- `PivotTable.PageFields.Move(currIndex, destIndex)`, sıra modunu değiştirmeden sayfa alanlarını yeniden sıralar.

Bu makale, ortak bir veri kümesi üzerinde bu üç işlemin her birini gösteren üç kod örneğini adım adım açıklar; böylece ortaya çıkan düzenleri yan yana karşılaştırabilirsiniz.

## **Kaynak Veri**

Aşağıdaki üç örnek de bu sekiz satırlık satış verisini `PivotData` adlı bir çalışma sayfasına yükler. Veri, iki sayfa alanı adayı (`Year`, `Region`), bir satır alanı adayı (`Fruit`) ve bir ölçü (`Amount`) içerir; bu da sayfa alanı şeridinin incelenmesini anlamlı kılar.

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

Sekiz satırın tamamı her kod örneğinde aynı sırada doldurulur; dolayısıyla kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklılık gösterir.

## **Örnek 1: Önce Yatay Sonra Dikey**

İlk senaryoda, iki sayfa alanını (`Year`, `Region`) pivot tablonun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Fruit` öğesini satır eksenine atıyoruz, `Year` öğesini sayfa ekseninde birinci ve `Region` öğesini ikinci sıraya yerleştiriyoruz (`AddFieldToArea` çağrılarının sırası başlangıç dizinini belirler), `Amount` (Sum) öğesini veri alanı olarak ekliyoruz ve ardından `PageFieldOrder` değerini `PrintOrderType.OverThenDown` ve `PageFieldWrapCount` değerini `2` olarak ayarlıyoruz. `OverThenDown` ve kaydırma sayısı 2 ile, iki sayfa alanı pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir; dolayısıyla şerit genişliği iki olan tek bir satır kaplar.

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

// Başlıklar (satır 0)
pivotDataCells[0, 0].PutValue("Fruit");
pivotDataCells[0, 1].PutValue("Year");
pivotDataCells[0, 2].PutValue("Region");
pivotDataCells[0, 3].PutValue("Amount");

// Satır 1: Elma, 2022, Kuzey, 150
pivotDataCells[1, 0].PutValue("Apple");
pivotDataCells[1, 1].PutValue(2022);
pivotDataCells[1, 2].PutValue("North");
pivotDataCells[1, 3].PutValue(150);

// Satır 2: Elma, 2023, Kuzey, 180
pivotDataCells[2, 0].PutValue("Apple");
pivotDataCells[2, 1].PutValue(2023);
pivotDataCells[2, 2].PutValue("North");
pivotDataCells[2, 3].PutValue(180);

// Satır 3: Muz, 2022, Güney, 120
pivotDataCells[3, 0].PutValue("Banana");
pivotDataCells[3, 1].PutValue(2022);
pivotDataCells[3, 2].PutValue("South");
pivotDataCells[3, 3].PutValue(120);

// Satır 4: Muz, 2023, Güney, 140
pivotDataCells[4, 0].PutValue("Banana");
pivotDataCells[4, 1].PutValue(2023);
pivotDataCells[4, 2].PutValue("South");
pivotDataCells[4, 3].PutValue(140);

// Satır 5: Kiraz, 2022, Doğu, 200
pivotDataCells[5, 0].PutValue("Cherry");
pivotDataCells[5, 1].PutValue(2022);
pivotDataCells[5, 2].PutValue("East");
pivotDataCells[5, 3].PutValue(200);

// Satır 6: Kiraz, 2023, Doğu, 220
pivotDataCells[6, 0].PutValue("Cherry");
pivotDataCells[6, 1].PutValue(2023);
pivotDataCells[6, 2].PutValue("East");
pivotDataCells[6, 3].PutValue(220);

// Satır 7: Üzüm, 2022, Batı, 90
pivotDataCells[7, 0].PutValue("Grape");
pivotDataCells[7, 1].PutValue(2022);
pivotDataCells[7, 2].PutValue("West");
pivotDataCells[7, 3].PutValue(90);

// Satır 8: Üzüm, 2023, Batı, 110
pivotDataCells[8, 0].PutValue("Grape");
pivotDataCells[8, 1].PutValue(2023);
pivotDataCells[8, 2].PutValue("West");
pivotDataCells[8, 3].PutValue(110);

// PivotTableReport sayfasını ekle
int pivotTableSheetIdx = worksheets.Add("PivotTableReport");
Worksheet pivotTableSheet = worksheets[pivotTableSheetIdx];
PivotTableCollection pivotTables = pivotTableSheet.PivotTables;

// PivotData!A1:D9 kaynağından PivotTableReport'ta A1'e yerleştirilen pivot tablo oluştur
int pivotIndex = pivotTables.Add("PivotData!A1:D9", "A1", "PivotTable1");
PivotTable pivotTable = pivotTables[pivotIndex];

// Alanları ekle
pivotTable.AddFieldToArea(PivotFieldType.Row, 0);   // Meyve
pivotTable.AddFieldToArea(PivotFieldType.Page, 1);  // Yıl
pivotTable.AddFieldToArea(PivotFieldType.Page, 2);  // Bölge
pivotTable.AddFieldToArea(PivotFieldType.Data, 3);  // Miktar
pivotTable.DataFields[0].Function = ConsolidationFunction.Sum;

// Sayfa alanı düzenini yapılandır: sayfa alanlarını önce yatay olarak yerleştir, her 2 alandan sonra alta geç
pivotTable.PageFieldOrder = PrintOrderType.OverThenDown;
pivotTable.PageFieldWrapCount = 2;

// Yenile ve hesapla
pivotTable.CalculateData();

// Kaydet
workbook.Save(Path.Combine(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Örnek 2: Önce Dikey Sonra Yatay**

Bu örnekte, `Fruit` öğesini satır eksenine, `Year` ve `Region` öğelerini sayfa eksenine (`Year` birinci sırada olacak şekilde) ve `Amount` (Sum) öğesini veri alanı olarak yerleştiriyoruz — tıpkı Örnek 1'de olduğu gibi. Ardından `PageFieldOrder` değerini `PrintOrderType.DownThenOver` ve `PageFieldWrapCount` değerini `2` olarak ayarlıyoruz. `DownThenOver` ve kaydırma sayısı 2 ile, iki sayfa alanı dikey olarak istiflenir — `Year` üstte, `Region` doğrudan altında — pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine, genişliği bir olan iki satır kaplar.

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

## **Örnek 3: Bir Sayfa Alanını Taşıma**

Üçüncü senaryoda bu veri kümesini ve alan atamasını koruyoruz, nötr bir düzen ayarlıyoruz (`OverThenDown` ve kaydırma sayısı `2`) ve ardından `PageFields.Move` işlemini gösteriyoruz. `Move(0, 1)` çağrısı, dizin 0'daki sayfa alanını (`Year`) 1 konumuna taşır ve 1 konumundaki sayfa alanı (`Region`) 0 konumuna kayar. Bu çağrıdan sonra `Region` ilk sayfa alanı, `Year` ise ikinci sayfa alanı olur. Kaydırma ve sıra modu değişmediğinden şerit hâlâ yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiş olur.

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

## **İlgili Makaleler**

- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/net/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan üst sayfa.
- [Pivot Tablosundaki Satır ve Sütun Alanları](/cells/tr/net/pivot-table-add-row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan, alanların satır ve sütun eksenlerine atanmasını ele alır.
- [Pivot Tablosundaki Değer Alanlarını Yönetme](/cells/tr/net/manage-value-fields/) — bu makalede kullanılan `Sum` toplaması dahil olmak üzere veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/net/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `RefreshData` ve `CalculateData` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/net/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="csharp" >}}