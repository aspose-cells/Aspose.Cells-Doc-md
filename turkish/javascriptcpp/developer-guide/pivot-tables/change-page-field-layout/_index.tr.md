---
title: Özet Tablosunda Sayfa Alanı Düzenini Değiştirme
linktitle: Özet Tablosunda Sayfa Alanı Düzenini Değiştirme
description: Aspose.Cells for JavaScript via C++ kullanarak bir özet tablosunda sayfa alanı bölgesinin düzenini nasıl kontrol edeceğinizi öğrenin. Özet tablosunun üst kısmındaki sayfa alanlarının görüntüleme sırasını, sarmalama sayısını ve alan sırasını belirleyin.
keywords: Aspose.Cells for JavaScript via C++, elektronik tablo, özet tablo, sayfa alanı, sayfa alanı sırası, sayfa alanı sarmalama sayısı, sayfa alanını taşıma
type: docs
weight: 191
url: /tr/javascript-cpp/change-page-field-layout/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Bu makale, **Özet Tablosuna Sayfa Alanı Ekleme** konusunun devamıdır. Özet tablosunun üst kısmındaki filtre denetimlerinden oluşan sayfa alanı bölgesinin düzenini nasıl kontrol edeceğinizi gösterir. Görüntüleme sırası, sarmalama sayısı ve alanların yeniden sıralanması da ele alınır.
{{% /alert %}}

## **Giriş**
Microsoft Excel'deki bir özet tablo, tablonun satır, sütun ve veri gövdesinin üzerinde bulunan özel bir **sayfa alanı bölgesi** sunar. Bu bölge, her sayfa alanı için bir tane olmak üzere açılır listeli filtre denetimlerinden oluşan bir şerit olarak görüntülenir. Bu bölgedeki denetimler, son kullanıcıların özet tabloyu yıl veya bölge gibi ölçütlere göre dilimlemesini sağlar. Aspose.Cells bu alanı `pivotTable.pageFields` koleksiyonu aracılığıyla modeller ve şeridin görsel düzenini kontrol eden üç özellik sunar:
- `pivotTable.pageFieldOrder` (bir `Aspose.Cells.PrintOrderType` değeri), ek sayfa alanlarının mevcut alanların *yanına* mı yoksa *altına* mı yerleştirileceğini belirler.
- `pivotTable.pageFieldWrapCount`, sarmalama gerçekleşmeden önce her satıra veya sütuna yerleştirilecek sayfa alanı sayısını belirler.
- `pivotTable.pageFields.move(currIndex, destIndex)`, sayfa alanlarını sıra modunu değiştirmeden yeniden sıralar.
Bu makale, ortak bir veri kümesi üzerinde bu işlemlerin her birini gösteren üç kod örneğini ele alır. Böylece ortaya çıkan düzenleri yan yana karşılaştırabilirsiniz.

## **Kaynak Veri**
| Meyve | Yıl | Bölge | Tutar |
|-------|-----|-------|-------|
| Elma  | 2022 | Kuzey | 150   |
| Elma  | 2023 | Kuzey | 180   |
| Muz   | 2022 | Güney | 120   |
| Muz   | 2023 | Güney | 140   |
| Kiraz | 2022 | Doğu  | 200   |
| Kiraz | 2023 | Doğu  | 220   |
| Üzüm  | 2022 | Batı  | 90    |
| Üzüm  | 2023 | Batı  | 110   |
Her kod örneğinde sekiz satırın tamamı aynı sırayla yer alır. Bu nedenle kaynak veri senaryolar arasında hiçbir zaman değişmez; yalnızca sayfa alanı düzenine ilişkin özellikler değişir.

