---
title: Özet Tablolarını Etiket veya Değere Göre Filtreleme
linktitle: Özet Tablolarını Etiket veya Değere Göre Filtreleme
description: Aspose.Cells for JavaScript via C++ kapsamlı özet tablo filtreleme özelliklerini destekler. Bu makale; etiket filtreleri, tarih filtreleri, değer filtreleri ve ilk 10 filtresi aracılığıyla özet tablo verilerinin nasıl filtrelendiğini ve özet tablo öğelerinin nasıl gizleneceğini ya da görünür hâle getirileceğini açıklar.
keywords: Aspose.Cells, JavaScript via C++ kitaplığı, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet tablo öğesi, özet tablo öğesini gizleme
type: docs
weight: 10
url: /tr/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir özet tabloda görüntülenen verileri filtrelemek için beş pratik strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir, alan yalnızca tarih-saat hücrelerinden veya boş değerlerden oluşuyorsa tarih filtreleri kullanabilir, toplulaştırılmış sayılar üzerinde değer filtreleri uygulayabilir, bir değer alanına göre sıralama yapmak için ilk 10 filtresini kullanabilir veya `isHidden` özelliğini kullanarak özet tablo öğelerini tek tek gizleyebilir ve görünür hâle getirebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıflarındaki ayrı API'lerle sunulur.
{{% /alert %}}

## **Giriş**
Özet tablolar güçlü analitik araçlardır; ancak ham özetler genellikle sunmak istediğinizden çok daha fazla bilgi içerir. Filtreleme, bir özet tabloyu belirli bir rapor için yalnızca önemli satırları, sütunları veya değerleri içerecek şekilde daraltmanın temel mekanizmasıdır. Aspose.Cells for JavaScript via C++, Microsoft Excel'de bulunan filtreleme özelliklerini yansıtır ve bunları programatik olarak sunar; böylece rapor oluşturma tamamen otomatikleştirilebilir.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — satır veya sütun alanının öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri (veya boş değerler) içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplulaştırılmış değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanan en yüksek veya en düşük N öğeyi gösterir.
5. **Özet Tablo Öğelerini Gizleme / Görünür Hâle Getirme** — bir alandaki her öğenin görünürlüğünü elle denetler.
Her yaklaşım, `PivotField` sınıfındaki farklı bir yöntemi veya `PivotItem` sınıfındaki bir özelliği kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tabloda `pivotCache.refresh()` çağrısı yapmalısınız.

## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanının öğelerini metin etiketlerini bir kalıpla karşılaştırarak filtrelemenize olanak tanır. Bu, yalnızca adları belirli bir harfle başlayan, belirli bir kelimeyi içeren veya başka bir etikete dayalı ölçütle eşleşen ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemesini `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` yöntemiyle sunar. `filterType` bağımsız değişkeni karşılaştırma modunu belirler (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri). `label1` ve `label2` bağımsız değişkenleri karşılaştırma metnini belirtir — yalnızca tek bir karşılaştırma değeri gerektirdiğinizde `label2` için `""` iletin (örneğin, belirli bir metinle başlar veya belirli bir kelimeyi içerir filtrelerinde).
Mevcut bir özet tablo içeren çalışma kitabını yükleyen, yalnızca belirli bir önek ile başlayan öğelerin görünür kalmasını sağlayan bir etiket filtresi uygulayan, özet tabloyu yenileyen ve sonucu kaydeden örnek aşağıda verilmiştir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, SaveFormat } = AsposeCells;
            const fileInput = document.getElementById("fileInput");
            const runExampleButton = document.getElementById("runExample");
            const downloadLink = document.getElementById("downloadLink");
            const result = document.getElementById("result");
            AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            runExampleButton.addEventListener("click", async () => {
                try {
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                        return;
                    }
                    // Load the existing workbook containing a pivot table
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Access the worksheet by index (first worksheet)
                    const worksheet = workbook.worksheets.get(0);
                    // Access the pivot table by index
                    const pivotTable = worksheet.pivotTables.get(0);
                    // Retrieve the first row PivotField
                    const rowField = pivotTable.rowFields.get(0);
                    // Apply the label filter — show only row items whose labels begin with the supplied prefix
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Refresh and recalculate the pivot table data so the filter takes effect
                    pivotTable.pivotCache.refresh();
                    // Save the workbook back to disk
                    const outputData = workbook.save(SaveFormat.Xlsx);
                    const blob = new Blob([outputData], {
                        type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                    });
                    downloadLink.href = URL.createObjectURL(blob);
                    downloadLink.download = "sample.xlsx";
                    downloadLink.style.display = "block";
                    result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
                } catch (error) {
                    console.error(error);
                    result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + "</p>";
                }
            });
        </script>
    </body>
