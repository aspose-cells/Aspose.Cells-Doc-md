---
title: Limiter le nombre de pages générées  Conversion d Excel en PDF avec JavaScript via C++
linktitle: Limitez le nombre de pages générées  Conversion Excel en PDF
type: docs
weight: 180
url: /fr/javascript-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Apprendre comment limiter le nombre de pages générées lors de la conversion d une feuille de calcul Excel en PDF en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Parfois, vous souhaitez imprimer une plage de pages dans un fichier PDF de sortie. Aspose.Cells for JavaScript via C++ a la capacité de définir une limite sur le nombre de pages générées lors de la conversion d'une feuille de calcul Excel en format PDF.

{{% /alert %}}

## **Limitez le nombre de pages générées**

L'exemple suivant montre comment restituer une plage de pages (3 et 4) dans un fichier Microsoft Excel au format PDF.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells PDF Export Example</title>
    </head>
    <body>
        <h1>Export Specific Pages to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
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

            // Open an Excel file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Instantiate the PdfSaveOption
            const options = new PdfSaveOptions();

            // Print only Page 3 and Page 4 in the output PDF
            // Starting page index (0-based index)
            options.pageIndex = 3;
            // Number of pages to be printed
            options.pageCount = 2;

            // Save the PDF file
            const outputData = workbook.save(SaveFormat.Pdf, options);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outPDF1.out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the file.</p>';
        });
    </script>
</html>
```

{{% alert color="primary" %}}

Si la feuille de calcul contient des formules, il est préférable d'appeler [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/javascript-cpp/workbook/#calculateFormula--) juste avant de l'exporter en PDF. Cela garantit que les valeurs dépendantes des formules sont recalculées, et que les bonnes valeurs sont affichées dans le fichier de sortie.

{{% /alert %}}
