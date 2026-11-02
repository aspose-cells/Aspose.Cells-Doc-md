---
title: Aspose.Cells for JavaScript via C++ ile Özet Tabloya Filtre Alanları Ekleme
linktitle: Aspose.Cells for JavaScript via C++ ile Özet Tabloya Filtre Alanları Ekleme
description: Aspose.Cells for JavaScript via C++ kullanarak özet tablolarda filtre alanlarını nasıl ekleyeceğinizi ve yapılandıracağınızı öğrenin. Bu kılavuz, filtre alanları ekleme, tekli seçimle filtreleme ve çoklu seçimle filtreleme senaryolarını kapsar.
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++, özet tablo, filtre alanı, PivotFieldType.Page, PageFields, IsMultipleItemSelectionAllowed, CurrentPageItem, PivotItem, IsHidden, filtre
type: docs
weight: 250
url: /tr/javascript-cpp/add-page-field-in-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet tablolardaki filtre alanlarının tüm yaşam döngüsünü destekler. Bir filtre alanını yüksek seviyeli kolaylık API'si veya daha alt seviyeli `getPageFields()` koleksiyonu aracılığıyla ekleyebilir, filtreyi tekli seçim modunda kullanabilir, filtreyi temizleyerek tüm filtre öğelerini gösterebilir veya alanı çoklu seçime geçirerek kullanıcıların Excel'deki onay kutusu arayüzü üzerinden aynı anda birden fazla filtre öğesi seçmesini sağlayabilirsiniz.
{{% /alert %}}

## **Giriş**
Filtre alanı, özet tablo gövdesinin kaynak verinin hangi alt kümesini görüntüleyeceğini denetleyen bir özet tablo alanıdır. Son kullanıcılar bunu Excel'de oluşturulan özet tablonun üst kısmındaki bir açılır listede görür. Kullanılabilir filtre öğelerinden biri seçildiğinde özet tablo gövdesi yeniden oluşturulur ve yalnızca o filtre öğesine ait kayıtlar özetlenir. Bir özet tablo alanı, `PivotFieldType.Row`, `PivotFieldType.Column` veya `PivotFieldType.Data` yerine `PivotFieldType.Page` olarak tanımlandığında filtre alanına dönüşür.

## **Filtre Alanı Ekleme**

### `addFieldToArea` ile Filtre Alanı Ekleme
Aşağıdaki örnek, küçük bir `Fruit` / `Year` / `Amount` veri kümesi oluşturur, E3 hücresine bir özet tablo yerleştirir, `Fruit` alanını satır alanına, `Amount` alanını veri alanına ve `Year` alanını filtre alanına ekler, özet tabloyu yeniler ve çalışma kitabını kaydeder.

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
            // Yeni bir çalışma kitabı oluştur
            const workbook = new Workbook();
            const worksheet = workbook.worksheets.get(0);
            worksheet.name = "Data";
            // Başlık satırını ayarla
            const cells = worksheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // Örnek verilerle 9 satır doldur: Fruit, Year, Amount
            const data = [
                ["apple", 2020, 100],
                ["banana", 2021, 200],
                ["apple", 2021, 150],
                ["grape", 2020, 120],
                ["orange", 2022, 180],
                ["banana", 2020, 90],
                ["grape", 2021, 130],
                ["apple", 2022, 170],
                ["orange", 2021, 110]
            ];
            for (let i = 0; i < data.length; i++) {
                cells.get(i + 1, 0).value = data[i][0];
                cells.get(i + 1, 1).value = data[i][1];
                cells.get(i + 1, 2).value = data[i][2];
            }
            // E3 hücresine sabitlenmiş bir pivot tablo ekle
            const pivotTableIndex = worksheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = worksheet.pivotTables.get(pivotTableIndex);
            // Alanları ilgili alanlara ekle: Fruit Satır, Amount Veri, Year Sayfa alanı olarak
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            // Pivot tablo verilerini yenile ve hesapla
            pivotTable.calculateData();
            // Çalışma kitabını kaydet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "pageFieldSample.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

