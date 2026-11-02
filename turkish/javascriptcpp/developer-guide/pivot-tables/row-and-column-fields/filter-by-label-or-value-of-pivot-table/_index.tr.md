---
title: Özet Tablolarını Etiket veya Değere Göre Filtreleme
linktitle: Özet Tablolarını Etiket veya Değere Göre Filtreleme
description: Aspose.Cells for JavaScript via C++ kapsamlı özet tablosu filtreleme özelliklerini destekler. Bu makale; etiket filtreleri, tarih filtreleri, değer filtreleri ve ilk 10 filtrelerini kullanarak özet tablosu verilerinin nasıl filtreleneceğini, özet tablosu öğelerinin nasıl gizleneceğini veya görünür hâle getirileceğini açıklar.
keywords: Aspose.Cells, JavaScript aracılığıyla C++ kitaplığı, elektronik tablo, özet tablo, filtre, etiket filtresi, değer filtresi, tarih filtresi, ilk 10 filtresi, özet tablosu öğesi, özet tablosu öğesini gizleme
type: docs
weight: 10
url: /tr/javascript-cpp/filter-by-label-or-value-of-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, bir özet tabloda görüntülenen verileri filtrelemek için beş kullanışlı strateji sunar. Metin tabanlı satır veya sütun alanlarına etiket filtreleri uygulayabilir; alan yalnızca tarih-saat hücreleri veya boş değerler içerdiğinde tarih filtreleri kullanabilir; toplulaştırılmış sayılar üzerinde değer filtreleri uygulayabilir; bir değer alanına göre sıralama yapmak için ilk 10 filtresini kullanabilir; ayrıca `isHidden` özelliğiyle özet tablosu öğelerini tek tek gizleyip görünür hâle getirebilirsiniz. Her strateji, `PivotField` ve `PivotItem` sınıflarındaki özel API'ler aracılığıyla kullanılabilir.
{{% /alert %}}

## **Giriş**
Özet tablolar güçlü analitik araçlardır; ancak ham özetler genellikle sunum için ihtiyaç duyduğunuzdan çok daha fazla bilgi içerir. Filtreleme, bir özet tabloyu belirli bir rapor için önemli satırlar, sütunlar veya değerlerle sınırlandırmanın temel mekanizmasıdır. Aspose.Cells for JavaScript via C++, Microsoft Excel'de bulunan filtreleme yeteneklerini sunar ve bunları programatik olarak kullanıma açarak rapor oluşturma sürecinin tamamen otomatikleştirilmesini sağlar.
Bu makalede aşağıdaki filtreleme stratejileri ele alınmaktadır:
1. **Etiket Filtresi** — satır veya sütun alanı öğelerini metin etiketlerine göre filtreler.
2. **Tarih Filtresi** — yalnızca tarih-saat değerleri veya boş değerler içeren satır veya sütun alanlarını filtreler.
3. **Değer Filtresi** — öğeleri bir veri alanının toplulaştırılmış değerlerine göre filtreler.
4. **İlk 10 Filtresi** — bir değer alanına göre sıralanan ilk veya son N öğeyi gösterir.
5. **Özet Tablosu Öğelerini Gizleme / Görünür Hâle Getirme** — bir alandaki her öğenin görünürlüğünü manuel olarak denetler.
Her yaklaşım, `PivotField` sınıfındaki farklı bir yöntemi veya `PivotItem` sınıfındaki bir özelliği kullanır. Herhangi bir filtre uyguladıktan sonra, önbelleğe alınmış verilerin ve hesaplanan değerlerin yeni filtre durumunu yansıtması için özet tablosu üzerinde `pivotCache.refresh()` çağrısı yapmalısınız.

