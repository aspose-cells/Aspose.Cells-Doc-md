---
title: Aralığı Transpoze Et
linktitle: Aralığı Transpoze Et
description: Bu makale, Aspose.Cells for JavaScript via C++ kullanarak Excel dosyalarında satırları sütunlara veya tersine dönüştürmek (transpoze) için üç farklı yaklaşımı açıklar.
keywords: Aspose.Cells, JavaScript via C++, elektronik tablo, aralığı transpoze et, verileri transpoze et, TRANSPOSE işlevi, dinamik dizi formülü, dizi formülü, Excel TRANSPOSE, satırlardan sütunlara
type: docs
weight: 80
url: /tr/javascript-cpp/transpose-rotate-data-from-rows-to-columns-or-vice-versa/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ verileri (satırların sütun, sütunların satır olmasını sağlayarak) üç farklı yöntemle döndürmeyi (transpose) destekler. İlk yaklaşım, yerinde `range.transpose()` yöntemini kullanır ve tüm Excel sürümlerinde çalışır; ikinci yöntem `cell.setDynamicArrayFormula()` kullanarak modern bir dinamik dizi `=TRANSPOSE(...)` formülünü yazar ve bu formül Excel 365 veya Excel 2021'de otomatik olarak dökülür. Üçüncü yaklaşım `cell.setArrayFormula()` kullanarak eski Excel sürümleriyle uyumlu klasik Ctrl+Shift+Enter (CSE) dizi formülünü yazar. Bu makale, adım adım talimatlar ve tam kod örnekleriyle her yaklaşımı anlatır.
{{% /alert %}}

## **Giriş**
Bir aralığı transpoze etmek, satır olanın sütun, sütun olanın ise satır haline gelmesiyle dönüştürülmesi demektir; bu, verileri ana köşegen boyunca yansıtmak anlamına gelir. Microsoft Excel'de, çalışma sayfası işlevi `TRANSPOSE` bu işlemi gerçekleştirir ve kavramsal referans şu adreste belgelenmiştir: https://support.microsoft.com/en-us/excel/functions/transpose-function. Bu kavram, bir hücre aralığına programlı olarak uygulanabilir ve birçok iş ve raporlama senaryosunda kullanışlıdır.
- Çeyrek veya yıllık satış raporlarını, çeyreklerin genellikle sayfada yan yana, bölgelerin ise aşağı doğru olduğu şekilde yeniden yönlendirmek ya da tersine.
- Gösterge panellerinde veya grafiklerde eksen yönlendirmesini değiştirerek zaman serisinin sayfada yan yerine aşağı doğru ilerlemesini sağlamak.
- Harici sistemlerden içe aktarılan verileri, sonraki analiz veya raporlama şablonlarının beklediği düzenle eşleşecek şekilde yeniden şekillendirmek.
Makalenin geri kalanını somutlaştırmak için, tüm örneklerde aşağıdaki küçük bölge‑çeyrek satış tablosu kullanılmaktadır. Örnek çalışma kitabında bu tablo **A1:D5** aralığını kaplar; **A1** sol üst köşe olarak boş bırakılır, **B1:D1** bölge başlıklarını, **A2:A5** ise çeyrek başlıklarını içerir.
| Bölge            | Avrupa    | Asya      | Kuzey Amerika |
|-------------------|-----------|-----------|---------------|
| Çeyrek 1          | 21704714  | 8774099   | 12094215      |
| Çeyrek 2          | 17987034  | 12214447  | 10873099      |
| Çeyrek 3          | 19485029  | 14356879  | 15689543      |
| Çeyrek 4          | 22567894  | 15763492  | 17456723      |
Makale, Aspose.Cells for JavaScript via C++ kullanarak bu verileri transpoze etmenin üç farklı yolunu sunar; her biri farklı bir Excel sürümü ve kullanım durumuna uygundur.

