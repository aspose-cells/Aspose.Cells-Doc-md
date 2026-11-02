---
title: Özet Tablosunda İlk 10 Öğeyi Gösterme veya Filtreleme
linktitle: Özet Tablosunda İlk 10 Öğeyi Gösterme veya Filtreleme
description: Aspose.Cells for .Net kullanarak bir özet tablo alanında yalnızca en yüksek veya en düşük sıralı öğelerin nasıl gösterileceğini öğrenin. Bu makale; Excel 97-2003 için Top10AutoShow yöntemini, Top10AutoShowSettings ile seçenekleri okumayı ve Excel 2007-365 için FilterTop10 aracılığıyla İlk 10 filtresini ele alır.
keywords: Aspose.Cells, .NET, özet tablo, ilk 10, otomatik göster, Top10AutoShow, Top10AutoShowSettings, PivotFieldTop10AutoShowSettings, FilterTop10, PivotFilterType, PivotField, C#
type: docs
weight: 20
url: /tr/net/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alan onlarca öğe içerdiğinde okunması zor olabilir. İlk 10 raporu yalnızca en yüksek veya en düşük sıralı öğeleri korur; bu da sıralama raporlarının tam olarak ihtiyaç duyduğu özelliktir — "gelire göre ilk 5 ürün" veya "satış sayısına göre en alt 3 bölge" gibi. Aspose.Cells bunun için iki mekanizmayı destekler; bu mekanizmalar Microsoft Excel'in iki farklı nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `PivotField.Top10AutoShow()` yöntemi. Bu, doğrudan özet tablo alanında saklanan klasik "En üst/en alt N öğeyi göster" ayarıdır. Özgün özet tablo biçiminin bir parçası olduğu için eski ve yeni dahil her Excel sürümünde çalışır.
- **Excel 2007-365 İlk 10 Filtresi** — `PivotField.FilterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern İlk 10 değer filtresidir. Alana bağlı bir `PivotFilter` nesnesi olarak saklanır ve öğe sayısına ve yüzdeye dayalı sıralama seçenekleri sunar.

## **Excel 97-2003 Sürümünde İlk 10 Öğeyi Gösterme (Top10AutoShow)**
Klasik AutoShow, `PivotField.Top10AutoShow(bool isAutoShow, bool isTop, int count, int rankBy)` çağrısıyla yapılandırılır:
- `isAutoShow` — alan üzerindeki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isTop` — `true` olduğunda en yüksek sıralı öğeleri (Üst), `false` olduğunda en düşük sıralı öğeleri (Alt) korur.
- `count` — korunacak öğe sayısı; örneğin klasik bir İlk 10 raporu için 10.
- `rankBy` — öğeleri sıralayan **veri alanının** sıfırdan başlayan indeksi. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama bir değer alanına veya alanın kendisine göre belirlenebilir. Aşağıda bu iki doğal varyant gösterilmektedir.

### **Bir Değer Alanına Göre Sıralama**
Satır alanının öğelerini, Satışların Toplamı gibi sıradan bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur ve ardından satış değerlerine göre ilk 2 sporu gösterir. `rankBy` değeri 0'dır; çünkü "Satışların Toplamı" veri alanının indeksi 0'dır.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Show the top 2 items ranked by "Sum of Sales" (data field index 0)
sportField.Top10AutoShow(true, true, 2, 0);
pivotTable.CalculateData();
workbook.Save("output-top10-by-value-field.xlsx");
```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisine göre de sıralanabilir; bunun için `rankBy` değeri olarak -1 geçirin. Bu varyant için ek veri alanı gerekmez; alanın yalnızca satır (veya sütun) alanında bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 bu biçimin varsayılan değeri olduğundan `rankBy` özniteliği özet tablo XML'inden çıkarılır ve `Top10AutoShowSettings.RankBy` -1 değerini döndürür.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// Alanın kendisine göre sıralanan en alt 3 öğeyi göster (rankBy = -1)
sportField.Top10AutoShow(true, false, 3, -1);
pivotTable.CalculateData();
workbook.Save("output-top10-by-field-itself.xlsx");
```