### `getPageFields().add` ile Filtre Alanı Ekleme
Halihazırda bir `PivotField` örneğiyle çalışıyorsanız, bu nesneyi doğrudan `pivotTable.getPageFields().add(pivotField)` çağrısında kullanabilirsiniz. Özet tablo ve filtre alanı, önceki senaryodaki gibi oluşturulur; yalnızca son filtre alanı kaydı, alt seviyeli API çağrısıyla değiştirilir.

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
            // — Pivot tablo ve sayfa alanı, tam olarak
            //   Senaryo 1a'daki gibi oluşturulur (Fruit/Year/Amount verisi, pivot E3'te,
            //   Fruit→Satır, Amount→Veri). Aşağıda Year PivotField'i
            //   BaseFields koleksiyonundan alıp PageFields.Add'e geçiriyoruz —
            //   AddFieldToArea'nın düşük seviyeli alternatifi. Sonuç,
            //   işlevsel olarak Senaryo 1a ile aynıdır.
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Başlıklar
            sheet.cells.get("A1").value = "Fruit";
            sheet.cells.get("B1").value = "Year";
            sheet.cells.get("C1").value = "Amount";
            // Örnek veri (9 satır)
            sheet.cells.get("A2").value = "apple";    sheet.cells.get("B2").value = "2020"; sheet.cells.get("C2").value = 100;
            sheet.cells.get("A3").value = "apple";    sheet.cells.get("B3").value = "2021"; sheet.cells.get("C3").value = 150;
            sheet.cells.get("A4").value = "apple";    sheet.cells.get("B4").value = "2022"; sheet.cells.get("C4").value = 200;
            sheet.cells.get("A5").value = "grape";    sheet.cells.get("B5").value = "2020"; sheet.cells.get("C5").value = 300;
            sheet.cells.get("A6").value = "grape";    sheet.cells.get("B6").value = "2021"; sheet.cells.get("C6").value = 400;
            sheet.cells.get("A7").value = "grape";    sheet.cells.get("B7").value = "2022"; sheet.cells.get("C7").value = 500;
            sheet.cells.get("A8").value = "blueberry"; sheet.cells.get("B8").value = "2020"; sheet.cells.get("C8").value = 250;
            sheet.cells.get("A9").value = "blueberry"; sheet.cells.get("B9").value = "2021"; sheet.cells.get("C9").value = 350;
            sheet.cells.get("A10").value = "blueberry"; sheet.cells.get("B10").value = "2022"; sheet.cells.get("C10").value = 450;
            // E3 konumunda A1:C10 aralığını kapsayan pivot tabloyu ekle
            const pivotTableIndex = sheet.pivotTables.add("=A1:C10", "E3", "PivotTable1");
            const pivotTable = sheet.pivotTables.get(pivotTableIndex);
            // Fruit -> Satır, Amount -> Veri (Year aşağıda Sayfa alanına gidecek)
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Düşük seviyeli yaklaşım: mevcut Year PivotField'i BaseFields'ten al
            // ve PageFields.Add(PivotField) kullanarak Sayfa alanına kaydet.
            const yearField = pivotTable.baseFields.get("Year");
            pivotTable.pageFields.add(yearField);
            // Yeni sayfa alanının kaydedilen çalışma kitabına yansıması için yenile
            pivotTable.calculateData();
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Tekli Seçimle Filtreleme (Tek Bir Filtre Öğesini Gösterme)**
Varsayılan tekli seçim davranışında filtre alanı tek bir açılır liste olarak görüntülenir ve `pivotField.currentPageItem` tamsayı değeri, özet tablo gövdesinde hangi filtre öğesinin kullanılacağını belirler. Belirli bir dizin atamak yalnızca o öğeyi seçer; özel `0x7FFD` (ondalık 32765) değerini atamak ise filtreyi temizler ve tüm filtre öğelerinin aynı anda özetlenmesini sağlar. Tekli seçim varsayılandır; açıkça etkinleştirmeniz gerekmez.

