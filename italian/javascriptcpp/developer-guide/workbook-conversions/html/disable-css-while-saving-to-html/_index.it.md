---
title: Disabilita CSS durante il salvataggio in HTML con JavaScript tramite C++
linktitle: Disabilitare CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/javascript-cpp/disable-css-while-saving-to-html/
description: Impara come disabilitare CSS durante il salvataggio di file Excel in HTML usando Aspose.Cells for JavaScript tramite C++. 
---

## **Possibili Scenari di Utilizzo**

Quando salvi il file Excel come HTML a pagina singola, di solito gli elementi CSS saranno incorporati nel file HTML e collocati nella sezione HEAD. Se allegi questo file come contenuto/corpo di un'email, la maggior parte dei client di posta eliminerà gli elementi CSS, risultando in una visualizzazione non corretta. La versione 24.12 di Aspose.Cells introduce un'opzione che permette di disabilitare opzionalmente il CSS, consentendo di applicare gli stili direttamente agli elementi HTML stessi. Se vuoi impostare l'HTML come contenuto/corpo dell'email, usa la proprietà [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--) e impostala su **true**.

## **Disabilita CSS durante il salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.disableCss**](https://reference.aspose.com/cells/javascript-cpp/htmlsaveoptions/#disableCss--). 

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Disable CSS Example</title>
    </head>
    <body>
        <h1>Disable CSS Save Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, HtmlSaveOptions } = AsposeCells;

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
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            const opts = new HtmlSaveOptions();
            opts.disableCss = true;

            const outputData = workbook.save(SaveFormat.Html, opts);
            const blob = new Blob([outputData], { type: 'text/html' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputDisable.html';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download HTML File';

            document.getElementById('result').innerHTML = '<p style="color: green;">HTML file generated successfully! Click the download link to get the modified file.</p>';
        });
    </script>
</html>
```
