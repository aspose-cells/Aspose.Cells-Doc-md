---
title: Convertir fechas a fechas japonesas con JavaScript vía C++
linktitle: Convertir Fechas a Fechas Japonesas
type: docs
weight: 350
url: /es/javascript-cpp/convert-dates-to-japanese-dates/
description: Aprende cómo convertir fechas gregorianas a fechas japonesas usando Aspose.Cells for JavaScript vía C++.
---  

{{% alert color="primary" %}}  

En el Calendario Japonés, una nueva era comienza con el reinado de un nuevo emperador. El 1 de mayo de 2019, un nuevo emperador tomó el poder con lo cual terminó la era Heisei y comenzó la era Reiwa.  

{{% /alert %}}  

Aspose.Cells ofrece una forma de convertir fechas gregorianas a fechas japonesas. Durante esta conversión, también se consideran los cambios en la era. El siguiente fragmento de código convierte el archivo [Excel fuente](90112015.xlsx) que contiene fechas gregorianas a un [PDF de salida](90112016.pdf) con fechas japonesas, como se muestra en la imagen abajo.  

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
