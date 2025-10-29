---
title: Rendu d une page PDF par feuille Excel  Conversion Excel en PDF avec JavaScript via C++
linktitle: Rendre une page PDF par feuille de calcul Excel  Conversion Excel en PDF
type: docs
weight: 100
url: /fr/javascript-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Lors de la manipulation de grands fichiers Microsoft Excel (par exemple un classeur avec de nombreuses feuilles, chacune avec 50 colonnes et 300 lignes ou plus), vous pourriez vouloir que la sortie PDF affiche une page par feuille, indépendamment de la taille de la feuille. Cela signifierait que chaque page pourrait avoir une taille de page très différente. Ceci peut être réalisé en utilisant Aspose.Cells for JavaScript via C++.

{{% /alert %}}

Veuillez consulter le code d'exemple suivant qui convertit un fichier Excel avec plusieurs feuilles de calcul en PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example - Excel to PDF</title>
    </head>
    <body>
        <h1>Convert Excel to PDF (One Page Per Worksheet)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Convert to PDF</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, PdfSaveOptions } = AsposeCells;

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

            // Initialize a new Workbook by opening the selected Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Implement one page per worksheet option
            const pdfSaveOptions = new PdfSaveOptions();
            pdfSaveOptions.onePagePerSheet = true;

            // Save the PDF file (returns binary data)
            const outputData = workbook.save(SaveFormat.Pdf, pdfSaveOptions);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'OutputFile.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si l'option [PdfSaveOptions.onePagePerSheet](https://reference.aspose.com/cells/javascript-cpp/pdfsaveoptions/#onePagePerSheet--) est réglée sur **true**, tout le contenu de la feuille sera rendu sur une seule page PDF.

{{% /alert %}} {{% alert color="primary" %}}

Si votre feuille de calcul contient des formules, il est préférable d'appeler [Workbook.calculateFormula()](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) juste avant de rendre la feuille de calcul en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et que les bonnes valeurs sont rendues dans le PDF.

{{% /alert %}}