## **Etiket Filtresi**
Etiket filtresi, bir satır veya sütun alanındaki öğelerin metin etiketlerini bir kalıpla karşılaştırarak filtrelemenizi sağlar. Bu özellik; yalnızca adı belirli bir harfle başlayan, belirli bir sözcük içeren veya başka bir etiket ölçütüyle eşleşen ürünleri görüntülemek istediğinizde kullanışlıdır.
Aspose.Cells, etiket filtrelemeyi `pivotField.filterByLabel(PivotFilterType filterType, string label1, string label2)` yöntemiyle sunar. `filterType` argümanı karşılaştırma modunu (`CaptionBeginsWith`, `CaptionContains`, `CaptionEndsWith`, `CaptionDoesNotContain`, `CaptionIsNotBlank`, `CaptionIsBlank` ve benzeri) belirler. `label1` ve `label2` argümanları karşılaştırma metnini sağlar; yalnızca bir karşılaştırma değeriyle işlem yapmak istediğinizde `label2` için `""` değerini geçirin (örneğin, başlangıç veya içerme eşleşmesi).
Aşağıdaki örnek, mevcut bir özet tablo içeren çalışma kitabını yükler, yalnızca etiketleri belirtilen ön eki ile başlayan öğelerin görünür kalmasını sağlayan bir etiket filtresi uygular, özet tabloyu yeniler ve sonucu kaydeder.

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
                    // Pivot tablosu içeren mevcut çalışma kitabını yükle
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    // Çalışma sayfasına dizine göre eriş (ilk çalışma sayfası)
                    const worksheet = workbook.worksheets.get(0);
                    // Pivot tablosuna dizine göre eriş
                    const pivotTable = worksheet.pivotTables.get(0);
                    // İlk satır PivotField alanını al
                    const rowField = pivotTable.rowFields.get(0);
                    // Etiket filtresini uygula — yalnızca etiketleri belirtilen önek ile başlayan satır öğelerini göster
                    rowField.filterByLabel(AsposeCells.PivotFilterType.CaptionBeginsWith, "B", "");
                    // Filtrein etkili olması için pivot tablosu verilerini yenile ve yeniden hesapla
                    pivotTable.refreshData();
                    // Çalışma kitabını diske kaydet
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
Tarih filtreleri, bir özet tabloyu bugün, geçen hafta, bu ay, gelecek çeyrek veya belirli bir tarih aralığı gibi tarihe dayalı ölçütlerle daraltmanızı sağlar. Bunlar, yalnızca tarih-saat bilgisi saklayan alanlarda çalışan özel filtrelerdir.

{{% alert color="primary" %}}
Tarih filtresi; satır veya sütun alanında yalnızca tarih-saat hücreleri veya boş değerler bulunduğunda çalışır. Kaynak alan sayı veya metin gibi diğer veri türlerini içeriyorsa tarih filtresi beklenen sonucu vermez. Bu filtreyi uygulamadan önce alanın tarih olarak biçimlendirildiğinden ve tüm değerlerin geçerli `DateTime` örnekleri veya boş hücreler olduğundan emin olun.
Aspose.Cells, tarih filtrelemeyi `pivotField.filterByDate(PivotFilterType, DateTime[] values)` yöntemiyle sunar. `PivotFilterType` numaralandırması; `Today`, `Yesterday`, `LastWeek`, `ThisWeek`, `NextWeek`, `LastMonth`, `ThisMonth`, `NextMonth`, `LastQuarter`, `ThisQuarter`, `NextQuarter`, `LastYear`, `ThisYear`, `NextYear` ve `Between` gibi özel tarih değerlerini içerir. Seçilen filtre türüne göre bir veya iki `DateTime` değeri belirtirsiniz (`Between` için başlangıç ve bitiş tarihlerini belirtirsiniz).
Aşağıdaki örnek, satır alanında bir tarih alanı bulunan çalışma kitabını ve özet tabloyu yükler, görünür öğeleri belirli bir tarih aralığıyla sınırlayan bir tarih filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.
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
                // Pivot tablosu içeren mevcut çalışma kitabını yükle
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Pivot tablosunu içeren çalışma sayfasına eriş (indeksle)
                const worksheet = workbook.worksheets.get(0);
                // Pivot tablosuna indeksle eriş
                const pivotTable = worksheet.pivotTables.get(0);
                // Tarih PivotField alanını satır alanından al
                // (Tarih filtresi yalnızca satır/sütun alanı yalnızca tarih-saat hücreleri veya boş hücreler içerdiğinde çalışır)
                const dateField = pivotTable.rowFields.get(0);
                // Between filtresi için tarih ölçütünü tanımla
                const startDate = new Date(2020, 0, 1);
                const endDate = new Date(2020, 11, 31);
                // Pivot alanına tarih filtresini uygula
                dateField.filterByDate(AsposeCells.PivotFilterType.DateBetween, startDate, endDate);
                // Filtreyi etkinleştirmek için pivot tablosunu yenile ve yeniden hesapla
                pivotTable.refreshData();
                // Çalışma kitabını kaydet
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
Değer filtreleri, bir özet tablonun veri alanında hesapladığı toplulaştırılmış değerler üzerinde çalışır. Metin etiketleriyle eşleştirmek yerine sayısal toplamları bir eşik değerle karşılaştırırlar. Tipik kullanım örnekleri, yalnızca satış toplamı hedef tutarı aşan ürünleri veya işlem sayısı belirli bir aralıkta bulunan bölgeleri göstermektir.
Aspose.Cells, değer filtrelemeyi `pivotField.filterByValue(int valueFieldIndex, PivotFilterType filterType, double value1, double value2)` yöntemiyle sunar. `valueFieldIndex` parametresi, değerlendirilecek veri alanını belirtir (`pivotTable.getDataFields().indexOf(dataField)` kullanın veya koleksiyon üzerinde gezinerek konumu bulun). `filterType` parametresi; `ValueGreaterThan`, `ValueLessThan`, `ValueBetween`, `ValueEqual`, `ValueNotEqual`, `ValueGreaterThanOrEqual` ve `ValueLessThanOrEqual` gibi değerlerden birini belirtir. İki `double` argümanı gerekli eşik değerleri sağlar.
Aşağıdaki örnek, bir özet tablo içeren çalışma kitabını yükler, yalnızca toplulaştırılmış satışları sayısal eşiği aşan öğeleri koruyan bir değer filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.

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
                // PivotFieldCollection'da IndexOf bulunmadığından veri alanı dizinini elle bul
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
                pivotTable.refreshData();
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
İlk 10 filtresi, seçilen bir değer alanına göre yalnızca en yüksek veya en düşük N öğeyi koruyan, değer filtresinin özel bir türüdür. "gelire göre en iyi 10 ürün" veya "satış sayısına göre en düşük 5 bölge" gibi sıralama raporlarında sıkça kullanılır.