## **Yaklaşım 1 — Yerinde Aralığı Transpoze Et (Range.transpose)**
Bu yaklaşımı, `TRANSPOSE` çalışma sayfası işlevini kullanmadan verileri transpoze etmek istediğinizde kullanın. **Tüm Excel sürümlerinde** çalışır ve dinamik dizilere bağımlılığı yoktur; bu da onu sürüm geçişi açısından en güvenli seçenek haline getirir. Yalnızca son transpoze edilmiş çıktıya ihtiyacınız olduğunda ve orijinal `TRANSPOSE` formülünü çalışma kitabında tutmak istemediğinizde idealdir.

### **Kullanılan API**
`Range.transpose()` yöntemi, `Aspose.Cells.Range` sınıfının bir örnek metodudur. Çağırıldığında, satır ve sütunları değiştirerek aralığı yerinde döndürür; böylece satır olan sütun, sütun olan ise satır hâline gelir. Metot, bir formül yazmadan doğrudan alttaki hücreleri değiştirir.

### **Adımlar**
1. `LoadOptions`'ı `.xlsx` formatına ayarlayarak kaynak çalışma kitabını `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` şeklinde açın.  
2. Çalışma kitabından `workbook.getWorksheets().get(0)` koduyla ilk çalışma sayfasını alın.  
3. Çalışma sayfasının hücre koleksiyonuna `worksheet.getCells()` ile erişin.  
4. `cells.createRange("A1:D5")` çağrısıyla **A1:D5** aralığını oluşturun.  
5. Aralığı yerinde döndürmek ve satırları sütunlarla takas etmek için `source.transpose()` çağırın.  
6. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.  
Transpozisyon sonrası bu köşe aralığı döndürülmüş verileri tutar. İlk satır (boş, **Europe**, **Asia**, **North America**) ve ilk sütun (boş, **Qtr 1**, **Qtr 2**, **Qtr 3**, **Qtr 4**) şeklinde okunur. Orijinal her satış sütunu, transpoze edilmiş aralıkta bir satır hâline gelir.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
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
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an .xlsx file.</p>';
                return;
            }
            try {
                const file = fileInput.files[0];
                const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                const source = cells.createRange("A1:D5");
                source.transpose();
                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "transposed.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                result.innerHTML = '<p style="color: red;">An error occurred while processing the file.</p>';
            }
        });
    </script>
