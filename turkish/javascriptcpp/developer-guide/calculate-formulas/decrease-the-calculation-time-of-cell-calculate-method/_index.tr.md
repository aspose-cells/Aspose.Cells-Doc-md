---
title: JavaScript ile C++ üzerinden Hücre.Hesapla metodunun Hesaplama Süresini Azaltın
linktitle: Hücre.Calculate yönteminin Hesaplama Zamanını Düşürme
description: Bu makale, Aspose.Cells kütüphanesini kullanarak, Excel de hücre hesaplama metodları için hesaplama süresini JavaScript ile C++ kullanarak nasıl azaltacağınızı anlatmaktadır.
keywords: Aspose.Cells, Excel, Hücre hesaplama metodları, optimizasyon, performans, hesaplama süresinin azaltılması, JavaScript ile C++
type: docs
weight: 100
url: /tr/javascript-cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **Olası Kullanım Senaryoları**

 Genellikle, kullanıcılara [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) yöntemini bir kez çağırmalarını ve ardından bireysel hücrelerin hesaplanan değerlerini almalarını öneririz. Ancak bazen, kullanıcılar tüm çalışma kitabını hesaplamak istemezler. Sadece tek bir hücreyi hesaplamak isterler. Aspose.Cells, [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--) özelliği sağlar, bunu **false** olarak ayarlayarak bireysel hücrelerin hesaplama süresini önemli ölçüde azaltabilirsiniz. Recursive özelliği **true** olarak ayarlandığında, tüm bağlı hücreler her çağrıda yeniden hesaplanır. Ancak,recursive özelliği **false** ise, bağlı hücreler yalnızca bir kez hesaplanır ve sonraki çağrılarda yeniden hesaplanmaz.

## **Hücre.calculate() Yönteminin Hesaplama Süresini Azaltma**

 Aşağıdaki örnek kod, [**CalculationOptions.recursive**](https://reference.aspose.com/cells/javascript-cpp/calculationoptions/#recursive--) özelliğinin kullanımını gösterir. Lütfen bu kodu verilen [örnek excel dosyasıyla](5113710.xlsx) çalıştırın ve konsol çıktılarını kontrol edin. Recursive özelliğini **false** olarak ayarlamanın hesaplama süresini önemli ölçüde azalttığını göreceksiniz. Ayrıca, bu özelliğin daha iyi anlaşılması için yorumları da okuyunuz.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Calculate Formulas Example</title>
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
            const resultEl = document.getElementById('result');
            if (!fileInput.files.length) {
                resultEl.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Test calculation time after setting recursive true
            workbook.calculateFormula(); // initiate calculation

            // Test calculation time after setting recursive false (specify ignoreError as false)
            workbook.calculateFormula(false);

            // Save the modified workbook and provide a download link
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.calculated.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Calculated Excel File';

            resultEl.innerHTML = '<p style="color: green;">Calculation completed successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```  
```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
        <meta charset="utf-8" />
    </head>
    <body>
        <h1>Calculation Time Recursive Test</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Calculation Test (Recursive true/false)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, CalculationOptions } = AsposeCells;

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
            const resultDiv = document.getElementById('result');
            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access first worksheet
            const ws = workbook.worksheets.get(0);

            const runs = [true, false];
            let outputHtml = '';
            for (let r = 0; r < runs.length; r++) {
                const rec = runs[r];

                // Set the calculation option, set recursive true or false as per parameter
                const opts = new CalculationOptions();
                opts.recursive = rec;

                // Start stopwatch
                const start = performance.now();

                // Calculate cell A1 one million times
                for (let i = 0; i < 1000000; i++) {
                    ws.cells.get("A1").calculate(opts);
                }

                // Stop the watch
                const end = performance.now();

                // Calculate elapsed time in seconds
                const estimatedTime = (end - start) / 1000;

                // Record the elapsed time
                const message = `Recursive ${rec}: ${estimatedTime} seconds`;
                console.log(message);
                outputHtml += `<p>${message}</p>`;
            }

            resultDiv.innerHTML = `<div style="color: green;">${outputHtml}</div>`;
        });
    </script>
</html>
```

## **Konsol Çıktısı**

 Bu, yukarıdaki örnek kodun, bizim makinemizde verilen [örnek excel dosyasıyla](5113710.xlsx) çalıştırıldığında konsol çıktısıdır. Lütfen, çıktınız farklı olabilir, ancak recursive özelliğini **false** olarak ayarladıktan sonra geçen süre her zaman **true** yapmaktan daha az olacaktır.

{{< highlight java >}}  
Recursive True: 96 seconds  

Recursive False: 42 seconds  
{{< /highlight >}}