### Tüm Öğeleri Gösterme
`currentPageItem` özelliğini özel `0x7FFD` değerine ayarlamak filtreyi temizlemekyle eşdeğerdir: özet tablo gövdesi, hiçbir filtre uygulanmamış gibi her filtre öğesini özetler.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <button id="runExample" disabled>Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;
        const readyPromise = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
            document.getElementById('runExample').disabled = false;
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            // Yeni bir çalışma kitabı oluştur
            const workbook = new Workbook();
            const sheet = workbook.worksheets.get(0);
            // Fruit/Year/Amount verilerini doldur
            const cells = sheet.cells;
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            const data = [
                ["Apple", 2022, 100],
                ["Apple", 2023, 150],
                ["Banana", 2022, 80],
                ["Banana", 2023, 120],
                ["Cherry", 2022, 200],
                ["Cherry", 2023, 250]
            ];
            for (let r = 0; r < data.length; r++) {
                for (let c = 0; c < data[r].length; c++) {
                    cells.get(r + 1, c).value = data[r][c];
                }
            }
            // E3 konumunda pivot tablo oluştur
            const pivotTables = sheet.pivotTables;
            const pivotTableIndex = pivotTables.add("=A1:C7", "E3", "PivotTable1");
            const pivotTable = pivotTables.get(pivotTableIndex);
            // Pivot alanlarını yapılandır: Fruit→Satır, Amount→Veri, Year→Sayfa
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
            pivotTable.calculateData();
            // Sayfa filtresini temizle ki sayfa alanındaki her öğe görünür olsun.
            // 0x7FFD (ondalık 32765), "tüm öğeler" anlamına gelen özel sentinel değerdir —
            // Excel'ın sayfa alanı açılır listesinde "(Tümü)" seçmeye eşdeğerdir.
            pivotTable.pageFields.get(0).currentPageItem = 0x7FFD;
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
        </script>
    </body>
</html>
```

### Belirli Bir Öğeyi Gösterme
`currentPageItem` özelliğini geçerli bir dizine ayarlamak yalnızca o filtre öğesini seçer. Dizin, öğenin filtre alanının sıralanmış öğe listesindeki konumunu belirtir; dolayısıyla örneğin `1`, sıralamadan sonraki ikinci öğeyi seçer.

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
            document.getElementById("runExample").addEventListener("click", async () => {
                // Create workbook
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Add sample data (Fruit/Year/Amount)
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "Apple";
                cells.get("B2").value = "2020";
                cells.get("C2").value = "100";
                cells.get("A3").value = "Apple";
                cells.get("B3").value = "2021";
                cells.get("C3").value = "150";
                cells.get("A4").value = "Banana";
                cells.get("B4").value = "2020";
                cells.get("C4").value = "200";
                cells.get("A5").value = "Banana";
                cells.get("B5").value = "2021";
                cells.get("C5").value = "250";
                // Add pivot table at E3
                const pivotTables = sheet.pivotTables;
                const pivotTableIndex = pivotTables.add("=A1:C5", "E3", "PivotTable1");
                const pivotTable = pivotTables.get(pivotTableIndex);
                // Add fields: Fruit→Row, Amount→Data, Year→Page
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // Page-field-specific operations
                pivotTable.pageFields.get(0).currentPageItem = 1; // 1 = second item in sorted order (e.g. "2021")
                // Refresh and calculate pivot table
                pivotTable.calculateData();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

## **Çoklu Seçimle Filtreleme**
Çoklu seçimle filtreleme, filtre açılır listesini onay kutusu listesine dönüştürür ve son kullanıcının aynı anda birden fazla filtre öğesi seçmesini sağlar. Aspose.Cells birlikte çalışan iki özellik sunar. `pivotField.isMultipleItemSelectionAllowed` özelliğinin `true` olarak ayarlanması, çoklu seçim arayüzünün etkinleşmesi için zorunludur. Etkinleştirildikten sonra `pivotItem.isHidden` özelliği, onay kutusu listesinde hangi öğelerin görüneceğini denetler; böylece tüm öğeleri gösterebilir veya yalnızca belirli öğeleri görünür tutabilirsiniz.

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
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                // — Pivot tablo ve sayfa alanı tam olarak
                //   Senaryo 1a'daki gibi oluşturulur (Fruit/Year/Amount verisi, E3'te pivot,
                //   Fruit→Satır, Amount→Veri, Year→Sayfa, AddFieldToArea kullanılarak).
                //   Aşağıda sayfa alanına çoklu seçim filtresi uyguluyoruz.
                const workbook = new Workbook();
                const sheet = workbook.worksheets.get(0);
                const cells = sheet.cells;
                // Örnek veri: Fruit | Year | Amount
                cells.get(0, 0).value = "Fruit";
                cells.get(0, 1).value = "Year";
                cells.get(0, 2).value = "Amount";
                const data = [
                    ["apple", "2019", "100"],
                    ["apple", "2020", "150"],
                    ["apple", "2021", "200"],
                    ["banana", "2019", "110"],
                    ["banana", "2020", "160"],
                    ["banana", "2021", "210"],
                    ["grape", "2019", "120"],
                    ["grape", "2020", "170"],
                    ["grape", "2021", "220"]
                ];
                for (let i = 0; i < data.length; i++) {
                    cells.get(i + 1, 0).value = data[i][0];
                    cells.get(i + 1, 1).value = Number(data[i][1]);
                    cells.get(i + 1, 2).value = Number(data[i][2]);
                }
                const pivotSheet = workbook.worksheets.add("Pivot");
                const pivots = pivotSheet.pivotTables;
                const pivotTableIndex = pivots.add("=A1:C10", "E3", "PivotTable1");
                const pivotTable = pivots.get(pivotTableIndex);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Page, "Year");
                // — Sayfa alanında çoklu seçimi etkinleştir
                const pageField = pivotTable.pageFields.get(0);
                pageField.isMultipleItemSelectionAllowed = true;
                const pivotItems = pageField.pivotItems;
                // Bölüm A — TÜM öğeleri seç (her öğeyi görünür yap)
                for (let i = 0; i < pivotItems.count; i++) {
                    pivotItems.get(i).isHidden = false;
                }
                // Bölüm B — Kaynak değerine göre yalnızca belirli öğeleri seç
                for (let i = 0; i < pivotItems.count; i++) {
                    const pivotItem = pivotItems.get(i);
                    switch (pivotItem.getStringValue()) {
                        case "2020":
                        case "grape":
                        case "blueberry":
                            pivotItem.isHidden = false;
                            break;
                        default:
                            pivotItem.isHidden = true;
                            break;
                    }
                }
                pivotTable.calculateData();
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById('result').innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        </script>
    </body>
</html>
```

