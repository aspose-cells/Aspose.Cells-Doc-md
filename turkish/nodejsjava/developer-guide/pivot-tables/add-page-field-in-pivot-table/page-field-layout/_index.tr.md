---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for Node.js via Java kullanarak bir pivot tablosunda sayfa alanı düzenini nasıl kontrol edeceğinizi öğrenin; pivot tablonun üst kısmındaki sayfa alanlarının görüntüleme sırası, kaydırma sayısı ve alan sırasının ayarlanması dahil.
keywords: Aspose.Cells, Node.js via Java kütüphanesi, elektronik tablo, Pivot Tablosu, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/nodejs-java/change-page-field-layout/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---
{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Pivot tablonun üst kısmındaki filtre denetimleri şeridi olan sayfa alanı düzeninin nasıl kontrol edileceğini; görüntüleme sırası, kaydırma sayısı ve alanların yeniden sıralanması dahil olmak üzere gösterir.
{{% /alert %}}
## **Giriş**
Microsoft Excel'deki bir pivot tablo, tablonun satır/sütun/veri gövdesinin üzerinde konumlanan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, açılır filtre denetimlerinden oluşan bir şerit olarak işlenir (her sayfa alanı için bir tane) ve son kullanıcıların pivot tabloyu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells bu bölgeyi `PivotTable.PageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl düzenleneceğini kontrol eden üç özellik sunar:
- `PivotTable.PageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut alanların *yanına* mı yoksa *altına* mı yerleştirileceğine karar verir.
- `PivotTable.PageFieldWrapCount`, kaydırmadan önce satır veya sütun başına kaç sayfa alanı yerleştirileceğini ayarlar.
- `PivotTable.PageFields.Move(currIndex, destIndex)`, sıralama modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, her bir işlemi ortak bir veri kümesi üzerinde gösteren üç kod örneğini ele alır, böylece sonuçtaki düzenleri yan yana karşılaştırabilirsiniz.
## **Kaynak Veri**
Aşağıdaki üç örnek de bu sekiz satırlık satış verisini `PivotData` adlı bir çalışma sayfasına yükler. Veriler iki sayfa alanı adayı (`Year`, `Region`), bir satır alanı adayı (`Fruit`) ve bir ölçü (`Amount`) içerir; bu da sayfa alanı şeridinin incelenmesini anlamlı kılar.
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
Sekiz satırın tümü her kod örneğinde aynı sırada doldurulur, dolayısıyla kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzeni özellikleri farklılık gösterir.
## **Örnek 1: Önce Yatay, Sonra Dikey**
İlk senaryoda iki sayfa alanını (`Year`, `Region`) pivot tablonun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Fruit`'ı satır eksenine atarız, `Year`'ı önce ve `Region`'ı ikinci olarak sayfa eksenine yerleştiririz (`addFieldToArea` çağrılarının sırası başlangıç dizinini belirler), `Amount` (Sum) öğesini veri alanı olarak ekleriz ve ardından `PageFieldOrder` değerini `PrintOrderType.OVER_THEN_DOWN`, `PageFieldWrapCount` değerini ise `2` olarak ayarlarız. `OVER_THEN_DOWN` ve 2'lik kaydırma sayısı ile iki sayfa alanı, pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana düzenlenir; böylece şerit genişliği iki olan tek bir satır kaplar.
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

// Satır 1: Apple, 2022, North, 150
pivotDataCells.get(1, 0).putValue("Apple");
pivotDataCells.get(1, 1).putValue(2022);
pivotDataCells.get(1, 2).putValue("North");
pivotDataCells.get(1, 3).putValue(150);

// Satır 2: Apple, 2023, North, 180
pivotDataCells.get(2, 0).putValue("Apple");
pivotDataCells.get(2, 1).putValue(2023);
pivotDataCells.get(2, 2).putValue("North");
pivotDataCells.get(2, 3).putValue(180);

// Satır 3: Banana, 2022, South, 120
pivotDataCells.get(3, 0).putValue("Banana");
pivotDataCells.get(3, 1).putValue(2022);
pivotDataCells.get(3, 2).putValue("South");
pivotDataCells.get(3, 3).putValue(120);

// Satır 4: Banana, 2023, South, 140
pivotDataCells.get(4, 0).putValue("Banana");
pivotDataCells.get(4, 1).putValue(2023);
pivotDataCells.get(4, 2).putValue("South");
pivotDataCells.get(4, 3).putValue(140);

// Satır 5: Cherry, 2022, East, 200
pivotDataCells.get(5, 0).putValue("Cherry");
pivotDataCells.get(5, 1).putValue(2022);
pivotDataCells.get(5, 2).putValue("East");
pivotDataCells.get(5, 3).putValue(200);

// Satır 6: Cherry, 2023, East, 220
pivotDataCells.get(6, 0).putValue("Cherry");
pivotDataCells.get(6, 1).putValue(2023);
pivotDataCells.get(6, 2).putValue("East");
pivotDataCells.get(6, 3).putValue(220);

// Satır 7: Grape, 2022, West, 90
pivotDataCells.get(7, 0).putValue("Grape");
pivotDataCells.get(7, 1).putValue(2022);
pivotDataCells.get(7, 2).putValue("West");
pivotDataCells.get(7, 3).putValue(90);

// Satır 8: Grape, 2023, West, 110
pivotDataCells.get(8, 0).putValue("Grape");
pivotDataCells.get(8, 1).putValue(2023);
pivotDataCells.get(8, 2).putValue("West");
pivotDataCells.get(8, 3).putValue(110);

// PivotTableReport sayfasını ekle
let pivotTableSheetIdx = worksheets.add("PivotTableReport");
let pivotTableSheet = worksheets.get(pivotTableSheetIdx);
let pivotTables = pivotTableSheet.getPivotTables();

// PivotData!A1:D9 kaynaklı, PivotTableReport üzerinde A1'e yerleştirilen pivot tablosu oluştur
let pivotIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
let pivotTable = pivotTables.get(pivotIndex);

// Alanları ekle
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Fruit
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Year
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Region
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Amount
pivotTable.getDataFields().get(0).setFunction(AsposeCells.ConsolidationFunction.Sum);

// Sayfa alanı yerleşimini yapılandır: sayfa alanlarını yatayda yan yana, her 2 alandan sonra alt satıra geç
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);