</html>
```

## **Yaklaşım 2 — Dinamik Dizi Formülü ile Transpoze Et (Excel 365 / 2021)**
Kaynak veri değiştiğinde sonuç otomatik olarak güncellenmesi amacıyla `=TRANSPOSE(A1:D5)` formülünü çıktı çalışma kitabında canlı tutmak ve hedef Excel dosyasının **Excel 365 / Excel 2021 veya daha yeni** bir sürümde açılacağını, dinamik diziler ve dökülme operatörünün desteklendiğini varsaydığınızda bu yaklaşımı kullanın.

### **Kullanılan API**
`Cell.setDynamicArrayFormula(formula, options, calculateValue)` yöntemi, `Aspose.Cells.Cell` sınıfının bir metodudur ve hücrenin formülünü **dinamik dizi formülü** olarak ayarlar. Excel formülü bir kez değerlendirir ve sonucu otomatik olarak çevresindeki hücrelere döker. Üçüncü parametre `true` olarak ayarlandığında, Aspose.Cells'in yazma zamanında ortaya çıkan değerleri de hesaplamasını sağlar.

### **Adımlar**
1. `new Workbook(srcFile, new LoadOptions(LoadFormat.Xlsx))` kullanarak kaynak çalışma kitabını yükleyin.  
2. İlk çalışma sayfasını alın ve hücre koleksiyonuna erişin.  
3. Dinamik dizi formülünü, kaynak aralığının hemen altında **A6** hücresine, `cells.get("A6").setDynamicArrayFormula("=TRANSPOSE(A1:D5)", new FormulaParseOptions(), true)` çağrısı ile yerleştirin.  
4. `new FormulaParseOptions()` bağımsız değişkeni varsayılan `FormulaParseOptions` ayarlarını kullanır ve üçüncü bağımsız değişken `true`, Aspose.Cells'e formülü dinamik dizi olarak ele almasını ve dökülen değerlerin çalışma kitabına yazılmasını söyler.  
5. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.  
**A6** hücresi `=TRANSPOSE(A1:D5)` formülünü tutar ve Excel sonucu otomatik olarak **A6:E9** bölgesine döker; bu, transpoze edilmiş veri ile eşleşen 4 satır ve 5 sütunluk bir bloktur.

{{% alert color="primary" %}}
Bu yaklaşım **yalnızca Excel 365 / 2021 veya daha yeni** sürümlerde çalışır. Eski Excel sürümleri dinamik dizi formüllerini doğru şekilde dökmeyecektir.
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
        const { Workbook, FormulaParseOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            await initialization;
            const fileInput = document.getElementById('fileInput');
            const downloadLink = document.getElementById('downloadLink');
            const result = document.getElementById('result');
            if (!fileInput.files.length) {
                result.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }
            const workbook = new Workbook(new Uint8Array(await fileInput.files[0].arrayBuffer()));
            const worksheet = workbook.worksheets.get(0);
            const cells = worksheet.cells;
            cells.get("A6").setDynamicArrayFormula(
                "=TRANSPOSE(A1:D5)",
                new FormulaParseOptions(),
                true
            );
            const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = "output_transpose_dynamic.xlsx";
            downloadLink.style.display = "block";
            result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
        });
    </script>
</html>
```

## **Yaklaşım 3 — Klasik Dizi Formülü (CSE) ile Transpoze Et**
Bu yaklaşımı, `TRANSPOSE` formülünün çalışma kitabında korunmasını istediğinizde, ancak hedef Excel dosyasının **eski Excel sürümlerinde (2021 öncesi, 2019, 2016, 2013 ve benzeri)** açılabileceği ve dinamik dizi dökülmesinin desteklenmediği durumlarda kullanın.

### **Kullanılan API**
`Cell.setArrayFormula(arrayFormula, nRows, nColumns)` yöntemi, `Aspose.Cells.Cell` sınıfının bir metodudur ve **klasik dizi (CSE) formülünü** köşe hücresine atar ve ortaya çıkan dizinin boyutlarını bildirir. Aspose.Cells, çok hücreli dizi-formül işaretleyicisini yazar; böylece Excel formülü tek bir dizi ifadesi olarak değerlendirir ve belirtilen aralığı doldurur.

### **Adımlar**
1. Önceki yaklaşımlarda açıklandığı gibi kaynak çalışma kitabını yükleyin.  
2. İlk çalışma sayfasını alın ve hücre koleksiyonuna erişin.  
3. `cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5)` çağrısını yapın. İkinci bağımsız değişken `4`, hedef dizinin satır sayısını; üçüncü bağımsız değişken `5` ise sütun sayısını belirtir.  
4. Çalışma kitabını `workbook.save(outputFile)` ile kaydedin.  
**A6** hücresi dizi formülünün köşesidir ve değerlendirilmiş dizi A6'dan başlayarak 4 satır ve 5 sütun kapsar; bu, A1:D5 kaynağının transpoze edilmiş boyutlarıyla eşleşir. Excel, ortaya çıkan aralıkta tek bir dizi-formül işaretleyicisi yazar; böylece eski Excel sürümleri bunu doğru şekilde değerlendirir.

