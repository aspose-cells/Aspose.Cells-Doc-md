---
title: Aspose.Cells for JavaScript via C++ ile Özet Tablolarını ve Özet Önbelleklerini Yenileyin
linktitle: Aspose.Cells for JavaScript via C++ ile Özet Tablolarını ve Özet Önbelleklerini Yenileyin
description: Aspose.Cells for JavaScript via C++ v26.7+ özet tablo yenileme API'sini kullanarak özet tablolarının nasıl yenileneceğini öğrenin. Bu makale; workbook.refreshAll, worksheet.refreshPivotTables, pivotCache.refresh, pivotTable.calculateData ve pivotCache.getPivotTables işlevlerini pratik kod örnekleriyle ele alır.
keywords: Aspose.Cells, JavaScript via C++, özet tablo, yenileme, PivotCache, calculateData, refreshAll, refreshPivotTables, getPivotTables, v26.7
type: docs
weight: 200
url: /tr/javascript-cpp/refresh-pivot-table/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells, özet tablo verisini çalışma kitabının tamamından tek bir özet tablosuna kadar dört farklı kapsamda yeniden yüklemenizi sağlayan katmanlı bir yenileme API'si sunar. **Aspose.Cells for JavaScript via C++ v26.7** sürümüyle birlikte, eski `pivotTable.refreshData()` yöntemi kullanımdan kaldırılmış olarak işaretlenmiştir ve bu makalede açıklanan, daha verimli ve önbelleği dikkate alan API'lerle değiştirilmelidir.
{{% /alert %}}

## Giriş
Bir özet tabloyu yenilemek genellikle tek bir işlem değildir. Aspose.Cells arka planda, kaynak verilerinizi çalışma sayfasında görüntülenen değerlere bağlayan katmanlı bir veri zinciri sürdürür. Bu zinciri anlamak, her durum için doğru yenileme API'sini seçmenin anahtarıdır.
Dört katmanlı veri zinciri şöyledir:
1. **Veri Kaynağı** — ham değerlerin bulunduğu kaynak çalışma sayfası aralıkları, veritabanı sorgusu veya birleştirme aralığı.
2. **PivotCache** — kaynak verinin bellek içi anlık görüntüsü. Her özet tablo bir `PivotCache` üzerine kuruludur; tüm veriler burada toplanır ve birleştirilir.
3. **PivotTable** — satır, sütun, değer ve filtre alanlarını tanımlayan görünüm nesnesi. Bir `PivotTable` yalnızca kendi `PivotCache` öğesinden okur, hiçbir zaman doğrudan veri kaynağından okumaz.
4. **Cells** — `getCells()` işlevinin döndürdüğü çalışma sayfası hücreleri; `PivotTable` hesaplanan değerlerini ve biçimlerini bu hücrelere işler.