## **Örnek 1: Over Then Down**
İlk senaryoda, `Year` ve `Region` sayfa alanlarını özet tablosunun üst kısmında **tek satırda yan yana** gösterecek şekilde yapılandırıyoruz. `Fruit` alanını satır eksenine atıyoruz; sayfa ekseninde önce `Year`, ardından `Region` alanını yerleştiriyoruz (`addFieldToArea` çağrılarının sırası başlangıç indeksini belirler). `Amount` (Sum) alanını veri alanı olarak ekliyoruz ve ardından `pivotTable.pageFieldOrder` özelliğini `PrintOrderType.OverThenDown` değerine, `pivotTable.pageFieldWrapCount` özelliğini de `2` değerine ayarlıyoruz. `OverThenDown` düzeni ve 2 sarmalama sayısıyla iki sayfa alanı, özet tablosunun üst kısmında tek bir satırda yatay olarak yan yana yerleştirilir. Dolayısıyla şerit, iki alan genişliğinde tek bir satır kaplar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const worksheets = workbook.worksheets;
            const pivotDataSheet = worksheets.add("PivotData");
            const pivotDataCells = pivotDataSheet.cells;
            // Başlıklar (satır 0)
            pivotDataCells.get(0, 0).value = "Fruit";
            pivotDataCells.get(0, 1).value = "Year";
            pivotDataCells.get(0, 2).value = "Region";
            pivotDataCells.get(0, 3).value = "Amount";
            // Satır 1: Apple, 2022, North, 150
            pivotDataCells.get(1, 0).value = "Apple";
            pivotDataCells.get(1, 1).value = 2022;
            pivotDataCells.get(1, 2).value = "North";
            pivotDataCells.get(1, 3).value = 150;
            // Satır 2: Apple, 2023, North, 180
            pivotDataCells.get(2, 0).value = "Apple";
            pivotDataCells.get(2, 1).value = 2023;
            pivotDataCells.get(2, 2).value = "North";
            pivotDataCells.get(2, 3).value = 180;
            // Satır 3: Banana, 2022, South, 120
            pivotDataCells.get(3, 0).value = "Banana";
            pivotDataCells.get(3, 1).value = 2022;
            pivotDataCells.get(3, 2).value = "South";
            pivotDataCells.get(3, 3).value = 120;
            // Satır 4: Banana, 2023, South, 140
            pivotDataCells.get(4, 0).value = "Banana";
            pivotDataCells.get(4, 1).value = 2023;
            pivotDataCells.get(4, 2).value = "South";
            pivotDataCells.get(4, 3).value = 140;
            // Satır 5: Cherry, 2022, East, 200
            pivotDataCells.get(5, 0).value = "Cherry";
            pivotDataCells.get(5, 1).value = 2022;
            pivotDataCells.get(5, 2).value = "East";
            pivotDataCells.get(5, 3).value = 200;
            // Satır 6: Cherry, 2023, East, 220
            pivotDataCells.get(6, 0).value = "Cherry";
            pivotDataCells.get(6, 1).value = 2023;
            pivotDataCells.get(6, 2).value = "East";
            pivotDataCells.get(6, 3).value = 220;
            // Satır 7: Grape, 2022, West, 90
            pivotDataCells.get(7, 0).value = "Grape";
            pivotDataCells.get(7, 1).value = 2022;
            pivotDataCells.get(7, 2).value = "West";
            pivotDataCells.get(7, 3).value = 90;
            // Satır 8: Grape, 2023, West, 110
            pivotDataCells.get(8, 0).value = "Grape";
            pivotDataCells.get(8, 1).value = 2023;
            pivotDataCells.get(8, 2).value = "West";
            pivotDataCells.get(8, 3).value = 110;
            // PivotTableReport sayfasını ekle
            const pivotTableSheet = worksheets.add("PivotTableReport");
            const pivotTables = pivotTableSheet.pivotTables;
            // PivotData!A1:D9 kaynağından verileri alan ve PivotTableReport üzerinde A1 konumuna yerleştirilen özet tabloyu oluştur
            const pivotTableIndex = pivotTables.add("PivotData!A1:D9", "A1", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Alanları ekle
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);   // Meyve
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);  // Yıl
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);  // Bölge
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);  // Tutar
            pivotTable.dataFields.get(0).function = AsposeCells.ConsolidationFunction.Sum;
            // Sayfa alanı alan düzenini yapılandır: sayfa alanlarını önce yatay olarak yerleştir, her 2 alandan sonra satıra geç
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            // Yenile ve hesapla
            pivotTable.calculateData();
            // Kaydet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_overThenDown.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Örnek 2: Down Then Over**
