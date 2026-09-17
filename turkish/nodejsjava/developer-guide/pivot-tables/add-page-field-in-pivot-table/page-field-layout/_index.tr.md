---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for Node.js via Java kullanarak bir pivot tabloda sayfa alanı düzenini nasıl kontrol edeceğinizi öğrenin; görüntüleme sırasını, kaydırma sayısını ve sayfa alanlarının pivot tablonun üstündeki sırasını ayarlamayı içerir.
keywords: Aspose.Cells, Node.js via Java kitaplığı, elektronik tablo, pivot tablosu, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Pivot tablonun üst kısmındaki filtre kontrolleri şeridi olan sayfa alanı düzeninin nasıl kontrol edileceğini gösterir; görüntüleme sırası, kaydırma sayısı ve alanların yeniden sıralanması dahil.
{{% /alert %}}

## **Introduction**
Microsoft Excel'deki bir pivot tablo, tablonun satır/sütun/veri gövdesinin üzerinde yer alan özel bir **sayfa alanı** sunar. Bu alan, açılır filtre kontrollerinden oluşan bir şerit (sayfa alanı başına bir tane) olarak işlenir ve son kullanıcıların pivotu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells bu alanı `PivotTable.PageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl yerleştirileceğini kontrol eden üç özellik sunar:
- `PivotTable.PageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut olanların *yanına* mı yoksa *altına* mı yerleştirileceğine karar verir.
- `PivotTable.PageFieldWrapCount`, sarma işleminden önce satır veya sütun başına kaç sayfa alanının yerleştirileceğini ayarlar.
- `PivotTable.PageFields.Move(currIndex, destIndex)`, sıra modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, her bir işlemi ortak bir veri kümesi üzerinde gösteren üç kod örneğini ele alır; böylece elde edilen düzenleri yan yana karşılaştırabilirsiniz.

## **Source Data**
| Meyve | Yıl  | Bölge | Tutar |
|--------|------|--------|--------|
| Elma   | 2022 | Kuzey  | 150    |
| Elma   | 2023 | Kuzey  | 180    |
| Muz    | 2022 | Güney  | 120    |
| Muz    | 2023 | Güney  | 140    |
| Kiraz  | 2022 | Doğu   | 200    |
| Kiraz  | 2023 | Doğu   | 220    |
| Üzüm   | 2022 | Batı   | 90     |
| Üzüm   | 2023 | Batı   | 110    |
Sekiz satırın tamamı her kod örneğinde aynı sırada doldurulur; dolayısıyla kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklılık gösterir.

## **Example 1: Over Then Down**
İlk senaryoda, iki sayfa alanını (`Year`, `Region`) pivot tablonun üstünde **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Fruit`'ı satır eksenine atarız, `Year`'ı sayfa eksenine ilk, `Region`'ı ise ikinci olarak yerleştiririz (`addFieldToArea` çağrılarının sırası başlangıç dizinini belirler), `Amount`'ı (Sum) veri alanı olarak ekleriz ve ardından `PageFieldOrder`'ı `PrintOrderType.OVER_THEN_DOWN` ile `PageFieldWrapCount = 2` olarak ayarlarız. `OVER_THEN_DOWN` ve 2'lik bir kaydırma sayısıyla, iki sayfa alanı pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir; böylece şerit, iki sütun genişliğinde tek bir satır kaplar.

```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) fs.mkdirSync(dataDir, { recursive: true });
let workbook = new AsposeCells.Workbook();
let worksheets = workbook.getWorksheets();
let pivotDataIdx = worksheets.add("PivotData");
let pivotDataSheet = worksheets.get(pivotDataIdx);
let pivotDataCells = pivotDataSheet.getCells();
// Başlıklar (satır 0)
pivotDataCells.get(0, 0).putValue("Fruit");
pivotDataCells.get(0, 1).putValue("Year");
pivotDataCells.get(0, 2).putValue("Region");
pivotDataCells.get(0, 3).putValue("Amount");
// Satır 1: Elma, 2022, Kuzey, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);
// Satır 2: Elma, 2023, Kuzey, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);
// Satır 3: Muz, 2022, Güney, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);
// Satır 4: Muz, 2023, Güney, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);
// Satır 5: Kiraz, 2022, Doğu, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);
// Satır 6: Kiraz, 2023, Doğu, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);
// Satır 7: Üzüm, 2022, Batı, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);
// Satır 8: Üzüm, 2023, Batı, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);
// PivotTableReport sayfası ekle
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();
// PivotData!A1:D9 kaynaklı pivot tablosu oluştur, PivotTableReport üzerinde A1'e yerleştir
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);
// Alanları ekle
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Meyve
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Yıl
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Bölge
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Tutar
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);
// Sayfa alanı düzenini yapılandır: sayfa alanlarını önce yatay yerleştir, her 2 alandan sonra kaydır
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
// Yenile ve hesapla
pivotTable.calculateData();
// Kaydet
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```