{{% alert color="primary" %}}
CSE dizi formülleri, bir `TRANSPOSE` ifadesini değerlendirmek için klasik Excel yoludur ve bu yaklaşım tüm Excel sürümlerinde evrensel olarak uyumludur.
{{% /alert %}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>
    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, LoadOptions } = AsposeCells;
        const initialization = AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });
        document.getElementById('runExample').addEventListener('click', async () => {
            try {
                await initialization;
                const fileInput = document.getElementById('fileInput');
                const downloadLink = document.getElementById('downloadLink');
                const result = document.getElementById('result');
                const file = fileInput.files[0];
                if (!file) {
                    throw new Error("Please select an XLSX workbook.");
                }
                // Kaynak çalışma kitabını xlsx LoadOptions ile yükle
                const loadOptions = new LoadOptions(AsposeCells.LoadFormat.Xlsx);
                const workbook = new Workbook(
                    new Uint8Array(await file.arrayBuffer()),
                    loadOptions
                );
                // İlk çalışma sayfasına ve onun Cells koleksiyonuna eriş
                const worksheet = workbook.worksheets.get(0);
                const cells = worksheet.cells;
                // A6 hücresine klasik CSE dizi formülünü ayarla.
                // Formül =TRANSPOSE(A1:D5), 5 satır x 4 sütun kaynak aralığını döndürür
                // 4 satır x 5 sütunluk bir diziye. İkinci argüman (4) satır sayısıdır
                // ve üçüncü argüman (5) oluşan dizinin sütun sayısıdır.
                // Aspose.Cells, CSE dizi-formül işaretçisini yazar, böylece Excel bunu şu şekilde değerlendirir:
                // tek bir çok hücreli dizi formülü olarak, daha eski Excel sürümleriyle uyumlu
                // (2019, 2016, 2013, vb.) dinamik dizi taşmasını desteklemeyen.
                cells.get("A6").setArrayFormula("=TRANSPOSE(A1:D5)", 4, 5);
                // Çalışma kitabını kaydedin, böylece dizi-formül işaretçisi kalıcı olur
                const outputData = workbook.save(AsposeCells.SaveFormat.Xlsx);
                const blob = new Blob([outputData], {
                    type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                });
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = "output.xlsx";
                downloadLink.style.display = "block";
                result.innerHTML = '<p style="color: green;">Done! Click the download link to get the result file.</p>';
            } catch (error) {
                console.error(error);
                document.getElementById('result').innerHTML =
                    '<p style="color: red;">Error: ' + error.message + '</p>';
            }
        });
    </script>
</html>
```

## **Karşılaştırma — Hangi Durumda Hangi Yaklaşım Kullanılır**
| Yaklaşım | API / Metod | Excel Sürümü | Kaynak formül korundu? | Çıktı aralığı |
|----------|--------------|---------------|--------------------------|--------------|
| Yaklaşım 1 — Yerinde transpoze | `range.transpose()` | Tüm Excel sürümleri | Hayır (sadece değerler) | İlk köşe aralığı, 5×4 |
| Yaklaşım 2 — Dinamik dizi formülü | `cell.setDynamicArrayFormula()` | Excel 365 / 2021+ | Evet (dinamik olarak dökülür) | Köşeden dökülür |
| Yaklaşım 3 — Klasik dizi formülü (CSE) | `cell.setArrayFormula()` | Tüm Excel sürümleri | Evet (çok hücreli dizi formülü) | Açık boyut, 4×5 |
**Yaklaşım 1**'i, hızlı bir dönüşüm gerektiğinde ve sadece transpoze edilmiş değerlerin dosyaya yazılması yeterli olduğunda kullanın. **Yaklaşım 2**'yi, modern Excel'in kesinlikle kullanılacağı ve formülün canlı kalmasını, kaynak değiştiğinde güncellenmesini istediğinizde tercih edin. **Yaklaşım 3**'ü ise, tüm Excel sürümlerinde, dinamik dizi desteği olmayan eski sürümler dahil, korunan bir formül ile en geniş uyumluluğa ihtiyaç duyduğunuzda seçin.

{{< app/cells/assistant language="javascript-cpp" >}}