> **Not:** `pivotItem.isHidden` üzerinden çoklu seçimli filtreleme kullanılırken, **en az bir `PivotItem` görünür durumda kalmalıdır** (`isHidden === false`). Tüm öğeler gizlenirse Excel dosyayı açarken çöker veya boş bir özet tablo görüntüler. Çoklu seçim izin listenizin kaynak verinizdeki en az bir öğeyi içerdiğini mutlaka doğrulayın.

## **Hangi API ve Hangi Mod Kullanılmalı?**
Aşağıdaki tablo, her API'nin ve modun ne zaman kullanılacağını özetler; böylece her senaryoyu ayrıntılı olarak okumadan doğru birleşimi seçebilirsiniz.
| Senaryo / Kullanım Alanı | Önerilen API | Kullanılan Özellik | Notlar |
|---|---|---|---|
| Kaynak sütun adına göre filtre alanı ekleme (en yaygın kullanım) | `pivotTable.addFieldToArea(PivotFieldType.Page, "fieldName")` | Yok | Yüksek seviyeli, tek satırlık çözüm. Bir `PivotField` referansına ihtiyacınız yoksa bu yöntemi kullanın. |
| Elinizde bir `PivotField` nesnesi olduğunda filtre alanı ekleme | `pivotTable.getPageFields().add(pivotField)` | Yok | Alan nesnesi başka bir yerden elde edilmişse veya yeniden kullanılacaksa bu yöntemi kullanın. |
| Tek bir filtre öğesine göre filtreleme (varsayılan mod) | `pivotField.currentPageItem` | Belirli bir dizine ayarlanır | Örneğin, `1` sıralanmış listedeki ikinci öğeyi gösterir. |
| Tüm öğeleri gösterme / filtreyi temizleme | `pivotField.currentPageItem` | `0x7FFD` olarak ayarlanır | Özel `0x7FFD` değeri (ondalık 32765), "tüm öğeler" durumu için kullanılan sentinel değeridir. |
| Excel'de çoklu seçim arayüzünü etkinleştirme | `pivotField.isMultipleItemSelectionAllowed` | `true` olarak ayarlanır | Herhangi bir `isHidden` atamasının etkili olabilmesi için gereklidir. |
| Çoklu seçim listesinde bireysel öğeleri gizleme/gösterme | `pivotItem.isHidden` | Her öğe için ayarlanır | En az bir öğe görünür durumda kalmalıdır (`isHidden === false`). |

{{% alert color="primary" %}}
Çoklu seçimli filtrelemeyi yapılandırırken görünürlük kısıtını mutlaka hatırlayın. Çoklu seçimli bir filtre alanındaki tüm `PivotItem` öğeleri gizlenirse Excel, dosya açılırken çöker veya boş bir özet tablo görüntüler. İzin verilen öğeler listesini kaynak verinize göre oluşturun ve en az bir öğenin görünür kalmasını sağlayın; böylece kaydettiğiniz çalışma kitapları her makinede güvenilir şekilde açılır.
{{% /alert %}}

{{< app/cells/assistant language="javascript-cpp" >}}