{{% alert color="primary" %}}
`pivotCache.getSourceType()` (`PivotTableSourceType` enum'ü), önbellek verisinin nereden geldiğini gösterir. v26.7 sürümü itibarıyla `pivotCache.refresh()` yalnızca **`SHEET`** ve **`CONSOLIDATION`** kaynak türlerini destekler; yani çalışma sayfası aralıklarında bulunan verileri. Harici kaynaklar (veritabanları, harici bağlantılar vb.) önbellek API'si üzerinden henüz yenilenemez.
Bu veri zinciri nedeniyle Aspose.Cells içinde iki temel yenileme yolu vardır:
- **`pivotTable.calculateData()`** — veri kaynağına geri dönüş yapmadan, önbelleğe alınmış verilerden tek bir `PivotTable` öğesinin görünümünü yeniden hesaplar.
Bu makaledeki tüm senaryolarda kaynak veri çalışma sayfası hücrelerinden gelir; bu nedenle kaynak türü `SHEET` değerindedir ve yenileme işlemleri açıklandığı gibi davranır.
{{% /alert %}}

## Hızlı Başlangıç
Yalnızca çalışma kitabındaki tüm özet tabloları yenilemek için en kısa kodu istiyorsanız, tek bir çağrı yeterlidir:

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
                result.innerHTML = '<p style="color: red;">Please select an input file.</p>';
                return;
            }
            try {
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                workbook.refreshAll();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                result.innerHTML = '<p style="color: red;">An error occurred: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

Bu makalenin geri kalanı, daha dar kapsamlı bir API'yi ne zaman seçmeniz gerektiğini açıklar.

## Gerekli İçe Aktarımlar
Bu makaledeki tüm JavaScript örnekleri, özet tablo türleri `Aspose.Cells.Pivot` namespace'i içinde sunulduğu için aşağıdaki modül içe aktarımıyla başlar:
- `const Aspose = require('aspose.cells');`

## Çalışma Kitabındaki Tüm Özet Tablolarını Yenileyin
Çalışma kitabındaki her `PivotCache` öğesinin ve her özet tablonun en güncel kaynak verileri yansıtmasını sağlamak istediğinizde, en basit ve kapsamlı API, `workbook.refreshAll()` yöntemidir. Tek çağrı tüm çalışma kitabını kapsar — her `PivotCache` öğesini kaynağından yeniler ve ardından ona bağlı her `PivotTable` öğesini yeniden hesaplar. Bu yaklaşım, performansın bir sorun olmadığı genel ve belgenin tamamını kapsayan yenilemeler için önerilir.
Aşağıdaki örnek, `Fruit/Year/Amount` kaynak aralığını içeren bir çalışma kitabı oluşturur, tek bir özet tablo ekler, bazı kaynak değerlerini değiştirir ve ardından her şeyi tek çağrıda güncel hâle getirmek için `refreshAll()` yöntemini kullanır.

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
            const cells = worksheet.cells;
            // A1:C1 hücrelerine başlık satırını yaz
            cells.get("A1").value = "Fruit";
            cells.get("B1").value = "Year";
            cells.get("C1").value = "Amount";
            // A2:C9 hücrelerine veri satırlarını yaz (2020 ve 2021 yıllarına ait 8 satır meyve verisi)
            cells.get("A2").value = "grape";
            cells.get("B2").value = 2020;
            cells.get("C2").value = 50;
            cells.get("A3").value = "blueberry";
            cells.get("B3").value = 2020;
            cells.get("C3").value = 60;
            cells.get("A4").value = "kiwi";
            cells.get("B4").value = 2020;
            cells.get("C4").value = 70;
            cells.get("A5").value = "cherry";
            cells.get("B5").value = 2020;
            cells.get("C5").value = 80;
            cells.get("A6").value = "grape";
            cells.get("B6").value = 2021;
            cells.get("C6").value = 90;
            cells.get("A7").value = "blueberry";
            cells.get("B7").value = 2021;
            cells.get("C7").value = 100;
            cells.get("A8").value = "kiwi";
            cells.get("B8").value = 2021;
            cells.get("C8").value = 110;
            cells.get("A9").value = "cherry";
            cells.get("B9").value = 2021;
            cells.get("C9").value = 120;
            // Bir özet tablo ekle: kaynak aralığı "A1:C9", hedef hücresi "E3"
            const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
            // Özet alanlarını ata: Fruit'ı Satırlara, Year'ı Sütunlara, Amount'ı Veriye
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
            pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
            // Değişiklikleri simüle etmek için kaynak verideki birkaç Amount değerini değiştir
            cells.get("C2").value = 55;
            cells.get("C5").value = 85;
            cells.get("C9").value = 125;
            // Çalışma kitabındaki tüm özet tabloları / özet önbelleklerini yenile
            workbook.refreshAll();
            // Çalışma kitabını kaydet
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output.xlsx";
            downloadLink.style.display = "block";
            document.getElementById('result').innerHTML =
                '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## Tek Çalışma Sayfasındaki Tüm Özet Tablolarını Yenileyin
Bazen yalnızca belirli bir çalışma sayfasında bulunan özet tablolarını yenilemeniz gerekebilir — örneğin başka çalışma sayfalarındaki özet tablolarının ilişkisiz olduğu biliniyorsa ve bunlara dokunulmamalıysa. Bu durumda Aspose.Cells, kapsamı tek bir `Worksheet` örneğiyle sınırlı olan `worksheet.refreshPivotTables()` işlevini sunar.

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
            const initializationPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            }).then(() => {
                console.log("Aspose.Cells initialized");
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                await initializationPromise;
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                cells.get("A2").value = "grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "blueberry";
                cells.get("B3").value = 2021;
                cells.get("C3").value = 150;
                cells.get("A4").value = "kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 200;
                cells.get("A5").value = "cherry";
                cells.get("B5").value = 2021;
                cells.get("C5").value = 120;
                cells.get("A6").value = "grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 180;
                cells.get("A7").value = "blueberry";
                cells.get("B7").value = 2020;
                cells.get("C7").value = 130;
                cells.get("A8").value = "kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 220;
                cells.get("A9").value = "cherry";
                cells.get("B9").value = 2020;
                cells.get("C9").value = 140;
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                cells.get("C2").value = 300;
                cells.get("C5").value = 250;
                cells.get("C9").value = 400;
                worksheet.refreshPivotTables();
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

## Tek Bir Özet Tablosunu Yenileyin
Tek bir özet tablo üzerinde ayrıntılı denetim istediğinizde, önbellek tabanlı API size iki seçenek sunar. Seçim, gerçekte neyin değiştiğine bağlıdır: kaynak verileri mi, yoksa yalnızca özet tablonun görünüm veya düzen ayarları mı?

### Kaynak Verileri Değişti — `pivotCache.refresh()` Kullanın
Kaynak verileri değiştiyse, doğru giriş noktası `pivotTable.getPivotCache().refresh()` yöntemidir. Bu çağrı, kaynak verilerini yeniden okuyup önbelleğe alır ve ardından o önbelleğe bağlı her `PivotTable` öğesini yeniden hesaplar.

### Yalnızca Görünüm/Düzen Değişti — `pivotTable.calculateData()` Kullanın
Kaynak veri değişmemiş ve yalnızca özet tablonun görünüm veya düzen ayarları değiştirilmişse (örneğin bir alan farklı bir alana taşınmışsa veya açılışta yenileme ayarı değiştirilmişse), veri kaynağına geri dönüşe gerek yoktur. Önbellek zaten doğru verileri içerir; yalnızca görüntülenen `PivotTable` öğesinin yeniden hesaplanması gerekir. Bu durumda doğru seçim `pivotTable.calculateData()` yöntemidir.
Aşağıdaki örnek, özet tablonun kaynak dışı bir özelliğini değiştirir ve ardından mevcut önbellekten yeniden oluşturulması için `calculateData()` çağırır.

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
            document.getElementById("runExample").addEventListener("click", async () => {
                const workbook = new Workbook();
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // Fruit / Year / Amount başlık satırını yaz
                cells.get("A1").value = "Fruit";
                cells.get("B1").value = "Year";
                cells.get("C1").value = "Amount";
                // 8 veri satırı yaz (2-9. satırlar, A1:C9 kaynak aralığına uyacak şekilde)
                cells.get("A2").value = "Grape";
                cells.get("B2").value = 2020;
                cells.get("C2").value = 100;
                cells.get("A3").value = "Blueberry";
                cells.get("B3").value = 2020;
                cells.get("C3").value = 200;
                cells.get("A4").value = "Kiwi";
                cells.get("B4").value = 2020;
                cells.get("C4").value = 300;
                cells.get("A5").value = "Cherry";
                cells.get("B5").value = 2020;
                cells.get("C5").value = 400;
                cells.get("A6").value = "Grape";
                cells.get("B6").value = 2021;
                cells.get("C6").value = 150;
                cells.get("A7").value = "Blueberry";
                cells.get("B7").value = 2021;
                cells.get("C7").value = 250;
                cells.get("A8").value = "Kiwi";
                cells.get("B8").value = 2021;
                cells.get("C8").value = 350;
                cells.get("A9").value = "Cherry";
                cells.get("B9").value = 2021;
                cells.get("C9").value = 450;
                // E3 hedef hücresine yerleştirilen ve A1:C9 aralığından veri alan bir pivot tablo ekle
                const pivotTable = worksheet.pivotTables.add("=A1:C9", 2, 4);
                // Alanları ata: Fruit → Row, Year → Column, Amount → Data
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Fruit");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Year");
                pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Amount");
                // Bir görünüm/düzen özelliğini değiştir — bu yalnızca sunumla ilgili bir değişikliktir,
                // bu nedenle PivotCache.Refresh() aracılığıyla kaynak verilerin yeniden okunmasını GEREKTİRMEZ.
                pivotTable.refreshDataOnOpeningFile = false;
                // CalculateData(), BU pivot tablonun gösterimini (veri + stil) PivotCache içinde
                // zaten saklanan verilerden yeniden oluşturur. Kaynak veri değişmediğinden,
                // kaynağa geri dönülmez — yalnızca önbelleğe alınmış değerler yeniden hesaplanarak
                // çalışma sayfası hücrelerine yazılır.
                pivotTable.calculateData();
                // Çalışma kitabını diske kaydet
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData]);
                const downloadLink = document.getElementById("downloadLink");
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                document.getElementById("result").innerHTML =
                    '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            });
        });
    </script>
