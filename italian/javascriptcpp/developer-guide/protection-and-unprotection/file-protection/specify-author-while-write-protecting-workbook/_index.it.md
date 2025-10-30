---
title: Specifica l autore durante la protezione in scrittura del workbook con JavaScript via C++
linktitle: Specificare l autore durante la protezione in scrittura del libro di lavoro
type: docs
weight: 40
url: /it/javascript-cpp/specify-author-while-write-protecting-workbook/
description: Specifica un nome autore durante la protezione in scrittura di un workbook usando Aspose.Cells for JavaScript via C++.
---

## **Possibili Scenari di Utilizzo**

Puoi specificare un nome autore durante la protezione in scrittura del tuo workbook usando l'API Aspose.Cells. Usa la proprietà [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--) per questo scopo.

## **Specificare l'autore durante la protezione in scrittura del workbook**

Il codice di esempio seguente illustra l'uso della proprietà [**Workbook.author**](https://reference.aspose.com/cells/javascript-cpp/writeprotection/#author--). Il codice crea un workbook vuoto, lo protegge con una password, specifica il nome dell'autore e lo salva come [file Excel in output](67338582.xlsx). La schermata seguente illustra l'effetto del codice di esempio sul file Excel in output per tua referenza.

![todo:image_alt_text](specify-author-while-write-protecting-workbook_1.png)

## **Codice di Esempio**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Specify Author While Write Protecting Workbook</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            // Create empty workbook.
            const workbook = new Workbook();

            // Write protect workbook with password.
            workbook.settings.writeProtection.password = "1234";

            // Specify author while write protecting workbook.
            workbook.settings.writeProtection.author = "SimonAspose";

            // Save the workbook in XLSX format.
            const outputData = workbook.save(SaveFormat.Xlsx);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputSpecifyAuthorWhileWriteProtectingWorkbook.xlsx';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Excel File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Workbook created and write-protected successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