</html>
```

## **Tarih Filtresi**
Tarih filtreleri, bir özet tabloyu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarihe dayalı ölçütlerle daraltmanıza olanak tanır. Bunlar, yalnızca tarih-saat bilgisi saklayan alanlarda kullanılabilen özel filtrelerdir.

{{% alert color="primary" %}}
Tarih filtresi, yalnızca satır veya sütun alanında tarih-saat hücreleri veya boş değerler bulunduğunda çalışır. Alanın temel verileri sayı veya metin gibi diğer veri türlerini içeriyorsa, tarih filtresi beklenen sonucu vermez. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.
Aspose.Cells, tarih filtrelemesini `pivotField.filterByDate(PivotFilterType, DateTime[] values)` yöntemiyle sunar. `PivotFilterType` sabit listesi `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi belirli tarih değerlerini içerir. Seçilen filtre türüne bağlı olarak bir veya iki `DateTime` değeri iletirsiniz (`Between` için başlangıç ve bitiş tarihlerini iletirsiniz).
Mevcut bir özet tablo içeren ve satır alanında bir tarih alanı bulunan çalışma kitabını yükleyen, görünür öğeleri belirli bir tarih aralığıyla sınırlayan bir tarih filtresi uygulayan, özet tabloyu yenileyen ve çalışma kitabını kaydeden örnek aşağıda verilmiştir.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook } = AsposeCells;
        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Source workbook not found.");
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (by index)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Retrieve the date PivotField from the row area
                // (Date filter only works when the row/column area contains only date-time cells or blanks)
                const dateField = pivotTable.rowFields.get(0);
                // Define the date criterion for the Between filter
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Apply the date filter on the pivot field
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Refresh and recalculate the pivot table so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Persist the workbook
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
                console.error(error);
            }
        });
    </script>
</html>
```

## **Değer Filtresi**
Değer filtreleri, bir özet tablonun veri alanında hesapladığı toplulaştırılmış değerler üzerinde çalışır. Metin etiketleriyle eşleştirmek yerine, sayısal toplamları bir eşik değerle karşılaştırırlar. Tipik kullanım örnekleri; yalnızca satış toplamı hedef tutarı aşan ürünleri veya işlem sayısı belirli bir aralıkta bulunan bölgeleri göstermektir.
Aspose.Cells, değer filtrelemesini `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` yöntemiyle sunar. `valueFieldIndex` parametresi, değerlendirilecek veri alanını belirtir. Konumu `pivotTable.getDataFields().indexOf(dataField)` ile bulabilir veya koleksiyon üzerinde yineleyerek belirleyebilirsiniz. `filterType` parametresi `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerlerden birini belirtir. İki `double` bağımsız değişkeni eşik değeri veya değerlerini belirtir.
Mevcut bir özet tablo içeren çalışma kitabını yükleyen, yalnızca toplulaştırılmış satışları bir sayısal eşiği aşan öğeleri tutan bir değer filtresi uygulayan, özet tabloyu yenileyen ve çalışma kitabını kaydeden örnek aşağıda verilmiştir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
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
            const downloadLink = document.getElementById('downloadLink');
            const file = fileInput.files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const pivotTable = worksheet.pivotTables.get(0);
                const rowField = pivotTable.rowFields.get(0);
                const dataField = pivotTable.dataFields.get(0);
                // Find the data field index manually since PivotFieldCollection doesn't have IndexOf
                let dataFieldIndex = -1;
                for (let i = 0; i < pivotTable.dataFields.count; i++) {
                    if (pivotTable.dataFields.get(i) === dataField) {
                        dataFieldIndex = i;
                        break;
                    }
                }
                if (dataFieldIndex >= 0) {
                    rowField.filterByValue(
                        dataFieldIndex,
                        AsposeCells.PivotFilterType.ValueGreaterThan,
                        5000,
                        Number.MAX_VALUE
                    );
                }
                pivotTable.pivotCache.refresh();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = `<p style="color: red;">${error.message}</p>`;
            }
        });
    </script>