</html>
```

Bir çalışma kitabı genellikle tek bir paylaşılan önbellek üzerine kurulmuş çok sayıda özet tablo içerir. Bunları listelemek için — örneğin toplu yenileme yapmadan önce veya paylaşılan önbelleğin etkisini teşhis etmek amacıyla — `pivotCache.getPivotTables()` yöntemini kullanın. Bu yöntem, verilen önbelleğe bağlı tüm `PivotTable` öğelerinden oluşan koleksiyonu döndürür.

## Kullanımdan Kaldırılmış `pivotTable.refreshData()` Yönteminden Geçiş
Aspose.Cells for JavaScript via C++ v26.7 sürümünden önce, bir özet tabloyu yenilemenin standart yolu her özet tabloda ayrı ayrı `pivotTable.refreshData()` çağırmaktı. v26.7 sürümünden itibaren bu yöntem **kullanımdan kaldırılmış** olarak işaretlenmiştir ve yukarıda açıklanan önbelleği dikkate alan API'lerle değiştirilmelidir.
Gerçek dünya çalışma kitaplarında tablo bazlı `refreshData()` yaklaşımının sorunlu olmasının iki nedeni vardır:
- Kaynak veri değişmemiş olsa bile, her çağrıldığında verileri kaynaktan *yeniden* getirir.
Önerilen değişiklikler şunlardır:
Aşağıdaki örnek, tek bir önbelleği paylaşan birden fazla özet tablo içeren çalışma kitapları için yeni ve verimli kalıbı gösterir.

## Hangi Yenileme API'sini Kullanmalıyım?
Aşağıdaki tabloda kullanılabilir yenileme API'leri ve her birinin ne zaman seçilmesi gerektiği özetlenmiştir.
| Hedef | Önerilen API | Notlar |
|------|-----------------|-------|
| Çalışma kitabındaki her şeyi yenile | `workbook.refreshAll()` | Tek çağrı; tüm önbellekleri ve özet tablolarını kapsar. |
| Yalnızca tek bir çalışma sayfasındaki özet tablolarını yenile | `worksheet.refreshPivotTables()` | Tek çalışma sayfasıyla sınırlıdır. |
| Bir önbelleğin kaynak verisi değişti | `pivotTable.getPivotCache().refresh()` | Paylaşılan önbellekteki TÜM özet tablolarını yeniler. |
| Yalnızca görünüm/düzen ayarları değişti | `pivotTable.calculateData()` | Gereksiz kaynağa geri dönüşü atlar. |
| Paylaşılan önbellekteki tüm özet tablolarını listele | `pivotCache.getPivotTables()` | Toplu yenilemeden önce listelemek için kullanın. |
Uygulamada, kullanımdan kaldırılmış tablo bazlı `refreshData()` yerine önbellek tabanlı API'leri tercih edin. Bu API'ler paylaşılan önbellekleri dikkate alır, gereksiz kaynak getirmelerini önler ve yenileme gereksiniminizi karşılayan en dar kapsamı seçmenize olanak tanır.

## Yaygın Tuzaklar
- **Kaydetmeden önce yenilemeyi unutmak.** Bir özet tablo, veri zinciri yenilendiğinde yalnızca görüntülenen değerlerini çalışma sayfasına yazar. Kaynak hücreleri değiştirdiyseniz, `workbook.save()` çağrısından önce `pivotCache.refresh()` (veya `workbook.refreshAll()`) çağırın; aksi halde kaydedilen dosya hâlâ eski toplulaştırılmış değerleri içerir.
- **Her tablo için kullanımdan kaldırılmış `refreshData()` çağırmak.** v26.7 sürümünde `pivotTable.refreshData()` kullanımdan kaldırılmış olarak işaretlenmiştir ve her çağrıda kaynağı yeniden getirir. Bir önbelleği paylaşan birden fazla özet tablo olduğunda bu, N gereksiz kaynak getirmesi anlamına gelir. Bunu tek bir `pivotCache.refresh()` çağrısı ve ardından her tablo için `pivotTable.calculateData()` çağrısıyla değiştirin.
- **Yalnızca düzen değiştiğinde yenilemek.** Yalnızca özet tablonun görünümünü (sütun sırası, `getConsolidationFunction()` vb.) değiştirip kaynak verilere dokunmadıysanız, `pivotCache.refresh()` gereksiz ve yavaştır. Mevcut önbellekten yeniden görüntülemek için `pivotTable.calculateData()` çağırın.
- **`pivotCache.refresh()` tarafından desteklenmeyen harici kaynak.** Özet tablonun kaynağı harici bir bağlantıdan geliyorsa (veritabanı, OLAP küpü vb.), `pivotCache.refresh()` v26.7 sürümünde bunu yenileyemez — hâlihazırda yalnızca `SHEET` ve `CONSOLIDATION` kaynak türlerini destekler. Harici kaynaklar için çalışma kitabını yeniden açın veya önbelleği kaynaktan yeniden oluşturun.

{{< app/cells/assistant language="javascript-cpp" >}}