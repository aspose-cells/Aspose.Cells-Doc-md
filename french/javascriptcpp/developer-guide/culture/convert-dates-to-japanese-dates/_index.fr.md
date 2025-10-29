---
title: Convertir les dates en dates japonaises avec JavaScript via C++
linktitle: Convertir les dates en dates japonaises
type: docs
weight: 350
url: /fr/javascript-cpp/convert-dates-to-japanese-dates/
description: Apprenez comment convertir des dates grégoriennes en dates japonaises en utilisant Aspose.Cells for JavaScript via C++.
---  

{{% alert color="primary" %}}  

Dans le calendrier japonais, une nouvelle ère commence avec le règne d'un nouvel empereur. Le 1er mai 2019, un nouvel empereur est entré en fonction, mettant fin à l'ère Heisei et marquant le début de l'ère Reiwa.  

{{% /alert %}}  

Aspose.Cells offre un moyen de convertir les dates grégoriennes en dates japonaises. Lors de cette conversion, les changements d'ère sont également pris en compte. Le fragment de code suivant convertit le fichier [Excel source](90112015.xlsx) contenant des dates grégoriennes en [PDF de sortie](90112016.pdf) avec des dates japonaises comme indiqué dans l'image ci-dessous.  

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
