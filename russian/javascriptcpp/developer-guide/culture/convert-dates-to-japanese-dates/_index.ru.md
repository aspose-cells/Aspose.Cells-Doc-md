---
title: Конвертация дат в японский формат дат с помощью JavaScript через C++
linktitle: Преобразование дат в японские даты
type: docs
weight: 350
url: /ru/javascript-cpp/convert-dates-to-japanese-dates/
description: Узнайте, как преобразовать григорианские даты в японские даты с помощью Aspose.Cells for JavaScript через C++.
---  

{{% alert color="primary" %}}  

В японском календаре новая эра начинается с царствования нового императора. 1 мая 2019 года новый император пришел к власти, и эра Хейсэи закончилась, началась эра Рэйва.  

{{% /alert %}}  

Aspose.Cells предоставляет способ конвертировать григорианские даты в японские. Во время этой конвертации также учитываются изменения в эпохе. Следующий пример кода преобразует исходный Excel-файл (90112015.xlsx) с григорианскими датами в PDF (90112016.pdf) с японскими датами, как показано на изображении ниже.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel with Japanese Dates to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, LoadOptions, LoadFormat, CountryCode } = AsposeCells;

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

            // Create LoadOptions for XLSX and set language/region to Japan
            const options = new LoadOptions(LoadFormat.Xlsx);
            options.languageCode = CountryCode.Japan;
            options.region = CountryCode.Japan;

            // Instantiate workbook from uploaded file with load options
            const workbook = new Workbook(new Uint8Array(arrayBuffer), options);

            // Save workbook to PDF format
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'JapaneseDates.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF created successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