</html>
```

## **İlk 10 Filtresi**
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi tutan, değer filtresinin özelleşmiş bir biçimidir. Gelire göre ilk 10 ürün veya satış sayısına göre en alt 5 bölge gibi sıralama raporlarında sıkça kullanılır.

{{% alert color="primary" %}}
İlk 10 filtresi yalnızca özet tablonun veri alanı bölümünde bir veya daha fazla değer alanı bulunduğunda etkilidir. En az bir değer alanı yoksa, öğeleri sıralayacak toplulaştırılmış bir ölçüt bulunmaz ve filtre uygulanamaz.
Aspose.Cells, ilk 10 filtrelemesini `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` yöntemiyle sunar. `valueFieldIndex` parametresi, öğelerin toplulaştırılmış değerlere göre sıralanmasını sağlayan veri alanının dizinidir; `filterType`, `itemCount` birimini seçer (`Count` sabit sayıda öğeyi, `Percent` ise öğelerin belirtilen yüzdesini tutar; bu nedenle `itemCount` yüzde değerinin kendisidir), `isTop`, üstteki öğelerin (true) mi yoksa alttaki öğelerin (false) mi tutulacağını belirtir; `itemCount` ise kaç öğenin veya öğelerin yüzde kaçının tutulacağını belirler.
Mevcut bir özet tablo içeren ve bir değer alanı bulunan çalışma kitabını yükleyen, satış toplamına göre yalnızca en yüksek 10 öğeyi tutan bir ilk 10 filtresi uygulayan, özet tabloyu yenileyen ve çalışma kitabını kaydeden örnek aşağıda verilmiştir.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            try {
                const file = fileInput.files[0];
                if (!file) {
                    result.textContent = "Please select an input workbook.";
                    return;
                }
                // Load the existing workbook that contains the pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the worksheet that holds the pivot table (index 0)
                const worksheet = workbook.worksheets.get(0);
                // Access the pivot table by index
                const pivotTable = worksheet.pivotTables.get(0);
                // Confirm there is at least one value PivotField in the data area
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Retrieve the target row PivotField (the field we want to apply Top 10 on)
                const rowField = pivotTable.rowFields.get(0);
                // The first (and only) data field is at index 0; Top 10 ranks by it.
                const valueFieldIndex = 0;
                // Apply the Top 10 filter on the row field:
                //   - valueFieldIndex = 0 — the data field used to rank items
                //   - filterType  = PivotFilterType.Count (keep a fixed number of items;
                //     PivotFilterType.Percent would interpret 10 as "top 10 percent")
                //   - isTop       = true (top N; false would mean bottom N)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Refresh the pivot table data and recalculate it so the filter takes effect
                pivotTable.pivotCache.refresh();
                // Save the workbook
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.textContent = `Error: ${error.message || error}`;
            }
        });
    </script>
</html>
```

## **Özet Tablo Öğelerini Gizleyerek veya Görünür Hâle Getirerek Filtreleme**
Yapılandırılmış filtre API'lerine ek olarak, Aspose.Cells her özet tablo öğesinin görünürlüğünü doğrudan denetlemenizi sağlar. `PivotField` nesnesinin `pivotField.getPivotItems()` koleksiyonunda yineleyerek ve `isHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `pivotItem.isHidden = true` ayarı öğeyi özet tablodan gizler; `pivotItem.isHidden = false` ayarı öğeyi görünür hâle getirir.
Bu yaklaşım; belirli bir raporda görünmemeleri gereken, adlandırılmış kategorilerden yalnızca birkaçını gizlemek gibi düzensiz veya öğeye özgü filtre kurallarında kullanışlıdır. Aşağıdaki örnek, bir özet tabloyu yükler, belirli bir öğeyi adına göre gizler, bir öğenin görünür hâle getirilmesini gösterir, özet tabloyu yeniler ve çalışma kitabını kaydeder.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
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
            const result = document.getElementById('result');
            const downloadLink = document.getElementById('downloadLink');
            const file = document.getElementById('fileInput').files[0];
            if (!file) {
                result.innerHTML = '<p style="color: red;">Please select a workbook containing a pivot table.</p>';
                return;
            }
            try {
                // Load an existing workbook containing a pivot table
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Access the first worksheet which contains the pivot table
                const sheet = workbook.worksheets.get(0);
                // Access the pivot table by index (the first pivot table on the sheet)
                const pivotTable = sheet.pivotTables.get(0);
                // Retrieve the target PivotField (the first row label field that we'll hide/unhide items in)
                const pivotField = pivotTable.rowFields.get(0);
                // Iterate through the PivotItems collection of the selected PivotField
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Hide pivot items that match a specific name/criterion
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Demonstrate unhiding: re-show a previously hidden pivot item
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Refresh and recalculate the pivot table so changes take effect
                pivotTable.pivotCache.refresh();
                // Save the workbook — hidden items stay in the underlying data
                // but are excluded from the displayed pivot table output
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output_pivot_filtered.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Özet**
Aspose.Cells for JavaScript via C++, Microsoft Excel'de bulunanlarla eşleşen kapsamlı özet tablo filtreleme özelliklerini sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsarken, ilk 10 filtresi sıralama raporlarını ele alır. Filtreleme kuralı düzensiz olduğunda, `pivotItem.isHidden` özelliği öğe düzeyinde esnek bir alternatif sağlar. Bu stratejileri birleştirerek — örneğin bir etiket filtresi uygulayıp ardından belirli öğeleri gizleyerek — yalnızca kod kullanarak tam olarak hedeflenmiş özet tablo raporları oluşturabilirsiniz.

{{< app/cells/assistant language="javascript-cpp" >}}