## **Example 2: Down Then Over**
Bu örnekte, Örnek 1'deki gibi `Fruit`'ı satır eksenine, `Year` ve `Region`'ı sayfa eksenine (`Year` ilk olacak şekilde) ve `Amount`'ı (Sum) veri alanı olarak yerleştiririz. Ardından `PageFieldOrder`'ı `PrintOrderType.DOWN_THEN_OVER` ve `PageFieldWrapCount`'u `2` olarak ayarlarız. `DOWN_THEN_OVER` ve 2'lik bir kaydırma sayısıyla, iki sayfa alanı dikey olarak istiflenir — `Year` üstte, `Region` doğrudan altında — pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine bir sütun genişliğinde iki satır kaplar.

```javascript
var workbook = new AsposeCells.Workbook();
var pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
var pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
var pivotReport = workbook.getWorksheets().get(pivotReportIdx);
var headers = ["Fruit", "Year", "Region", "Amount"];
for (var c = 0; c < headers.length; c++)
{
    pivotData.getCells().get(0, c).putValue(headers[c]);
}
var data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];
for (var r = 0; r < data.length; r++)
{
    for (var c = 0; c < data[r].length; c++)
    {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
var idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
var pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**
Üçüncü senaryoda bu veri kümesini ve alan tahsisini koruruz, nötr bir düzen (`OVER_THEN_DOWN` ile `2` kaydırma sayısı) ayarlarız ve ardından `PageFields.Move` işlemini gösteririz. `Move(0, 1)` çağrısı, 0 dizinindeki sayfa alanını (`Year`) 1. konuma taşır ve 1. konumdaki sayfa alanı (`Region`) 0. konuma kayar. Bu çağrıdan sonra `Region` ilk sayfa alanı, `Year` ise ikinci sayfa alanı olur. Kaydırma ve sıra modu değişmediğinden, şerit yatay olarak yan yana işlenmeye devam eder — yalnızca iki açılır menünün sırası değiştirilmiştir.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const dataSheet = workbook.getWorksheets().get(0);
dataSheet.setName("PivotData");
dataSheet.getCells().get("A1").putValue("Fruit");
dataSheet.getCells().get("B1").putValue("Year");
dataSheet.getCells().get("C1").putValue("Region");
dataSheet.getCells().get("D1").putValue("Amount");
dataSheet.getCells().get("A2").putValue("Apple");
dataSheet.getCells().get("B2").putValue(2022);
dataSheet.getCells().get("C2").putValue("North");
dataSheet.getCells().get("D2").putValue(150);
dataSheet.getCells().get("A3").putValue("Apple");
dataSheet.getCells().get("B3").putValue(2023);
dataSheet.getCells().get("C3").putValue("North");
dataSheet.getCells().get("D3").putValue(180);
dataSheet.getCells().get("A4").putValue("Banana");
dataSheet.getCells().get("B4").putValue(2022);
dataSheet.getCells().get("C4").putValue("South");
dataSheet.getCells().get("D4").putValue(120);
dataSheet.getCells().get("A5").putValue("Banana");
dataSheet.getCells().get("B5").putValue(2023);
dataSheet.getCells().get("C5").putValue("South");
dataSheet.getCells().get("D5").putValue(140);
dataSheet.getCells().get("A6").putValue("Cherry");
dataSheet.getCells().get("B6").putValue(2022);
dataSheet.getCells().get("C6").putValue("East");
dataSheet.getCells().get("D6").putValue(200);
dataSheet.getCells().get("A7").putValue("Cherry");
dataSheet.getCells().get("B7").putValue(2023);
dataSheet.getCells().get("C7").putValue("East");
dataSheet.getCells().get("D7").putValue(220);
dataSheet.getCells().get("A8").putValue("Grape");
dataSheet.getCells().get("B8").putValue(2022);
dataSheet.getCells().get("C8").putValue("West");
dataSheet.getCells().get("D8").putValue(90);
dataSheet.getCells().get("A9").putValue("Grape");
dataSheet.getCells().get("B9").putValue(2023);
dataSheet.getCells().get("C9").putValue("West");
dataSheet.getCells().get("D9").putValue(110);
const pivotSheetIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotSheet = workbook.getWorksheets().get(pivotSheetIdx);
const pivotIdx = pivotSheet.getPivotTables().add("PivotData!A1:D9", "A3", "PivotTable");
const pivotTable = pivotSheet.getPivotTables().get(pivotIdx);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.ROW, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.PAGE, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.DATA, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OVER_THEN_DOWN);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Related Articles**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/nodejs-java/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan üst sayfa.
- [Pivot Tablosunda Satır ve Sütun Alanları](/cells/tr/nodejs-java/row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan şekilde, alanların satır ve sütun eksenlerine tahsis edilmesini ele alır.
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-java/manage-value-fields/) — bu makalede kullanılan `Sum` toplama işlemi dahil, veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `refreshData` ve `calculateData` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="nodejs-java" >}}