---
title: Rendre le motif de format de date personnalisé g et ge mm dd
linktitle: Rendre le motif de format de date personnalisé g et ge mm dd  
description: Apprenez à rendre les modèles de format de date personnalisés g et ge dans Aspose.Cells for JavaScript via C++ pour contrôler l affichage des dates dans les feuilles de calcul.  
keywords: Aspose.Cells, bibliothèque JavaScript, feuille de calcul électronique, format de date personnalisé, rendu, motif g , motif ge , contrôle d affichage    
type: docs  
weight: 160  
url: /fr/javascript-cpp/render-custom-date-format-pattern-g-and-ge-mm-dd/  
---  

{{% alert color="primary" %}}  

Aspose.Cells est maintenant capable de rendre les motifs de format de date personnalisés comme g, ge.mm.dd et similaires. Veuillez consulter le fichier Excel source joint (5112361.xlsx) et le PDF converti (5112360.pdf) par Aspose.Cells pour votre référence.

{{% /alert %}}  

Le code d'exemple suivant convertit le fichier Excel source (5112361.xlsx) qui contient des valeurs de date avec des motifs de format personnalisés comme g et ge.mm.dd en un PDF de sortie (5112360.pdf).  


```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Convert Excel to PDF Example</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Convert to PDF</button>
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
            const fileInput = document.getElementById('fileInput');
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object by loading the selected file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Saving the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'CustomDateFormat_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">Conversion completed successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