Bu örnekte, Örnek 1'deki gibi, `Fruit` alanını satır eksenine, `Year` ve `Region` alanlarını sayfa eksenine (`Year` önce olacak şekilde) ve `Amount` (Sum) alanını veri alanı olarak yerleştiriyoruz. Ardından `pivotTable.pageFieldOrder` özelliğini `PrintOrderType.DownThenOver` değerine ve `pivotTable.pageFieldWrapCount` özelliğini `2` değerine ayarlıyoruz. `DownThenOver` düzeni ve 2 sarmalama sayısıyla iki sayfa alanı dikey olarak üst üste yerleştirilir: üstte `Year`, doğrudan altında `Region` bulunur. Bu yerleşim, özet tablosunun üst kısmında tek bir sütun oluşturur. Dolayısıyla şerit, Örnek 1'in aksine, tek sütun genişliğinde iki satır kaplar.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const workbook = new Workbook();
            const pivotData = workbook.worksheets.get(0);
            pivotData.name = "PivotData";
            const pivotReport = workbook.worksheets.add("PivotTableReport");
            const headers = ["Fruit", "Year", "Region", "Amount"];
            for (let c = 0; c < headers.length; c++) {
                pivotData.cells.get(0, c).value = headers[c];
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
                    pivotData.cells.get(r + 1, c).value = data[r][c];
                }
            }
            const pivotTableIndex = pivotReport.pivotTables.add(
                "=PivotData!A1:D9",
                "A1",
                "PivotTable1"
            );
            const pivotTable = pivotReport.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, 0);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 1);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, 2);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, 3);
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.DownThenOver;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], {
                type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_downThenOver.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Örnek 3: Sayfa Alanını Taşıma**
Üçüncü senaryoda aynı veri kümesini ve alan dağılımını kullanarak başlangıç düzenini (`OverThenDown` ve `2` sarmalama sayısı) ayarlıyor ve ardından `pivotTable.pageFields.move` işlemini gösteriyoruz. `move(0, 1)` çağrısı, indeks 0'daki sayfa alanını (`Year`) 1 konumuna taşır; 1 konumundaki sayfa alanı (`Region`) ise 0 konumuna kayar. Bu çağrıdan sonra `Region` ilk sayfa alanı, `Year` ise ikinci sayfa alanı olur. Sarmalama ayarı ve sıra modu değişmediğinden şerit yine yatay olarak, alanlar yan yana görüntülenir; yalnızca iki açılır listenin sırası takas edilir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const workbook = new Workbook();
            const dataSheet = workbook.worksheets.get(0);
            dataSheet.name = "PivotData";
            const cells = dataSheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Region";
            cells.get("D1").value = "Amount";
            cells.get("A2").value = "Apple";
            cells.get("B2").value = 2022;
            cells.get("C2").value = "North";
            cells.get("D2").value = 150;
            cells.get("A3").value = "Apple";
            cells.get("B3").value = 2023;
            cells.get("C3").value = "North";
            cells.get("D3").value = 180;
            cells.get("A4").value = "Banana";
            cells.get("B4").value = 2022;
            cells.get("C4").value = "South";
            cells.get("D4").value = 120;
            cells.get("A5").value = "Banana";
            cells.get("B5").value = 2023;
            cells.get("C5").value = "South";
            cells.get("D5").value = 140;
            cells.get("A6").value = "Cherry";
            cells.get("B6").value = 2022;
            cells.get("C6").value = "East";
            cells.get("D6").value = 200;
            cells.get("A7").value = "Cherry";
            cells.get("B7").value = 2023;
            cells.get("C7").value = "East";
            cells.get("D7").value = 220;
            cells.get("A8").value = "Grape";
            cells.get("B8").value = 2022;
            cells.get("C8").value = "West";
            cells.get("D8").value = 90;
            cells.get("A9").value = "Grape";
            cells.get("B9").value = 2023;
            cells.get("C9").value = "West";
            cells.get("D9").value = 110;
            const pivotSheet = workbook.worksheets.add("PivotTableReport");
            const pivotTableIndex = pivotSheet.pivotTables.add(
                "=PivotData!A1:D9",
                "A3",
                "PivotTable1"
            );
            const pivotTable = pivotSheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Region");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.pageFieldOrder = AsposeCells.PrintOrderType.OverThenDown;
            pivotTable.pageFieldWrapCount = 2;
            pivotTable.pageFields.move(0, 1);
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldLayout_move.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **İlgili Makaleler**
- [Özet Tablosuna Sayfa Alanı Ekleme](/cells/tr/javascript-cpp/add-page-field-in-pivot-table/) — sayfa alanlarının bir özet tabloya nasıl eklendiğini tanıtan üst sayfa.
- [Özet Tablosunda Değer Alanlarını Yönetme](/cells/tr/javascript-cpp/manage-value-fields/) — veri (değer) alanının nasıl yapılandırılacağını ve bu makalede kullanılan `Sum` toplamasını açıklar.
- [Özet Tablosuna Stil Uygula](/cells/tr/javascript-cpp/apply-style-to-pivot-table/) — sayfa alanı şeridi yerleştirildikten sonra oluşturulan özet tablosunun nasıl biçimlendirileceğini gösterir.

{{< app/cells/assistant language="javascript-cpp" >}}