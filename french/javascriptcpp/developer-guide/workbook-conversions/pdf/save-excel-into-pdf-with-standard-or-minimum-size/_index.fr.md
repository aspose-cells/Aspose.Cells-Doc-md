---
title: Enregistrer Excel en PDF avec une taille standard ou minimale en utilisant JavaScript via C++
linktitle: Enregistrer Excel en PDF avec une taille standard ou minimale
type: docs
weight: 340
url: /fr/javascript-cpp/save-excel-into-pdf-with-standard-or-minimum-size/
description: Apprenez comment sauvegarder des fichiers Excel au format PDF avec une taille standard ou minimale en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}} 

Par défaut, Aspose.Cells enregistre Excel en PDF avec une taille standard. Cependant, vous pouvez également l'enregistrer avec une taille minimale en utilisant la propriété [PdfSaveOptions.optimizationType](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#optimizationType--). Elle accepte les valeurs suivantes :

- PdfOptimizationType.Standard
- PdfOptimizationType.MinimumSize

{{% /alert %}} 

## **Enregistrez Excel en PDF avec une taille standard ou minimale en utilisant le script Aspose.Cells for Java via C++**
Le code d'exemple suivant montre comment enregistrer Excel en PDF avec une taille standard ou minimale en utilisant la propriété [PdfSaveOptions.optimizationType](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#optimizationType--).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells PDF Optimization Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions, PdfOptimizationType, Utils } = AsposeCells;

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

            // Instantiating a Workbook object by loading the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Create PdfSaveOptions and set optimization type to MinimumSize
            const opts = new PdfSaveOptions();
            opts.optimizationType = PdfOptimizationType.MinimumSize;

            // Save workbook to PDF with optimization options
            const outputData = workbook.save(SaveFormat.Pdf, opts);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OptimizedOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Optimized PDF';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the optimized file.</p>';
        });
    </script>
</html>
```