// Yenile ve hesapla
pivotTable.calculateData();

// Kaydet
workbook.save(path.join(dataDir, "pageFieldLayout_overThenDown.xlsx"));
```
## **Örnek 2: Önce Dikey, Sonra Yatay**
Bu örnekte, Örnek 1'deki gibi tam olarak `Fruit`'ı satır eksenine, `Year` ve `Region`'ı sayfa eksenine (`Year` önce olacak şekilde) ve `Amount` (Sum) öğesini veri alanı olarak yerleştiriyoruz. Ardından `PageFieldOrder` değerini `PrintOrderType.DOWN_THEN_OVER` ve `PageFieldWrapCount` değerini `2` olarak ayarlıyoruz. `DOWN_THEN_OVER` ve 2'lik kaydırma sayısı ile iki sayfa alanı dikey olarak istiflenir — `Year` üstte, `Region` hemen altında — ve pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine, genişliği bir olan iki satır kaplar.
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
## **Örnek 3: Bir Sayfa Alanını Taşıma**
Üçüncü senaryoda bu veri kümesini ve alan ayırmasını koruyoruz, tarafsız bir düzen (`OVER_THEN_DOWN` ve kaydırma sayısı `2`) ayarlıyoruz ve ardından `PageFields.Move` işlemini gösteriyoruz. `Move(0, 1)` çağrısı, dizin 0'daki sayfa alanını (`Year`) 1 konumuna taşır ve 1 konumundaki sayfa alanı (`Region`) 0 konumuna geçer. Bu çağrıdan sonra `Region` ilk sayfa alanı, `Year` ise ikinci sayfa alanı olur. Kaydırma ve sıralama modu değişmediğinden şerit yine yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiştir.
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
## **İlgili Makaleler**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/nodejs-java/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan ana sayfa.
- [Pivot Tablosunda Satır ve Sütun Alanları](/cells/tr/nodejs-java/row-and-column-fields/) — burada gösterilen sayfa ekseni çalışmasını tamamlayan şekilde alanların satır ve sütun eksenlerine atanmasını ele alır.
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-java/manage-value-fields/) — bu makalede kullanılan `Sum` toplaması dahil, veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-java/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `refreshData` ve `calculateData` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-java/apply-style-to-pivot-table/) — sayfa alanı şeridi düzenlendikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.
{{< app/cells/assistant language="nodejs-java" >}}