{{% alert color="primary" %}}
İlk 10 filtresi yalnızca özet tablonun veri alanında bir veya daha fazla değer alanı bulunduğunda etkilidir. En az bir değer alanı yoksa, öğeleri sıralamak için toplulaştırılmış bir ölçüt bulunmaz ve filtre uygulanamaz.
Aspose.Cells, ilk 10 filtreleme özelliğini `pivotField.filterTop10(int valueFieldIndex, PivotFilterType filterType, bool isTop, int itemCount)` yöntemiyle sunar. `valueFieldIndex` parametresi, öğelerin toplulaştırılmış değerlerine göre sıralandığı veri alanının dizinidir. `filterType`, `itemCount` birimini seçer (`Count` sabit sayıda öğeyi korur; `Percent` öğelerin belirli bir yüzdesini korur ve bu durumda `itemCount` yüzdenin kendisidir). `isTop`, ilk öğelerin (`true`) mi yoksa son öğelerin (`false`) mi korunacağını belirtir. `itemCount` ise kaç öğenin veya hangi yüzdenin korunacağını tanımlar.
Aşağıdaki örnek, bir değer alanı içeren çalışma kitabını ve özet tabloyu yükler, yalnızca satış toplamına göre en yüksek 10 öğeyi koruyan bir ilk 10 filtresi uygular, özet tabloyu yeniler ve çalışma kitabını kaydeder.
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
                // Pivot tabloyu içeren mevcut çalışma kitabını yükle
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Pivot tabloyu içeren çalışma sayfasına eriş (dizin 0)
                const worksheet = workbook.worksheets.get(0);
                // Pivot tabloya dizin kullanarak eriş
                const pivotTable = worksheet.pivotTables.get(0);
                // Veri alanında en az bir değer PivotField bulunduğunu doğrula
                if (pivotTable.dataFields.count === 0) {
                    throw new Error("Pivot table has no value (data) PivotField.");
                }
                const valueField = pivotTable.dataFields.get(0);
                // Hedef satır PivotField'ini al (Top 10 uygulamak istediğimiz alan)
                const rowField = pivotTable.rowFields.get(0);
                // İlk (ve tek) veri alanı dizin 0'dadır; Top 10 bu alana göre sıralama yapar.
                const valueFieldIndex = 0;
                // Satır alanına Top 10 filtresini uygula:
                //   - valueFieldIndex = 0 — öğeleri sıralamak için kullanılan veri alanı
                //   - filterType  = PivotFilterType.Count (belirli sayıda öğe tut;
                //     PivotFilterType.Percent, 10'u "ilk yüzde 10" olarak yorumlar)
                //   - isTop       = true (ilk N; false ise son N anlamına gelir)
                //   - itemCount   = 10
                rowField.filterTop10(valueFieldIndex, AsposeCells.PivotFilterType.Count, true, 10);
                // Pivot tablo verilerini yenile ve filtrenin etkinleşmesi için yeniden hesapla
                pivotTable.refreshData();
                // Çalışma kitabını kaydet
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

