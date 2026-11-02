---
title: Özet Tabloda En Üst 10 Öğeyi Gösterme veya Filtreleme
linktitle: Özet Tabloda En Üst 10 Öğeyi Gösterme veya Filtreleme
description: Aspose.Cells for JavaScript via C++ kullanarak bir özet tablo alanının yalnızca sıralamada en üstte veya en altta yer alan öğelerini nasıl göstereceğinizi öğrenin. Bu makale; Excel 97-2003 AutoShow özelliklerini (isAutoShow ve ilgili özellikler), seçeneklerin geri okunmasını ve filterTop10 aracılığıyla Excel 2007-365 En Üst 10 Filtresini ele alır.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, özet tablo, en üst 10, otomatik gösterim, isAutoShow, isAscendShow, autoShowCount, autoShowField, filterTop10, PivotFilterType, PivotField, JavaScript
type: docs
weight: 20
url: /tr/javascript-cpp/top-10-show-or-filter-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Olası Kullanım Senaryoları**
Bir satır alanındaki her öğeyi listeleyen bir özet tablo, alan onlarca üyeye sahip olduğunda okunması zor olabilir. En Üst 10 raporu yalnızca sıralamada en üstte veya en altta yer alan öğeleri içerir; bu da sıralama raporlarının tam olarak ihtiyaç duyduğu şeydir — "gelire göre en üst 5 ürün" veya "satış sayısına göre en alt 3 bölge". Aspose.Cells bunun için iki mekanizmayı destekler ve bunlar Microsoft Excel'in iki farklı nesline karşılık gelir.
- **Excel 97-2003 AutoShow** — `PivotField` sınıfının `isAutoShow`, `isAscendShow`, `autoShowCount` ve `autoShowField` özellikleri. Bu, doğrudan özet tablo alanı üzerinde saklanan klasik "En üst/alt N öğeyi göster" ayarıdır. Özgün özet tablo biçiminin bir parçası olduğu için eski ve yeni tüm Excel sürümlerinde çalışır.
- **Excel 2007-365 En Üst 10 Filtresi** — `PivotField.filterTop10()` yöntemi. Bu, alan menüsündeki Değer Filtreleri bölümünde bulunan modern En Üst 10 değer filtresidir. İlgili alana bağlı bir `PivotFilter` nesnesi olarak saklanır ve öğe sayısına veya yüzdeye dayalı sıralama sunar.

## **Excel 97-2003'te En Üst 10 Öğeyi Gösterme (AutoShow)**
Klasik AutoShow, `PivotField` üzerinde dört özellik atamasıyla yapılandırılır:
- `isAutoShow` — alan üzerindeki AutoShow ayarını etkinleştirir veya devre dışı bırakır.
- `isAscendShow` — `false`, sıralamada en üstte yer alan öğeleri (Üst) korur; `true`, en altta yer alan öğeleri (Alt) korur.
- `autoShowCount` — korunacak öğe sayısı; klasik bir En Üst 10 raporu için örneğin 10.
- `autoShowField` — öğeleri sıralayan **veri alanının** sıfırdan başlayan dizini. Öğeleri alanın kendisine göre sıralamak için -1 değerini geçirin.
Sıralama, bir değer alanı veya alanın kendisi tarafından belirlenebilir. Aşağıda iki temel varyant gösterilmektedir.

### **Değer Alanına Göre Sıralama**
Satır alanının öğelerini Satışların Toplamı gibi sıradan bir değer alanına göre sıralayın. Aşağıdaki örnek, bir satır alanı (`Sport`) ve bir veri alanı (`Sales`) içeren bir özet tablo oluşturur ve ardından satışlara göre en üst 2 sporu gösterir. `rankBy` 0'dır çünkü "Satışların Toplamı" veri alanı 0 dizinindedir.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // "Sum of Sales" değerine göre sıralanan ilk 2 öğeyi göster (veri alanı dizini 0)
            sportField.isAutoShow = true;
            sportField.isAscendShow = false;
            sportField.autoShowCount = 2;
            sportField.autoShowField = 0;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-value-field.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### **Alanın Kendisine Göre Sıralama**
