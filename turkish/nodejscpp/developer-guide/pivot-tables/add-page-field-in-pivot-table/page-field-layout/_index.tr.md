---
title: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Pivot Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for Node.js via C++ kullanarak bir pivot tabloda sayfa alanı düzenini nasıl kontrol edeceğinizi öğrenin; görüntüleme sırasını, kaydırma sayısını ve pivot tablonun üst kısmındaki sayfa alanlarının alan sırasını ayarlamayı içerir.
keywords: Aspose.Cells, Node.js via C++ kitaplığı, elektronik tablo, pivot tablo, sayfa alanı, sayfa alanı sırası, sayfa alanı kaydırma sayısı, sayfa alanını taşı
type: docs
weight: 191
url: /tr/nodejs-cpp/change-page-field-layout/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Bu makale, **Pivot Tablosuna Sayfa Alanı Ekleme** konusunun devamı niteliğindedir. Sayfa alanı düzeninin — pivot tablonun üst kısmındaki filtre denetimleri şeridinin — görüntüleme sırası, kaydırma sayısı ve alan yeniden sıralaması dahil nasıl kontrol edileceğini gösterir.
{{% /alert %}}

## **Introduction**
Microsoft Excel'deki bir pivot tablo, tablonun satır/sütun/veri gövdesinin üzerinde yer alan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, her sayfa alanı için bir açılır filtre denetimi şeridi olarak işlenir ve son kullanıcıların pivotu yıl veya bölge gibi ölçütlere göre dilimlemek için tıkladığı yerdir. Aspose.Cells for Node.js via C++ bu bölgeyi `pivotTable.pageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel olarak nasıl yerleştirileceğini kontrol eden üç özellik sunar:
- `pivotTable.pageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut alanların *yanına* mı yoksa *altına* mı yerleştirileceğini belirler.
- `pivotTable.pageFieldWrapCount`, kaydırmadan önce satır veya sütun başına yerleştirilecek sayfa alanı sayısını ayarlar.
- `pivotTable.pageFields.move(currIndex, destIndex)`, sıra modunu değiştirmeden sayfa alanlarını yeniden sıralar.
Bu makale, ortak bir veri kümesi üzerinde bu işlemlerin her birini gösteren üç kod örneğini adım adım açıklar; böylece elde edilen düzenleri yan yana karşılaştırabilirsiniz.

## **Source Data**
| Meyve  | Yıl | Bölge | Tutar |
|--------|------|--------|--------|
| Elma   | 2022 | Kuzey  | 150    |
| Elma   | 2023 | Kuzey  | 180    |
| Muz    | 2022 | Güney  | 120    |
| Muz    | 2023 | Güney  | 140    |
| Kiraz  | 2022 | Doğu   | 200    |
| Kiraz  | 2023 | Doğu   | 220    |
| Üzüm   | 2022 | Batı   | 90     |
| Üzüm   | 2023 | Batı   | 110    |
Sekiz satırın tümü her kod örneğinde, aynı sırada doldurulur; dolayısıyla kaynak veri senaryolar arasında asla farklılık göstermez — yalnızca sayfa alanı düzen özellikleri farklılık gösterir.

## **Example 1: Over Then Down**
İlk senaryoda, iki sayfa alanını (`Yıl`, `Bölge`) pivot tablonun üst kısmında **tek bir satırda yan yana** görünecek şekilde yapılandırıyoruz. `Meyve` öğesini satır eksenine atarız, `Yıl` ve `Region` öğelerini sayfa eksenine sırasıyla birinci ve ikinci olarak yerleştiririz (`addFieldToArea` çağrılarının sırası başlangıç dizinini belirler), `Tutar` (Toplam) öğesini veri alanı olarak ekler ve ardından `pageFieldOrder` öğesini `PrintOrderType.OverThenDown` ve `pageFieldWrapCount = 2` olarak ayarlarız. `OverThenDown` ve kaydırma sayısı 2 ile, iki sayfa alanı pivot tablonun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir; böylece şerit iki genişliğinde tek bir satır kaplar.

```javascript
let dataDir = "output";
if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
}
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
// PivotData!A1:D9'dan kaynaklanan ve PivotTableReport üzerinde A1'e yerleştirilen pivot tablo oluştur
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
Bu örnekte, `Meyve` öğesini satır eksenine, `Yıl` ve `Region` öğelerini sayfa eksenine (`Yıl` birinci olacak şekilde) ve `Tutar` (Toplam) öğesini veri alanı olarak yerleştiriyoruz — tıpkı Örnek 1'deki gibi. Ardından `pageFieldOrder` öğesini `PrintOrderType.DownThenOver` ve `pageFieldWrapCount` öğesini `2` olarak ayarlıyoruz. `DownThenOver` ve kaydırma sayısı 2 ile, iki sayfa alanı dikey olarak istiflenir — `Yıl` üstte, `Bölge` doğrudan altında — ve pivot tablonun üst kısmında tek bir sütun oluşturur. Bu nedenle şerit, Örnek 1'in aksine, bir genişliğinde iki satır kaplar.

