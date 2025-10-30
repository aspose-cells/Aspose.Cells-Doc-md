---
title: JavaScript ile C++ aracılığıyla Formülleri Hesapla
linktitle: Formülleri Hesapla
description: Bu makale, Aspose.Cells kütüphanesini kullanarak C++ aracılığıyla JavaScript ile Microsoft Excel de formülleri nasıl hesaplayacağını tanıtır. Mevcut bir Excel dosyasını yükleyerek veya yeni bir Excel dosyası oluşturarak, Aspose.Cells tarafından sağlanan yöntemleri kullanarak formülü hesaplayabilir ve sonucu alabiliriz. Son olarak, değiştirilmiş Excel dosyasını diske kaydederiz.
keywords: Aspose.Cells, Excel, formüller, hesaplamalar, Formülü Doğrudan Hesaplama, Formülleri Tekrar Hesapla, JavaScript ile formüller ekleme (C++)
type: docs
weight: 125
url: /tr/javascript-cpp/calculate-formulas/
---

## **Formüller Ekleyin ve Sonuçlarını Hesaplayın**

Aspose.Cells gömülü bir formül hesaplama motoruna sahiptir. Tasarımcı şablonlarından ithal edilen formülleri tekrar hesaplamanın yanı sıra, çalışma zamanında eklenen formüllerin sonuçlarını da hesaplamayı destekler.

Aspose.Cells, Microsoft Excel'in (hızla listeyi destekleyen fonksiyonlar listesine bakın) çoğu formül veya fonksiyonunu destekler. Bu fonksiyonlar, API'ler veya tasarımcı tabloları aracılığıyla kullanılabilir. Aspose.Cells, çok çeşitli matematiksel, dize, mantıksal, tarih/zaman, istatistik, veritabanı, arama ve referans formüllerini destekler.

