---
title: Formülleri içeren CSV dosyasını yükle veya İçe aktar via JavaScript
linktitle: Formülleri içeren CSV dosyasını yükle veya içe aktar
type: docs
weight: 350
url: /tr/javascript-cpp/load-or-import-csv-file-with-formulas/
description: Formülleri içeren CSV dosyalarını yükleme ve içe aktarma konusunda bilgi edinin, Aspose.Cells for JavaScript kullanarak C++.
---

{{% alert color="primary" %}}

CSV dosyaları çoğunlukla metin verisi içerir ve formüller içermez. Ancak bazen CSV dosyaları da formüller içerebilir. Bu tür CSV dosyalarını, [TxtLoadOptions.hasFormula](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#hasFormula--) özelliğini **true** yaparak yüklemelisiniz. Bu özellik **true** ayarlandığında, Aspose.Cells formülleri basit metin olarak değil, formüller olarak işler ve Aspose.Cells'in formül hesaplama motoru bunları normal şekilde işler.

{{% /alert %}}

Aşağıdaki kod, formüllü CSV dosyasını nasıl yükleyeceğinizi ve içeri aktaracağınızı gösterir. Herhangi bir CSV dosyasını kullanabilirsiniz. Örnek olarak, bu veriyi içeren [basit CSV dosyası](5115034.csv) kullanıyoruz. Görüldüğü gibi, formüller içerir.

{{< highlight javascript >}}
<!DOCTYPE html>
<html>
    <head>
        <title>Load CSV with Formulas and Save as XLSX</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="convertToXlsx">Convert to XLSX</button>
        <a id="downloadLink" style="display: none;">Download XLSX</a>
        <div id="result"></div>

        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook, TxtLoadOptions, SaveFormat } = AsposeCells;

            AsposeCells.onReady().then(() => {
                console.log("Aspose.Cells initialized");
            });

            document.getElementById('convertToXlsx').addEventListener('click', async () => {
                const fileInput = document.getElementById('fileInput');
                if (!fileInput.files.length) {
                    document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                    return;
                }

                const file = fileInput.files[0];
                const arrayBuffer = await file.arrayBuffer();

                const loadOptions = new TxtLoadOptions();
                loadOptions.hasFormula = true;

                const workbook = new Workbook(new Uint8Array(arrayBuffer), loadOptions);

                const outputData = workbook.save(SaveFormat.Xlsx);
                const blob = new Blob([outputData], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
                const downloadLink = document.getElementById('downloadLink');
                downloadLink.href = URL.createObjectURL(blob);
                downloadLink.download = file.name.replace(/\.csv$/i, '.xlsx');
                downloadLink.style.display = 'block';
                downloadLink.textContent = 'Download XLSX File';

                document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed! Click the download link to get the XLSX file.</p>';
            });
        </script>
    </body>
</html>
{{< /highlight >}}

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells CSV Load Example</title>
    </head>
    <body>
        <h1>Load CSV with Formulas and Save as XLSX</h1>
        <input type="file" id="fileInput" accept=".csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, TxtLoadOptions, Utils } = AsposeCells;

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
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select a CSV file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();
            const bytes = new Uint8Array(arrayBuffer);

            // TxtLoadOptions configuration
            const opts = new TxtLoadOptions();
            opts.separator = ',';
            opts.hasFormula = true;

            // Load your CSV file with formulas in a Workbook object
            const workbook = new Workbook(bytes, opts);

            // You can also import your CSV file like this
            // The code below is importing CSV file starting from cell D4 (rowIndex=3, colIndex=3)
            const worksheet = workbook.worksheets.get(0);
            worksheet.cells.importCSV(bytes, opts, 3, 3);

            // Save your workbook in Xlsx format
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output_out.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the converted file.</p>';
        });
    </script>
</html>
```

Kod ilk olarak CSV dosyasını yükler, ardından tekrar D4 hücresine içe aktarır. Son olarak, çalışma kitabı nesnesini XLSX biçiminde kaydeder. [Çıktı XLSX dosyası](5115052.xlsx) böyle görünür. Görüldüğü gibi, C3 ve F4 hücreleri formüller içerir ve sonucu 800'dür.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |
