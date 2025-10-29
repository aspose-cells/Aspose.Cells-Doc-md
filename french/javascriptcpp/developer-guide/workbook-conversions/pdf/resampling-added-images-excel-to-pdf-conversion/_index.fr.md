---
title: Resampling des images ajoutées  Conversion d Excel en PDF avec JavaScript via C++
linktitle: Ajout d images échantillonnées
type: docs
weight: 150
url: /fr/javascript-cpp/resampling-added-images-excel-to-pdf-conversion/
description: Apprenez comment compresser les images ajoutées dans les fichiers Excel pour réduire la taille du PDF et améliorer la performance de conversion en utilisant Aspose.Cells for JavaScript via C++.
---

{{% alert color="primary" %}}

 Lors de la manipulation de gros fichiers Microsoft Excel avec beaucoup d'images, vous pourriez avoir besoin de compresser les images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer la performance globale de la conversion. Aspose.Cells for JavaScript via C++ supporte le resampling des images ajoutées pour réduire la taille du fichier PDF de sortie et améliorer la performance dans une certaine mesure.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui décrit comment effectuer la tâche à l'aide de l'API Aspose.Cells. L'exemple convertit un fichier Microsoft Excel en un fichier PDF tout en compressant les images dans le fichier.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells - Convert Excel to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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

            // Initialize a new Workbook by opening the uploaded Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOptions
            const pdfSaveOptions = new PdfSaveOptions();

            // Set Image Resample properties (converted from setImageResample(300, 70))
            // Universal setter->property conversion: setImageResample(...) -> imageResample = [...]
            pdfSaveOptions.imageResample = [300, 70];

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile_out_pdf.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

L'option [**imageResample(number, number)**](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#imageResample-number-number-) minimise la taille du PDF de sortie, mais cela peut affecter un peu la qualité de l'image.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [**workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) juste avant de rendre la feuille de calcul au format PDF. Cela garantira que les valeurs dépendant des formules sont recalculées et que les valeurs correctes sont rendues dans le PDF.

{{% /alert %}}
