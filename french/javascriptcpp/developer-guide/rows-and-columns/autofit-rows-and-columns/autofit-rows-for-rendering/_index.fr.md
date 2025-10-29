---
title: Ajustement automatique des lignes pour le rendu avec JavaScript via C++
linktitle: Ajuster automatiquement les lignes pour le rendu
type: docs
weight: 130
url: /fr/javascript-cpp/autofit-rows-for-rendering/
description: Apprenez comment ajuster automatiquement les lignes pour le rendu dans Excel en utilisant Aspose.Cells for JavaScript via C++. Empêchez la coupure du texte dans les fichiers PDF enregistrés.
---

En général, lorsque vous souhaitez afficher tout le texte dans une cellule, vous pouvez ajuster automatiquement la hauteur de la ligne en mode Normal avec un zoom de 100% dans Microsoft Excel. Cela permet au texte d'être entièrement visible en mode Normal, et même lors de l'impression ou de la sauvegarde du fichier en PDF, le texte sera affiché correctement.

Cependant, dans certains cas, l'ajustement automatique de la ligne fonctionne bien en mode Normal, mais lorsque vous passez en mode impression ou que vous enregistrez le fichier en PDF, le texte est coupé. Veuillez vérifier le fichier source [Book1.xlsx](Book1.xlsx) et les captures d'écran.

![le texte est tronqué en mode d'impression](text_clipped_in_printview.png)

Si vous souhaitez empêcher que le texte ne soit coupé dans le fichier PDF enregistré, vous pouvez ajuster automatiquement la ligne avec l'option [AutoFitterOptions.forRendering](https://reference.aspose.com/cells/javascript-cpp/autofitteroptions/#forRendering--) .

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Autofit Rows and Save as PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, AutoFitterOptions, SaveFormat, Utils } = AsposeCells;

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

            // Init workbook instance from uploaded file.
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Set autofit options for rendering.
            const autoFitterOptions = new AutoFitterOptions();
            autoFitterOptions.forRendering = true;

            // Autofit rows with options on first worksheet.
            const worksheet = workbook.worksheets.get(0);
            worksheet.autoFitRows(autoFitterOptions);

            // Save to pdf.
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'output.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Operation completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

Maintenant, le texte n'est pas tronqué dans le fichier PDF de sortie.

![le texte n'est pas tronqué dans le PDF enregistré](text_not_clipped_in_saved_pdf.png)