## **Mevcut Seçenekleri Okuma (Top10AutoShowSettings)**
`PivotField.Top10AutoShowSettings` özelliği, alan üzerinde saklanan AutoShow seçeneklerini ortaya çıkaran bir `PivotFieldTop10AutoShowSettings` nesnesi döndürür. Mevcut bir çalışma kitabının veya yeni yapılandırdığınız bir özet tablonun öğelerinin nasıl gösterileceğini incelemek için bu özelliği kullanın; dosyadan yüklenen çalışma kitapları da kapsama dâhildir.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook("output-top10-by-value-field.xlsx");
PivotTable pivotTable = workbook.Worksheets[0].PivotTables[0];
PivotField sportField = pivotTable.RowFields[0];
PivotFieldTop10AutoShowSettings settings = sportField.Top10AutoShowSettings;
Console.WriteLine("AutoShow enabled: " + settings.IsAutoShow);
Console.WriteLine("Direction: " + (settings.IsTop ? "Top" : "Bottom"));
Console.WriteLine("Item count: " + settings.AutoShowCount);
Console.WriteLine("Ranking data field index: " + settings.RankBy);
```

Dört özellik, özet tablo XML'ine yazılan klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir; bu nedenle geri okunan değerler, her Excel sürümünün uygulayacağı değerlerdir.

## **Not**

{{% alert color="primary" %}}
- `PivotField` tarafından doğrudan sunulan `IsAutoShow`, `IsAscendShow`, `AutoShowCount` ve `AutoShowField` özellikleri kullanımdan kaldırılmış olarak işaretlenmiştir. Bunun yerine `Top10AutoShowSettings` nesnesini kullanın: `IsAutoShow` özelliği `Top10AutoShowSettings.IsAutoShow`, `IsAscendShow` özelliği `Top10AutoShowSettings.IsTop`, `AutoShowCount` özelliği `Top10AutoShowSettings.AutoShowCount` ve `AutoShowField` özelliği `Top10AutoShowSettings.RankBy` alanlarına karşılık gelir. `Top10AutoShow()` yöntemi, ayarları değiştirmek için desteklenen yöntemdir.
- `Top10AutoShow`, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan bu şekilde sıralanamaz; çünkü öğeleri özet tablonun gövdesinde yer almaz.
{{% /alert %}}

## **Excel 2007-365: İlk 10 Filtresi (FilterTop10)**
Modern Excel sürümlerinde, alan menüsündeki Değer Filtreleri bölümünde İlk 10 filtresi sunulur (Değer Filtreleri, İlk 10...). Aspose.Cells bunu, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.FilterTop10(int valueFieldIndex, PivotFilterType type, bool isTop, int itemCount)` yöntemiyle temsil eder:
- `valueFieldIndex` — öğelerin toplu değerlerine göre sıralandığı veri alanının sıfırdan başlayan indeksi.
- `type` — `itemCount` değerinin ne anlama geldiğini belirler. `PivotFilterType.Count` sabit sayıda öğe korur (iletişim kutusundaki Öğeler seçeneği). `PivotFilterType.Percent` öğelerin belirli bir yüzdesini korur; bu nedenle `itemCount` değerinin kendisi yüzdeyi belirtir — 30, öğelerin ilk yüzde 30'unu korur. `PivotFilterType.Sum` ise kümülatif değer kapsamına göre sıralama yapar.
- `isTop` — Üst için `true`, Alt için `false`.
- `itemCount` — İlk N ifadesindeki N değeri; birimi `type` değerine bağlıdır.

```csharp
using System;
using Aspose.Cells;
using Aspose.Cells.Pivot;
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
worksheet.Cells["A1"].PutValue("Sport");
worksheet.Cells["B1"].PutValue("Quarter");
worksheet.Cells["C1"].PutValue("Sales");
string[] sports = { "Golf", "Tennis", "Rugby", "Cricket", "Boxing" };
int row = 2;
foreach (string sport in sports)
{
    for (int quarter = 1; quarter <= 3; quarter++)
    {
        worksheet.Cells[row, 0].PutValue(sport);
        worksheet.Cells[row, 1].PutValue("Qtr" + quarter);
        worksheet.Cells[row, 2].PutValue(1000 + 777 * row);
        row++;
    }
}
PivotTable pivotTable = worksheet.PivotTables.Add("A1:C16", 2, 5);
pivotTable.AddFieldToArea(PivotFieldType.Row, "Sport");
pivotTable.AddFieldToArea(PivotFieldType.Data, "Sales");
pivotTable.CalculateData();
PivotField sportField = pivotTable.RowFields[0];
// İlk 10 Filtresi — öğeleri "Satışların Toplamı" ölçütüne göre ilk 2 öğe olarak tut (veri alanı indeksi 0)
PivotFilter filter = sportField.FilterTop10(0, PivotFilterType.Count, true, 2);
// Bunun yerine yüzdeye dayalı bir filtre kullanarak öğelerin ilk yüzde 30'unu tut:
// sportField.FilterTop10(0, PivotFilterType.Percent, true, 30);
pivotTable.PivotCache.Refresh();
pivotTable.CalculateData();
workbook.Save("output-top10-filter.xlsx");
```

{{% alert color="primary" %}}
`Top10AutoShow` ve `FilterTop10` iki ayrı işlevdir. AutoShow, özet tablo alanı üzerinde saklanan klasik `autoShow` öznitelikleri kümesini yazar ve Excel 97'den itibaren tüm Excel sürümlerinde uygulanır. `FilterTop10` ise modern bir `PivotFilter` girdisi yazar ve Excel 2007 veya sonraki sürümlerini gerektirir. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan bir özet tablo tüm öğeleri gösterir duruma düşer. Eski araçlarla gidiş-dönüş gerektiren belgelerde `Top10AutoShow`; modern çalışma kitaplarında ise diğer değer filtreleriyle birlikte kullanılabilmesi nedeniyle `FilterTop10` tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tablolarını Etikete veya Değere Göre Filtreleme](/cells/tr/net/filter-by-label-or-value-of-pivot-table/)
- [Özet Tablosuna Satır ve Sütun Alanları Ekle](/cells/tr/net/pivot-table-add-row-and-column-fields/)
- [Özet Tablosundaki Özet Alanlarını Gruplayın](/cells/tr/net/group-pivot-fields-in-the-pivot-table/)
- [Özet Tablosunu Yenileyin](/cells/tr/net/refresh-pivot-table/)
- [Özet Tablosuna Sayfa Alanı Ekle](/cells/tr/net/add-page-field-in-pivot-table/)

{{< app/cells/assistant language="csharp" >}}