```javascript
const AsposeCells = require("aspose.cells");
const workbook = new AsposeCells.Workbook();
const pivotData = workbook.getWorksheets().get(0);
pivotData.setName("PivotData");
const pivotReportIdx = workbook.getWorksheets().add("PivotTableReport");
const pivotReport = workbook.getWorksheets().get(pivotReportIdx);
const headers = ["Fruit", "Year", "Region", "Amount"];
for (let c = 0; c < headers.length; c++) {
    pivotData.getCells().get(0, c).putValue(headers[c]);
}
const data = [
    ["Apple", 2022, "North", 150],
    ["Apple", 2023, "North", 180],
    ["Banana", 2022, "South", 120],
    ["Banana", 2023, "South", 140],
    ["Cherry", 2022, "East", 200],
    ["Cherry", 2023, "East", 220],
    ["Grape", 2022, "West", 90],
    ["Grape", 2023, "West", 110]
];
for (let r = 0; r < data.length; r++) {
    for (let c = 0; c < data[r].length; c++) {
        pivotData.getCells().get(r + 1, c).putValue(data[r][c]);
    }
}
const idx = pivotReport.getPivotTables().add("PivotData!A1:D9", "A1", "PivotTable");
const pivotTable = pivotReport.getPivotTables().get(idx);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.Pivot.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.DownThenOver);
pivotTable.setPageFieldWrapCount(2);
pivotTable.calculateData();
workbook.save("pageFieldLayout_downThenOver.xlsx");
```

## **Example 3: Move a Page Field**
Üçüncü senaryoda bu veri kümesini ve alan atamasını koruyoruz, nötr bir düzen (`OverThenDown` ve kaydırma sayısı `2`) ayarlıyoruz ve ardından `pageFields.move` işlemini gösteriyoruz. `move(0, 1)` çağrısı, dizin 0'daki sayfa alanını (`Yıl`) konum 1'e taşır ve konum 1'deki sayfa alanı (`Bölge`) konum 0'a kayar. Bu çağrıdan sonra `Bölge` ilk sayfa alanı ve `Yıl` ikinci sayfa alanı olur. Kaydırma ve sıra modu değişmediğinden şerit hâlâ yatay olarak yan yana işlenir — yalnızca iki açılır menünün sırası değiştirilmiştir.

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
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
pivotTable.setPageFieldOrder(AsposeCells.PrintOrderType.OverThenDown);
pivotTable.setPageFieldWrapCount(2);
pivotTable.getPageFields().move(0, 1);
pivotTable.calculateData();
workbook.save("pageFieldLayout_move.xlsx");
```

## **Related Articles**
- [Pivot Tablosuna Sayfa Alanı Ekleme](/cells/tr/nodejs-cpp/add-page-field-in-pivot-table/) — sayfa alanlarının bir pivot tabloya nasıl ekleneceğini tanıtan üst sayfa.
- [Pivot Tablosunda Satır ve Sütun Alanları](/cells/tr/nodejs-cpp/row-and-column-fields/) — alanların satır ve sütun eksenlerine atanmasını kapsar; burada gösterilen sayfa ekseni çalışmasını tamamlar.
- [Pivot Tablosunda Değer Alanlarını Yönetme](/cells/tr/nodejs-cpp/manage-value-fields/) — bu makalede kullanılan `Sum` toplaması dahil, veri (değer) alanının nasıl yapılandırılacağını açıklar.
- [Pivot Tablosunu Yenileme](/cells/tr/nodejs-cpp/refresh-pivot-table/) — sayfa alanları yeniden sıralandıktan sonra gerekli olan `refreshData` ve `calculateData` işlemlerini açıklar.
- [Pivot Tablosuna Stil Uygulama](/cells/tr/nodejs-cpp/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra işlenmiş pivot tablonun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="nodejs-cpp" >}}