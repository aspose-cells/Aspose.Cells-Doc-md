---
title: Загрузить или импортировать CSV файл с формулами via JavaScript
linktitle: Загрузка или импорт файла CSV с формулами
type: docs
weight: 350
url: /ru/javascript-cpp/load-or-import-csv-file-with-formulas/
description: Узнайте, как загружать и импортировать CSV файлы, содержащие формулы, с помощью Script Aspose.Cells for Java на C++.
---

{{% alert color="primary" %}}

 CSV-файлы в основном содержат текстовые данные и не содержат формул. Однако иногда в CSV-файлах также встречаются формулы. Такие файлы необходимо загружать, устанавливая [TxtLoadOptions.hasFormula](https://reference.aspose.com/cells/javascript-cpp/txtloadoptions/#hasFormula--) в **true**. Как только это свойство будет установлено в **true**, Aspose.Cells перестанет рассматривать формулы как обычный текст. Они будут восприниматься как формулы, и движок расчетов Aspose.Cells будет обрабатывать их как обычно.

{{% /alert %}}

 Следующий код демонстрирует, как загружать и импортировать CSV-файл с формулами. Можно использовать любой CSV-файл. В качестве примера используется [простой CSV-файл](5115034.csv), содержащий эти данные. Как видите, он содержит формулу.

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

Сначала код загружает CSV-файл, затем импортирует его заново в ячейку D4. В конце он сохраняет рабочую книгу в формате XLSX. [Выходной XLSX-файл](5115052.xlsx) выглядит так. Как видно, ячейки C3 и F4 содержат формулы, а их результат — 800.

|![todo:image_alt_text](load-or-import-csv-file-with-formulas_1.png)|  
| :- |