Bir alan kendisiyle de sıralanabilir; bunun için `autoShowField` özelliğine -1 değerini geçirin. Bu varyant için ek bir veri alanına gerek yoktur; alanın satır (veya sütun) alanında bulunması yeterlidir. Aşağıdaki örnek, alanın kendisine göre sıralanan en alt 3 sporu gösterir. Bu ayar kaydedildiğinde, -1 biçimin varsayılan değeri olduğu için `rankBy` özniteliği özet tablo XML'inden çıkarılır ve `autoShowField` -1 değerini geri okur.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            for (const sport of sports) {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
            }
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C16", "F3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");
            pivotTable.calculateData();
            const sportField = pivotTable.rowFields.get(0);
            // Alanın kendisine göre sıralanan en alt 3 öğeyi göster (rankBy = -1)
            sportField.isAutoShow = true;
            sportField.isAscendShow = true;
            sportField.autoShowCount = 3;
            sportField.autoShowField = -1;
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output-top10-by-field-itself.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Mevcut AutoShow Seçeneklerini Okuma**
`PivotField` sınıfının `isAutoShow`, `isAscendShow`, `autoShowCount` ve `autoShowField` özellikleri, alan üzerinde şu anda saklanan AutoShow seçeneklerini sunar. Bu özellikleri, dosyadan yüklenen çalışma kitapları da dâhil olmak üzere, var olan bir çalışma kitabında veya yeni yapılandırdığınız bir özet tabloda öğelerin nasıl sunulacağını incelemek için kullanın.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const fileInput = document.getElementById('fileInput');
            const result = document.getElementById('result');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const sportField = pivotTable.rowFields.get(0);
                const autoShowEnabled = sportField.isAutoShow;
                const direction = sportField.isAscendShow ? "Bottom" : "Top";
                const itemCount = sportField.autoShowCount;
                const rankingDataFieldIndex = sportField.autoShowField;
                result.innerHTML =
                    '<p>AutoShow enabled: ' + autoShowEnabled + '</p>' +
                    '<p>Direction: ' + direction + '</p>' +
                    '<p>Item count: ' + itemCount + '</p>' +
                    '<p>Ranking data field index: ' + rankingDataFieldIndex + '</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
                console.error(error);
            }
        });
    </script>
</html>
```

Bu dört özellik, özet tablo XML'ine yazılan klasik AutoShow öznitelikleriyle (`autoShow`, `topAutoShow`, `itemPageCount`, `rankBy`) eşleşir; bu nedenle geri okunan değerler, her Excel sürümünün dikkate alacağı değerlerdir.

## **Not**

{{% alert color="primary" %}}
- Herhangi bir AutoShow özelliğini değiştirdikten sonra `pivotTable.calculateData()` çağrısını yeniden yapın; ayarlar yalnızca bir sonraki yeniden hesaplamada, görüntülenen yerleşimde etkinleşir.
- AutoShow ayarları, satır ve sütun alanlarıyla çalışır. Yalnızca sayfa (filtre) alanında bulunan bir alan bu yolla sıralanamaz; çünkü öğeleri özet tablo gövdesinde yer almaz.
{{% /alert %}}

## **Excel 2007-365: En Üst 10 Filtresi (filterTop10)**
Modern Excel sürümleri, En Üst 10 seçeneğini alan menüsünde bir değer filtresi olarak sunar (Değer Filtreleri, En Üst 10...). Aspose.Cells bunu, oluşturulan `PivotFilter` nesnesini döndüren `PivotField.filterTop10(number valueFieldIndex, PivotFilterType type, boolean isTop, number itemCount)` yöntemiyle modeller:
- `valueFieldIndex` — öğelerin toplu değerlerine göre sıralandığı veri alanının sıfırdan başlayan dizini.
- `type` — `itemCount` değerinin ne anlama geldiğini belirtir. `PivotFilterType.Count`, sabit sayıda öğe tutar (iletişim kutusundaki Öğeler seçeneği). `PivotFilterType.Percent`, öğelerin belirli bir yüzdesini tutar; dolayısıyla `itemCount` doğrudan yüzde değeridir — 30, en üst yüzde 30'u tutar. `PivotFilterType.Sum`, öğeleri kümülatif değer kapsamına göre sıralar.
- `isTop` — Üst için `true`, Alt için `false`.
- `itemCount` — En Üst N ifadesindeki N; birimi `type` değerine bağlıdır.

```javascript
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PivotTable Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
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
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A1").value = "Sport";
            cells.get("B1").value = "Quarter";
            cells.get("C1").value = "Sales";
            const sports = ["Golf", "Tennis", "Rugby", "Cricket", "Boxing"];
            let row = 2;
            sports.forEach(sport => {
                for (let quarter = 1; quarter <= 3; quarter++) {
                    cells.get(row, 0).value = sport;
                    cells.get(row, 1).value = "Qtr" + quarter;
                    cells.get(row, 2).value = 1000 + 777 * row;
                    row++;
                }
        });
    </script>
</html>
```

{{% alert color="primary" %}}
AutoShow özellikleri ile `filterTop10` iki ayrı mekanizmadır. AutoShow, özet tablo alanı üzerindeki klasik `autoShow` öznitelik kümesini yazar ve Excel 97'den itibaren tüm Excel sürümlerinde dikkate alınır. `filterTop10`, Excel 2007 veya sonrasını gerektiren modern bir `PivotFilter` girdisi yazar. Bir çalışma kitabı daha eski bir Excel sürümünde açıldığında, modern filtreyi kullanan özet tablo tüm öğeleri gösterecek şekilde geri döner. Eski araçlarla açılıp yeniden kaydedilmesi gereken belgelerde AutoShow özelliklerini; modern çalışma kitaplarında ise diğer değer filtreleriyle birleşebildiği için `filterTop10` yöntemini tercih edin.
{{% /alert %}}

## **İlgili Makaleler**
- [Özet Tabloda Pivot Alanlarını Gruplandırma](/cells/tr/javascript-cpp/group-pivot-fields-in-the-pivot-table/)

{{< app/cells/assistant language="javascript-cpp" >}}