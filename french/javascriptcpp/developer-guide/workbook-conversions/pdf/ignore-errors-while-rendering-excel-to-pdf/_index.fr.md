---
title: Ignorer les erreurs lors du rendu d Excel en PDF avec JavaScript via C++
linktitle: Ignorer les erreurs lors de la conversion Excel en PDF
type: docs
weight: 80
url: /fr/javascript-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Apprendre comment ignorer les erreurs lors de la conversion des fichiers Excel en PDF en utilisant Aspose.Cells for JavaScript via C++.
---

## **Scénarios d'utilisation possibles**  

Parfois, lors de la conversion de votre fichier Excel en PDF, des erreurs ou exceptions se produisent et le processus de conversion se termine. Vous pouvez ignorer toutes ces erreurs pendant la conversion en utilisant la propriété [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--). De cette façon, le processus de conversion se terminera en douceur sans générer d'erreur ou d'exception, mais une perte de données peut survenir. Utilisez cette propriété uniquement si la perte de données n'est pas critique pour vous.  

## **Ignorer les erreurs lors du rendu Excel vers PDF**  

Le code suivant charge le [fichier Excel d'exemple](55541778.xlsx) mais ce fichier Excel est erroné et génère une erreur lors de la [conversion en PDF](55541779.pdf) en 17.11. Mais comme nous utilisons la propriété [**PdfSaveOptions.ignoreError**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#ignoreError--), aucune erreur n'est levée. Cependant, une *forme en flèche rouge arrondie* comme montrée dans cette capture d'écran est perdue.  

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)  

## **Code d'exemple**  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Excel to PDF (Ignore Errors) Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF (Ignore Errors)</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, Utils } = AsposeCells;

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

            // Specify Pdf Save Options - Ignore Error
            const opts = new PdfSaveOptions();
            opts.ignoreError = true;

            // Save the Workbook in Pdf with Pdf Save Options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputErrorExcel2Pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```