Bir hücreye formül eklemek için [**formula**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula--) sınıfının [**formula(string, object)**](https://reference.aspose.com/cells/javascript-cpp/cell/#formula-string-object-) özelliği veya [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) metodunu kullanın. Bir formül uygularken, her zaman Microsoft Excel'de formül oluştururken yaptığınız gibi eşittir (=) ile başlayın ve fonksiyon parametrelerini ayırmak için virgül (,) kullanın.

Formüllerin sonuçlarını hesaplamak için, kullanıcı [**calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) metodunu çağırabilir; bu metod, bir Excel dosyasına gömülü tüm formülleri işler. Alternatif olarak, yine [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook) sınıfının [**calculateFormula(string)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-) metodunu çağırarak, bir sayfaya gömülü tüm formülleri işleyebilirsiniz. Ayrıca, yalnızca bir Hücre’nin formülünü işleyen [**calculate(CalculationOptions)**](https://reference.aspose.com/cells/javascript-cpp/cell/#calculate-calculationoptions-) metodunu da çağırabilirsiniz:

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
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            // Instantiate a new Workbook object
            const workbook = new Workbook();

            // Add a new worksheet to the Excel object
            const sheetIndex = workbook.worksheets.add();

            // Obtain the reference of the newly added worksheet by passing its sheet index
            const worksheet = workbook.worksheets.get(sheetIndex);

            // Adding a value to "A1" cell
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 1;

            // Adding a value to "A2" cell
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 2;

            // Adding a value to "A3" cell
            const cellA3 = worksheet.cells.get("A3");
            cellA3.value = 3;

            // Adding a SUM formula to "A4" cell
            const cellA4 = worksheet.cells.get("A4");
            cellA4.formula = "=SUM(A1:A3)";

            // Calculating the results of formulas
            workbook.calculateFormula();

            // Get the calculated value of the cell
            const value = worksheet.cells.get("A4").value.toString();

            // Saving the Excel file
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<p style="color: green;">Operation completed successfully! Calculated value in A4: ${value}. Click the download link to get the file.</p>`;
        });
    </script>
</html>
```

### **Formüller İçin Bilinmesi Gerekenler**

{{% alert color="primary" %}}

 [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıfının **Formül** özelliği ve **formül(...)** yöntemleri, [**Workbook**](https://reference.aspose.com/cells/javascript-cpp/workbook), [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) ve [**Cell**](https://reference.aspose.com/cells/javascript-cpp/cell) sınıflarının **calculate** yöntemlerinden farklı çalışır. **Formül** özelliği ve **formül(...)** yöntemleri, yalnızca hücreye formülü ekler, ancak çalışma zamanında sonucu hesaplamaz. Formüllerin sonucunu almak için **calculate** yöntemlerini çağırmalısınız.

{{% /alert %}}

## **Formülün Doğrudan Hesaplanması**

Aspose.Cells, gömülü bir formül hesaplama motoruna sahiptir. Bir tasarımcı dosyasından içe aktarılmış formülleri hesaplamanın yanı sıra, Aspose.Cells, formül sonuçlarını doğrudan hesaplamayı da destekler.

B sometimes, doğrudan formül sonuçlarını hesaplamanız gerekebilir, ve bu sonuçları çalışma sayfasına eklemeden de yapabilirsiniz. Formülde kullanılan hücrelerin değerleri zaten bir çalışma sayfasında mevcuttur ve sizin yapmanız gereken, bu değerlerin sonucunu Microsoft Excel formülleri kullanarak bulmaktır, formülü çalışma sayfasına ekmeden.

Aspose.Cells’ın formül hesaplama motoru API’lerini kullanarak, [**Worksheet**](https://reference.aspose.com/cells/javascript-cpp/worksheet) ile [**calculateFormula(string, FormulaParseOptions, CalculationOptions, number, number, CalculationData)**](https://reference.aspose.com/cells/javascript-cpp/worksheet/#calculateFormula-string-formulaparseoptions-calculationoptions-number-number-calculationdata-) arasındaki formüllerin sonuçlarını, bunları çalışma sayfasına eklemeden alabilirsiniz:

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example - Calculate Sum</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');

            // Create or load workbook
            let workbook;
            if (fileInput.files && fileInput.files.length > 0) {
                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();
                workbook = new Workbook(new Uint8Array(arrayBuffer));
            } else {
                workbook = new Workbook();
            }

            // Access first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Put 20 in cell A1
            const cellA1 = worksheet.cells.get("A1");
            cellA1.value = 20;

            // Put 30 in cell A2
            const cellA2 = worksheet.cells.get("A2");
            cellA2.value = 30;

            // Calculate the Sum of A1 and A2
            const results = worksheet.calculateFormula("=Sum(A1:A2)");

            // Prepare output text
            const outputHtml = [
                `<p>Value of A1: ${cellA1.stringValue}</p>`,
                `<p>Value of A2: ${cellA2.stringValue}</p>`,
                `<p>Result of Sum(A1:A2): ${results.toString()}</p>`
            ].join("");

            // Save the workbook to a downloadable file
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData], { type: "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet" });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = `<div style="color: green;">Operation completed successfully!</div>${outputHtml}`;
        });
    </script>
    </body>
</html>
```

Formülleri Tekrarlı Hesaplamak İçin Nasıl
{{< highlight nodejs >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **Formülleri tekrar tekrar hesaplama**

Çok sayıda formül bulunduğunda ve sadece küçük bir kısmını değiştirilerek tekrar hesaplanması gerekiyorsa, performans açısından hesaplama zincirini etkinleştirmek faydalı olabilir: [**formulaSettings.enableCalculationChain**](https://reference.aspose.com/cells/javascript-cpp/formulasettings/#enableCalculationChain--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Calculate Formulas</title>
    </head>
    <body>
        <h1>Calculate Formulas Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Print the time before formula calculation
            console.log(new Date());

            // Set the CreateCalcChain as true
            workbook.settings.formulaSettings.enableCalculationChain = true;

            // Calculate the workbook formulas
            workbook.calculateFormula();

            // Print the time after formula calculation
            console.log(new Date());

            // Change the value of one cell (A1 in first worksheet)
            const worksheet = workbook.worksheets.get(0);
            const cell = worksheet.cells.get("A1");
            cell.value = "newvalue";

            // Re-calculate those formulas which depend on cell A1
            workbook.calculateFormula();

            // Save the modified workbook and provide download link
            const outputData = workbook.save(SaveFormat.Excel97To2003);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.out.xls';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Formulas calculated and cell updated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```

### **Bilinmesi Gerekenler**

{{% alert color="primary" %}}

Varsayılan olarak, hesaplama zinciri devre dışıdır. Zincirin oluşturulması ek zaman alır, bu yüzden ilk defa formülleri ([**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--)) hesaplarken, zincirsiz hesaplamaya kıyasla daha fazla CPU işlem süresi ve belleğin kullanılması muhtemeldir. Eğer kullanıcı formülleri tekrar tekrar hesaplamıyorsa, varsayılan davranış (formülü doğrudan hesaplama ve hesaplama Zinciri oluşturmama) daha iyi olur.

{{% /alert %}}

## **Gelişmiş Konular**
- [Microsoft Excel Formül İzleme Penceresine Hücreler Ekleme](/cells/tr/javascript-cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [Aspose.Cells ile IFNA işlevinin hesaplanması](/cells/tr/javascript-cpp/calculating-ifna-function-using-aspose-cells/)
- [Veri Tablolarının Dizi Formül Hesaplama](/cells/tr/javascript-cpp/calculation-of-array-formula-of-data-tables/)
- [Excel 2016 MINIFS ve MAXIFS işlevlerinin hesaplanması](/cells/tr/javascript-cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [Hücre.hesapla metodunun Hesaplama Süresini Azaltın](/cells/tr/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [Dairesel Referansı Algılama](/cells/tr/javascript-cpp/detecting-circular-reference/)
- [Özel işlevin çalışma tablosuna yazılmadan doğrudan hesaplanması](/cells/tr/javascript-cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [Aspose.Cells'in Varsayılan Hesaplama Motorunu Genişletmek için Özel Hesaplama Motoru Uygulamak](/cells/tr/javascript-cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [Çalışma Kitabının Formül Hesaplamasını Kesmek veya İptal Etmek](/cells/tr/javascript-cpp/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [AbstractCalculationEngine Kullanarak Bir Değer Aralığı Döndürme](/cells/tr/javascript-cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [Çalışma Kitabının Formül Hesaplama Modunu Ayarlama](/cells/tr/javascript-cpp/setting-formula-calculation-mode-of-workbook/)
- [Aspose.Cells'te FormulaText Fonksiyonu Kullanma](/cells/tr/javascript-cpp/using-formulatext-function-in-aspose-cells/)
