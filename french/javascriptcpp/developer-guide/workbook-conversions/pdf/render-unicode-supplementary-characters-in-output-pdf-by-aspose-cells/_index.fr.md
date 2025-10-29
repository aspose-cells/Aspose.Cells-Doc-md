---
title: Rendre les caractères Unicode supplémentaires dans le PDF de sortie par Aspose.Cells for JavaScript via C++
linktitle: Rendre les caractères Unicode supplémentaires dans le PDF de sortie par Aspose.Cells
type: docs
weight: 350
url: /fr/javascript-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Apprenez comment rendre les caractères Unicode supplémentaires dans le PDF de sortie en utilisant Aspose.Cells for JavaScript via C++. 
---

{{% alert color="primary" %}}

Les caractères Unicode normaux ont une longueur de 2 octets tandis que les caractères Unicode supplémentaires ont une longueur de 4 octets. Aspose.Cells prend maintenant en charge le rendu de ces caractères Unicode de 4 octets.

Dans la norme des caractères Unicode, les Caractères supplémentaires sont les caractères aux points de code de U+10000 à U+10FFFF. En d'autres termes, ce sont les caractères Unicode supérieurs à U+FFFF.

- En UTF-8, ces caractères ont une longueur de 4 octets.
- En UTF-16, ces caractères nécessitent 2 substituts (unités de 16 bits).

{{% /alert %}}

## Rendre les caractères Unicode supplémentaires dans le PDF de sortie par Aspose.Cells for JavaScript via C++

La capture d'écran suivante montre comment Aspose.Cells a rendu le [fichier Excel source](5115563.xlsx) en [PDF de sortie](5115564.pdf). Comme vous pouvez le voir, tous les trois caractères Unicode supplémentaires ont été rendus exactement comme Microsoft Excel.

![todo:image_alt_text](output.png)

## Code d'exemple

Vous pouvez utiliser ce code d'exemple pour convertir le [fichier Excel source](5115563.xlsx) en [PDF de sortie](5115564.pdf).

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Render Unicode Supplementary Characters to PDF</title>
    </head>
    <body>
        <h1>Render Unicode Supplementary Characters to PDF</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat } = AsposeCells;

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

            // Save the workbook as PDF
            const outputData = workbook.save(SaveFormat.Pdf);
            const blob = new Blob([outputData], { type: 'application/pdf' });
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'RenderUnicodeInOutput_out.pdf';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download PDF File';

            document.getElementById('result').innerHTML = '<p style="color: green;">PDF generated successfully! Click the download link to get the PDF file.</p>';
        });
    </script>
</html>
```