## **Özet Tablosu Öğelerini Gizleyerek veya Görünür Hâle Getirerek Filtreleme**
Yapılandırılmış filtre API'lerinin yanı sıra Aspose.Cells, her özet tablosu öğesinin görünürlüğünü doğrudan denetlemenizi sağlar. `PivotField` nesnesinin `pivotField.getPivotItems()` koleksiyonu üzerinde gezinerek ve `isHidden` özelliğini değiştirerek, formül tabanlı bir filtre uygulamadan belirli öğeleri seçici olarak gizleyebilirsiniz. `pivotItem.isHidden = true` ayarı öğeyi özet tablosunda gizler; `pivotItem.isHidden = false` ayarı öğeyi görünür hâle getirir.
Bu yaklaşım; filtreleme kuralı düzensiz veya öğeye özgü olduğunda, örneğin belirli bir raporda görünmemesi gereken az sayıda adlandırılmış kategoriyi gizlemek için kullanışlıdır. Aşağıdaki örnek, bir özet tablo içeren çalışma kitabını yükler, ada göre belirli bir öğeyi gizler, öğeyi görünür hâle getirme işlemini gösterir, özet tabloyu yeniler ve çalışma kitabını kaydeder.

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
                // Pivot tablo içeren mevcut bir çalışma kitabını yükle
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                // Pivot tablonun bulunduğu ilk çalışma sayfasına eriş
                const sheet = workbook.worksheets.get(0);
                // Dizine göre pivot tabloya eriş (sayfadaki ilk pivot tablo)
                const pivotTable = sheet.pivotTables.get(0);
                // Hedef PivotField'i al (öğeleri gizleyip göstereceğimiz ilk satır etiketi alanı)
                const pivotField = pivotTable.rowFields.get(0);
                // Seçilen PivotField'in PivotItems koleksiyonunda yinele
                const itemCount = pivotField.pivotItems.count;
                for (let i = 0; i < itemCount; i++) {
                    const item = pivotField.pivotItems.get(i);
                    // Belirli bir ad veya ölçütle eşleşen pivot öğelerini gizle
                    if (item.name === "Item1" || item.name === "Item2") {
                        item.isHidden = true;
                    }
                    // Gizlemeyi gösterme: daha önce gizlenmiş bir pivot öğesini yeniden göster
                    if (item.name === "Item3") {
                        item.isHidden = false;
                    }
                }
                // Değişikliklerin etkili olması için pivot tabloyu yenile ve yeniden hesapla
                pivotTable.refreshData();
                // Çalışma kitabını kaydet — gizli öğeler temel veride kalır
                // ancak görüntülenen pivot tablo çıktısından hariç tutulur
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
Aspose.Cells for JavaScript via C++, Microsoft Excel'deki filtreleme yeteneklerini kapsayan eksiksiz bir özet tablosu filtreleme özellikleri seti sunar. Etiket, tarih ve değer filtreleri en yaygın analitik senaryoları kapsarken ilk 10 filtresi sıralama raporları için kullanılır. Filtreleme kuralı düzensiz olduğunda `pivotItem.isHidden` özelliği, öğe bazında esnek bir alternatif sunar. Bu stratejileri birleştirerek — örneğin bir etiket filtresi uygulayıp ardından belirli öğeleri gizleyerek — yalnızca kodla, tam olarak hedeflenmiş özet tablosu raporları oluşturabilirsiniz.

{{< app/cells/assistant language="javascript-cpp" >}}